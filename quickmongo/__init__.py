"""
QuickMongo.py
By Science Spot from Decimal Developement

Simple wrapper for PyMongo written in python!
"""
# v0.0.1
__version__ ='0.0.1'

# Import mongo client from pymongo
from pymongo import MongoClient

# Import time package
from time import time

# Default Options
defaultOptions = {
    'collection_name': 'python'
}

# Util Class

class Util():

    # Startswith filter
    def startswith(self, data, query: str):
        result = []

        for doc in data:
            if(doc['key'].startswith(query)):
                result.append(doc)

        return result


# Base Class with basic things: Set, Get, Delete, All...
class Base():

    # Constructor Class
    def __init__(self, mongoURL: str, dbname: str, options: dict = defaultOptions):
        self.client = MongoClient(mongoURL)
        self.db = self.client[dbname]
        self.options = options
        self.collection = self.db[self.options['collection_name']]

    def set(self, key, value):
        self.collection.delete_many({
            'key': key
        })
        
        self.collection.insert_one({
            'key': key,
            'value': value
        })
        return

    def get(self, key):
        try:
            return self.collection.find({ 'key': key })[0]['value']
        except:
            return None

    def all(self):
        data = self.collection.find({})
        res = []
        
        for doc in list(data):
            res.append({
                'key': doc['key'],
                'value': doc['value']
            })

        return res

    def drop(self):
        self.collection.drop()

    def delete(self, key: str):
        self.collection.delete_many({
            'key': key
        })
        return

# Database Class which is the main class
class Database():

    def __init__(self, mongoURL: str, dbname: str, options: dict = defaultOptions):
        self.base = Base(mongoURL, dbname, options)
        self.options = options
        self.client = self.base.client
        self.db = self.base.db
        self.collection = self.base.collection

        if dbname not in self.base.client.list_database_names():
            raise TypeError('invalid database provided! select any from them: ' + str(self.base.client.list_database_names()))

    def all_database_names(self):
        return self.base.client.list_database_names()

    def database_exists(self, dbname: str):
        if dbname not in self.base.client.list_database_names():
            return False
        return True

    def all_collection_names(self):
        return self.base.db.list_collection_names()

    def collection_exists(self, name: str):
        if name in self.base.db.list_collection_names():
            return True
        return False

    def set(self, key: str, value):
        return self.base.set(key, value)

    def get(self, key: str):
        return self.base.get(key)

    def all(self):
        return self.base.all()

    def startsWith(self, query: str):
        return Util().startswith(self.base.all(), query)

    def add(self, key: str, amount: int):
        oldData = self.base.get(key)

        if not isinstance(oldData, int):
            raise TypeError('old data is not an int!')

        self.base.set(key, oldData + amount)

    def subtract(self, key: str, amount: int):
        oldData = self.base.get(key)

        if not isinstance(oldData, int):
            raise TypeError('old data is not an int!')

        self.base.set(key, oldData - amount)

    def exists(self, key: str):
        if not self.base.get(key):
            return False
        return True

    def typeof(self, key: str):
        return type(self.base.get(key))

    def deleteAll(self):
        return self.base.drop()

    def delete(self, key: str):
        return self.base.delete(key)