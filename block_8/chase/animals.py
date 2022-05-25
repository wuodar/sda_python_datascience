from typing import List, Optional, Tuple
import random
from math import dist


class Animal:
    def __init__(self, x_pos: float, y_pos: float, move_dist: float) -> None:
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.move_dist = move_dist

    @property
    def cords(self):
        return self.x_pos, self.y_pos

    def move(self):
        # random.choice pobiera jako parametr sekwencje (lista/tupla) i zwraca losowy element
        pass


class Sheep(Animal):
    def __init__(self, init_pos_limit: float, move_dist: float):
        pass

    def move(self):
        self.x_pos = self.move_dist * random.choice([-1, 0, 1])
        self.y_pos = self.move_dist * random.choice([-1, 0, 1])


class Wolf(Animal):
    def __init__(self, move_dist: float):
        super(Wolf, self).__init__(0, 0, move_dist)
        self.eaten_sheeps = 0

    def __get_closest_sheep(self, sheeps: List[Sheep]) -> Tuple[int, float]:
        """
        returns index of the closest sheep, and the distance of the sheep
        """
        pass

    def chase(self, sheeps: List[Sheep]):
        pass

