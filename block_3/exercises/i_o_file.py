f = open("data.txt")

line = f.readline() # czytamy pojdeyńczą linię z pliku
rest_of_file = f.read()

print(line)
print(rest_of_file)

