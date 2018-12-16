import cassandra_main_lib as cl
import logging


def del_from_db(conn, table, where_statement):
    """
    Delete single record from DB
    """
    statement = "Delete from "
    where_keyword = "where "
    table_name = table + " "
    eol = ";"

    cql_statement = statement + table_name + where_keyword + where_statement + eol

    result, cursor = cl.query(conn, cql_statement)
    logging.info("result" + result)


def bulk_del_from_db(table, path):
    """
    Delete bulk records from DB given the table name and path of file containing primary keys
    """
    conn = cl.connect_to_cassandra()
    input_file = open(path, 'r')
    contents = input_file.read()
    list_content = contents.split("\n")
    for where_statement in list_content:
        del_from_db(conn, table, where_statement)

    logging.info("records deleted")

    cl.disconnect_from_cassandra(conn)
