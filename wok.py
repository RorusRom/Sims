class HO:
    def __init__(self, mood, disorder, money):
        self.mood = mood
        self.mess = disorder
        self.money = money

    def chill(self):
        self.mood += 10
        self.mess += 5

    def clean_home(self):
        self.mood -= 5
        self.mess = 0

    def to_repair(self):
        self.car += 100
        self.money -= 50
