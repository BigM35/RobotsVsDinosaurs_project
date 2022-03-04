
from weapon import Weapon


class Robot:
    def __init__(self, name) -> None:
        self.name = name
        self.health = 500
        self.weapon = Weapon

    def attack(self, dinosaur): #void
        dinosaur.health - self.weapon.attack_power

    def get_weapon(self):
        user_choice = int(input("Choose your ability!\n1. Excalibur\n2. Force Cascade\n3. Meteor Cannon: \n"))
        while user_choice < 1 or user_choice > 3:
            user_choice = int(input("***INVALID RESPONSE***\nChoose your ability!\n1. Excalibur\n2. Force Cascade\n3. Meteor Cannon: \n"))
            if user_choice == 1:
                self.weapon = Weapon("Excalibur", 75)
                break
            elif user_choice == 2:    
                self.weapon = Weapon("Force Cascade", 50)
                break
            elif user_choice == 3:   
                self.weapon = Weapon("Meteor Cannon", 100)
        if user_choice == 1:
            self.weapon = Weapon("Excalibur", 75)
        elif user_choice == 2:    
            self.weapon = Weapon("Force Cascade", 50)
        elif user_choice == 3:   
            self.weapon = Weapon("Meteor Cannon", 100)
                   
       

