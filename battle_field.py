from fleet import Fleet
from herd import Herd
from weapon import Weapon
from robot import Robot

class BattleField:
    def __init__(self) -> None:
        self.fleet = Fleet
        self.herd = Herd

    def run_game(self): #void
        pass
    
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
        Robot.get_weapon()
        #Choose robot
        self.fleet.choose_robo_attacker()
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
excalibur = Weapon("Excalibur", 75)
force = Weapon("Force Cascade", 50)
meteor = Weapon("Meteor Cannon", 100)

#Robot Fleet
robot_fleet = Fleet()


#arm robot

#choose robot to attack
robot_fleet
