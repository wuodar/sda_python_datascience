i = input("Podaj liczbę całkowitą: ")
i = int(i)

if i > 10:
    if i > 15:
        print("Liczba większa od 15.")
    else:
        print("Liczba mniejsza od 10.")
elif i < 5:
    print("Liczba mniejsza od 5.")
else:
    print("Liczba mniejsza od 10 i większa od 5.")