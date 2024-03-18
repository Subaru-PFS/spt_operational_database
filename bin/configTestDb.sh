# This is the user part of setting up a read-mostly database for testing. The intent is that we get read-only access to 
# the real 'opdb', and write access to a handful of specified tables.
#

# We are provided with a shadow database on pfsa-db01-gb:5434: the 'pfs' user there can only select from the tables on the real 
# database, In this script we specify the tables which we need to *write* to: those will be the only ones we can write to. 
# *Currently* they will also be empty

TEST_DBHOST=pfsa-db01-gb.subaru.nao.ac.jp
TEST_DBPORT=5434

# The normal user account which will use and configure the shadow database.
DBUSER=pfs

send_sql_command() {
    if [ $VERBOSE -eq 1 ]; then
        echo psql -h $TEST_DBHOST -p $TEST_DBPORT -U $DBUSER -d $TESTDB -c \""$@"\"
    fi
    if [ $NORUN -eq 0 ]; then
        psql -h $TEST_DBHOST -p $TEST_DBPORT -U $DBUSER -d $TESTDB -c "$@"
    fi

    if [ $? -ne 0 ]; then
        echo "Failed to execute SQL command: $sql_command" 1>&2
        exit 1
    fi
}

MCS_TABLES="mcs_data cobra_match fiducial_fiber_match mcs_pfi_transformation"
AG_TABLES="...eventually....."
usage() {
    (
        echo "Usage: $(basename $0) [-D] [-v] [-n] [-s NAME] [-h dbhost] [-p dbport] databaseName"
        echo "  -v                  Verbose mode"
        echo "  -n                  Dry-run mode: print commands, but do not run them"
        echo "  -s NAME             The subsystem to setup writable tables for."
        echo "  -t tables           Additional comma-separated list of tables to allow writes to"
        echo "  -h dbhost           The host of the database to configure. default: $TEST_DBHOST"
        echo "  -p dbport           The port of the database to configure. default: $TEST_DBPORT"
        echo 
        echo "     databaseName - the name of the database to configure."
        echo 
        echo "System names and their tables are:"
        echo "    MCS: $MCS_TABLES"
        echo "    AG: $AG_TABLES"

    ) 1>&2
    exit 1
}

VERBOSE=0
NORUN=0
TABLES=""
while getopts ":Dvnht:s:h:p:" opt; do
    case ${opt} in
        v ) VERBOSE=1
            ;;
        n ) NORUN=1
            ;;
        t ) EXTRA_TABLES=$OPTARG
            ;;
        s ) case $OPTARG in
                MCS ) TABLES=$MCS_TABLES
                    ;;
                AG ) TABLES=$AG_TABLES
                    ;;
                * ) echo "Unknown subsystem: $OPTARG" 1>&2
                    usage
                    ;;
            esac
            ;;
        h ) TEST_DBHOST=$OPTARG
            ;;
        p ) TEST_DBPORT=$OPTARG
            ;;
        \? )
            echo "Invalid option: $OPTARG" 1>&2
            usage
            ;;
        : )
            echo "Invalid option: $OPTARG requires an argument" 1>&2
            usage
            ;;
    esac
done
shift $((OPTIND -1))
TESTDB=$1

if [ -z "$TESTDB" ]; then
    echo "No database name specified" 1>&2
    echo 1>&2
    usage
fi

if [ $NORUN -eq 1 ]; then
    echo "Running in dry-run mode"
    VERBOSE=1
fi

# The tables we want to write to.
# Start with any TABLES specified by the -s option, then add any specified by the -t option.
EXTRA_TABLES=$(echo $EXTRA_TABLES | tr ',' ' ')
if [ -n "$EXTRA_TABLES" ]; then
    TABLES="$TABLES $EXTRA_TABLES"
fi

echo "Configuring database $TESTDB on $TEST_DBHOST:$TEST_DBPORT in 3s...."
echo "  to allow writes only to the following tables: "
echo "     $TABLES"
echo "note that all changes are made in a single transaction: any anything fails, nothing will be changed."
sleep 3
echo

DB=$TESTDB

printAndOrPsql () {
    if [ $VERBOSE -eq 1 ]; then
        echo $1
    fi
    if [ $NORUN -eq 0 ]; then
        echo $1 | psql -h $TEST_DBHOST -p $TEST_DBPORT -U $DBUSER -d $DB
    fi
}

tf=$(mktemp)
# Run all configuration as a single transaction. This might be dumb and incredibly confusing, 
# but I worry about one table rename failing.
( echo "import foreign schema public from server foreign_opdb_srv into public;"
  for table in $TABLES; do
     echo "alter foreign table $table rename to opdb_$table;"
     echo "create table $table (like opdb_$table);"
  done
) > $tf

if [ $VERBOSE -eq 1 ]; then
    cat $tf
fi

if [ $NORUN -eq 0 ]; then
    psql -h $TEST_DBHOST -p $TEST_DBPORT -U $DBUSER -d $DB -f $tf --single-transaction
fi

rm $tf
