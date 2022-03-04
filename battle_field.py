from importlib.machinery import PathFinder
from fleet import Fleet
from herd import Herd
from weapon import Weapon
from robot import Robot
from random import Random
class BattleField:
    def __init__(self) -> None:
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self): #void
        self.fleet = Fleet.create_fleet(pathfinder)
        self.fleet = Fleet.create_fleet(r2d2)
        self.fleet = Fleet.create_fleet(ash)
        self.herd = Herd.create_herd
    def display_welcome(self): #void
        pass            
    
    def battle(self): #void
        pass

    def dino_turn(self): #void
            pass
        #Choose Dino (attacker)
        #choose attack
        #choose opponet & attack

    def robo_turn(self): #void
        #Get weapon
        #Choose robot
        rob_atk = self.fleet.choose_robo_attacker()
        #choose opponet & attack
        
    def show_dino_opponent_option(self): #void
        pass

    def show_robo_opponent_option(self): #void
        pass

    def display_winners(self):  #void
        pass

#Create Robots
pathfinder = Robot("Pathfinder")
r2d2 = Robot("R2D2")
ash = Robot("Ash")
    
#Robo weapons

#Robot Fleet



#arm robot

#choose robot to attack

