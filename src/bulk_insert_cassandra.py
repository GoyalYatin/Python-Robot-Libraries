import cassandra_main_lib as cl
import logging


def insert_to_db_from_json(conn, table, json):
    """
    Insert one record in DB using json as input
    """
    insert_statement = "INSERT INTO  "
    json_keyword = "JSON "
    table_name = table + " "
    eol = ";"

    cql_statement = insert_statement + table_name + json_keyword + json + eol

    result, cursor = cl.query(conn, cql_statement)
    logging.info("result " + result)
    return result, cursor


def insert_to_db(conn, table, fields, values):
    """
    Insert one record in DB using standard cql query
    """
    statement = "INSERT INTO "
    values_keyword = " values "
    table_name = table + " "
    eol = ";"

    cql_statement = statement + table_name + fields + values_keyword + values + eol

    result, cursor = cl.query(conn, cql_statement)
    logging.info("result " + result)
    return result, cursor


def bulk_inserts(insert_type, path, table):
    """
    Insert in bulk reading from file, insert can be done either by reading json or the csv(corresponds to cql)
    :param insert_type:
                Type of query, it can cql or json
    :param path:
                Path of file from where the query is made
    :param table:
                The table in which insert to be performed
    :return:
            Nothing
    """
    conn, cursor = cl.connect_to_cassandra()
    if insert_type == "JSON":
        input_file = open(path, 'r')
        contents = input_file.read()
        insert_to_db_from_json(conn, table, contents)

    elif insert_type == "CQL":
        input_file = open(path, 'r')
        contents = input_file.read()
        list_content = contents.split("\n")

        heading = list_content.pop(0)

        for values in list_content:
            fields = heading
            insert_to_db(table, fields, values)

    cl.disconnect_from_cassandra(conn)
