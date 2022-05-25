import random
import math


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
        return self.x_pos, self.y_pos

"""
Z klasy Animal dziedziczyć będą klasy Wolf, oraz Sheep
	Sheep będzie zawierać w konstruktorze parametr init_pos_limit, który będzie float'em informującym o zakresie pozycji
	możliwej do zajęcia w początkowej fazie symulacji przez owce.
		# random.uniform() pobiera zakres wartości i zwraca wartość losową z tego zakresu
		- x_pos = random.uniform(-init_pos_limit, init_pos_limit)
		- y_pos = random.uniform(-init_pos_limit, init_pos_limit)
		- move_dist - do przekazania do konstruktora klasy bazowej, Animal
		- alive - atrybut klasy Sheep, inicjalizowany jako True podczas tworzenia obiektu (mówi nam o tym, czy owca jest żywa)
"""
class Sheep(Animal):
    def __init__(self, init_pos_limit: float, move_dist: float):
        # super().__init__(self.x_pos, self.y_pos, self.move_dist)
        x_pos = random.uniform(-init_pos_limit, init_pos_limit)
        y_pos = random.uniform(-init_pos_limit, init_pos_limit)
        super(Sheep, self).__init__(x_pos, y_pos, move_dist)
        self.alive = True
"""
Wolf będzie tworzony zawsze w pozycji (0, 0)
		- x_pos = 0
		- y_pos = 0
		- move_dist - podajemy podczas tworzenia obiektu
		- eaten_sheeps - liczba zjedzonych owiec, ustawiana na początku na 0
		
Dodatkowo, klasa Wolf będzie zawierać dwie metody
			# jeżeli macie Pythona starszego niż 3.9, to musicie pamiętać zaimportować typy do annotacji
			# from typing import List, Tuple, Set, Dict, Optional, Union # Optional[List] - parametr opcjonalny (czyli np. list albo None)
			# Union[List, Dict] - parametr klasy List bądź Dict (jeden z dwóch)
			# zwracamy parę wartości (tupla) index najbliższej owcy, odległość najbliższej owcy od wilka
			# do policzenia odległości wykorzystajcie funkcję dist z biblioteki math # import math # math.dist(cords_1, cords_2)
			# stwórzcie listę odległości, licząc odległość wilka od kązdej z żywych owiec
			# w pythonie aby oznaczyć wartość nieskończoną typu float, zapiszemy float("inf") (będziemy tak oznaczać odległość wiloka od nieżywych owiec, żeby nie zjadał ich dwa razy)
			- def __get_closest_sheep(self, sheeps: List[Sheep]) -> Tuple[int, float]:
				 ...
 		Druga metoda:
			# w metodzie chase będziemy dokonywać pościgu owcy
			# na początku musimy wywołać funkcję __get_closest_sheep, i zapisać index najbliższej owcy oraz odległość od wilka
			# sheep_index, distance = self.__get_closest_sheep(sheeps)
			# następnie musimy sprawdzić, czy odległość owcy od wilka jest mniejsza bądź równa niż move_dist wilka
			# jeżeli tak, to musimy wybrać owcę będącą najbliżej wilka z listy owiec podanej jako parametr do funkcji chase
			# a następnie zmienić dla tej owcy wartość atrybutu .alive na False
			# następnie zmieniamy pozycję wilka na taką samą jak pozycja owcy
			# ostatnim krokiem jest zwiększenie wartości atrybutu eatenb_sheeps o 1 i zwrócenie z funkcji obiektu zjedzonej owcy
			# w przypadku, gdy wilk nie będzie wystarczająco blisko owcy, wywołujemy funkcję .move() i nie zwracamy z funkcji niczego (None)
			- def chase(self, sheeps: List[Sheep]) -> Optional[Sheep]:
"""
class Wolf(Animal):
    def __init__(self, move_dist: float):
        super(Wolf, self).__init__(0, 0, move_dist)
        self.eaten_sheeps = 0

    def __get_closest_sheep(self, sheeps: list[Sheep]) -> tuple[int, float]:
        """
        returns index of the closest sheep, and the distance of the sheep
        """
        distances = [math.dist(self.cords, sheep.cords) if sheep.alive else float("inf") for sheep in sheeps]

        minimum_distance = min(distances)
        closest_sheep_index = distances.index(minimum_distance)
        return closest_sheep_index, minimum_distance

    def chase(self, sheeps: list[Sheep]):
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
 # [i for i in list]

