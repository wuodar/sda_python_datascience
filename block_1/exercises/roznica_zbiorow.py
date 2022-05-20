"""
    Poproś użytkownika o podanie elementów dla dwóch list. # input()
    W tym celu użytkownik najpierw dodaje do pierwszej listy, aż wpisze zero. # if else
    Następnie dodaje do drugiej listy, aż znów wpisze zero. # if else
    Twoim zadaniem jest wyświetlić posortowaną różnicę symetryczną zbiorów utworzonych z tych dwóch list.

    Przyklad:
        input:
            list_1 = [2, 1, 3, 4, 5]
            list_2 = [3, 4, 5, 6, 7]

        roznica symetryczna tych list (list_1-list_2) = [2, 1, 6, 7]

        output: [1, 2, 6, 7]
"""

list_1 = []
list_2 = []

input_val = 1  # nie chcemy 0, więc podajemy dowolną inną wartość
print("Lista numer 1")
while input_val != 0:
    input_val_str = input("Podaj liczbe: ")  # pobieramy od użytkownika wartość o typie str
    input_val = int(input_val_str)  # konwertujemy str do liczby całkowitej (int)
    list_1.append(input_val)  # dodajemy do listy

print("Lista numer 2")
input_val = 1  # nie chcemy 0, więc podajemy dowolną inną wartość

while input_val != 0:
    input_val_str = input("Podaj liczbe: ")  # pobieramy od użytkownika wartość o typie str
    input_val = int(input_val_str)  # konwertujemy str do liczby całkowitej (int)
    list_2.append(input_val)  # dodajemy do listy


#   ROZWIAZANIE NUMER 1 - PRZY UZYCIU LIST
symmetric_difference = []  # tworzymy pustą listę
for i in list_1:  # iterujemy po elementach pierwszej listy
    if i not in list_2:  # not in - sprawdz czy element z listy list_1 (i) nie występuje w liście list_2
        symmetric_difference.append(i)  # dodanie elementu do listy, w przypadku spełnionego warunku z instrukcji if
for j in list_2:
    if j not in list_1:  # not in - sprawdz czy element z listy list_2 (i) nie występuje w liście list_1
        symmetric_difference.append(j)  # dodanie elementu do listy, w przypadku spełnionego warunku z instrukcji if
#   KONIEC ROZWIĄZANIA NUMER 1

#   ROZWIAZANIE NUMER 2 - PRZY UZYCIU METODY KLASY set()
# symmetric_difference = set(list_1).symmetric_difference(set(list_2))
# symmetric_difference = list(symmetric_difference)
#   KONIEC ROZWIĄZANIA NUMER 2


symmetric_difference.sort()  # na koniec sortujemy listę
print(symmetric_difference)  # wyprintowanie wyniku
