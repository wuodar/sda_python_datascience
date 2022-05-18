# Operatory 
Operatory służą do wykonywania operacji na zmiennych i ich wartościach.
Najważniejsze operatory zostały opisane poniżej

### 1. Operatory Arytmetyczne
- `+` operator dodawania, np. `5 + 3` - zwróci `8` (typy numeryczne), `"Hello " + "World"` zwróci `"Hello World"`(typ str), `[1, 2, 3] + [4, 5, 6]` zwróci `[1, 2, 3, 4, 5, 6]` (typ list, tuple, ale już set i dict nie!!!)
- `-` operator odejmowania, np. `5 - 3` - zwróci `2` (typy numeryczne), operator nie działa dla typu str oraz typów złożonych (list, tuple, set, dict)
- `*` operator mnożenia, np. `5 * 3` - zwróci `15` (typy numeryczne), `"Hello" * 3` zwróci `"HelloHelloHello"` (typ str), `[1] * 3` zwróci `[1, 1, 1]` (typ list, tuple)
- `/` operator dzielenia, np. `5 / 3` - zwróci `1.6666666666666667` (typy numeryczne), operator nie działa dla typu str oraz typów złożonych (list, tuple, set, dict)
- `%` operator modulo, np. `5 % 3` - zwróci `2` (reszta z dzielenia) (typy numeryczne), operator nie działa dla typu str oraz typów złożonych (list, tuple, set, dict)
- `**` operator potęgowania, np. `5 ** 3` - zwróci `125` (typy numeryczne), operator nie działa dla typu str oraz typów złożonych (list, tuple, set, dict)
- `//` operator floor division (część całkowita z dzielenia), np. `5 // 3` - zwróci `1` (typy numeryczne), operator nie działa dla typu str oraz typów złożonych (list, tuple, set, dict)

### 2. Operatory Przypisania
Pozwalają na skrócony zapis w przypadku nadpisywania wartości zmiennej
| Operator | Przykład użycia | Oznacza to samo, co | Typ działania                                         |
|----------|-----------------|---------------------|-------------------------------------------------------|
| =        | x = 5           | x = 5               | przypisanie wartości (5) do zmiennej (x)              |
| +=       | x += 3          | x = x + 3           | dodawanie                                             |
| -=       | x -= 3          | x = x - 3           | odejmowanie                                           |
| *=       | x *= 3          | x = x * 3           | mnożenie                                              |
| /=       | x /= 3          | x = x / 3           | dzielenie                                             |
| %=       | x %= 3          | x = x % 3           | operacja modulo (reszta z dzielenia)                  |
| //=      | x //= 3         | x = x // 3          | operacja floor division (część całkowita z dzielenia) |
| **=      | x **= 3         | x = x ** 3          | potęgowanie                                           |

# Operatory logiczne
- &nbsp; `a == b` - "a równe b", np. `a == b` - zwróci `True`, jeżeli wartość _a_ będzie równa wartości _b_, inaczej `False`
- &nbsp; `a != b` - "a różne od b", np. `a != b` - zwróci `False`, jeżeli wartość _a_ będzie równa wartości _b_, inaczej `True`
- &nbsp; `a > b` - "a większe od b", np. `a > b` - zwróci `False`, jeżeli _a_ będzie mniejsze bądź równe _b_, inaczej `True`
- &nbsp; `a < b` - "a mniejsze od b", np. `a < b` - zwróci `True`, jeżeli _a_ będzie mniejsze bądź równe _b_, inaczej `False`
- &nbsp; `a >= b` - "a większe bądź równe b", np. `a >= b` - zwróci `False`, jeżeli _a_ będzie mniejsze od _b_, inaczej `True`
- &nbsp; `a <= b` - "a mniejsze bądź równe b", np. `a <= b` - zwróci `False`, jeżeli _a_ będzie większe od _b_, inaczej `True`
- &nbsp; `a > 0 and b > 0` - "a większe od 0 i b większe od 0", np. `a > 0 and b > 0` - zwróci `False`, jeżeli _a_ bądź _b_ (bądź obie zmienne) mniejsze od 0, inaczej `True`
- &nbsp; `a > 0 or b > 0` - "a większe od 0 lub b większe od 0", np. `a > 0 or b > 0` - zwróci `False`, jeżeli ani _a_ ani _b_ nie będzie większe od 0, inaczej `True`
- &nbsp; `not(a > 0)` - zaprzeczneie, "nie prawda, że a większe od 0", np. `not(a > 0)` - zwróci `False`, jeżeli _a_ będzie większe od 0, inaczej `True`
- &nbsp; `a is b` - "a jest b", np. `a is b` - zwróci `True`, jeżeli _a_ będzie wskazywać na ten sam obiekt co _b_, inaczej `False`
- &nbsp; `a is not b` - "a nie jest b", np. `a is not b` - zwróci `False`, jeżeli _a_ będzie wskazywać na ten sam obiekt co _b_, inaczej `True`
