
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

        self.battle()

        
    def display_welcome(self): #void
        user_input = input("WELCOME TO ROBOTS VS DINOSAURS!\nYOU WILL BE GIVEN THE OPTION TO PLAY AS FLEET OF ROBOT WITH MISSION TO MAKE THE DINOSAURS GO EXTINCT,\nOR AS A HERD DINOSAURS, FIGHTING OFF YOUR EXTINTION AND TERMINATING THE ROBOTS!\nUSE THE NUMBER KEYS [0] ,[1] ,AND [2] TO MAKE YOUR CHOICES.\n\nARE YOU READY TO START THIS EPIC BATTLE? TYPE [YES] OR [NO] TO GET STARTED: \n   ").lower()            
        if user_input == "yes":
            self.run_game()
        else:
            print("GOODBYE, COME BACK WHEN YOU ARE READY FOR THE CHALLEGE OF YOUR LIFE!!!")
    
    def battle(self): #void
        user_choice = int(input("------------------------------------------------------------------------------------------------------------------------------------------------------------------------\nChoose your side!!!\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n1. Robot Fleet\n2. Dinosaurs Herd\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n"))
        while user_choice  < 1 or user_choice > 2:
            user_choice = int(input("------------------------------------------------------------------------------------------------------------------------------------------------------------------------\nINVALID INPUT!!!\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------\nPress 1 or 2\n1. Robot Fleet\n2. Dinosaurs Herd\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n"))
            if user_choice > 1 or user_choice < 2:
                continue
        if user_choice == 1:
            for players in range(len(self.fleet.robots)) and range(len(self.herd.dinosaurs)):
                while self.fleet.robots[players].health > 0 and self.herd.dinosaurs[players].health > 0:
                    self.herd.remove_dead_dino()
                    self.robo_turn()
                    self.fleet.remove_dead_bot()
                    self.random_dino_turn()
                    if self.fleet.robots[0].health == 0 and (self.fleet.robots[1].health == 0, self.fleet.robots[2].health == 0):
                        self.display_loser()
                    elif self.herd.dinosaurs[0].health == 0 and (self.herd.dinosaurs[1].health == 0, self.herd.dinosaurs[2].health == 0):
                        self.display_winner
                
        if  user_choice == 2:
            for players in range(len(self.fleet.robots)) and range(len(self.herd.dinosaurs)):
                while self.fleet.robots[players].health > 0 and self.herd.dinosaurs[players].health > 0:
                    self.dino_turn()
                    self.herd.remove_dead_dino()
                    self.random_robo_turn()
                    self.fleet.remove_dead_bot()
                    if self.fleet.robots[0].health == 0 and (self.fleet.robots[1].health == 0, self.fleet.robots[2].health == 0):
                        self.display_winner()
                    elif self.herd.dinosaurs[0].health == 0 and (self.herd.dinosaurs[1].health == 0, self.herd.dinosaurs[2].health == 0):
                        self.display_loser()
                         
    def random_dino_turn(self):
        #Choose robot
        dino_atker = self.herd.choose_random_dino_attacker()
        #choose opponet & attack
        robot_target = self.fleet.random_robot_to_be_attacked()
        for dino in range(len(self.herd.dinosaurs)):
            if robot_target == "na"  or dino_atker == "na":
                continue
            if dino_atker == self.herd.dinosaurs[dino].name:
                self.herd.dinosaurs[dino].attack(robot_target)   
                   
    def random_robo_turn(self):
        #Choose robot
        robot_atker = self.fleet.choose_random_robo_attacker()
        #choose opponet & attack
        dino_target = self.herd.random_dinosaur_to_be_attacked()
        for robot in range(len(self.fleet.robots)):
            if dino_target == "na"  or robot_atker == "na":
                continue
            if robot_atker == self.fleet.robots[robot].name:
               self.fleet.robots[robot].attack(dino_target)  

    def dino_turn(self): #void
        #Choose Dino (attacker)
        dino_atker = self.herd.choose_dino_attacker()
        #choose opponet & attack
        robot_target = self.fleet.robot_to_be_attacked()
        for dino in range(len(self.herd.dinosaurs)):
            if robot_target == "na" or dino_atker == "na":
                continue
            if dino_atker == self.herd.dinosaurs[dino].name:
                self.herd.dinosaurs[dino].attack(robot_target)

    def robo_turn(self):
        #Choose robot
        robot_atker = self.fleet.choose_robo_attacker()
        #choose opponet & attack
        dino_target = self.herd.dinosaur_to_be_attacked()
        for robot in range(len(self.fleet.robots)):
            if dino_target == "na"  or robot_atker == "na":
                continue
            if robot_atker == self.fleet.robots[robot].name:
               self.fleet.robots[robot].attack(dino_target)
           
    def display_winner(self):  #void
        print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------\nCONGRATULATIONS! \nYOU ARE THE WINNER!!!\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

    def display_loser(self):  #void
        print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------\nGAME OVER! \nYOU LOST!!!\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

#Instantiate Robots
pathfinder = Robot("Pathfinder")
r2d2 = Robot("R2D2")
ash = Robot("Ash")
    
#instantiate Dinosaurs
irritator = Dinosaur("Irritator", 100, 30)
rexicutioner = Dinosaur("Rexicutioner", 200, 75)
yoshi_saurus = Dinosaur("Yoshi-saurus", 50, 20)

