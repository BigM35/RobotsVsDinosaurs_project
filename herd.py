import random
from unicodedata import name



class Herd:
    def __init__(self) -> None:
        self.dinosaurs = []

    def create_herd(self, dinosaur): #void
        self.dinosaurs.append(dinosaur)

    def choose_dino_attacker(self):
        user_choice = int(input(f"------------------------------------------------------------------------------------------------------------------------------------------------------------------------\nChoose your fighter!\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n0. {self.dinosaurs[0].name}\n    Health:{self.dinosaurs[0].health}\n     Damage:{self.dinosaurs[0].attack_power}\n       Energy:{self.dinosaurs[0].energy}\n1. {self.dinosaurs[1].name}\n    Health:{self.dinosaurs[1].health}\n     Damage:{self.dinosaurs[1].attack_power}\n       Energy:{self.dinosaurs[0].energy}\n2. {self.dinosaurs[2].name}\n    Health:{self.dinosaurs[2].health}\n     Damage:{self.dinosaurs[2].attack_power}\n       Energy:{self.dinosaurs[0].energy}\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n"))
        while user_choice  < 0 or user_choice > 2:
            user_choice = int(input(f"------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n***INVALID RESPONSE*** \nChoose your fighter!\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n0. {self.dinosaurs[0].name}\n    Health:{self.dinosaurs[0].health}\n     Damage:{self.dinosaurs[0].attack_power}\n       Energy:{self.dinosaurs[0].energy}\n1. {self.dinosaurs[1].name}\n    Health:{self.dinosaurs[1].health}\n     Damage:{self.dinosaurs[1].attack_power}\n       Energy:{self.dinosaurs[0].energy}\n2. {self.dinosaurs[2].name}\n    Health:{self.dinosaurs[2].health}\n     Damage:{self.dinosaurs[2].attack_power}\n       Energy:{self.dinosaurs[0].energy}\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n"))
            if user_choice > 0 or user_choice < 2:
                continue
        for dino in range(len(self.dinosaurs)):
            if user_choice == dino: 
                if self.dinosaurs[dino].health > 0:
                    print(f"{self.dinosaurs[dino].name} is preparing to attack")
                    self.dinosaurs[dino].ability = self.dinosaurs[dino].choose_attack()
                    return self.dinosaurs[dino].name
                else:
                    print("Chosen Dinosaur is EXTINCT!!!")
                    return "na"

    def choose_random_dino_attacker(self):
        choice = random.choice([0,1,2])
        for dino in range(len(self.dinosaurs)):
                if choice == dino:
                    if self.dinosaurs[dino].health > 0:
                        print(f"{self.dinosaurs[dino].name} is preparing to attack")
                        self.dinosaurs[dino].ability = self.dinosaurs[dino].choose_random_attack()
                        if self.dinosaurs[dino].req_energy > self.dinosaurs[dino].energy:
                            print(f"{self.dinosaurs[dino].name}does not have the required energy to use{self.dinosaurs[dino].ability}")
                            return "na"
                        else:
                            return self.dinosaurs[dino].name
                    else:
                        print("Chosen Dinosaur is EXTINCT!!!")
                        return "na"
       
    def remove_dead_dino(self):
        for dino in range(len(self.dinosaurs)):
            if self.dinosaurs[dino].health < 1:
                if "(EXTINCT)" in self.dinosaurs[dino].name:
                    continue
                else:
                    print(f"{self.dinosaurs[dino].name} is Extinct!!!")
                    self.dinosaurs[dino].name += " (EXTINCT)"
                    self.dinosaurs[dino].health = 0
                    self.dinosaurs[dino].attack_power = 0
            
    def dinosaur_to_be_attacked(self):
        user_choice = int(input(f"------------------------------------------------------------------------------------------------------------------------------------------------------------------------\nChoose your choose your target!!!\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n0. {self.dinosaurs[0].name}\n    Health:{self.dinosaurs[0].health}\n1. {self.dinosaurs[1].name}\n    Health:{self.dinosaurs[1].health}\n2. {self.dinosaurs[2].name}\n    Health:{self.dinosaurs[2].health}\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n"))
        while user_choice  < 0 or user_choice > 2:
            user_choice = int(input(f"------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n***INVALID RESPONSE*** \nChoose your choose your target!!!\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n0. {self.dinosaurs[0].name}\n Health:   {self.dinosaurs[0].health}\n1. {self.dinosaurs[1].name}\n Health:   {self.dinosaurs[1].health}\n2. {self.dinosaurs[2].name}\n Health:   {self.dinosaurs[2].health}\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n"))
            if user_choice > 0 or user_choice < 2:
                continue
        for dino in range(len(self.dinosaurs)):
            if user_choice == dino:
                if self.dinosaurs[dino].health > 0:
                    return self.dinosaurs[dino]
                else:
                    print("Chosen Dinosaur is already EXTINCT!!!")
                    return "na"

    def random_dinosaur_to_be_attacked(self):
        choice = random.choice([0,1,2])
        for dino in range(len(self.dinosaurs)):
            if choice == dino:
                if self.dinosaurs[dino].health > 0:
                    return self.dinosaurs[dino]
                else:
                    print("Chosen Dinosaur is already EXTINCT!!!")
                    return "na"
           
