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
        self.position = position


class SalaryEmployee(Employee):
    def __init__(self, name, position, weekly_salary):
        super().__init__(name, position)
        self.weekly_salary = weekly_salary


class HourlyEmployee(Employee):
    def __init__(self, name, position, hours_worked, hour_rate):
        super().__init__(name, position)
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        return self.hour_rate * self.hours_worked


if __name__ == "__main__":
    hourly_employee = HourlyEmployee("Kacper", "Programista", 160, 30)
    employee_payroll = hourly_employee.calculate_payroll()
    print(f"Employee {hourly_employee.name} payroll is {employee_payroll}")
