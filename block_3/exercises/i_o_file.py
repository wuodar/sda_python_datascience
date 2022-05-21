f = open("data.txt")

line = f.readline() # czytamy pojdeyńczą linię z pliku
rest_of_file = f.read()

print(line)
print(rest_of_file)

"""
Napisz funkcje, która wczyta dwie ostatnie linie w pliku .txt i wyswietli je na ekranie
(użyj funkcji seek)

def read_last_2_lines(filename):
    with open(filename) as f: