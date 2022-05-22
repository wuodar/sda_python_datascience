"""
Napisz funkcję, która pobiera jako pierwszy parametr operator ("+", "-", "/", "*")
a następnie *numbers, czyli dowolną liczbę liczb int/float (dowolne).
Następnie w funkcji sprawdź, jaki operator został podany, i zwróc odpowiednio
sumę/różnicę/iloraz/iloczyn
przekazanych liczb w zmiennej numbers (wykorzystaj do tego celu if/elif)
"""

from functools import reduce

def mathematical_operation(operator, *numbers):
    if operator == "+":
        return reduce(lambda a, b: a + b, numbers)
    elif operator == "-":
        return reduce(lambda a, b: a - b, numbers)
    elif operator == "*":
        return reduce(lambda a, b: a * b, numbers)
    elif operator == "/":
        return reduce(lambda a, b: a / b, numbers)
    else:
        print(f"Znak {operator} jest nieobsługiwany.")