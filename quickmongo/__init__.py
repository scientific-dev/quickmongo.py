"""
QuickMongo.py
By Science Spot from Decimal Development

Simple wrapper for PyMongo written in python!
v1.0.0 | MIT License
"""

# v1.0.0
__version__ ='1.0.0'

# Import Time
from time import time

# Import mongo client from pymongo
from pymongo import MongoClient

# Import any type from typings
from typing import Any

# Import files
from .Util import startswith
from .Base import Base
from .Exception import *

# Database Class which is the main class
class Database():

    def __init__(self, mongoURL: str, options: dict = {}):
        self.started_at = time()

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

    def uptime(self) -> int:
        return time() - self.started_at

    def disconnect(self) -> None:
        self.client.close()
        self.base.client.close()
        return

    def all_database_names(self) -> list:
        return self.base.client.list_database_names()

    def database_exists(self, db_name: str) -> bool:
        return db_name not in self.base.client.list_database_names()

    def all_collection_names(self) -> list:
        return self.base.db.list_collection_names()

    def collection_exists(self, name: str) -> bool:
        return name in self.base.db.list_collection_names()

    def set(self, key: str, value) -> None:
        self.base.set(key, value)

    def get(self, key: str) -> Any:
        return self.base.get(key)

    def all(self) -> list:
        return self.base.all()

    def startswith(self, query: str) -> list:
        return startswith(self.base.all(), query)

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
        return bool(self.base.get(key))

    def typeof(self, key: str) -> Any:
        return type(self.base.get(key))

    def delete_all(self) -> None:
        self.base.drop()

    def delete(self, key: str) -> None:
        self.base.delete(key)
