from typing import Optional
import logging
from animals import Sheep, Wolf


logging.basicConfig(level=logging.INFO)


def count_alive_sheeps(sheeps: list[Sheep]) -> int:
    count_alive_sheeps = [1 if sheep.alive else 0 for sheep in sheeps]
    return sum(count_alive_sheeps)

def move_sheeps(sheeps: list[Sheep]) -> None:
    for sheep in sheeps:
        sheep.move()

def run_simulation(iterations_count: int, wolf: Wolf, sheeps: list[Sheep]):
    logging.info("Starting simulation!")

    i = 0
    while iterations_count >= i and count_alive_sheeps(sheeps) > 0:
        move_sheeps(sheeps)
        eaten_sheep = wolf.chase(sheeps)
        if eaten_sheep is not None:
            logging.info(f"Wolf ate sheep number {sheeps.index(eaten_sheep)+1}")
        i += 1
    logging.info(f"There are {count_alive_sheeps(sheeps)} alive sheeps!")

if __name__ == "__main__":
    sheeps = [Sheep(10, 7) for i in range(20)]
    wolf = Wolf(5)
    run_simulation(30, wolf, sheeps)
