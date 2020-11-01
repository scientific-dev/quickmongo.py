# Database Options

There are some options to connect with the database

| Option name | Type   | Default Value |Description                  |
|-------------|--------|---------------|-----------------------------|
| collection_name | string | python | Your custom collection name |
| db_name | string | first element of database list | Database name to select |

```py
options = {
    'collection_name': 'yourCollectionName', # Collection name will be 'python' as default
    'db_name': 'Cluster0' # This is optional unless you are using localhost you have to set it to local!
}

db = Database(mongoURL, options)
# mongoURL is described above
```