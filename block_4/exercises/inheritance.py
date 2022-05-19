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