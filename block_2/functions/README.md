# Funkcje

Funkcje to reużywalne bloki kodu, które możemy wielokrotnie wykorzystywać w naszym kodzie, co pozwala na zmniejszenie linii kodu który piszemy.
Funkcja składa się z nagłówka `def nazwa_funkcji(parametr1, parametr2, ...):`, po którym następuje ciało funkcji.
Funkcja może, ale nie musi, zwrócić jakąś wartość przy użyciu słowa kluczowego `return`. Domyślnie, podczas wywołania funkcji musisz podać tyle parametrów, ile jest w nagłówku definicji funkcji. Jednak jeśli jakiś parametr ma wartość domyślną (patrz przykład), to możesz pominąć ten parametr. Parametry domyślne muszą być zawsze po parametrach wymagających wartości (po prawej stronie)

Przykład (bez return)
```python
def my_function(child3, child2, child1="Adam"): # ostatni parametr ma wartośc domyślną "Adam" - nie musimy podawać tego parametru przy wywołaniu, ale możemy.
  print("The youngest child is " + child3)

# wywołanie, sposob numer 1
my_function("Thomas", "Patrick", "Lukas") # wyprintuje: "The youngest child is Lukas" 

# wywołanie, sposob numer 2
my_function("Thomas", "Patrick") # wyprintuje: "The youngest child is Adam" 
```
## `pass` - domyślnie ciało funkcji nie może być puste, jednak jeśli z jakiegoś powodu potrzebujesz pustej funkcji, podając słowo kluczowe `pass` interpeter nie wyrzuci błędu
```python
def myfunction():
  pass
```
## `*args` i `**kwargs`
### &nbsp; `*args` - pozwala na przekazanie dowolnej ilości parametrów, do których w ciele funkcji odwołujemy się jak do listy:
```python
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")
```
### &nbsp; `**kwargs` - pozwala na przekazanie dowolnej ilości par parametrów klucz-wartość, do którego w ciele funkcji odwołujemy się jak do słownika:
```python
def my_function(**kwargs):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes") # musimy podać nazwę parametru, child1, child2...
```