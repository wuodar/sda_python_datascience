"""
Napisz funkcję, która wczyta dwie ostatnie linie w pliku. txt i wyświetlki
je na ekranie
(użyj funkcji seek)

def read_last_2_lines(filename):
    with open(filename) as f:
"""
# #Rozwiązanie:
# def read_last_N_lines2(file_name, N):
#     with open(file_name) as file:
#         x = len(file.readlines())
#         file.seek(x - N + 2)
#
#         for line in file:
#             print(line)
#
# read_last_N_lines2("data2.txt", 2)
#
"""
f = open("tekstunio.txt", "r")
f.seek(1)

print(f.tell())
print(f.readline())
f.close()
# line = f.readline() # czytamy pojdeyńczą linię z pliku
# rest_of_file = f.read()
#
# print(line)
# print(rest_of_file)
"""

# # Rozwiązanie z czatu
# def file_reader(file):
#     with open(file) as f:
#         g = f.readlines()
#         print(g[-2:])
#
# file_reader("plik.txt")
#

def read_file_2_lines(path):
    with open(path) as f:
        file_lines = [line for line in f] # ponieważ obiekt pliku, f jest iteratorem
        file_lines_2 = file_lines[::-2]
        line = [print(line) for line in file_lines_2]
    return line