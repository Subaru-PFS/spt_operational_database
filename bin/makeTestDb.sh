# This is the admin part of setting up a read-mostly database for testing. The intent is that we get read-only access to 
# the real 'opdb', and write access to a handful of specified tables. That part is not done here, but in a user script.
#
# There is a real instance of 'opdb' on pfsa-db01-gb:5432: the 'pfs' user there can insert/update.
# We are not *connecting* to this instance at all, but have configured it with a read-only user account, 'public_user'
#
REAL_DBHOST=pfsa-db01-gb.subaru.nao.ac.jp
REAL_DBPORT=5432
FOREIGN_USER=public_user
FOREIGN_PASS=public_user

# We are making a shadow database on pfsa-db01-gb:5434: the 'pfs' user here can only select from the tables on the real database.
# We are connecting to this instance and configuring it as a "FOREIGN SERVER" to the real database. Users will connect to the test 
# database as the main 'pfs' user, but that gets translated internally to the read-only 'public_user' on the real database.
#
TEST_DBHOST=pfsa-db01-gb.subaru.nao.ac.jp
TEST_DBPORT=5434
FOREIGN_SERVER_NAME=foreign_opdb_srv
EXTENSION_NAME=postgres_fdw

# The admin user on the test instance. This is the user that will be used to create the test database, the foreign server and the user mapping.
DBADMIN=admin2
ADMINDB=postgres

# The normal user account which will use and configure the shadow database.
TEST_DBUSER=pfs

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

# Yes these two functions should be merged.
send_admin_sql_command() {
    if [ $VERBOSE -eq 1 ]; then
        echo psql -h $TEST_DBHOST -p $TEST_DBPORT -U $DBADMIN -d $ADMINDB -c \""$@"\"
    fi
    if [ $NORUN -eq 0 ]; then
        psql -h $TEST_DBHOST -p $TEST_DBPORT -U $DBADMIN -d $ADMINDB -c "$@"
    fi

    if [ $? -ne 0 ]; then
        echo "Failed to execute SQL command: $sql_command" 1>&2
        exit 1
    fi
}

usage() {
    echo "Usage: $(basename $0) [-D] [-v] [-n] databaseName" 1>&2
    echo "  -D                  Drop the database if it already exists" 1>&2
    echo "  -v                  Verbose mode" 1>&2
    echo "  -n                  Dry-run mode: print commands, but do not run them" 1>&2
    echo "  databaseName - the name of the database to create." 1>&2
    exit 1
}

VERBOSE=0
NORUN=0
DODROP=0   # Whether we should try to DROP the database.
while getopts ":Dvnh" opt; do
    case ${opt} in
        D ) DODROP=1
            ;;
        v ) VERBOSE=1
            ;;
        n ) NORUN=1
            ;;
        \? )
            echo "Invalid option: $OPTARG" 1>&2
            ;;
        : )
            echo "Invalid option: $OPTARG requires an argument" 1>&2
            ;;
        h )
            usage
            echo "Usage: makeTestDb.sh [-d <database name>]" 1>&2
            ;;
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

if [ $DODROP -eq 1 ]; then
    echo "DROPPING database $TESTDB"
    send_admin_sql_command "DROP DATABASE IF EXISTS $TESTDB;"
fi

echo "Creating database $TESTDB"
send_admin_sql_command "CREATE DATABASE $TESTDB WITH OWNER $TEST_DBUSER;"

# Now switch to the new database and configure it.
echo "Configuring database $TESTDB"
DB=$TESTDB

send_admin_sql_command "CREATE EXTENSION IF NOT EXISTS $EXTENSION_NAME WITH SCHEMA public;"

send_admin_sql_command "CREATE SERVER IF NOT EXISTS $FOREIGN_SERVER_NAME \
  FOREIGN DATA WRAPPER $EXTENSION_NAME \
  OPTIONS(host '$REAL_DBHOST', dbname '$TESTDB', port '$REAL_DBPORT');"

send_admin_sql_command "CREATE USER MAPPING IF NOT EXISTS FOR $TEST_DBUSER \
  SERVER $FOREIGN_SERVER_NAME \
  OPTIONS (user '$FOREIGN_USER', password '$FOREIGN_PASS');"    

send_admin_sql_command "grant usage on foreign server $FOREIGN_SERVER_NAME to $TEST_DBUSER;"

echo "Database $TESTDB on ${TEST_DBHOST}:${TEST_DBPORT} is ready for use by $TEST_DBUSER."
