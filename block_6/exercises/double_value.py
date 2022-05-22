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

def double_result(function):
    def double_result_of_function(*args, **kwargs):
        return function(*args) * 2
    return double_result_of_function

@double_result
def add(a, b):
    return a + b

print(add(2, 2))