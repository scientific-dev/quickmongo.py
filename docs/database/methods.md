# All Methods

List of all database methods

```py
db.set('foo', 'bar') # Will set value 'bar' for the key 'foo'
db.get('foo') # Will return 'bar' which is the value of the key 'foo'

db.all() # Will return all keys and values of the collection! {'key': 'foo', 'value': 'bar'} as a dict
db.startswith('f') # Will sort all data whose keys startswith 'f' as {'key': 'foo', 'value': 'bar'}

db.delete('foo') # Will delete value of the key 'foo'
db.delete_all() # Will delete all values of the all keys! Simple drop() function

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

## Set
Set's a value for the key

**Returns:** None

**Parameters:**

| Name  | Type   | Description |
|-------|--------|-------------|
| key   | string | ID          |
| value | any    | data        |

## Get
Get value of the key

**Returns:** Any

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| key  | string | ID |

## All
Returns an list of all data

**Returns:** List

**Parameters:** None

## Startswith
Returns an list of all data filtered with key startswith

**Returns:** List

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| text | string | To filter with startswith |

## Delete
Deletes a key from the database

**Returns:** None

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| key  | string | ID |

## Delete_all
Deletes the whole database

**Returns:** None

**Parameters:** None

## Typeof
Returns the type of the value of the key

**Returns:** Type

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| key  | string | ID |

## Math
Math with the key's value

**Returns:** Number

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| key  | string | ID |
| symbol | string | +, -, *, /, ^ |
| amount | int | Number to do math |

> You can even use add() and subtract() to make it short with key, amount as parameter...