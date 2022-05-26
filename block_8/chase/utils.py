from time import time

def timer_with_param(some_value):
    def timer(func):
        def wrapper(*args, **kwargs):
            print(some_value)
            tik = time()
            res = func(*args, **kwargs)
            tok = time()
            execution_time = tok - tik
            print(f"Function exeuction has taken {execution_time} seconds.")
            return res
        return wrapper
    return timer

def something():
    pass

# ten zapis
# @timer_with_param("abc")
# def something():
#     pass

# odpowiada temu zapisowi
# something = timer_with_param("abc")(something)

"""
Napisz dekorator, który po udekorowaniu dowolnej funkcji, przed jej wykonaniem wyprintuje
nazwę tej funkcji oraz parametry przekazane do niej. Następnie wywoła dekorowaną funkcję i wyprintuje wynik funkcji.
Dekorator powinien printować informacje w przejrzysty sposób, oddzielając od siebie wywołania funkcji specjalnymi znakami,
np. :
-------------------------------------------------------------

ale mogą być też inne :)
Napisz dekorator w pliku block_8/chase/utils.py, a następnie zaimportuj go w pliku block_8/chase/simulation.py
i udekoruj nim dowolne, wybrane przez siebie funkcję. Sprawdź działanie dekoratora.
"""

def print_info_about_func(func):
    def wrapper(*args, **kwargs):
        print("\n===================")
        print(f"Wywołana funkcja nazywa się {func.__name__}, do której przekazano następujące argumenty: {args, kwargs}")
        print("===================")
        res = func(*args, *kwargs)
        print(f"Funkcja zwraca {res}.")
        print("===================\n")
        return res
    return wrapper
        
