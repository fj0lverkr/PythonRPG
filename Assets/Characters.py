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

    def __str__(self):
        return f"Player {self.full_name}, a level {self.level} {self.race}."