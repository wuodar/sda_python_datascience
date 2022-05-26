""""
Napisz funkcję
    def divide(a: float, b: float) -> float:
Dzielącą dwie liczby o zwracającą wynik dzielenia.
Następnie dopisz dekorator
    def smart_divide(func):
który sprawdz, czy parametr b nie jest równy 0 (nie dzielimy przez 0!).
Jeśli tak, wyprintuj "Whoops! cannot divide" i zwróć z funkcji wartość None.
"""

def smart_divide(func):
    def wrapper(a, b):
        if a == 0:
            print("Whoops! cannot divide")
            return None
        if b == 0:
            print("Whoops! cannot divide")
            return None
        return func(a, b)
        # if a == 0 or b == 0:
        #     print("Whoops! cannot divide")
        #     return None

    return wrapper


@smart_divide
def divide(a: float, b: float) -> float:
    return a / b


if __name__ == "__main__":
    a = 3
    b = 0
    res = divide(a, b)
