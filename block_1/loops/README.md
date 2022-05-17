# Pętle

Python pozwala na korzystanie z dwóch typów pętli
### &nbsp; `for` loop
- &nbsp; pętla `for` wykonuje się iteracyjnie - programista ustala ile razy ma się wykonać pętla
### &nbsp; `while` loop
- &nbsp; pętla `while` wykonuje się warunkowo - programista ustala warunek, który musi zostać spełniony aby pętla while się wykonała

Przykład `for`
```python
for i in range(1, 100):
    print(i)
```
przechodzimy po wartościach z zakresu [1, 100) - pętla wykona się 99 razy

Pętla `for` pozwala też przechodzić po elementach iteratorów (czyli np. list, tupli)
```python
things_list = ["abc", "cde", 1, 2, 3]
for item in things_list: # iterujemy po każdym elemencie z listy things_list
    print(item)
```
przechodzimy po wartościach z zakresu [1, 100) - pętla wykona się 99 razy

Przykład `while`
```python
value = 10

while value > 0:
    print(value)
    value = value - 1
```
pętla będzie wykonywać się dopóki wartość zmiennej value będzie dodatnia. Ponieważ w każdej iteracji zmniejszamy wartośc tej zmiennej o 1, po 10 iteracji warunek nie zostanie spełniony i wykonywanie pętli się zakończy.


Możemy zagnieżdżać pętle
```python
i = 5
while i > 5:
    print("i=", i)
    for j in range(j):
        print("j=", j)
    i = i -1
```

## Słowa kluczowe `break` oraz `continue`

### &nbsp; `break` - użycie tego słowa kluczowego powoduje zakończenie wykonywania się pętli w dowolnym momencie
```python
fruits = ["apple", "orange", "banana", "cherry"]
for fruit in fruits: # iterujhemy po elementach listy
    if fruit == "banana": # sprawdzamy czy element nie jest równy "banana"
        break # kończymy wykonywanie się pętli, wychodzimy z bloku "for", nie wykona się już więcej iteracji tej pętli
    print(fruit)
```
### &nbsp; `continue` - użycie tego słowa kluczowego powoduje zakończenie wykonywania się aktualnej iteracji pętli i rozpoczęcie następnej iteracji (niue kończy się wykonywanie pętli)
```python
fruits = ["apple", "orange", "banana", "cherry"]
for fruit in fruits: # iterujhemy po elementach listy
    if fruit == "banana": # sprawdzamy czy element nie jest równy "banana"
        continue # kończymy wykonywanie się iteracji, przechodzimy do następnej iteracji pętli
    print(fruit)
```
## Metody `zip` oraz `enumerate`
### &nbsp; `zip` - metoda ta służy do iterowania po wielu listach/setach/tuplach/słownikach/stringach na raz, działa następująco:
```python
frequences = [1,2,3]
fruits = ["banana", "apple", "orange"]

for i, fruit in zip(frequences, fruits): # funkcja zip pozwala na łączenie list/setów/słowników i równoległym iterowaniu po nich
    print(f"There are {i} {fruit}")
```
output:
```text
There are 1 banana
There are 2 apple
There are 3 orange
```
### &nbsp; `enumerate` - metoda ta pozwala na iterowanie po obiekcie oraz po kolejnych indeksach:
```python
fruits = ["banana", "apple", "orange"]

for i, fruit in enumerate(fruits):
    print(f"There are {i} {fruit}")
```
output:
```text
There are 1 banana
There are 2 apple
There are 3 orange
```
