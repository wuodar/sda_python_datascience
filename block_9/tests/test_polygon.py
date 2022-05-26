import unittest
from repo.block_9.tests.polygon import Polygon, Triangle


class TestPolygon(unittest.TestCase):
    def setUp(self) -> None:
        self.polygon = Polygon(4)

    def test_number_of_sides(self):
        # When
        # input od użytkownika na temat długości boków

        # Then
        deisred_number_of_sides = 4
        self.assertEqual(deisred_number_of_sides, len(self.polygon.sides),
                         msg=f"The deisred number of sides is {deisred_number_of_sides}, not {len(self.polygon.sides)}")

    def test_lengths_of_sides(self):
        # When

        # Then
        desired_lengths_of_sides = [1, 4, 9, 16]
        self.assertEqual(desired_lengths_of_sides, self.polygon.sides,
                        msg = f"The desired lengths of sides are {desired_lengths_of_sides}, not {self.polygon.sides}")

class TestTriangle(unittest.TestCase):
    def setUp(self) -> None:
        self.triangle = Triangle()

    def test_get_area(self):
        # When
        triangle_area = self.triangle.get_area()
        # Then
        desired_area = 7.0
        self.assertEqual(desired_area, triangle_area, msg=f"The desired area is {desired_area}, not {triangle_area}")

    def test_number_of_sides(self):
        # When
        # input od użytkownika na temat długości boków

        # Then
        deisred_number_of_sides = 3
        self.assertEqual(deisred_number_of_sides, len(self.triangle.sides),
                         msg=f"The desired number of sides is {deisred_number_of_sides}, not {len(self.triangle.sides)}")

    def test_lengths_of_sides(self):
        # When

        # Then
        desired_lengths_of_sides = [1, 4, 9]
        self.assertEqual(desired_lengths_of_sides, self.triangle.sides,
                        msg = f"The desired lengths of sides are {desired_lengths_of_sides}, not {self.triangle.sides}")
