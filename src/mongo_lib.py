from pymongo import MongoClient
import config as cons


def fetch_record_by_column(collection_name, column_name, column_value):
    """
    Get record from DB for given column_name and value
    """
    db = init_db()
    collection = db[collection_name]
    document = list(collection.find({column_name: column_value}))
    return document


def insert_to_db(collection_name):
    """
    TODO: To add later
    """


def del_from_db():
    """
    TODO: To add later
    """


def init_db():
    """
    Establishing the connection with MongoDB
    """
    connection = MongoClient(cons.ip_port_initial_db)
    connection.sampledb.authenticate(cons.mongoUserName, cons.mongoPasswd)
    db = connection.sampledb
    return db
