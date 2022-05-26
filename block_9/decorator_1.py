"""
Napisz program pobierający od użytkownika dowolny input.
Pobrany input będzie parametrem do funkcji
    def print_reversed(input_str: str) -> None:
Funkcja ma wyprintować wejściowego stringa w odwrotnej kolejności
(np. input_str="abcde", wtedy funkcja wyprintuje "edcba").
Dodatkowo, napisz dekorator
    def make_pretty(func):
który będzie printował linię "===================="
przed i po wykonaniu się funkcji print_reversed.
Po udekorowaniu funkcji print_reversed dekoratorem make_pretty, przykładowym outputem z wykonania się programu,
dla inputu od użytkownika "abecadło", będzie następująca wartość:
    "===================="
    "ołdaceba"
    "===================="
"""


def make_pretty(func):
    def wrapper(*args, **kwargs):
        # printujemy przed wywołaniem funkcji znaki "===================="
        print("====================")
        # wywołujemy dekorowaną funkcję i wynik jej wywołania przypisujemy do zmiennej
        # żeby nie musieć wywoływać funkcji dwa razy
        res = func(*args, **kwargs)
        print("====================")
        # zwracamy wynik funkcji
        return res
    return wrapper


@make_pretty
def print_reversed(input_str: str) -> None:
    # odwracamy stringa, przy użyciu slicingu
    input_str_reversed = input_str[::-1]
    # printujemy odwrócony string
    print(input_str_reversed)


if __name__ == "__main__":
    input_str = input("Podaj dowolną wartość: ")

    print_reversed(input_str)

