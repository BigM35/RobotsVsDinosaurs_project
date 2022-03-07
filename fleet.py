import random



class Fleet:
    def __init__(self) -> None:
        self.robots = []

    def create_fleet(self, robot): #void
        self.robots.append(robot)
    
    def choose_robo_attacker(self):
        user_choice = int(input(f"------------------------------------------------------------------------------------------------------------------------------------------------------------------------\nChoose your fighter!\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n0. {self.robots[0].name}\n    Health:{self.robots[0].health}\n      Power:{self.robots[0].power_level}\n1. {self.robots[1].name}\n    Health:{self.robots[1].health}\n      Power:{self.robots[1].power_level}\n2. {self.robots[2].name}\n    Health:{self.robots[2].health}\n     Power:{self.robots[2].power_level}\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n"))
        while user_choice  < 0 or user_choice > 2:
            user_choice = int(input(f"------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n***INVALID RESPONSE***\nChoose your Fighter!\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n0. {self.robots[0].name}\n Health:   {self.robots[0].health}      \n{self.robots[0].power_level}\n1. {self.robots[1].name}\n Health:   {self.robots[1].health}      \n{self.robots[1].power_level}\n2. {self.robots[2].name}\n Health:   {self.robots[2].health}      \n{self.robots[2].power_level}\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n"))
            if user_choice > 0 or user_choice < 2:
                continue
        for robot in range(len(self.robots)):
            if user_choice == robot:
                if self.robots[robot].health > 0:
                    print(f"{self.robots[robot].name} is preparing to attack")
                    self.robots[robot].weapon = self.robots[robot].get_weapon()
                    if self.robots[robot].weapon.power_require > self.robots[robot].power_level:
                        print(f"{self.robots[robot].name}does not have the required power to use{self.robots[robot].weapon.name}")
                        return "na"
                    else:
                        return self.robots[robot].name
                else:
                    print("Chosen Robot was TERMINATED!!!")
                    return "na"

    def choose_random_robo_attacker(self):
        choice = random.choice([0, 1, 2])
        for robot in range(len(self.robots)):
            if choice == robot:
                if self.robots[robot].health > 0:
                    print(f"{self.robots[robot].name} is preparing to attack")
                    self.robots[robot].weapon = self.robots[robot].get_random_weapon()
                    if self.robots[robot].weapon.power_require > self.robots[robot].power_level:
                        print(f"{self.robots[robot].name}does not have the required power to use{self.robots[robot].weapon.name}")
                        return "na"
                    else:
                        return self.robots[robot].name
                else:
                    print("Chosen Robot was TERMINATED!!!")
                    return "na"
                
    def random_robot_to_be_attacked(self):
        choice = random.choice([0, 1, 2])
        for robo in range(len(self.robots)):
            if choice == robo:
                if self.robots[robo].health > 0:
                    return self.robots[robo]
                else:
                    print("Chosen Robot was already TERMINATED!!!")
                    return "na"

    def robot_to_be_attacked(self):
        user_choice = int(input(f"------------------------------------------------------------------------------------------------------------------------------------------------------------------------\nChoose your choose your target!!!\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n0. {self.robots[0].name}\n    Health:{self.robots[0].health}\n1. {self.robots[1].name}\n    Health:{self.robots[1].health}\n2. {self.robots[2].name}\n    Health:{self.robots[2].health}\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n"))
        while user_choice  < 0 or user_choice > 2:
            user_choice = int(input(f"------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n***INVALID RESPONSE*** \nChoose your choose your target!!!\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n0. {self.robots[0].name}\n Health:   {self.robots[0].health}\n1. {self.robots[1].name}\n Health:   {self.robots[1].health}\n2. {self.robots[2].name}\n Health:   {self.robots[2].health}\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n"))
            if user_choice > 0 or user_choice < 2:
                continue
        for robo in range(len(self.robots)):
            if user_choice == robo:
                if self.robots[robo].health > 0:
                    return self.robots[robo]
                else:
                    print("Chosen Robot was already TERMINATED!!!")
                    return "na"
        
    def remove_dead_bot(self):
        for robo in range(len(self.robots)):
            if self.robots[robo].health < 1:
                if "(TERMINATED)" in  self.robots[robo].name:
                    continue
                else:
                    print(f"{self.robots[robo].name} was Terminated!!!")
                    self.robots[robo].name += " (TERMINATED)"
                    self.robots[robo].health = 0
