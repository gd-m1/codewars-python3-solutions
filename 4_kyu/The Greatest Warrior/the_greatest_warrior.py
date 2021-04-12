# https://www.codewars.com/kata/5941c545f5c394fef900000c

RANKS = ("Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage",
         "Elite", "Conqueror", "Champion", "Master", "Greatest")


class Warrior():
    def __init__(self, experience=100):
        self.experience = experience
        self.achievements = []

    @property
    def level(self):
        return self.experience // 100 if self.experience <= 10000 else 100

    @property
    def rank(self):
        return RANKS[self.level // 10] if self.level <= 100 else RANKS[-1]

    def training(self, array):
        if self.level >= array[2]:
            self.experience += array[1]
            if self.experience > 10000:
                self.experience = 10000
            self.achievements.append(array[0])
            return array[0]
        return "Not strong enough"

    def battle(self, enemy):
        if not 0 < enemy <= 100:
            return "Invalid level"
        delta = enemy - self.level
        if delta == 0:
            self.experience += 10
            return "A good fight"
        elif delta == -1:
            self.experience += 5
            return "A good fight"
        elif (enemy // 10 - self.level // 10) > 0 and (enemy - self.level) > 4:
            return "You've been defeated"
        elif delta > 0:
            self.experience += 20 * delta * delta
            return "An intense fight"
        return "Easy fight"
