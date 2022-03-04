from robot import Robot



class Fleet:
    def __init__(self) -> None:
        self.robots = []

    def create_fleet(self, robot1, robot2, robot3): #void
        self.robots.append(robot1)
        self.robots.append(robot2)
        self.robots.append(robot3)
       
    

    def choose_robo_attacker(self):
        for robot in self.robots:
            user_choice = int(input(f"Choose your fighter!\n1. {self.robots[0].name}\n Health:   {self.robots[0].health}\n2. {self.robots[1].name}\n Health:   {self.robots[1].health}\n3. {self.robots[2].name}\n Health:   {self.robots[2].health}\n"))
            while user_choice != 1 or 2 or 3:
                user_choice = int(input("***INVALID RESPONSE*** \nChoose your Fighter!\n 1. {self.robots[0].name}\n Health:   {self.robots[0].health}\n\n2. {self.robots[1].name}\n Health:   {self.robots[1].health}\n3. {self.robots[2].name}\n Health:   {self.robots[2].health}\n"))
            if user_choice == 1:
                return self.robots[0]
            elif user_choice == 2:
                return self.robots[1]
            elif user_choice == 3:
                return self.robots[2]

