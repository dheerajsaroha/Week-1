# Build a custom python module
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b!= 0:
        return a/b
    else:
        return "Enter a valid value of b!"

def even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"