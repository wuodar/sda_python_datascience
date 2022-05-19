"""
    Stwórz klasę o nazwie Employee, oznaczającą pracownika firmy.
    Pracownicy mogą być opłacani na dwa sposoby:
        - godzinowo
        - na stałą stawkę
    Stwórz zatem dwie klasy, dziedziczące z klady Employee:
        - HourlyEmployee - dla pracowników którzy mają stawkę godzinową
        - SalaryEmployee - dla pracowników na stałej stawce
    
    Klasa Employee powinna zawierać w konstruktorze dwa pola: name (imię pracownika) oraz position (stanowisko) które należy potem przypisać jako pola klasy
    
    Klasa SalaryEmployee powinna dodatkowo (poza tym co klasa Employee) zawierać w konstruktorze (oraz jako pole klasy) zmienną weekly_salary (tygodniowa wypłata)
    
    Klasa HourlyEmployee powinna dodatkowo (poza tym co klasa Employee) zawierać w konstruktorze (oraz jako pole klasy) zmienne hours_worked 
        (ilość przepracownych godzin) oraz hour_rate (stawka godzinowa)

    Dodatkowo, klasy dziedziczące z klasy Employee powinny zawierać metodę calculate_payroll (oblicz wypłatę), z odpowiednią implementacją, zależnie od typu pracownika.
"""

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.postion = position

class SalaryEmployee(Employee):
    def __init__(self, name, position, weekly_salary):
        self.weekly_salary = weekly_salary
        super().__init__(name, position)

    def calculate_payroll(self):
        self.payroll = self.weekly_salary
        return self.payroll

class HourlyEmployee(Employee):
    def __init__(self, name, position, hours_worked, hour_rate):
        self.hours_worked = hours_worked
        self.hours_rate = hour_rate
        super().__init__(name, position)

    def calculate_payroll(self):
        self.payroll = self.hours_worked * self.hours_rate
        return self.payroll


Pracownik1 = SalaryEmployee("Maciej", "manager", 15000)
print(Pracownik1.calculate_payroll())

Pracownik2 = HourlyEmployee("Maciej", "magazynier", 160, 24)
print(Pracownik2.calculate_payroll())
