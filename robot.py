 
from weapon import Weapon



class Robot:
    def __init__(self, name) -> None:
        self.name = name
        self.health = 500
        self.weapon = Weapon(name, 0)



    def attack(self, dinosaur): #void
        dinosaur.health -= self.weapon.attack_power
        print(f"{self.name} attacked {dinosaur.name} with {self.weapon.name} dealing {self.weapon.attack_power} damage!!!")

    def get_weapon(self):
        excalibur = Weapon("Excalibur", 75)
        force = Weapon("Force Cascade", 50)
        meteor = Weapon("Meteor Cannon", 100)
        user_choice = int(input(f"Choose your weapon!\n1. {excalibur.name}\n      Damage:{excalibur.attack_power}\n2. {force.name}\n      Damage:{force.attack_power}\n3. {meteor.name} \n      Damage:{meteor.attack_power}\n"))
        while user_choice < 1 or user_choice > 3:
            user_choice = int(input(f"***INVALID RESPONSE***\n1. {excalibur.name}\n      Damage:{excalibur.attack_power}\n2. {force.name}\n      Damage:{force.attack_power}\n3. {meteor.name} \n      Damage:{meteor.attack_power}\n"))
        if user_choice == 1:
            return excalibur
        elif user_choice == 2:    
           return force
        elif user_choice == 3:   
            return meteor

    
    

                   
       

