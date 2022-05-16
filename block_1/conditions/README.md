# Appendix - operatory logiczne
- &nbsp; `a == b` - "a równe b", np. `a == b` - zwróci `True`, jeżeli wartość _a_ będzie równa wartości _b_, inaczej `False`
- &nbsp; `a != b` - "a różne od b", np. `a != b` - zwróci `False`, jeżeli wartość _a_ będzie równa wartości _b_, inaczej `True`
- &nbsp; `a > b` - "a większe od b", np. `a > b` - zwróci `False`, jeżeli _a_ będzie mniejsze bądź równe _b_, inaczej `True`
- &nbsp; `a < b` - "a mniejsze od b", np. `a < b` - zwróci `True`, jeżeli _a_ będzie mniejsze bądź równe _b_, inaczej `False`
- &nbsp; `a >= b` - "a większe bądź równe b", np. `a >= b` - zwróci `False`, jeżeli _a_ będzie mniejsze od _b_, inaczej `True`
- &nbsp; `a <= b` - "a mniejsze bądź równe b", np. `a <= b` - zwróci `False`, jeżeli _a_ będzie większe od _b_, inaczej `True`
- &nbsp; `a > 0 and b > 0` - "a większe od 0 i b większe od 0", np. `a > 0 and b > 0` - zwróci `False`, jeżeli _a_ bądź _b_ (bądź obie zmienne) mniejsze od 0, inaczej `True`
- &nbsp; `a > 0 or b > 0` - "a większe od 0 lub b większe od 0", np. `a > 0 or b > 0` - zwróci `False`, jeżeli ani _a_ ani _b_ nie będzie większe od 0, inaczej `True`
- &nbsp; `not(a > 0)` - zaprzeczneie, "nie prawda, że a większe od 0", np. `not(a > 0)` - zwróci `False`, jeżeli _a_ będzie większe od 0, inaczej `True`
- &nbsp; `a is b` - "a jest b", np. `a is b` - zwróci `True`, jeżeli _a_ będzie wskazywać na ten sam obiekt co _b_, inaczej `False`
- &nbsp; `a is not b` - "a nie jest b", np. `a is not b` - zwróci `False`, jeżeli _a_ będzie wskazywać na ten sam obiekt co _b_, inaczej `True`

# If else - kondycje warunkowe
Kondycje warunkowe wykorzystywane są do sprawdzania wartości logicznych zmiennych bądź wyrażeń, np. `10 < 5` jest wyrażeniem logicznym, a jego wartość to `False`, ponieważ _5_ nie jest większe od _10_.
Dzięki kondycjom warunkowym, możemy sterować przepływem flow naszego programu.
Na przykład, możemy pobrać od użytkownika input i na jego podstawie sprawdzić czy jest pełnoletni:
```python
age = input("Podaj swój wiek: ")

if age > 18:
    print("Pełnoletni")
else:
    print("Niepełnoletni")
```

Możemy również rozwijać takie warunkowanie o wiele różnych kondycji, i na ich podstawie kontrolować działanie programu.
```python
height = input("Podaj swój wzrost w cm: ")

if height > 185:
    print("Bardzo wysoki")
elif height > 175: # elif to skrót od else if, czyli w przypadku, gdy wcześniejsze kondycje warunkowe nie zostaną spełnione, przejdź do tego bloku i sprawdź kolejny warunek
    print("Wysoki")
else:
    print("Niski")
```

Możemy tworzyć zagnieżdżone kondycje warunkowe.
```python
age = input("Podaj swoj wiek: ")
sex = input("Podaj płeć ('k' - kobieta lub 'm' - mężczyzna): ")

if age > 18:
    if sex == 'k':
        print("Dorosła kobieta")
    else:
        print("Dorosły mężczyzna")
elif age > 10:
    if sex == 'k':
        print("Nastolatka")
    else:
        print("Nastolatek")
else:
    print("Dziecko")
```