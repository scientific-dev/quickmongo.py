"""
QuickMongo.py
By Science Spot from Decimal Developement

Simple wrapper for PyMongo written in python!
v0.0.9
"""

# v0.0.9
__version__ ='0.0.9'

# Import Time
from time import time

# Import mongo client from pymongo
from pymongo import MongoClient

# Import any type from typings
from typing import Any

# Import files
from .Util import *
from .Base import Base
from .Exception import *
from .EventHandler import Events

# Database Class which is the main class
class Database(Events):

    def __init__(self, mongoURL: str, options: dict = {}, events: dict = {}):
        self.started_at = time()
        self.events = events
        
        super().__init__(events)

        try:
            self.client = MongoClient(mongoURL)
        except:
            raise QuickMongoError('invalid mongo link provided!')

        database_names = self.client.list_database_names()

        if 'db_name' not in options.keys():
            options['db_name'] = database_names[0]
        elif options['db_name'] not in database_names:
            raise QuickMongoError('try to choose a db from here: ' + str(database_names))

        if 'collection_name' not in options.keys():
            options['collection_name'] = 'python'

        self.base = Base(self.client, options)
        self.options = options
        self.client = self.base.client
        self.db = self.base.db
        self.collection = self.base.collection

        self.emit('ready')

    def uptime(self) -> int:
        return time() - self.started_at

    def disconnect(self) -> None:
        self.client.close()
        self.base.client.close()
        return

    def all_database_names(self) -> list:
        return self.base.client.list_database_names()

    def database_exists(self, db_name: str) -> bool:
        if db_name not in self.base.client.list_database_names():
            return False
        return True

    def all_collection_names(self) -> list:
        return self.base.db.list_collection_names()

    def collection_exists(self, name: str) -> bool:
        if name in self.base.db.list_collection_names():
            return True
        return False

    def set(self, key: str, value) -> None:
        self.base.set(key, value)

    def get(self, key: str) -> Any:
        return self.base.get(key)

    def all(self) -> list:
        return self.base.all()

    def startsWith(self, query: str) -> list:
        return Util().startswith(self.base.all(), query)

    def math(self, key: str, symbol: str, amount: int) -> None:
        if symbol not in math_symbols:
            raise QuickMongoError('invalid symbol provided')

        oldData = self.base.get(key)

        if not oldData:
            oldData = 0
        
        if not isinstance(oldData, int):
            raise ValueNotIntError('old data is not an int!')

        newData = math_operations.get(symbol)(oldData, amount)

        self.base.set(key, newData)

    def add(self, key: str, amount: int) -> None:
        self.math(key, '+', amount)

    def subtract(self, key: str, amount: int) -> None:
        self.math(key, '-', amount)

    def exists(self, key: str) -> bool:
        if not self.base.get(key):
            return False
        return True

    def typeof(self, key: str) -> Any:
        return type(self.base.get(key))

    def deleteAll(self) -> None:
        self.base.drop()

    def delete(self, key: str) -> None:
        self.base.delete(key)
