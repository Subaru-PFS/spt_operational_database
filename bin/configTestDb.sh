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

usage() {
    echo "Usage: $(basename $0) [-D] [-v] [-n] databaseName" 1>&2
    echo "  -v                  Verbose mode" 1>&2
    echo "  -n                  Dry-run mode: print commands, but do not run them" 1>&2
    echo "  -t tables           Comma-separated list of tables to allow writes to" 1>&2
    echo "  databaseName - the name of the database to configure." 1>&2
    exit 1
}

VERBOSE=0
NORUN=0
while getopts ":Dvnht:" opt; do
    case ${opt} in
        v ) VERBOSE=1
            ;;
        n ) NORUN=1
            ;;
        t ) TABLES=$OPTARG
            ;;
        \? )
            echo "Invalid option: $OPTARG" 1>&2
            ;;
        : )
            echo "Invalid option: $OPTARG requires an argument" 1>&2
            ;;
        h )
            usage
    esac
done
shift $((OPTIND -1))
TESTDB=$1

if [ $NORUN -eq 1 ]; then
    echo "Running in dry-run mode"
    VERBOSE=1
fi

if [ -z "$TESTDB" ]; then
    echo "No database name specified" 1>&2
    echo 1>&2
    usage
fi

# The tables we want to write to
TABLES=$(echo $TABLES | tr ',' ' ')

echo "Configuring database $TESTDB"
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
# Run all configuration as a single transaction. This might be dumb, but I worry
# about one table rename failing.
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
    psql -h $TEST_DBHOST -p $TEST_DBPORT -U $DBUSER -d $DB -f $tf
fi

rm $tf
