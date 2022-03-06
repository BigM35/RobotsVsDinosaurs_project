import random



class Herd:
    def __init__(self) -> None:
        self.dinosaurs = []

    def create_herd(self, dinosaur): #void
        self.dinosaurs.append(dinosaur)

    def choose_dino_attacker(self):
        for dino in self.dinosaurs:
            user_choice = int(input(f"------------------------------------------------------------------------------------------------------------------------------------------------------------------------\nChoose your fighter!------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n1. {self.dinosaurs[0].name}\n    Health:{self.dinosaurs[0].health}\n2. {self.dinosaurs[1].name}\n    Health:{self.dinosaurs[1].health}\n3. {self.dinosaurs[2].name}\n    Health:{self.dinosaurs[2].health}\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n"))
            while user_choice  < 1 or user_choice > 3:
                user_choice = int(input(f"------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n***INVALID RESPONSE*** \nChoose your Fighter!\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n1. {self.dinosaurs[0].name}\n Health:   {self.dinosaurs[0].health}\n\n2. {self.dinosaurs[1].name}\n Health:   {self.dinosaurs[1].health}\n3. {self.dinosaurs[2].name}\n Health:   {self.dinosaurs[2].health}\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n"))
                if user_choice > 1 or user_choice < 3:
                    continue
            if user_choice == 1:
                print(f"{self.dinosaurs[0].name} is preparing to attack")
                self.dinosaurs[0].ability = self.dinosaurs[0].choose_attack()
                return self.dinosaurs[0]
            elif user_choice == 2:
                print(f"{self.dinosaurs[1].name} is preparing to attack")
                self.dinosaurs[1].ability = self.dinosaurs[1].choose_attack()
                return self.dinosaurs[1]
            elif user_choice == 3:
                print(f"{self.v[2].name} is preparing to attack")
                self.dinosaurs[2].ability = self.dinosaurs[2].choose_attack()
                return self.dinosaurs[2]

    def choose_random_dino_attacker(self):
        for dino in self.dinosaurs:
            choice = random.choice([1,2,3])
            if choice == 1:
                print(f"{self.dinosaurs[0].name} is preparing to attack")
                self.dinosaurs[0].ability = self.dinosaurs[0].choose_random_attack()
                return self.dinosaurs[0]
            elif choice == 2:
                print(f"{self.dinosaurs[1].name} is preparing to attack")
                self.dinosaurs[1].ability = self.dinosaurs[1].choose_random_attack()
                return self.dinosaurs[1]
            elif choice == 3:
                print(f"{self.dinosaurs[2].name} is preparing to attack")
                self.dinosaurs[2].ability = self.dinosaurs[2].choose_random_attack()
                return self.dinosaurs[2]

    def remove_dead_dino(self):
        for dino in self.dinosaurs:
            if self.dinosaurs[0].health < 1:
                self.dinosaurs.remove(self.dinosaurs[0])
                print(f"{self.dinosaurs[0].name} is dead!")
            elif self.dinosaurs[1].health < 1:
                self.dinosaurs.remove(self.dinosaurs[1])
                print(f"{self.dinosaurs[1].name} is dead!")
            elif self.dinosaurs[1].health < 1:
                self.dinosaurs.remove(self.dinosaurs[1])
                print(f"{self.dinosaurs[1].name} is dead!")

    def dinosaur_to_be_attacked(self):
        for dino in self.dinosaurs:
            user_choice = int(input(f"------------------------------------------------------------------------------------------------------------------------------------------------------------------------\nChoose your choose your target!!!\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n1. {self.dinosaurs[0].name}\n    Health:{self.dinosaurs[0].health}\n2. {self.dinosaurs[1].name}\n    Health:{self.dinosaurs[1].health}\n3. {self.dinosaurs[2].name}\n    Health:{self.dinosaurs[2].health}\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n"))
            while user_choice  < 1 or user_choice > 3:
                user_choice = int(input(f"------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n***INVALID RESPONSE*** \nChoose your choose your target!!!\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n1. {self.dinosaurs[0].name}\n Health:   {self.dinosaurs[0].health}\n2. {self.dinosaurs[1].name}\n Health:   {self.dinosaurs[1].health}\n3. {self.dinosaurs[2].name}\n Health:   {self.dinosaurs[2].health}\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n"))
                if user_choice > 1 or user_choice < 3:
                    continue
            if user_choice == 1:
                return self.dinosaurs[0]
            elif user_choice == 2:
                return self.dinosaurs[1]
            elif user_choice == 3:
                return self.dinosaurs[2]

    def random_dinosaur_to_be_attacked(self):
        for dino in self.dinosaurs:
            choice = random.choice([1,2,3])
            if choice == 1:
                return self.dinosaurs[0]
            elif choice == 2:
                return self.dinosaurs[1]
            elif choice == 3:
                return self.dinosaurs[2]
