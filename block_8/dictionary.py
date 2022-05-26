from typing import Dict, List, Any
from collections import Counter
"""
1)
Napisz funkcję, która pobierze od użytkownika dowolny input, a następnie stworzy z niego słownik.
Kluczami powinny być poszczególne znaki w stringu, a wartościami kolejne wartości od 1 do len(string)
Wyświetl na końcu funkcji stworzony słownik.

    Przykładowy input: kajakarz

    Output: {'k': 4, 'a': 5, 'j': 2, 'r': 6, 'z': 7}
    
2)
Napisz funkcję, która przyjmie jako parametr słownik, w którym wartości będą floatami.
Funkcja ma zwrócić listę trzech kluczy, dla których wartości w słowniku są największe.
Klucze mają być posortowane, od najmniejszego do największego (względem wartości danej pary (klucz, wartość) )

    Przykładowy słownik: {'k': 4, 'a': 5, 'j': 2, 'r': 6, 'z': 7}
    Output: ['a', 'r', 'z']
"""


def create_dict(input_string: str) -> Dict[str, int]:
    dictionary = dict()
    for i in range(len(input_string)):
        dictionary[input_string[i]] = i+1

    return dictionary

def create_dict2(input_string: str) -> Dict[str, int]:
    dictionary = dict()
    for i, v in enumerate(input_string):
        dictionary[v] = i + 1

    return dictionary

def create_dict3(input_string: str) -> Dict[str, int]:
    dictionary = {value: index+1 for index, value in enumerate(input_string)}

    return dictionary

# Any oznacza dowolny typ
def get_keys_with_largest_values(input_dict: Dict[Any, int]) -> List[Any]:
    d = Counter(input_dict).most_common(3)
    return [x[0] for x in d][::-1]

def get_keys_with_largest_values2(input_dict: Dict[Any, int]) -> List[Any]:
    sorted_values = sorted(input_dict.values())
    sorted_dict = dict()

    for val in sorted_values:
        for key in input_dict:
            if input_dict[key] == val:
                sorted_dict[key] = input_dict[key]
                break
    
    sorted_keys = list(sorted_dict.keys())
    return sorted_keys[-3:]
 

if __name__ == "__main__":
    #input_str = input("1) Podaj dowolnego stringa: ")
    input_str = "kajakarz"
    output_dict = create_dict(input_str)
    print(f"Zadanie 1, wynik: {output_dict}")
    print(f"Zadanie 2, wynik: {get_keys_with_largest_values(output_dict)}")

    #print(get_keys_with_largest_values2(output_dict))

