# Creating a Database

Create your mongodb database

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