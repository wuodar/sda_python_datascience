"""
Napisz program, który zwróci wartość bezwzgledna liczby pobranej od uzytkowinika.
Progrma powinien pytać o tę liczbę tak długo, aż nie zostanie ona poprawnie podana.

Pamiętaj, że użytkownik nie zawsze wpisze wartość numeryczną, może też wpisać np. "kalafior".
Sprawdź, co wtedy się stanie i pamiętaj o obsłudze wyjątków.
"""

# def absolute_value():
while True:
    try:
        value = input("Podaj liczbę: ")
        value = float(value)
        result = abs(value)
        print(f"Wartość bezwględna podanej liczby: {result}")
        break
    except ValueError as e:
        print(f"Wiadomosc o błędzie: {e.args[0]}")
        print("Podana wartość jest niepoprawna. Proszę, podaj liczbę rzeczywistą.")
