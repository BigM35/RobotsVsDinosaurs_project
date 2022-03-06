import random



class Fleet:
    def __init__(self) -> None:
        self.robots = []

    def create_fleet(self, robot): #void
        self.robots.append(robot)
    
    def choose_robo_attacker(self):
        for robot in self.robots:
            user_choice = int(input(f"------------------------------------------------------------------------------------------------------------------------------------------------------------------------\nChoose your fighter!\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n1. {self.robots[0].name}\n    Health:{self.robots[0].health}\n2. {self.robots[1].name}\n    Health:{self.robots[1].health}\n3. {self.robots[2].name}\n    Health:{self.robots[2].health}\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n"))
            while user_choice  < 1 or user_choice > 3:
                user_choice = int(input(f"------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n***INVALID RESPONSE***\nChoose your Fighter!\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n1. {self.robots[0].name}\n Health:   {self.robots[0].health}\n2. {self.robots[1].name}\n Health:   {self.robots[1].health}\n3. {self.robots[2].name}\n Health:   {self.robots[2].health}\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n"))
                if user_choice > 1 or user_choice < 3:
                    continue
            if user_choice == 1:
                print(f"{self.robots[0].name} is preparing to attack")
                self.robots[0].weapon = self.robots[0].get_weapon()
                return self.robots[0]
            elif user_choice == 2:
                print(f"{self.robots[1].name} is preparing to attack")
                self.robots[1].weapon = self.robots[1].get_weapon()
                return self.robots[1]
            elif user_choice == 3:
                print(f"{self.robots[2].name} is preparing to attack")
                self.robots[2].weapon = self.robots[2].get_weapon()
                return self.robots[2]

    def choose_random_robo_attacker(self):
        for robot in self.robots:
            choice = random.choice([1, 2, 3])
            if choice == 1:
                print(f"{self.robots[0].name} is preparing to attack")
                self.robots[0].weapon = self.robots[0].get_random_weapon()
                return self.robots[0]
            elif choice == 2:
                print(f"{self.robots[1].name} is preparing to attack")
                self.robots[1].weapon = self.robots[1].get_random_weapon()
                return self.robots[1]
            elif choice == 3:
                print(f"{self.robots[2].name} is preparing to attack")
                self.robots[2].weapon = self.robots[2].get_random_weapon()
                return self.robots[2]

    def remove_dead_bot(self):
        for robot in self.robots:
            if self.robots[0].health < 1:
                self.robots.remove(self.robots[0])
                print(f"{self.robots[0].name} is dead!")
            elif self.robots[1].health < 1:
                self.robots.remove(self.robots[1])
                print(f"{self.robots[1].name} is dead!")
            elif self.robots[1].health < 1:
                self.robots.remove(self.robots[1])
                print(f"{self.robots[1].name} is dead!")
                
    def random_robot_to_be_attacked(self):
        for robot in self.robots:
            choice = random.choice([1, 2, 3])
            if choice == 1:
                return self.robots[0]
            elif choice == 2:
                return self.robots[1]
            elif choice == 3:
                return self.robots[2]

    def robot_to_be_attacked(self):
        for robot in self.robots:
            user_choice = int(input(f"------------------------------------------------------------------------------------------------------------------------------------------------------------------------\nChoose your choose your target!!!\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n1. {self.robots[0].name}\n    Health:{self.robots[0].health}\n2. {self.robots[1].name}\n    Health:{self.robots[1].health}\n3. {self.robots[2].name}\n    Health:{self.robots[2].health}\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n"))
            while user_choice  < 1 or user_choice > 3:
                user_choice = int(input(f"------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n***INVALID RESPONSE*** \nChoose your choose your target!!!\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n1. {self.robots[0].name}\n Health:   {self.robots[0].health}\n2. {self.robots[1].name}\n Health:   {self.robots[1].health}\n3. {self.robots[2].name}\n Health:   {self.robots[2].health}\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n"))
                if user_choice > 1 or user_choice < 3:
                    continue
            if user_choice == 1:
                return self.robots[0]
            elif user_choice == 2:
                return self.robots[1]
            elif user_choice == 3:
                return self.robots[2]