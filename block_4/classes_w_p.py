# pusta klasa
# class Car: # class to słowo kluczowe oznaczające początek deifinicji klasy
#     pass
#     # def __init__(self): # self to słowo kluczowe pozwalające na dostęp w ciele funkcji do stanu (danych) obiektu klasy
#     #     pass
#
# some_car = Car() # tworzenie obiketu klasy Car, aby stworzyć obiekt, musimy wywołać tą klasę, czyli dopisać ()
# print(type(some_car))

# instancja klasy to inaczej obiekt klasy

class Car:
    class_attribute = "class attribute"

    def __init__(self, registration_number, manufacturer, model): # konstruktor klasy
        self.manufacturer = manufacturer
        self.model = model
        self.registration_number = registration_number # atrybut klasy
        self.speed = 0
        # self.number_of_speed_ups = None

    def speed_up(self, additional_speed):
        self.speed += additional_speed
        # self.number_of_speed_ups = 10 # zła praktyka, wszystkie pola klasy powinny być zainicjowane w konstruktorze klasy (czyli metodzie __init__)

    @staticmethod # staticmethod to inaczej metoda statyczna, nie ma dostępu do self ani cls - nie ma dostępu do danych klasy/obiektu
    def some_static_method():
        pass

    @classmethod # class method ma dostęp do klasy Car, przez co może być użyta np. do stworzenia obiektu klasy Car, można ją rozumieć jako fabryka
    def bmw_m3(cls, registration_number):
        return cls(registration_number, "BMW", "M3")

some_car = Car("ERA C3R1", "skoda", "octavia") # inicjalizujemy obiekt, czyli tworzymy instancję klasy Car
bmw_m3 = Car.bmw_m3("ERA C2CJ")
# print(bmw_m3.manufacturer)

class Reader:
    def __init__(self, path):
        self.path = path
        self.data = None

    def read_file(self):
        with open(self.path) as f:
            self.data = f.read()

    @staticmethod
    def check_if_valid(data):
        is_valid = len(data) > 10
        return is_valid

reader = Reader("data.txt")
reader.read_file()
# print(Reader.check_if_valid(reader.data))
