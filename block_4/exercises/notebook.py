"""
    Stwórz klasę Notebook, która będzie zawierała pola: producenta, cenę netto oraz pamięć RAM.
    Dopisz metody do obliczenia ceny brutto (+23% VAT) oraz zwiększenia ilości RAM-u.
"""

class Notebook:
    VAT_tax = 1.23

    def __init__(self, producent, price, amount_of_RAM):
        self.producent = producent
        self.price = price
        self.amount_of_RAM = amount_of_RAM

    def gross_price(self):
        return self.price * self.VAT_tax

    def add_RAM(self, RAM):
        self.amount_of_RAM += RAM