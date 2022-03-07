



from importlib.metadata import requires


class Weapon:
    def __init__(self, name:str, attack_power:int, power_require:int):
        self.name = name
        self.attack_power = attack_power
        self.power_require = power_require

    