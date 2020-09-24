"""
QuickMongo.py
By Science Spot from Decimal Developement

Simple wrapper for PyMongo written in python!
v0.0.7
"""

# v0.0.7
__version__ ='0.0.7'

# Import Time
from time import time

# Import mongo client from pymongo
from pymongo import MongoClient

# Import files
from .Util import Util, AttrDict
from .Base import Base

# Database Class which is the main class
class Database():

    def __init__(self, mongoURL: str, options: dict = {}, events: dict = {}):
        startedAt = time()
        try:
            self.client = MongoClient(mongoURL)
        except:
            raise TypeError('invalid mongo link provided!')

        database_names = self.client.list_database_names()

        if 'db_name' not in options.keys():
            options['db_name'] = database_names[0]
        elif options['db_name'] not in database_names:
            raise TypeError('try to choose a db from here: ' + database_names)

        if 'collection_name' not in options.keys():
            options['collection_name'] = 'python'

        self.base = Base(self.client, options)
        self.options = options
        self.client = self.base.client
        self.db = self.base.db
        self.collection = self.base.collection

        for callback in events.values():
            if not callable(callback):
                raise TypeError('event parameter dict values must contain a function')

        if 'ready' in events.keys():
            readyCallback = events['ready']
            param = AttrDict({
                'started_at': startedAt,
                'connected_at': time(),
                'time_took_to_connect': time() - startedAt
            })

            try:
                readyCallback(param)
            except TypeError:
                raise TypeError('ready callback function must have 1 parameter')

    def all_database_names(self):
        return self.base.client.list_database_names()

    def database_exists(self, db_name: str):
        if db_name not in self.base.client.list_database_names():
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
