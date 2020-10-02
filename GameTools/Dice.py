import random, math


class GameDice:
    def __init__(self, faces):
        self.faces = faces

    def roll(self):
        return math.ceil(random.random() * self.faces)