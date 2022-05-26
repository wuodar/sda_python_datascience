"""
Napisz dekorator double_result, który podwaja wartość zwracaną przez funkcję add.

Przykład:
    def add(a,b):
        return a+b

    add(5,5) # 10

    @double_result
    def add(a,b):
        return a+b

    add(5,5) # 20
"""

def double_result(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) * 2
    return wrapper

@double_result
def add(a, b):
    return a + b
