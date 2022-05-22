def return_absolute_value(function):
    """
    Funkcja dekoracyjna zmieniająca wartość liczbową na wartość abosolutną.
    """
    def wrapper(*args):
        value = function(*args)
        return abs(value)
    return wrapper

@return_absolute_value
def addition(a: int, b: int) -> int:
    return a + b

while True:
    try:
        a = int(input("Podaj pierwszą liczbę całkowitą: "))
        b = int(input("Podaj drugą liczbę całkowitą: "))
        print(addition(a, b))
        break
    except ValueError:
        print("Nie podałeś dwóch liczb całkowitych. Spróbuj ponownie.")
