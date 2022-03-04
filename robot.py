
from weapon import Weapon


class Robot:
    def __init__(self, name) -> None:
        self.name = name
        self.health = 500
        self.weapon = Weapon

    def attack(self, dinosaur): #void
        pass

    def give_weapon(self):
        user_choice = input("Choose your ability!\n 1. Excalibur\n2. Force Cascade\n3. Meteor Cannon")
        if  user_choice == 1:
            self.weapon = Weapon("Excalibur", 75)
        elif user_choice == 2:    
            self.weapon = Weapon(" Force Cascade", 50)
        elif user_choice == 3:    
            self.weapon = Weapon("Meteor Cannon", 100)

