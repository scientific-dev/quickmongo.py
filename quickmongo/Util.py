# Util Class
# Some functions which are different from Base

class Util():

    # Startswith filter
    def startswith(self, data, query: str):
        result = []

        for doc in data:
            if(doc['key'].startswith(query)):
                result.append(doc)

        return result

# Convert dict to attr
class AttrDict():

    def __init__(self, arg: dict):
        for key in arg.keys():
            setattr(self, key, arg[key])

# Math Functions
def add(a: int, b:int):
    return a + b
def subtract(a: int, b:int):
    return a - b
def multiply(a: int, b:int):
    return a * b
def divide(a: int, b:int):
    return a / b
def power(a: int, b:int):
    return a ** b

# Variables
math_symbols = ['+', '-', '/', '**', '*']
math_operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    '**': power
}
