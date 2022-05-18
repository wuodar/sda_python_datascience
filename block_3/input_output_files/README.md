# Operacje na plikach

### Tryby odczytu plików
- `r` - Otwiera plik tylko do odczytu. Wskaźnik pliku jest umieszczany na początku pliku. (domyślny)
- `w` - Otwiera plik do zapisu. W przypadku, gdy plik nie istnieje, to zostanie utworzony, jeśli istnieje to jego zawartość zostanie usunięta
- `a` - Służy do dopisywania danych do pliku. W przypadku, gdy plik nie istnieje, to zostanie utworzony, jeśli istnieje to nowa zawartość zostanie dopisana. (Kursor ustawia się na końcu pliku)
- `x` - Do tworzenia. Operacja nie powiedzie się, jeśli plik istnieje
- `t` - Tryb tekstowy (domyślny)
- `b` - Tryb binarny
- `+` - Oznacza, że po otwarciu pliku kursor ustawi się na jego końcu. (Domyślnie kursor ustawia się na początku)

Tryby można łączyć, np. tryb `ab` oznacza otwarcie pliku binarnego do zapisu, przy czym plik, jeśli istnieje, nie zostanie skrócony, a dopisywanie będzie się odbywać na końcu pliku.
Innym przykładem jest tryb `wb+` - oznacza otwarcie pliku zarówno w celu czytania i wpisywania, w formacie binarnym. Nadpisuje zawartośc istniejącego pliku, jeśli istnieje, w przeciwnym wypadku tworzy nowy plik.

### Metody obiektów File
| Metoda       | Opis                                                          |
|--------------|---------------------------------------------------------------|
| read()       | Zwraca zawartość pliku                                        |
| readline()   | Zwraca pojedyńczą linię z pliku                               |
| readlines()  | Zwraca listę linii z pliku                                    |
| seek()       | Zmienia pozycję kursora                                       |
| truncate()   | Zmienia długość pliku do określonej wartości                  |
| write()      | Wpisuje do pliku string podany jako argument                  |
| writelines() | Wpisuje listę stringów (każdy element w nowej linii) do pliku |
