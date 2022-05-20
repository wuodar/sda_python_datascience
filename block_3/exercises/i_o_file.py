# otwieranie pliku
# f = open("data.txt", "r")
# f.close()

#  lepiej robić to z użyciem kontekst managera
#  with open("data.txt", "r") as f: # po opuszczeniu ciała plik jest zamykany, nie musimy o tym pamiętać
#       ...

with open("data.txt", "a") as f:  # otwieramy plik w trybie append
    f.truncate(10)  # funkcja truncate "ucina" plik do określonej wartości (10 bajtów)

# printowanie wszystkich linii pliku wraz z indeksem za pomocą pętli for
def print_index_line_for_loop(file):
    for index, line in enumerate(file.readlines()):
        print(f"{index}: {line}")


# printowanie wszystkich linii pliku wraz z indeksem za pomocą pętli while
def print_index_line_while_loop(file):
    i = 0
    while line:
        print(f"{i}: {line}")
        line = file.readline()
        i += 1


# printowanie wszystkich linii pliku wraz z indeksem za pomocą list comprehension
def print_index_line_list_comp(file):
    [print(f"{i}: {line}") for i, line in enumerate(file.readlines())]


f = open("data.txt", "r")
line = f.readline()  # czytamy pojdeyńczą linię z pliku
rest_of_file = f.read()  # czytamy całą pozostałą zawartość pliku

print(line)
print(rest_of_file)

f.seek(0)
line = f.readline()
print(f"\n{line}")
f.close()


# comprehensions on lists/sets/dicts/tuples

lines = [line for line in f]  # list comprehension
# zapis powyżej jest równoważny z:
lines = []
for line in f:
    lines.append(line)


# list comprehension - pozwala na skrócony zapis pętli, wykorzystywane jest w prostych operacjiach, podczas tworzeniu obiektu list/setu/słownika
list_ = []
for i in range(10):
    list_.append(i)

list_x = [i + 2 for i in range(10)]
set_x = {i + 2 for i in range(10)}
dict_x = {f"klucz_{i}": i + 2 for i in range(10)}
tuple_x = tuple(f"item_{i}" for i in range(10))

# pętle zagnieżdżone - zagnieżdżone list comprehensions
nested_dict_comprehension = {f"{k}_{v}": v for k in range(10) for v in range(10, 20)}
slownik = dict()
for k in range(10):
    for v in range(10, 20):
        slownik[f"{k}_{v}"] = v

print(slownik)

list_comp = [i if i % 2 == 0 else 100 for i in range(-10, 10)]

print(list_comp)
