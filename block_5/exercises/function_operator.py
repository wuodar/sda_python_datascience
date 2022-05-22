"""
Napisz funkcję, która pobiera jako pierwszy parametr operator ("+", "-", "/", "*")
a następnie *numbers, czyli dowolną liczbę liczb int/float (dowolne).
Następnie w funkcji sprawdź, jaki operator został podany, i zwróc odpowiednio
sumę/różnicę/iloraz/iloczyn
przekazanych liczb w zmiennej numbers (wykorzystaj do tego celu if/elif)
"""

operator = input("Podaj operator (+, -, /, *): ")
count = int(input("Podaj liczbę cyfr do wykonania operacji: "))

number_list = []
for i in range(count):
    number = int(input("Podaj liczbę: "))
    number_list.append(number)

def function_operator(operator, *numbers):
    print("Podano operator: ", operator)
    print(number_list)
    result = 0
    for number in number_list:
        if operator == "+":
            result = result + number
        elif operator == "-":
            number -= number
        elif operator == "*":
            number *= number
        elif operator == "/":
            number /= number

    return number

print(function_operator(operator, number_list))


