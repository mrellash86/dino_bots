from robot import Robot
from weapon import Weapon

class Fleet:
    def __init__(self):
        self.robots = []
        self.create_fleet()
    
    def create_fleet(self):
        weapon_one = Weapon("M4", 5)
        weapon_two = Weapon("240 Bravo", 10)
        weapon_three = Weapon("50 cal", 20)

        robo_one = Robot("Tron", weapon_one)
        robo_two = Robot("Optimus", weapon_two)
        robo_three = Robot("NEO", weapon_three)

        self.robots.append(robo_one)
        self.robots.append(robo_two)
        self.robots.append(robo_three)

my_fleet = Fleet()
