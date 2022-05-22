"""
Stwórz dekorator o nazwie "debug", która podczas wywoływaia funkcji będzie wyświetlał informację o jej nazwie, przekazanych argumentach oraz zwracanym wyniku.
"""

def debug(func):
    def wrapper(*args):
        returned_value = func(*args)
        print(f"Nazwa wywoływanej funkcji: {func.__name__}", end=", ")
        print(f"która zwraca: {returned_value}, a przyjmuje argumenty {args}.")
        return returned_value
    return wrapper


@debug
def operation(a: int, b: int, c: int) -> int:
    return a + b * c

operation(2,3,4)