
from weapon import Weapon


class Robot:
    def __init__(self, name) -> None:
        self.name = name
        self.health = 500
        self.weapon = Weapon

    def attack(self, dinosaur): #void
        pass