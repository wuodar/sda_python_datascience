from time import time

# zwykły dekorator
def timer(func):
    def wrapper(*args, **kwargs):
        tik = time()
        res = func(*args, **kwargs)
        tok = time()
        execution_time = tok - tik
        print(f"Function exeuction has taken {execution_time} seconds.")
        return res

    return wrapper

# dekorator z dodatkowym parametrem przy wywołaniu (przykład użycia w linii 33)
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
