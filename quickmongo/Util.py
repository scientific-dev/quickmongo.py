# Util Class
# Some functions which are different from Base

# Filter for startswith()
def startswith(self, data, query: str):
    result = []

    for doc in data:
        if(doc['key'].startswith(query)):
            result.append(doc)

    return result

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
