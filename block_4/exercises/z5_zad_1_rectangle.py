"""
    Stwórz klasę o nazwie Rectangle.
    Klasa powinna mieć dwa pola dla boków oraz metodę area do liczenia pola prostokąta.
"""
class rectangle():

    def __init__(self, l, w):
        self.length = l
        self.width = w

    def rectangle_area(self):
        return self.length * self.width

newRectangle = rectangle(10, 10)
print(newRectangle.rectangle_area())
