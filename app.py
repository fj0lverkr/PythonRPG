from GameTools.Dice import GameDice
from Assets import Player

d20 = GameDice(20)
rolls = []
for i in range (5):
    rolls.append(d20.roll())

print(rolls)