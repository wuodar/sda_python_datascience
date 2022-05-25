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
        self.x_pos = random.choice([-1, 0, 1])
        self.y_pos = random.choice([-1, 0, 1])
        # random.choice pobiera jako parametr sekwencje (lista/tupla) i zwraca losowy element v
        # pass


class Sheep(Animal):
    def __init__(self, init_pos_limit: float, move_dist: float):
        self.x_pos = random.uniform(-init_pos_limit, init_pos_limit)
        self.y_pos = random.uniform(-init_pos_limit, init_pos_limit)
        self.move_dist = move_dist
        self.alive = True

    def move(self):
        self.x_pos = self.move_dist * random.choice([-1, 0, 1])
        self.y_pos = self.move_dist * random.choice([-1, 0, 1])


class Wolf(Animal):
    def __init__(self, move_dist: float):
        super(Wolf, self).__init__(0, 0, move_dist)
        self.eaten_sheeps = 0

    def move(self):
        self.x_pos = self.move_dist * random.choice([-1, 0, 1])
        self.y_pos = self.move_dist * random.choice([-1, 0, 1])

    def __get_closest_sheep(self, sheeps: List[Sheep]) -> Tuple[int, float]:
        """
        returns index of the closest sheep, and the distance of the sheep
        """
        distance = []
        distance_wolf = self.cords
        for sheep in sheeps:
            distance.append(dist(sheep.cords, distance_wolf))

        index = distance.index(min(distance))
        return index, min(distance)


    def chase(self, sheeps: List[Sheep]) -> Optional[Sheep]:
        closest_sheep = self.__get_closest_sheep(sheeps)
        if closest_sheep[1] > self.move_dist:
            self.move()
        else:
            sheep_cords = sheeps[closest_sheep[0]]
            self.x_pos = sheep_cords.x_pos
            self.y_pos = sheep_cords.y_pos
            sheeps[closest_sheep[0]].alive = False
            self.eaten_sheeps += 1

            return closest_sheep
            #return sheeps[closest_sheep[0]]

