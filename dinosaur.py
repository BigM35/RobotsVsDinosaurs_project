



from unicodedata import name


class Dinosaur:
    def __init__(self, name, attack_power) -> None:
        self.name = name
        self.attack_power = attack_power
        self.health = 500
    
    def attack(self, robot): #void 
        pass