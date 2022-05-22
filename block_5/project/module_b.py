def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> float:
    return a / b

# Zmienna globalna
GLOBAL_VALUE = 6

class Car:
    # zmienna CLASS_ATTRIBUTE istnieje od początku działania programu,
    # nawet bez tworzenia obiektów klasy Car. Pierwsza konsekwencja jest taka,
    # że mamy do niej dostęp przez całe życie programu możemy ją nadpisywać
    CLASS_ATTRIBUTE = "class attribute"

    def __init__(self, registration_number, manufacturer, model):  # konstruktor klasy
        self.manufacturer = manufacturer
        self.model = model
        self.registration_number = registration_number  # atrybut klasy
        self.speed = 0
        self.car_name = self.__get_car_name()

    # przedrostek __ oznacza metodę/atrybut prywatny,
    # czyli taki który nie powinien być używany poza ciałem klasy (np. na obiekcie)
    def __get_car_name(self):
        return f"{self.manufacturer} {self.model}"

    def speed_up(self, additional_speed):
        self.speed += additional_speed

    # staticmethod to inaczej metoda statyczna, nie ma dostępu do self ani cls - nie ma dostępu do danych klasy/obiektu,
    # możemy jej użyć kiedy potrzebujemy jakiejś funkcjonalności powiązanej z logiką klasy ale nie polegającej na
    # referencji klasy (atrybutach/metodach klasy)
    @staticmethod
    def check_which_car_is_faster(speed_1, speed_2):
        return 1 if speed_1 > speed_2 else 2

    # class method ma dostęp do klasy Car, przez co może być użyta np. do stworzenia obiektu klasy Car,
    # można ją rozumieć jako fabryka
    @classmethod
    def bmw_m3(cls, registration_number) -> 'Car':
        return cls(registration_number, "BMW", "M3")
