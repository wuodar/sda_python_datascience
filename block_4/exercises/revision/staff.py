"""
Stwórz klasę Teacher dziedziczącą  z klasy Staff i przekaż odpowiednie parametry do konstruktora
klasy Staff.

Następnie stwórz obiekty klasy Staff (staff) oraz Teacher (teacher) i używając metody isinstance()
(sprawdź w dokumentacji pythona/pycharma działanie tej funkcji) sprawdź czy zmienna teacher jest instancją klasy Staff.
"""

class Staff:
    def __init__(self, role, dept, salary): 
        self.role = role
        self.dept = dept
        self.salary = salary

    def show_details(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Role:", self.role)
        print("Department", self.dept)
