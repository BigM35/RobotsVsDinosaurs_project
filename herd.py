



class Herd:
    def __init__(self) -> None:
        self.dinosaurs = []

    def create_herd(self, dinosaur): #void
        self.dinosaurs.append(dinosaur)

    def choose_dino_attacker(self):
        for dino in self.dinosaurs:
            user_choice = int(input(f"Choose your fighter!\n1. {self.dinosaurs[0].name}\n    Health:{self.dinosaurs[0].health}\n2. {self.dinosaurs[1].name}\n    Health:{self.dinosaurs[1].health}\n3. {self.dinosaurs[2].name}\n    Health:{self.dinosaurs[2].health}\n"))
            while user_choice  < 1 or user_choice > 3:
                user_choice = int(input("***INVALID RESPONSE*** \nChoose your Fighter!\n 1. {self.dinosaurs[0].name}\n Health:   {self.dinosaurs[0].health}\n\n2. {self.dinosaurs[1].name}\n Health:   {self.dinosaurs[1].health}\n3. {self.dinosaurs[2].name}\n Health:   {self.dinosaurs[2].health}\n"))
                if user_choice > 1 or user_choice < 3:
                    continue
            if user_choice == 1:
                print(f"{self.dinosaurs[0].name} is preparing to attack")
                self.dinosaurs[0].weapon = self.dinosaurs[0].get_weapon()
                return self.dinosaurs[0].name
            elif user_choice == 2:
                print(f"{self.dinosaurs[1].name} is preparing to attack")
                self.dinosaurs[1].weapon = self.dinosaurs[1].get_weapon()
                return self.dinosaurs[1].name
            elif user_choice == 3:
                print(f"{self.v[2].name} is preparing to attack")
                self.dinosaurs[2].weapon = self.dinosaurs[2].get_weapon()
                return self.dinosaurs[2].name

    def remove_dead_dino(self):
        for robot in self.dinosaurs:
            if self.dinosaurs[robot].health < 1:
                self.dinosaurs.remove(robot)
                print(f"{self.dinosaurs(robot).name} is dead!")

    def dinosaur_to_be_attacked(self):
        for dino in self.dinosaurs:
            user_choice = int(input(f"Choose your choose your target!!!\n1. {self.dinosaurs[0].name}\n    Health:{self.dinosaurs[0].health}\n2. {self.dinosaurs[1].name}\n    Health:{self.dinosaurs[1].health}\n3. {self.dinosaurs[2].name}\n    Health:{self.dinosaurs[2].health}\n"))
            while user_choice  < 1 or user_choice > 3:
                user_choice = int(input(f"***INVALID RESPONSE*** \nChoose your choose your target!!!\n 1. {self.dinosaurs[0].name}\n Health:   {self.dinosaurs[0].health}\n2. {self.dinosaurs[1].name}\n Health:   {self.dinosaurs[1].health}\n3. {self.dinosaurs[2].name}\n Health:   {self.dinosaurs[2].health}\n"))
                if user_choice > 1 or user_choice < 3:
                    continue
            if user_choice == 1:
                return self.dinosaurs[0]
            elif user_choice == 2:
                return self.dinosaurs[1]
            elif user_choice == 3:
                return self.dinosaurs[2]

    def choose_dino_attacker(self):
        for dino in self.dinosaurs:
            user_choice = int(input(f"Choose your Dinosaur to attack with!\n1. {self.dinosaurs[0].name}\n    Health:{self.dinosaurs[0].health}\n     Damage:{self.dinosaurs[0].attack_power}\n2. {self.dinosaurs[1].name}\n    Health:{self.dinosaurs[1].health}\n     Damage:{self.dinosaurs[1].attack_power}\n3. {self.dinosaurs[2].name}\n    Health:{self.dinosaurs[2].health}\n     Damage:{self.dinosaurs[0].attack_power}\n"))
            while user_choice  < 1 or user_choice > 3:
                user_choice = int(input(f"***INVALID RESPONSE*** \nChoose your Dinosaur to attack with!\n1. {self.dinosaurs[0].name}\n    Health:{self.dinosaurs[0].health}\n     Damage:{self.dinosaurs[0].attack_power}\n2. {self.dinosaurs[1].name}\n    Health:{self.dinosaurs[1].health}\n     Damage:{self.dinosaurs[1].attack_power}\n3. {self.dinosaurs[2].name}\n    Health:{self.dinosaurs[2].health}\n     Damage:{self.dinosaurs[0].attack_power}\n"))
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
                print(f"{self.dinosaurs[2].name} is preparing to attack")
                self.dinosaurs[2].ability = self.dinosaurs[2].choose_attack()
                return self.dinosaurs[2]
