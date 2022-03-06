from csv import Dialect
from importlib.machinery import PathFinder
from dinosaur import Dinosaur
from fleet import Fleet
from herd import Herd
from weapon import Weapon
from robot import Robot
import random
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

        self.display_welcome()
        self.battle()

        
            
    def display_welcome(self): #void
        pass            
    
    def battle(self): #void
        user_choice = int(input("------------------------------------------------------------------------------------------------------------------------------------------------------------------------\nChoose your side!!!\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n1. Robot Fleet\n2. Dinosaurs Herd\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n"))
        while user_choice  < 1 or user_choice > 2:
            user_choice = int(input("------------------------------------------------------------------------------------------------------------------------------------------------------------------------\nINVALID INPUT!!!\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------\nPress 1 or 2\n1. Robot Fleet\n2. Dinosaurs Herd\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n"))
            if user_choice > 1 or user_choice < 2:
                continue
        if user_choice == 1:
            while len(self.fleet.robots) > 0 and len(self.herd.dinosaurs) > 0:
                while True:
                    self.robo_turn()
                    self.random_dino_turn()
        if user_choice == 2:
            starter = random.choice(self.random_robo_turn(),  self.dino_turn())
            if starter == self.random_dino_turn():
                while True:
                    if len(self.fleet.robots) > 0 and len(self.herd.dinosaurs) > 0:
                        self.robo_turn()
                        self.random_dino_turn()
                    else:
                        self.display_winners
            elif starter == self.robo_turn():      
                while True:
                    if len(self.fleet) > 0 and len(self.herd) > 0:    
                        self.random_dino_turn()
                        self.robo_turn()
                    else:
                        self.display_winners
    
    def random_dino_turn(self):
        #Choose robot
        dino_atker = self.herd.choose_random_dino_attacker()
        #choose opponet & attack
        robot_target = self.fleet.random_robot_to_be_attacked()
        for dino in self.herd.dinosaurs:
            if dino_atker.name == dino.name:
                dino.attack(robot_target)   
            else:
                continue
        self.herd.remove_dead_dino()      

    def random_robo_turn(self):
        #Choose robot
        robot_atker = self.fleet.choose_random_robo_attacker()
        #choose opponet & attack
        dino_target = self.herd.random_dinosaur_to_be_attacked()
        for robot in self.fleet.robots:
            if robot_atker.name == robot.name:
                robot.attack(dino_target)  
            else:
                continue
        self.fleet.remove_dead_bot()

    def dino_turn(self): #void
        #Choose Dino (attacker)
        dino_atker = self.herd.choose_dino_attacker()
        #choose opponet & attack
        robot_target = self.fleet.robot_to_be_attacked()
        for dino in self.herd.dinosaurs:
            if dino_atker.name == dino.name:
                dino.attack(robot_target)
            else:
                continue
        self.herd.remove_dead_dino()

    def robo_turn(self):
        #Choose robot
        robot_atker = self.fleet.choose_robo_attacker()
        #choose opponet & attack
        dino_target = self.herd.dinosaur_to_be_attacked()
        for robot in self.fleet.robots:
            if robot_atker.name == robot.name:
                robot.attack(dino_target)
            else:
                continue
        self.fleet.remove_dead_bot()   

    def show_dino_opponent_option(self): #void
        pass

    def show_robo_opponent_option(self): #void
        pass

    def display_winners(self):  #void
        pass


#Instantiate Robots
pathfinder = Robot("Pathfinder")
r2d2 = Robot("R2D2")
ash = Robot("Ash")
    
#Robo weapons

#Robot Fleet



#arm robot

#choose robot to attack



#Dinosaurs names
irritator = Dinosaur("Irritator", 100)
rexicutioner = Dinosaur("Rexicutioner", 200)
yoshi_saurus = Dinosaur("Yoshi-saurus", 50)

