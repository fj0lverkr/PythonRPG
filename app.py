from GameTools.Dice import GameDice
from Assets.Characters import Player
from GameTools.Game import Game

d20 = GameDice(20)
you = Player("Nils", "Human", 33, "M", last_name="Nahooy")
you.add_stat_point("strength", points=5)
you.show_stats()

if __name__ == "__main__":
    sample_game = Game("GameData/sample_game.xml", player=you)
    sample_game.start_game()
    