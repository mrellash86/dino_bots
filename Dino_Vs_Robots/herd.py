from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.create_herd()

    def create_herd(self):
        
        first_dino = Dinosaur("Triceryltops", 20)
        second_dino = Dinosaur("T-Rex", 25)
        third_dino = Dinosaur("Lizards", 5)

        self.dinosaurs.append(first_dino)
        self.dinosaurs.append(second_dino)
        self.dinosaurs.append(third_dino)

my_herd = Herd()
        