def debug(func):
    def wrapper(*args, **kwargs):
        a = f"Funkcja {func.__name__} zwrocila {args}  "
        return a
    return wrapper

@debug
def func(a,b,c):
    return a + b * c

print(func(3,4,5))