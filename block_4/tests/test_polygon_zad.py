import unittest
from block_4.exercises.polygon_orgin import Polygon

class TestPolygon(unittest.TestCase):
    def setUp(self) -> None:
        self.polygon = Polygon(4)

    def test_number_of_sides(self):
        #when
        #input od użytkownika na temat długości boków

        #then
        deisred_number_of_sides = 4
        self.assertEqual(len(self.polygon.sides), deisred_number_of_sides,
                         msg=f"The deisred number of side is {deisred_number_of_sides}, not {len(self.polygon.sides)}")
