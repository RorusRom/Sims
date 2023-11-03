class HO:
    def __init__(self, mood, disorder, money):
        self.mood = mood
        self.disorder = disorder
        self.money = money

    def chill(self):
        self.mood += 10
        self.disorder += 5

    def clean_home(self):
        self.mood -= 5
        self.disorder = 0

    def to_repair(self):
        self.car_condition += 100
        self.money -= 50