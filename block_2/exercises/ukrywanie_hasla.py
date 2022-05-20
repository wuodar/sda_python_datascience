"""
    Napisz prosta funkcje "szyfrujaca". Jej zadaniem jest zamiana
    co trzeciego znaku w hasle na znak gwiazdki (*).
    Przyklad:
    >> x = hide_password("moje_super_tajne_haslo123")
    >> print(x)
    "mo*e_*up*r_*aj*e_*as*o1*3"
    Pamietaj, ze dlugosc napisu nie musi byc podzielna przez 3.
"""

# ROZWIAZANIE NUMER 1
def hide_password(password):
    new_password = ""
    password_list = list(password)
    password_indexes = range(len(password_list))
    for i, letter in zip(
        password_indexes, password_list
    ):  # tak działa enumerate, które jest użyte w rozwiązaniu numer 3
        if (
            i + 1
        ) % 3 == 0:  # (i+1) bo indeksujemy od 0, ale w "realnym" świecie (nie komputerowym) liczymy od 1, % to operator dzielenia z resztą, zatem sprawdzamy czy ta reszta wynosi 0
            new_password += "*"  # new_password += "*" jest równoważne z new_password = new_password + "*"
        else:
            new_password += letter
    return new_password


# ROZWIAZANIE NUMER 2
# def hide_password(password):
#     """Ukrywa co trzecia litere w hasle password.
#
#     :param password: haslo z gwiazdkami co trzecia litere.
#     :return: napis z czesciowo ukrytym haslem.
#
#     """
#     encrypted_password = list(password)
#
#     for i in range(2, len(encrypted_password), 3):  # [start, stop)
#         encrypted_password[i] = '*'
#
#     encrypted_password = ''.join(encrypted_password)
#     return encrypted_password

# ROZWIAZANIE NUMER 3
# def hide_password(password):
#     password_list = list(password)
#     for i, letter in enumerate(password_list): # enumerate pobiera listę/set/slownik/tuple/string, i zwraca obiekt którego elementami są pary index, wartość, przy czym kolejnymi wartościami są kolejne elementy z podanego obiektu
#         if (i + 1) % 3 == 0:
#             password_list[i] = "*" # odnosimy się do elementu w liście pod indexem i i napdisujemy wartość listy pod tym indexem
#     encoded_password = "".join(password_list)
#     return encoded_password
