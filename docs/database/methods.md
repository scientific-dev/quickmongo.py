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

**Returns:** None

**Parameters:**

| Name  | Type   | Description |
|-------|--------|-------------|
| key   | string | ID          |
| value | any    | data        |

## Get

**Returns:** Any

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| key  | string | ID |

## All

**Returns:** List

**Parameters:** None

## Startswith

**Returns:** List

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| text | string | To filter with startswith |

## Delete

**Returns:** None

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| key  | string | ID |

## Delete_all

**Returns:** None

**Parameters:** None

## Typeof

**Returns:** Type

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| key  | string | ID |

## Math

**Returns:** Number

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| key  | string | ID |
| symbol | string | +, -, *, /, ^ |
| amount | int | Number to do math |