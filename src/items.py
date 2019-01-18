import random


class Consumable:
    adjectives = ('gross', 'weich', 'glitzernd', 'saftig')
    cookies = ('er Butterkeks', 'er Vanillekipferl', 'er Spritzkringel',
               'er Spekulatius', 'e Makrone', 'e Nussecke', 'e Rumkugel')

    def __init__(self, level: int):
        self.type = 'Keks'
        self.name = self.generate_name()
        self.factor = level * 20 + random.randint(level * 10 * -1, level * 10)

    def generate_name(self) -> str:
        return random.choice(self.adjectives) + random.choice(self.cookies)

    def __str__(self):
        return self.name


class Equipment:
    adjectives = ('hart', 'exquisit', 'rostig', 'glänzend')
    heads = ('e Kappe', 'er Helm')
    chests = ('e Ruestung', 'es Kettenhemd')
    legs = ('e Hose', 'e Kniepanzer')
    feet = ('e Stiefel', 'e Latschen')

    def __init__(self, level: int):
        self.type = None
        self.name = self.generate_name()
        self.factor = level * 20 + random.randint(level * 10 * -1, level * 10)

    def generate_name(self) -> str:
        equipment_type = random.choice(('head', 'chest', 'legs', 'feet'))
        adjcetive = random.choice(self.adjectives)
        if equipment_type == 'head':
            self.type = 'Kopf'
            return adjcetive + random.choice(self.heads)
        elif equipment_type == 'chest':
            self.type = 'Brust'
            return adjcetive + random.choice(self.chests)
        elif equipment_type == 'legs':
            self.type = 'Beine'
            return adjcetive + random.choice(self.legs)
        else:
            self.type = 'Fuesse'
            return adjcetive + random.choice(self.feet)

    def __str__(self):
        return self.name


class Weapon:
    adjectives = ('spitz', 'schwer', 'gross', 'perfekt')
    nouns = ('es Schwert', 'er Knueppel', 'er Morgenstern', 'er Dolch')

    def __init__(self, level: int):
        self.type = 'Waffe'
        self.name = self.generate_name()
        self.factor = level * 25 + random.randint(level * 10 * -1, level * 10)

    def generate_name(self) -> str:
        return random.choice(self.adjectives) + random.choice(self.nouns)

    def __str__(self):
        return self.name
