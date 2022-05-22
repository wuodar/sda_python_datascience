"""
Stwórz dekorator o nazwie debug, który podczas wywoływania funkcji będzie
wyświetlał informacje o jej nazwie, przekazanych parametrach oraz zwracanym wyniku.
"""

def debug(function):
    def wrapper(*args, **kwargs):
        print(function.__name__)
        print(args, kwargs)
        result = function(*args, **kwargs)
        return result
    return wrapper

@debug
def func(a, b, c):
    return a + b * c
print(func(3, 2, 4))

"""
def debug(function):
    def wrapper(*args, **kwargs):
        print(function.__name__)
        print(args, kwargs)
        result = function(*args, **kwargs)
        return result
    return wrapper

@debug
def func(a, b, c):
    return a + b * c
print(func(1, 2, 3))
"""