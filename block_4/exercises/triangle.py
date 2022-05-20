"""
Stwórz klasę Triangle. Klasa Triangle ma zawierać 3 parametry angle1, angle2, angle3
czyli kąty trójkąta. Napisz również metodę check_angles, która sprawdza
czy kąty w trójkącie sumują się do 180. Zwróć True lub False, zależnie od wyniku.
"""


class Triangle:
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    def check_angles(self):
        return (self.angle1 + self.angle2 + self.angle3) == 180


if __name__ == "__main__":
    triangle = Triangle(10, 30, 80)
    print(triangle.check_angles())
