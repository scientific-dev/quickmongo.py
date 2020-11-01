# Get Databases and Collections

List of methods which you can use to get databases and collections

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