#zhtr;yekhtujt;lk'll;l;l

# def print_hello():
#     print("Hello")


# # print_hello to funkcja, każda funkcja jest obiektem -
# # co za tym idzie, możemy ją przypisać od zmiennej
# x = print_hello
# # x() # wywołanie funkcji print_hello,
# # x jest referencją do tej funkcji

# def print_world():
#     print("World")


# def execeute_functions(*functions):
#     for func in functions:
#         func()

# # podajemy funkcje jako parametry do funkcji executer_functions
# # execeute_functions(x, print_world)

# # funkcje wewnętrzne
# # def print_hello_v2():
# #     def print_world_v2():
# #         print("World v2")
# #     print_world_v2()
# #     print("Hello v2")

# # wywołanie funkcji w return
# # def print_hello_v2():
# #     def print_world_v2():
# #         print("World v2")
# #     print("Hello v2")
# #     return print_world_v2()

# X = 10

# # def print_hello_v2(arg):
# #     #  funkcja print_world_v2 ma dostęp
# #     #  do atrybutów funkcji print_hello_v2
# #     def print_world_v2():
# #         return f"{arg} v2"
# #     print("Hello v2")
# #     return print_world_v2()

# # x jest referencją do funkcji print_world_v2
# # ponieważ zwracamy ją z funkcji print_hello_v2
# # x = print_hello_v2("Test")
# # x()

# from time import time

# #  dekorator liczący czas wykonania funkcji
# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print(f"BEFORE: {args}\n{kwargs}")
#         tik = time()
#         res = func(*args, **kwargs)
#         print(f"AFTER: {res}")
#         tok = time()
#         execution_time = tok - tik
#         print(f"Execution time: {execution_time}")
#         return res
#     return wrapper

# # wrapper = my_decorator(print_hello_v2)
# # value = wrapper("TEST")
# # print(value)

# @my_decorator
# def print_hello_v2(arg):
#     #  funkcja print_world_v2 ma dostęp
#     #  do atrybutów funkcji print_hello_v2
#     def print_world_v2():
#         return f"{arg} v2"
#     print("Hello v2")
#     return print_world_v2()

# print_hello_v2("TEST")