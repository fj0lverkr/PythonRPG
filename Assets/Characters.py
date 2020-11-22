from rich.table import Table
from rich.console import Console


class Character:
    def __init__(self, first_name, race, age, sex, last_name=None, job=None):
        self.first_name = first_name.title()
        if last_name != None:
            self.last_name = last_name.title()
            self.full_name = f"{self.first_name} {self.last_name}"
        else:
            self.last_name = ""
            self.full_name = self.first_name
        self.race = race.lower()
        self.age = age
        self.sex = sex.upper()
        self.level = 1
        self.stats = {"strength": 0, "wits":0, "charisma": 0, "agility": 0, "luck": 0, "dexterity": 0}
        self.max_health = 1
        self.max_stamina = 1
        self.health = 1
        self.stamina = 1

    def show_stats(self):

        table = Table(title=self.__str__())

        table.add_column("Health", justify="left", style="red", no_wrap=True)
        table.add_column("Stamina", justify="left", style="cyan")
        table.add_column("Strength", justify="right", style="magenta")
        table.add_column("Wits", justify="right", style="white")
        table.add_column("Charisma", justify="right", style="green")
        table.add_column("Agility", justify="right", style="yellow")
        table.add_column("Luck", justify="right", style="green")
        table.add_column("Dexterity", justify="right", style="blue")

        table.add_row(f"{self.health}/{self.max_health}", f"{self.stamina}/{self.max_stamina}",
                        str(self.stats["strength"]), str(self.stats["wits"]), str(self.stats["charisma"]),
                        str(self.stats["agility"]), str(self.stats["luck"]), str(self.stats["dexterity"]))

        console = Console()
        console.print(table)


class Player(Character):
    def __init__(self, first_name, race, age, sex, last_name=None, job=None):
        super().__init__(first_name, race, age, sex, last_name, job)
        if self.race == "human":
            self.max_health = 100
            self.max_stamina = 100
            self.stats["strength"] = 3
            self.stats["wits"] = 2
            self.stats["charisma"] = 3
            self.stats["agility"] = 2
            self.stats["luck"] = 2
            self.stats["dexterity"] = 3
        elif self.race == "dwarf":
            self.max_health = 120
            self.max_stamina = 75
            self.stats["strength"] = 5
            self.stats["wits"] = 2
            self.stats["charisma"] = 1
            self.stats["agility"] = 1
            self.stats["luck"] = 2
            self.stats["dexterity"] = 4

        self.health = self.max_health
        self.stamina = self.max_stamina

    def __str__(self):
        return f"Player {self.full_name}, a level {self.level} {self.race}."

    def add_stat_point(self, stat, points=1):
        self.stats[stat] += points
        print(f"Your {stat} is now {self.stats[stat]}.")
