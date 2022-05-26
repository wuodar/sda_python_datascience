from typing import List
import logging
from animals import Sheep, Wolf


logging.basicConfig(level=logging.INFO)


def count_alive_sheeps(sheeps: List[Sheep]) -> int:

    return sum(sheep.alive == True for sheep in sheeps)



def move_sheeps(sheeps: List[Sheep]) -> None:
    for sheep in sheeps:
        if sheep.alive:
            sheep.move()



def run_simulation(iterations_count: int, wolf: Wolf, sheeps: List[Sheep]):
    logging.info("Starting simulation!")


    for i in range(iterations_count):
        move_sheeps(sheeps)
        eaten_sheep = wolf.chase(sheeps)

        if eaten_sheep != None:
            logging.warning(f"Wolf ate sheep number {sheeps.index(eaten_sheep)+1}")

        if count_alive_sheeps(sheeps) == 0:
            logging.error(f"Simulation finished! There are {count_alive_sheeps(sheeps)} alive sheeps!")
            break

    logging.error(f"Simulation finished! There are {count_alive_sheeps(sheeps)} alive sheeps!")

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
