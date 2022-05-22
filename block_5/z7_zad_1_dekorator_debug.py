"""
Stwórz dekorator o nazwie debug, który podczas wywoływania funkcji będzie
wyświetlał informacje o jej nazwie, przekazanych parametrach oraz zwracanym wyniku.
"""

#@debug

def func(a, b, c):
    return a + b * c
print(func(3, 2, 4))