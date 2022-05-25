from typing import Optional, List
import logging
from animals import Sheep, Wolf

logging.basicConfig(level=logging.INFO)


def count_alive_sheeps(sheeps: List[Sheep]) -> int:
    count_alive = 0
    for sheep in sheeps:
        if sheep.alive:
            count_alive += 1

    return count_alive
    # pass


def move_sheeps(sheeps: List[Sheep]) -> None:
    for sheep in sheeps:
        if sheep.alive:
            sheep.move()


def run_simulation(iterations_count: int, wolf: Wolf, sheeps: List[Sheep]):
    for i in range(iterations_count):
        move_sheeps(sheeps)
        wolf_chase_result = wolf.chase(sheeps)
        if wolf_chase_result is not None:
            print("Wolf ate sheep number {}".format(wolf_chase_result[0]))

        if count_alive_sheeps(sheeps) == 0:
            print("Simulation finished! There are {} alive sheeps!".format(count_alive_sheeps(sheeps)))
            break

    print("Simulation finished! There are {} alive sheeps!".format(count_alive_sheeps(sheeps)))


if __name__ == "__main__":
    sheeps = [Sheep(10, 7) for i in range(20)]
    wolf = Wolf(5)
    run_simulation(30, wolf, sheeps)
