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
    def wrapper(*args):
        print("====================")
        res = func(*args)
        print("====================")
        return res
    return wrapper


@make_pretty
def print_reversed(input_str: str) -> None:
    print(input_str[::-1])


if __name__ == "__main__":
    input_str = input("Podaj dowolną wartość: ")

    print_reversed(input_str)

