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
        print("====================")
        f = func(*args, **kwargs)
        print("====================")
        return f
    return wrapper

@make_pretty
def print_reversed(input_str: str) -> None:
    reversed_input_str = input_str[::-1]
    print(reversed_input_str)


if __name__ == "__main__":    #tutaj zaczyna się wykonywanie programu
    input_str = input("Podaj dowolną wartość: ")
    print_reversed(input_str)

