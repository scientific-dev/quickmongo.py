# Import MongoClient from PyMongo
from pymongo import MongoClient

# Import Any from typing
from typing import Any

# Base Class aka raw database
class Base():

    # Constructor Class
    def __init__(self, client: Any, options: dict = {}):
        self.client = client
        self.db = self.client[options['db_name']]
        self.options = options
        self.collection = self.db[self.options['collection_name']]

    def set(self, key, value):
        self.collection.delete_many({ 'key': key }) 
        self.collection.insert_one({
            'key': key,
            'value': value
        })
        return

    def get(self, key):
        try:
            try:
                return self.collection.find({ 'key': key })[0]['value']
            except:
                return self.collection.find({ 'key': key })[0]
        except:
            return None

    def all(self):
        data = self.collection.find({})
        res = []
        
        for doc in list(data):
            try:
                res.append({
                    'key': doc['key'],
                    'value': doc['value']
                })
            except:
                return list(data)

        return res

    def drop(self):
        self.collection.drop()

    def delete(self, key: str):
        self.collection.delete_many({
            'key': key
        })
        return
