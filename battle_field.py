from csv import Dialect
from importlib.machinery import PathFinder
from dinosaur import Dinosaur
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
        self.fleet.create_fleet(pathfinder)
        self.fleet.create_fleet(r2d2)
        self.fleet.create_fleet(ash)
        self.herd.create_herd(irritator)
        self.herd.create_herd(yoshi_saurus)
        self.herd.create_herd(rexicutioner)

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
        self.fleet.choose_robo_attacker()
        #choose opponet & attack
        dino_target = self.herd.dinosaur_to_be_attacked()
        for robot in self.fleet.robots:
            if self.fleet.choose_robo_attacker == robot:
                self.fleet.robots.robot.attack(dino_target)
                            
            else:
                continue
    def show_dino_opponent_option(self): #void
        pass

    def show_robo_opponent_option(self): #void
        pass

    def display_winners(self):  #void
        pass

    #instain

#Create Robots
pathfinder = Robot("Pathfinder")
r2d2 = Robot("R2D2")
ash = Robot("Ash")
    
#Robo weapons

#Robot Fleet



#arm robot

#choose robot to attack



#Dinosaurs names
irritator = Dinosaur("Irritator", 75)
rexicutioner = Dinosaur("Rexicutioner", 100)
yoshi_saurus = Dinosaur("Yoshi-saurus", 50)

