import cql
import logging
import config as c


def connect_to_cassandra():
    """
    Connect to Cassandra host
    """
    conn = cql.connect(host=c.host, port=c.port, keyspace=c.keyspace,
                       user=c.user, password=c.password, cql_version=c.cql_version)

    logging.info("cassandra_lib connected")
    return conn


def disconnect_from_cassandra(conn):
    """
    Disconnects from the database.
    """
    conn.close()
    logging.info("cassandra_lib connection closed")


def query(conn, select_statement):
    """
    Triggering Query for the cassandra_lib DB and returning boole
    """
    logging.info(select_statement)
    cursor = conn.cursor()
    result = cursor.execute(str(select_statement))
    return result, cursor
