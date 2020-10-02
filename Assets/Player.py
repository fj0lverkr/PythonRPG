class Player:
    def __init__(self, first_name, race, age, sex, strength, wits, charisma, agility, luck, current_health, current_stamina, last_name=""):
        self.first_name = first_name
        self.race = race
        self.age = age
        self.sex = sex
        self.level = 1
        self.stats = {"strength": 0, "wits":0, "charisma": 0, "agility": 0, "luck": 0}
        if self.race == "human":
            self.max_health = 100
            self.max_stamina = 100
            self.stats["strength"] = 3
            self.stats["wits"] = 2
            self.stats["charisma"] = 3
            self.stats["agility"] = 2
            self.stats["luck"] = 5
