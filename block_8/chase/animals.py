import math
from typing import List, Optional, Tuple
import random
from utils import print_name_func


class Animal:
    def __init__(self, x_pos: float, y_pos: float, move_dist: float) -> None:
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.move_dist = move_dist

    @property
    def cords(self):
        return self.x_pos, self.y_pos

    def move(self):
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
        super(Wolf, self).__init__(x_pos=0, y_pos=0, move_dist=move_dist)
        self.eaten_sheeps = 0

    def __get_closest_sheep(self, sheeps: List[Sheep]) -> Tuple[int, float]:
        """
        returns index of the closest sheep, and the distance of the sheep
        """
        wolf_position = self.cords
        closest_sheep = float("inf")
        index_closest_sheep = float("inf")

        for i, sheep in enumerate(sheeps):
            sheep_position = sheep.cords  #[sheep.x_pos, sheep.y_pos]
            if math.dist(wolf_position, sheep_position) < closest_sheep:
                closest_sheep = math.dist(wolf_position, sheep_position)
                index_closest_sheep = i
        return (index_closest_sheep, closest_sheep)

    @print_name_func
    def chase(self, sheeps: List[Sheep]):
        sheep_index, distance = self.__get_closest_sheep(sheeps)
        if distance <= self.move_dist:
            sheeps[sheep_index].alive = False
            self.x_pos = sheeps[sheep_index].x_pos
            self.y_pos = sheeps[sheep_index].y_pos
            self.eaten_sheeps += 1
            sheeps[sheep_index].y_pos = float("inf")
            sheeps[sheep_index].x_pos = float("inf")
            return sheeps[sheep_index]
        else:
            self.move()



