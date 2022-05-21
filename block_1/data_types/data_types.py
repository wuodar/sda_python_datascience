# typy proste
integer = 10  # całkowity, numeryczny, może przyjąć wartości z zakresu
float_ = 10.45  # zmiennoprzecinkowy, numeryczny
string = "abc"  # łańcuch znaków
boolean = True  # logiczny - prawda/fałsz

numeric_sum = integer + float_
print(numeric_sum)

# nie możemy dodawać stringa do typu numerycznego
# string_plus_int = integer + string # wyrzuci błąd
# print(string_plus_int)

print(type(integer), type(float_), type(string), type(boolean))

# castowanie typów prostych (castowanie-konwersja typu)
print(type(numeric_sum))

numeric_sum_to_int = int(numeric_sum)
print(numeric_sum_to_int)

string_value = "20.10"

# w przypadku castowania liczby zmiennoprzecinkowej ze stringa do int'a, nie możemy tego zrobić bezpośrednio, musimy: 1. Przekonwertować string'a do float'a (liczby zmiennoprzecinkowej), 2. Wyciągnąć część całkowitą (float->int)
print(int(float(string_value)))

numeric_sum_float_from_int = float(numeric_sum_to_int)
print(numeric_sum_float_from_int)

# Complex numbers
a = 2 + 3j
print(type(a))

# None - inaczej null, jest to "pusta" wartość, a w zasadzie jej brak
x = None
print(type(x))

# listy

# tworzenie listy przy pomocy klamr
list_1 = [1, 2, 3, "str", 10.35, [10, 10]]
print(list_1)
print(type(list_1))
# tworzenie listy przy pomocy konstruktora klasy
list_2 = list([1, 2, 3])
print(list_2)
# kolejnosc elemntów w liscie jest zawsze taka sama jak podczas tworzenia


# sety

# tworzenie przy pomocy klamr
set_1 = {2, 1, 3, 4, 2}
print(set_1)
set_2 = set(list_2)
print(set_2)
# kolejność elementów podczas tworzenia nie jest zachowana
# wszystkie wartości muszą być unikalne, w przypadku powtórzeń elemnty będące takimi samymi są nadpisywane przez ostatni elemnt występującyt podczas tworzenia setu

# wyciągniecie elemntu z listy
item = list_1[0]
print(item)

# slicing
sublist = list_1[
    1:5
]  # wyciagajac elenty w list, i podajac zakres 1:5, wyciagamy de facto wartości o indeksach ze zbioru [1, 5)
print(sublist)

# ogólny wzór na slicing: lista[start:stop:krok]
sublist_every_two = list_1[1:6:2]
print(sublist_every_two)

# dodawanie do listy
list_1.append("nowy_element")
print(list_1)
list_1.pop(3)
print(list_1)
updated_list = list_2.sort(reverse=True)
print(list_2)

# mutability list, przyklad
def append_to_list(list):
    copy_list = list.copy()
    a = 10
    copy_list.append(a)
    return copy_list


list_3 = [5]
list_4 = append_to_list(list_3)

print(list_4)
print(list_3)

# immutability stringow, przyklad
def append_to_string(string):
    a = "10"
    string = string + a
    return string


base_string = "abc"
updated_string = append_to_string(base_string)
print(base_string)
print(updated_string)

set_3 = {2, 1, 3, 4, 2}
set_3.pop()
print(set_3)
set_3.add(111)

# słownik - struktura, w której występują pary (klucz, wartość).
#   - klucze muszą być unikalne wewnątrz danego słownika, w innym przypadku, wartości powtarzające się zostaną nadpisane
#   - wartości mogą się powtarzać
a = 10.5
dictionary = {"key1": "value", "key1": [1, 2, 3], a: "value3"}

message = "Hello"
bytes_ = bytes(message, "utf-8")

print(bytes_)

int_list = [1, 2, 3, 4, 5]
byte_ints = bytearray(int_list)
print(byte_ints)

# Operatory
#   +
#   -
#   /
#   *

print("Hello" + " world")
print("Hello " * 3)
print(10 + 7.5)

list_1 = [1, 2, 3]
list_2 = [4, 5, 6]

print(list_2 + list_1)

set_1 = {1, 2, 3}
set_2 = {1, 2, 6}
