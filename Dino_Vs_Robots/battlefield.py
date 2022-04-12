from fleet import Fleet
from herd import Herd
import random



class Battlefield:
    def __init__(self): 
        self.fleet = Fleet
        self.herd = Herd

    def run_game(self):
        self.display_welcome()
        self.battle()
        self.display_winners()

    def display_welcome(self):
        print('Welcome to Dino Jungle')

    def battle(self):
        while (len(self.herd.dinosaurs) > 0 and len(self.fleet.robots) > 0):
            roll_dice = random.randint(1,2)
            if roll_dice == 2:
                self.show_dino_opponent_options()
                dino_selection = int(input('Type the number of the Dino that you choose!'))
                self.dino_turn(self.herd.dinosaurs[dino_selection])
            else:
                self.show_robo_opponent_options()
                robo_selection = int(input("Type the numer of the Robot that you choose!"))
                self.robo_turn(self.fleet.robots[robo_selection])

    def dino_turn(self,dinosaur):
        self.show_robo_opponent_options()
        user_choice = input("Select the robots that you would like to attack:")
        dinosaur.attack(self.fleet.robots[user_choice])

        if self.fleet.robots[user_choice].health <= 0:
            print(f'It seems that {self.fleet.robots[user_choice].name} has died!!!')
            self.fleet.robots.remove(self.fleet.robots[user_choice])

    def robo_turn(self,robot):
        self.show_dino_opponent_options()
        user_choice = int(input("Choose a Dino to Attack"))
        robot.attack(self.herd.dinosaurs[user_choice])
        if self.herd.dinosaurs[user_choice].health <= 0: 
            print(f"{self.herd.dinosaurs[user_choice.name]} the dino is dead")
            self.herd.dinosaurs.remove(self.herd.dinosaurs[user_choice])

    def show_dino_opponent_options(self):
        print('These are the current Dino Opponents:')
        index = 0
        for dinosaurs in self.herd.dinosaurs:
            print(f'Type in {index} to choose {dinosaurs.name} the Dino. {dinosaurs.health} health & {dinosaurs.attack_power} attack power when at 100 percent')
            index += 1

    def show_robo_opponent_options(self):
        print('These are the current Dino Opponents:')
        index = 0
        for robots in self.fleet.robots:
            print(f'Type in {index} to choose {robots.name} the Dino. {robots.health} health & {robots.attack_power} attack power when at 100 percent')
            index += 1


    def display_winners(self):
        if len(self.fleet.robots) > len(self.herd.dinosaurs):
            print("The Robots have won!")
        else:
            print(" The Dinos Win!")
        

my_battlefield = Battlefield()
my_battlefield.show_dino_opponent_options() 
my_battlefield.show_robo_opponent_options()
