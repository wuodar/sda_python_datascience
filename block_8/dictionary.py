from typing import Dict, List, Any
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

        dic_return ={f"{n}": f"{i+1}" for i, n in enumerate(input_string)}
        return dic_return

# Any oznacza dowolny typ
def get_keys_with_largest_values(input_dict: Dict[Any, float]) -> List[Any]:
    print(input_dict)
    print(sorted(input_dict.values(), reverse=True))
    return input_dict



if __name__ == "__main__":
    input_str = input("1) Podaj dowolnego stringa: ")
    output_dict = create_dict(input_str)
    print(f"Zadanie 1, wynik: {output_dict}")
    print(f"Zadanie 2, wynik: {get_keys_with_largest_values(output_dict)}")

