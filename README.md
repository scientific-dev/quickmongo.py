<div align="center">
  <img src="https://github.com/Scientific-Guy/decimaldev/blob/master/assets/Quickmongo.png?raw=true">
  <div>
    <a href="https://pypi.org/project/quickmongo.py/"><img src="https://img.shields.io/pypi/l/quickmongo.py?label=License&style=for-the-badge"></a>
    <a href="https://pypi.org/project/quickmongo.py/"><img src="https://img.shields.io/pypi/v/quickmongo.py?label=Version&style=for-the-badge"></a>
    <a href="https://pypi.org/project/quickmongo.py/"><img src="https://img.shields.io/pypi/format/quickmongo.py?label=Format&style=for-the-badge"></a>
    <a href="https://github.com/Scientific-Guy/quickmongo.py/"><img src="https://img.shields.io/github/repo-size/scientific-guy/quickmongo.py?label=Size&style=for-the-badge"></a>
    <a href="https://discord.gg/FrduEZd"><img src="https://img.shields.io/discord/736099894963601438?label=Discord&style=for-the-badge"></a>
  </div><br>
</div>

# Quick Intro
Quickmongo.py is a quick wrapper for pymongo to access mongodb! You can use pymongo if you know it!

# Quick Docs

## Installation

**In your terminal:**
```
pip install quickmongo.py
```

**In your python file:**
```py
from quickmongo import Database

# If you are using locally
db = Database('mongodb://localhost:27017/', {'db_name': 'local'})

# if you are using 'mongodb+srv://' uri then you should do something like this
db = Database(mongoURL)
# mongourl will be the 'mongodb+srv://' uri link
# clusterName will be the name of the mongoose cluster. Eg:- Cluster0
# Incase if you don't know what is your clustername you will get an TypeError with available clusters!
```

## Options of Databases

Set some options for your database as a dict which is optional

```py
options = {
    'collection_name': 'yourCollectionName', # Collection name will be 'python' as default
    'db_name': 'Cluster0' # This is optional unless you are using localhost you have to set it to local!
}

db = Database(mongoURL, options)
# mongoURL is described above
```

## Get databases and collections

```py
# Get all database names under the link
print(db.all_database_names())
# Check if the given database exists in the list
print(db.database_exists('Cluster0'))

# Get all collections names under the link
print(db.all_collection_names())
# Check if the given collection exists in the list
print(db.collection_exists('python'))
```

## All Operations

```py
db.set('foo', 'bar') # Will set value 'bar' for the key 'foo'
db.get('foo') # Will return 'bar' which is the value of the key 'foo'

db.all() # Will return all keys and values of the collection! {'key': 'foo', 'value': 'bar'} as a dict
db.startsWith('f') # Will sort all data whose keys startswith 'f' as {'key': 'foo', 'value': 'bar'}

db.delete('foo') # Will delete value of the key 'foo'
db.deleteAll() # Will delete all values of the all keys! Simple drop() function

db.set('foo', 1) # Simple set function given description above

db.add('foo', 2) # Will add 2 to the old value. So the current value will be 3
db.subtract('foo', 1) # Will subtract 1 from old value of the key 'foo'. So the current value will be 1

db.math('foo', '*', 5) # Will multiply value by 5 so 1*5 = 5
db.math('foo', '**', 5) # 5**5 = 25
db.math('foo', '/', 5) # 25/5 = 5
db.math('foo', '+', 1) # 5+1 = 6
db.math('foo', '-', 1) # 6-1 = 5

db.typeof('foo') # Its currently int so it will return <class 'int'>
```

## Events

Events are functions which will trigger on paticular times

**Ready Event:**
```py
def ready():
    print('Connected with database')

db = Database(
    mongoURL='your-url',
    events={
        'ready': ready
    }
)

# Will run ready callback when db is ready!
```

> Contribute codes to this packages by github [here](https://github.com/Scientific-Guy/quickmongo.py)

# Support

- [Join our Discord Server](https://discord.gg/FrduEZd)
- [GitHub Repo](https://github.com/Scientific-Guy/quickmongo.py)
