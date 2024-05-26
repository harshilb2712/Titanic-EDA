def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0: return 'Division not allowed'
    else     : return a / b
    
def remainder(a, b):
    return a % b

def flooring(a):
    import math
    return math.floor(a)
    
pi = 3.14
e = 2.7

def some():
    print('hello')
    
print('This is a module')
some()
