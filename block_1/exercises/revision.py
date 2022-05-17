# lista, set, słownik, range - możemy po nich iterować
# for i in my_iterator:
#   ciało pętli, inaczej blok
#   break # zatrzymuje wykonywanie się pętli, to oznacza, że po wywołaniu słowa
#         # kluczowego "break" nie wykona się ani jedna iteracja więcej w naszej pętli
#   continue # nie wykonujemy instrukcji znajdujących się w pętli poniżej słowa kluczowego "continue",
#            # ale przechodzimy do następnej iteracji pętli

# some_list = [1,2,3]
#  i = 0
# while warunek_logiczny: # jeżeli waurnek logiczny jest prawdziwy (czyli ma wartość True), to pętla się wykona
#   break oraz continue można używać w ciele pętli while, tak jak w pętli for
#   i = i + 1
#   some_list[i]

# kluczem może być dowolny obiekt hashowalny (int, float, bool, string, tuple, set)
some_dict = {
    "k1": "w1",
    "k2": "w2",
    ("k3", "k4"): "w3"
}


# for k, v in some_dict.items(): # metoda items() jest metodą klasy dict, i zwraca set którego elementami są pary tupli (klucz, wartość)
#     print("klucz=", k)
#     print("wartosc=", v)

string = f"""Potęgą liczby 5 jest {some_dict["5"]}""" # w przypadku tworzenia stringów oraz fstringow, musimy pamietac o rozroznianiu cudzysłowów występujących w stringu, oraz oznaczających jego początek i koniec
print(string)


frequences = [1,2,3]
fruits = ["banana", "apple", "orange"]

for fruit, freq in zip(fruits, frequences): # funkcja zip pozwala na łączenie list/setów/słowników i równoległym iterowaniu po nich
    print(f"There are {freq} {fruit}")


# uzycie slowa kluczowego "in" jako zapobieganie wyrzuceniu bledu przy metodzie .index(), w przypadku gdy dana wartosc nie wystepuje w liscie
city_list = ["Warszawa", "Poznań", "Łódź", "Kraków"]

def get_index_if_exists(list_in, value): # nagłówek funkcji, przyjmujemy 2 parametry
    if value in list_in: # sprawdzamy, czy element występuje w liście
        return list_in.index(value)  # jeżeli tak, to zwracamy index elementu w liście
    else: # jeśli warunek nie został spełniony
        return -1 # zwracamy wartość -1, oznaczającą, że element nie występuje w liście

value_in = input("Podaj miasto, z którego pochodzisz: ")

index_of_city = get_index_if_exists(city_list, value_in)

if index_of_city != -1:
    print(f"Bus odwiedzi twoje miasto jako {index_of_city+1}")
else:
    print("Niestety, bus nie odwiedzi twojego miasta.")
