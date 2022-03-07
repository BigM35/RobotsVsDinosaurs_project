import random



class Dinosaur:
    def __init__(self, name, attack_power, req_energy):
        self.name = name
        self.attack_power = attack_power
        self.health = 500
        self.ability = ()
        self.energy = 800
        self.req_energy = req_energy
    touple = "Tail Whip", "Two Step", "Ferocious Licking"

    def attack(self, robot): #void
        if self.name == "Yoshi-saurus":
            hit = random.randint(0, 10)
            self.energy -= self.req_energy
            if hit <= 1:
                print(f"{self.name} missed the attack on {robot.name}!!!")        
            else:
                robot.health -= self.attack_power
                print(f"{self.name} attacked {robot.name} with {self.ability}, dealing {self.attack_power} damage!!!")
        elif self.name == "Irritator":
            hit = random.randint(0, 10)
            self.energy -= self.req_energy
            if hit <= 30:
                print(f"{self.name} missed the attack on {robot.name}!!!")        
            else:
                robot.health -= self.attack_power
                print(f"{self.name} attacked {robot.name} with {self.ability}, dealing {self.attack_power} damage!!!")
        elif self.name == "Rexicutioner":
            hit = random.randint(0, 10)
            self.energy -= self.req_energy
            if hit <= 5:
                print(f"{self.name} missed the attack on {robot.name}!!!")        
            else:
                robot.health -= self.attack_power
                print(f"{self.name} attacked {robot.name} with {self.ability}, dealing {self.attack_power} damage!!!")
    
    def choose_attack(self):
        dino_skills = "Tail Whip", "Two Step", "Ferocious Licking"
        user_choice = int(input(f"------------------------------------------------------------------------------------------------------------------------------------------------------------------------\nChoose your ability!\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n0. {dino_skills[0]}\n1. {dino_skills[1]}\n2. {dino_skills[2]}\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n"))
        while user_choice < 0 or user_choice > 2:
            user_choice = int(input(f"------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n***INVALID RESPONSE***\nChoose your ability!\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n0. {dino_skills[0]}\n1. {dino_skills[1]}\n2. {dino_skills[2]}\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n"))
        for skill in range(len(dino_skills)):
            if user_choice == skill:
                return dino_skills[skill]
            
    def choose_random_attack(self):
        dino_skill_tuple = "Tail Whip", "Two Step", "Ferocious Licking"
        choice = random.choice([0, 1, 2])
        for skill in range(len(dino_skill_tuple)):
            if choice == skill:
                return dino_skill_tuple[skill]
           