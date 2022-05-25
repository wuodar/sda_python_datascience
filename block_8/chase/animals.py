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
        self.x_pos += self.move_dist * random.choice([-1, 0, 1])
        self.y_pos += self.move_dist * random.choice([-1, 0, 1])


class Sheep(Animal):
    def __init__(self, init_pos_limit: float, move_dist: float):
        x_pos = random.uniform(-init_pos_limit, init_pos_limit)
        y_pos = random.uniform(-init_pos_limit, init_pos_limit)

        super(Sheep, self).__init__(x_pos, y_pos, move_dist)
        self.alive = True


class Wolf(Animal):
    def __init__(self, move_dist: float):
        super(Wolf, self).__init__(0, 0, move_dist)
        self.eaten_sheeps = 0

    def __get_closest_sheep(self, sheeps: List[Sheep]) -> Tuple[int, float]:
        """
        returns index of the closest sheep, and the distance of the sheep
        """
        distances = [dist(self.cords, sheep.cords) if sheep.alive else float("inf") for sheep in sheeps]

        minimum_distance = min(distances)
        closest_sheep_index = distances.index(minimum_distance)
        return closest_sheep_index, minimum_distance

    def chase(self, sheeps: List[Sheep]):
        sheep_index, distance = self.__get_closest_sheep(sheeps)

        if distance <= self.move_dist:
            sheep = sheeps[sheep_index]
            sheep.alive = False
            self.eaten_sheeps += 1
            self.x_pos = sheep.x_pos
            self.y_pos = sheep.y_pos
            return sheep
        else:
            self.move()
            return None

