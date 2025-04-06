import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def power(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Error! Cannot calculate the square root of a negative number."
    else:
        return math.sqrt(x)

def modulo(x, y):
    if y == 0:
        return "Error! Division by zero for modulo."
    else:
        return x % y 