from GameTools.Dice import GameDice
from Assets.Characters import Player

d20 = GameDice(20)
you = Player("Nils", "Human", 33, "M", last_name="Nahooy")
print(you)
you.add_stat_point("strength", points=5)
you.show_stats()