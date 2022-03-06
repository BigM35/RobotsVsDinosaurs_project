



class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 500
        self.ability = ("Tail Whip", "Two Step", "Ferocious Licking")
    
    def attack(self, robot): #void 
        robot.health -= self.attack_power
        print(f"{self.name} attacked {robot.name} with {self.ability} dealing {self.attack_power} damage!!!")

    def choose_attack(self):
        for ability in self.ability:
            user_choice = int(input(f"Choose your ability!\n1. {self.ability[0]}\n2. {self.ability[1]}\n3. {self.ability[2]} \n"))
            while user_choice < 1 or user_choice > 3:
                user_choice = int(input(f"***INVALID RESPONSE***\nChoose your ability!\n1. {self.ability[0]}\n2. {self.ability[1]}\n3. {self.ability[2]} \n"))
            if user_choice == 1:
                return self.ability[0]
            elif user_choice == 2:    
                return self.ability[1]
            elif user_choice == 3:   
                return self.ability[2]