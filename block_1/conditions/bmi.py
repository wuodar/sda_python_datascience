bmi = input("Podaj swoje bmi: ") # pobranie bmi od użytkownika
bmi = int(bmi) # ponieważ wartość zwrócona przez funkcje input() to string, musimy go przekonwertować na int

if bmi < 18.5: # jeżeli bmi jest mniejsze od 18.5
    result = "niedowaga"
elif bmi > 24.5: # jeżeli bmi większe od 24.5, ale dodatkowo jeżeli bmi jest mniejsze od 18.5
    result = "nadwaga"
else: # w przypadku nie spełnienia żadnego z wcześniejszych warunków
    results = "waga poprawna"
