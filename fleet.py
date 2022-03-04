from robot import Robot



class Fleet:
    def __init__(self) -> None:
        self.robots = []

    def create_fleet(self, robot): #void
        self.robots.append(robot)
    
    def get_weapon(self):
        user_choice = int(input("Choose your ability!\n1. Excalibur\n2. Force Cascade\n3. Meteor Cannon: \n"))
        while user_choice < 1 or user_choice > 3:
            user_choice = int(input("***INVALID RESPONSE***\nChoose your ability!\n1. Excalibur\n2. Force Cascade\n3. Meteor Cannon: \n"))
        excalibur = Weapon("Excalibur", 75)
        force = Weapon("Force Cascade", 50)
        meteor = Weapon("Meteor Cannon", 100)   
        
        if user_choice == 1:
            return excalibur
        elif user_choice == 2:    
            return force
        elif user_choice == 3:   
            return meteor

    def choose_robo_attacker(self):
        for robot in self.robots:
            user_choice = int(input(f"Choose your fighter!\n1. {self.robots[0].name}\n Health:   {self.robots[0].health}\n2. {self.robots[1].name}\n Health:   {self.robots[1].health}\n3. {self.robots[2].name}\n Health:   {self.robots[2].health}\n"))
            while user_choice  < 1 or user_choice > 3:
                user_choice = int(input("***INVALID RESPONSE*** \nChoose your Fighter!\n 1. {self.robots[0].name}\n Health:   {self.robots[0].health}\n\n2. {self.robots[1].name}\n Health:   {self.robots[1].health}\n3. {self.robots[2].name}\n Health:   {self.robots[2].health}\n"))
            if user_choice == 1:
                print(f"{self.robots[0].name} is preparing to attack")
                self.robots[0].weapon = self.robots[0].get_weapon()
            elif user_choice == 2:
                print(f"{self.robots[1].name} is preparing to attack")
                self.robots[1].weapon = self.robots[1].get_weapon()
            elif user_choice == 3:
                print(f"{self.robots[2].name} is preparing to attack")
                self.robots[2].weapon = self.robots[2].get_weapon()

    def remove_dead_bot(self):
        for robot in self.robots:
            if self.robots[robot].health < 1:
                self.robots.remove(robot)
                print(f"{self.robots(robot).name} is dead!")