"""
Stwórz klasę Triangle. Klasa Triangle ma zawierać 3 parametry angle1, angle2, angle3
czyli kąty trójkąta. Napisz również metodę check_angles, która sprawdza
czy kąty w trójkącie sumują się do 180. Zwróć True lub False, zależnie od wyniku.
"""

class triangle():

    def __init__(self, a1, a2, a3):
        self.angle_1 = a1
        self.angle_2 = a2
        self.angle_3 = a3

    def check_angles(self):
        suma = self.angle_1 + self.angle_2 + self.angle_3
        if suma == 180:
            return True
        else:
            return False



t1 = triangle(10, 10, 10)
print(t1.check_angles())

"""
Drugie rozwiązanie, które printuje odpowiedź, a nie zwraca wartość true lub false
"""
# class triangle():
#
#     def __init__(self, a1, a2, a3):
#         self.angle_1 = a1
#         self.angle_2 = a2
#         self.angle_3 = a3
#
#     def check_angles(self):
#         suma = self.angle_1 + self.angle_2 + self.angle_3
#         #suma = a1 + a2 + a3
#         if suma == 180: print('To trójkąt')
#         else: print('To nie trójkąt')
#
# t1 = triangle(10, 10, 10)
# t1.check_angles()