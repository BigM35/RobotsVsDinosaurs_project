 
from weapon import Weapon
import random


class Robot:
    def __init__(self, name) -> None:
        self.name = name
        self.health = 500
        self.weapon = Weapon(name, 0, 0)
        self.power_level = 1000


    def attack(self, dinosaur): #void
        if self.weapon.name == "Excalibur":
            self.power_level -= self.weapon.power_require
            hit = random.randint(0, 10)
            if hit <= 2:
                print(f"{self.name} missed the attack on {dinosaur.name}!!!")        
            else:
                dinosaur.health -= self.weapon.attack_power
                print(f"{self.name} attacked {dinosaur.name} with {self.weapon.name}, dealing {self.weapon.attack_power} damage!!!")
        elif self.weapon.name == "Force Cascade":
            self.power_level -= self.weapon.power_require
            hit = random.randint(0, 10)
            if hit <= 3:
                print(f"{self.name} missed the attack on {dinosaur.name}!!!")        
            else:
                dinosaur.health -= self.weapon.attack_power
                print(f"{self.name} attacked {dinosaur.name} with {self.weapon.name}, dealing {self.weapon.attack_power} damage!!!")
        elif self.weapon.name == "Meteor Cannon":
            self.power_level -= self.weapon.power_require
            hit = random.randint(0, 10)
            if hit <= 8:
                print(f"{self.name} missed the attack on {dinosaur.name}!!!")        
            else:
                dinosaur.health -= self.weapon.attack_power
                print(f"{self.name} attacked {dinosaur.name} with {self.weapon.name}, dealing {self.weapon.attack_power} damage!!!")
        
        
    def get_weapon(self):
        excalibur = Weapon("Excalibur", 75, 40)
        force = Weapon("Force Cascade", 100, 80)
        meteor = Weapon("Meteor Cannon", 400, 200)
        user_choice = int(input(f"------------------------------------------------------------------------------------------------------------------------------------------------------------------------\nChoose your weapon!\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n0. {excalibur.name}\n      Damage:{excalibur.attack_power}\n      Power Req.:{excalibur.power_require}\n1. {force.name}\n      Damage:{force.attack_power}\n      Power Req.:{force.power_require}\n2. {meteor.name} \n      Damage:{meteor.attack_power}\n      Power Req.:{meteor.power_require}\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n"))
        while user_choice < 0 or user_choice > 2:
            user_choice = int(input(f"------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n***INVALID RESPONSE***\nChoose your weapon!\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n0. {excalibur.name}\n      Damage:{excalibur.attack_power}\n1. {force.name}\n      Damage:{force.attack_power}\n2. {meteor.name} \n      Damage:{meteor.attack_power}\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n"))
        if user_choice == 0:
            return excalibur
        elif user_choice == 1:    
           return force
        elif user_choice == 2:   
            return meteor

    def get_random_weapon(self):
        excalibur = Weapon("Excalibur", 75, 50)
        force = Weapon("Force Cascade", 100, 60)
        meteor = Weapon("Meteor Cannon", 400, 200)
        choice = random.choice([0,1,2]) 
        if choice == 0:
            return excalibur
        elif choice == 1:    
           return force
        elif choice == 2:   
            return meteor   
    

                   
       

