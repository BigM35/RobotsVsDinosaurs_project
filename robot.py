 
from weapon import Weapon


class Robot:
    def __init__(self, name) -> None:
        self.name = name
        self.health = 500
        self.weapon = Weapon(name, 0)

    def attack(self, dinosaur): #void
        dinosaur.health - self.weapon.attack_power
    
   
                   
       

