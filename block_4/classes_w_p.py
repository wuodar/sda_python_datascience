# pusta klasa
class Class:  # class to słowo kluczowe oznaczające początek deifinicji klasy
    pass


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
    def bmw_m3(cls, registration_number):
        return cls(registration_number, "BMW", "M3")


# klasa bazowa
class Vehicle:
    def __init__(self, length):
        self.speed = 0
        self.length = length

    def speed_up(self, speed):
        self.speed += speed


# klasa SomeCar dziedziczy z Vehicle
class SomeCar(Vehicle):
    def __init__(self, registry_number):
        super().__init__(length=5)
        self.registry_number = registry_number


# class Bike dziedziczy z Vehicle
class Bike(Vehicle):
    pass


if __name__ == "__main__":
    # tworzenie obiektu klasy Car, aby stworzyć obiekt, musimy wywołać tą klasę, czyli dopisać ()
    some_class = Class()
    print(f"Typ obiektu pustej klasy Class: {type(some_class)}")

    some_car = Car("ERA C3R1", "skoda", "octavia")  # inicjalizujemy obiekt, czyli tworzymy instancję klasy Car
    bmw_m3 = Car.bmw_m3("ERA C2CJ")  # wywołanie classmethod, będącej fabryką obiektów klasy Car
    some_car.speed_up(10)
    bmw_m3.speed_up(20)
    # wywołanie staticmethod
    faster_car = Car.check_which_car_is_faster(some_car.speed, bmw_m3.speed)
    print(f"Szybszy jest samochód numer {faster_car}")
    
    car = SomeCar("ERA C1D5")
    print(car.speed)
    car.speed_up(10)
    print(car.speed)
    print(car.length)
