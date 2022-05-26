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
        #div = func(a, b)
        if b != 0:
            div = func(a, b)
            return div
        else:
            print("Whoops! cannot divide")
            return None
        return div
    return wrapper



@smart_divide
def divide(a: float, b: float) -> float:
    result = a/b
    return result


if __name__ == "__main__":
    a = 3
    b = 1
    res = divide(a, b)
    print(res)
