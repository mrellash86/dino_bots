class Robot:
    def __init__(self, name, weapon):
        self.name = name
        self.health = 100
        self.weapon = weapon
    
    def attack(self, dinosaur):
        dinosaur.health -= self.attack_power
        print(f'{dinosaur.name} took a hit for {self.weapon.attack_power}damage!')
        

