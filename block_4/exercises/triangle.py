"""
Stwórz klasę Triangle. Klasa Triangle ma zawierać 3 parametry angle1, angle2, angle3
czyli kąty trójkąta. Napisz również metodę check_angles, która sprawdza
czy kąty w trójkącie sumują się do 180. Zwróć True lub False, zależnie od wyniku.
"""

class Triangle:
    def __init__(self, angle_A=60, angle_B=60, angle_C=60):
        self.angle_A = angle_A
        self.angle_B = angle_B
        self.angle_C = angle_C

        if self.check_sum_of_angles():
            print(f"Kąty: {self.angle_A}, {self.angle_B}, {self.angle_C} tworzą prawidłowy trójkąt.")
        else:
            print(f"Kąty: {self.angle_A}, {self.angle_B}, {self.angle_C} tworzą nieprawidłowy trójkąt.")

    def check_sum_of_angles(self):
        return True if (self.angle_A + self.angle_B + self.angle_C) == 180 else False

tri = Triangle(90,30,60)
