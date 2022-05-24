import re # paczka służąca do pracy z wyrażeniami regularnymi

txt = "Lorem Ipsum is simply dummy 123 text of the printing and typesetting industry"

# funkcja search pobiera pattern oraz string w kórym podany pattern jest następnie wyszukiwany
# x = re.search("\d+", txt)
# print(x)
# print(txt[28:31])

# find all zwraca wystąpenia podanego patternu
# x = re.findall("\d+", txt)
# print(x)

# split dzieli string wejściowy na podstawie podanego patternu
# x = re.split("\s+", txt)
# print(x)

# sub zamienia w wejsciowym stringu miejsca matchujace z patternem na wartosc podana jako drugi parametr
# x = re.sub("\s+", "_", txt)
# print(x)

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

def is_email_valid(email: str) -> bool:
    return re.match(regex, email) is not None

email = input("Podaj email: ")

# print(is_email_valid(email))
