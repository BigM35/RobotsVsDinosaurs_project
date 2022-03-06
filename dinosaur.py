import random



class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 500
        self.ability = ("Tail Whip", "Two Step", "Ferocious Licking")
    
    def attack(self, robot): #void
        if self.name == "Yoshi-saurus":
            hit = random.randint(0, 10)
            if hit <= 1:
                print(f"{self.name} missed the attack on {robot.name}!!!")        
            else:
                robot.health -= self.attack_power
                print(f"{self.name} attacked {robot.name} with {self.ability}, dealing {self.attack_power} damage!!!")
        elif self.name == "Irritator":
            hit = random.randint(0, 10)
            if hit <= 30:
                print(f"{self.name} missed the attack on {robot.name}!!!")        
            else:
                robot.health -= self.attack_power
                print(f"{self.name} attacked {robot.name} with {self.ability}, dealing {self.attack_power} damage!!!")
        elif self.name == "Rexicutioner":
            hit = random.randint(0, 10)
            if hit <= 5:
                print(f"{self.name} missed the attack on {robot.name}!!!")        
            else:
                robot.health -= self.attack_power
                print(f"{self.name} attacked {robot.name} with {self.ability}, dealing {self.attack_power} damage!!!")
    
    def choose_attack(self):
        for ability in self.ability:
            user_choice = int(input(f"------------------------------------------------------------------------------------------------------------------------------------------------------------------------\nChoose your ability!\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n1. {self.ability[0]}\n2. {self.ability[1]}\n3. {self.ability[2]}\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n"))
            while user_choice < 1 or user_choice > 3:
                user_choice = int(input(f"------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n***INVALID RESPONSE***\nChoose your ability!\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n1. {self.ability[0]}\n2. {self.ability[1]}\n3. {self.ability[2]}\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n"))
            if user_choice == 1:
                return self.ability[0]
            elif user_choice == 2:    
                return self.ability[1]
            elif user_choice == 3:   
                return self.ability[2]

    def choose_random_attack(self):
        for skill in self.ability:
            choice = random.choice([1, 2, 3])
            if choice == 1:
                return self.ability[0]
            elif choice == 2:    
                return self.ability[1]
            elif choice == 3:   
                return self.ability[2]