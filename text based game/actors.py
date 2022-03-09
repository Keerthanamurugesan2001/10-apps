import random


class creators:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def get_defence_roll(self):
        return self.level * random.randint(1, 12)


class wizard(creators):

    def attack(self, enemy):
        hero_score = self.get_defence_roll()
        enemy_score = enemy.get_defence_roll()

        print(f"{self.name} has {hero_score}")
        print(f"{enemy.name} has {enemy_score}")

        if hero_score > enemy_score:
            return True
        else:
            return False

    def look_around(self, actor):
        print("-------------------------------")
        for i in actor:
            print(f"{i.name} has {i.level} level")
        print("---------------------------------")
    def runaway(self, enemy):
        pass


class smallanimal(creators):

    def get_defence_roll(self):
        return random.randint(1, 12) * self.level / 2


class dragon(creators):
    def __init__(self, name, level, scaliness, firebreath):
        super().__init__(name, level)
        self.scaliness = scaliness
        self.firebreath = firebreath

    def get_defence_roll(self):
        if self.scaliness:
            self.scaliness = self.scaliness / 2
        if self.firebreath:
            self.firebreath = self.firebreath * 2
        return random.randint(1, 12) * self.level * self.scaliness * self.firebreath
