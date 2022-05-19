"""
Napisz funkcje, która wczyta dwie ostatnie linie w pliku .txt i wyswietli je na ekranie

def read_last_2_lines(filename):
    with open(filename) as f:
        ....

"""

def read_last_N_lines(file_name, N):
    with open(file_name) as file:
        for line in file.readlines()[-N:]: # używamy funkcji readlines() która zwraca listę linii w pliku, oraz używamy slicingu do wyciągnięcia elementów od przedostatniego (-1) elementu do końca listy (:)
            print(line)

# rozwiązanie przy użyciu list comprehension
def read_last_N_lines2(file_name, N):
    with open(file_name) as file:
        [print(line) for line in file.readlines()[-N:]]
