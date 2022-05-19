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
        # self.car_name = self.get_car_name()
        # self.number_of_speed_ups = None

    # def __get_car_name(self):
    #     return f"{self.manufacturer} {self.model}"

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
    count = 99 # zmienna count istnieje od początku działania programu, nawet bez tworzenia obiektów klasy Reader
    # pierwsza konsekwencja jest taka, że mamy do niej dostęp przez całe życie programu
    # możemy ją nadpisywać
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

# reader = Reader("data.txt")
# print(Reader.count)
Reader.count += 10
# print(Reader.count)

# przykład zmiennej klasy
# class Rectangle:
#     counter_of_objects = 0  # to jest zmienna dostępna z poziomu klasy, nie obiektu
#
#     def __init__(self, b1, b2):
#         Rectangle.counter_of_objects += 1  # można użyć atrybutu klasy na przykład do liczenia ilości stworzonych obiektów
#         self.b1 = b1
#         self.b2 = b2
#
#     def get_area(self):  # dobra praktyka - funkcje nazywamy według tego co robią, nie tego co zwracają
#         # self.b1 * self.b2 = area # zmienna musi być po lewej stronie operatora przypisania, a wyrażenia, którego wynik chcemy wpisać do tej zmiennej, po prawej
#         area = self.b1 * self.b2
#         return area


# klasa bazowa
class Vehicle:
    def __init__(self, length):
        self.speed = 0
        self.length = length


    def speed_up(self, speed):
        self.speed += speed

# klasa Car dziedziczy z Vehicle
class Car(Vehicle):
    def __init__(self, registry_number):
        super().__init__(length=5)
        self.registry_number = registry_number

# class Bike dziedziczy z Vehicle
class Bike(Vehicle):
    pass

car = Car("ERA C1D5")
print(car.speed)
car.speed_up(10)
print(car.speed)
print(car.length)
# Employee.__init__(self, name, position)