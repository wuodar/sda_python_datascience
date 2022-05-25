from typing import Optional, List
import logging
from animals import Sheep, Wolf


logging.basicConfig(level=logging.INFO)


def count_alive_sheeps(sheeps: List[Sheep]) -> int:
    pass


def move_sheeps(sheeps: List[Sheep]) -> None:
    pass


def run_simulation(iterations_count: int, wolf: Wolf, sheeps: List[Sheep]):
    pass

if __name__ == "__main__":
    sheeps = [Sheep(10, 7) for i in range(20)]
    wolf = Wolf(5)
    run_simulation(30, wolf, sheeps)
