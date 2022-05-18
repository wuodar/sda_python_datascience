### Lista metod wbudowanyhc pythona: https://www.w3schools.com/python/python_ref_functions.asp

# Typy danych
## Łańcuchy znaków:	str
- str - string to łańcuch znaków. aby stworzyć zmienną typu string, musimy podać jej wartośc w cudzysłowie - _x = "jakas wartosc"_, albo _x = 'jakas wartosc'_.
- Lista metod klasy str: https://www.w3schools.com/python/python_ref_string.asp
## Typy numeryczne:	int, float, complex
- int - liczby całkowite. Tworząc zmienną i podając jako jej wartośc liczbę całkowitą, stworzymy zmienną typu int, np. _x = 5_.
- float - liczba zmiennoprzecinkowa, czyli taka, która poza częścią całkowitą zawiera część ułamkową, np. _x = 5.54_.
- complex - liczba zespolona, czyli taka, która składa się z dwóch części - rzeczywistej oraz urojonej, zapis jest następujący: _x = 2 + 3j_.
## Typy sekwencyjne:	list, tuple
### &nbsp; Lista
- listy są zbiornikami na dane, możemy w nich przechowywać wiele elementów, np. _x = [1, 2, 3, "abc", [4, 5, 6]]_
- lista zachowuje kolejność dodawanych elementów
- lista pozwala na przechowywanie wielu takich samych elementów, np. _x = [1, 1, 1]_
- można dodawać (metoda _.append()_) oraz usuwać (metoda _.remove()_) elementy w liście
- aby pobrać element z listy, musimy podać indeks/indeksy, które chcemy z niej wyciągnąć. Np. aby wyciągnąć z listy _x_ pierwszy element, napiszemy _x[0]_
 - Lista metod klasy list: https://www.w3schools.com/python/python_ref_list.asp
### &nbsp; Tupla
- tupla, podobnie jak lista, jest zbiornikiem na dane, różnicą jest sposób zapisu, zamiast nawiasóœ kwadratowych, wartości tupli zawarte są w nawiasach okrągłych, np. _x = (1, 2, 3, ["abc"], ("cda", 3))_
- tupla, tak jak lista, zachowuje kolejność dodanych elementów
- to co różni tuple od list, to fakt, iż są one niezmienialne - oznacza to, że kiedy stworzymy obiekt tupli jeden raz, to nie możemy potem dodawać ani usuwać dodanych elementów.
- Lista metod klasy tuple: https://www.w3schools.com/python/python_ref_tuple.asp
## Typ mappingowy:	dict
- Słownik jest typem danych przechowującym pary wartości _klucz:wartość_, np. _x = {"klucz1": "wartosc_1, "klucz_2": 2}_
- Klucze słownika muszą być unikalne, jeśli podamy dwie pary wartości o tym samym kluczu, to zostaną one nadpisane przez ostatnią parę.
- Kolejność elementów dodawanych do słownika jest zachowana dla Pythona w wersji wyższej bądź równej 3.7
- Aby pobrać ze słownika element musimy podać jego klucz, np. _x["klucz_1"]_
- Lista metod klasy dict: https://www.w3schools.com/python/python_ref_dictionary.asp
## Set Types:	set
- set jest typem podobnym do listy, również może przechowywać wiele elementów.
- set różni się od listy tym, że nie zachowuje kolejności, nie można zmienić (nadpisać) elementów w secie, ale można je dodawać bądź usuwać. Dodatkowo, elementy setu nie są indeksowane, co oznacza, że nie możemy wyciągnąć z setu wartości poprzez podanie jej indeksu, jak to jest w przypadku list i tupli.
- Lista metod klasy set: https://www.w3schools.com/python/python_ref_set.asp
## Boolean Type:	bool
- służy do przechowywania wartości _True/False_ (prawda/fałsz)
- jest wynikiem ewaluacji wyrażeń oraz zmiennych
## Binary Types:	bytes, bytearray
- służą do przechowywania oraz manipulacji wartościami binarnymi
- aby stworzyć obiekt bytes, musimy określic kodowanie danych wejściowych, np. _byte_message = bytes("jakis tekst, 'utf-8')_, gdzie _utf-8_ to sposób kodowania znaków wykorzystywany w informatyce.
- _bytes_ oraz _bytearray_ służą do przechowywania listy bajtów, przy czym każdy bajt reprezentowany jest za pomocą wartości od 0 do 255
- różnica pomiędzy _bytes_ oraz _bytearray_ to fakt, iż po stworzeniu obiektu _bytes_ nie możemy zmienić jego zawartości, natomiast _bytearray_ nam na to pozwala
## None Type:	NoneType
- NoneType oznacza brak wartości. Np. w przypadku funkcji, która nie zwraca żadnej wartości, jeśli chcielibyśmy przypisać wynik wywołania takiej funkcji do zmiennej, to była by to zmienna typu _NoneType_ o wartości _None_ (w innych językach nazywane _null_)
# Konwersja typów danych
Konwersja typów danych polega na zamianie jednego typu zmiennej na inny. Przykładowo, mając zmienną _x = 10.55_ możemy chcieć zmienić jej typ (float, bo jest to liczba zmiennoprzecinkowa) na liczbę całkowitą (int).
Aby tego dokonać, musimy wywołać konstruktor (konstruktor to taka funkcja klasy, która pozwala na stworzenie nowego obiektu tej klasy, poprzez podanie wartości wymaganych do jego stworzenia) klasy _int_ oraz podać naszą zmienną _x_ typu _float_. Robi się to w taki sposób: _x = int(10.45)_, wynikiem będzie wartość 10, ponieważ konwertując liczbę zmiennoprzecinkową do liczby całkowitej pozbawiamy ją części ułamkowej.
Python pozwala na konwersje stringów do liczb, np. _x = int("10")_, albo _x = float("11.45)_. Ponadto, możemy konwertować listy do setów, bądź sety do list, tuple do list i odwrotnie. Podobnie, jak w przypadku liczb i stringów, musimy wywołać konstruktor danej klasy, np. _x = set([1, 2, 3])_ - konwersja listy do seta.