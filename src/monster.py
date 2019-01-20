import random


class Monster:
    adjectives = ('riesig', 'leuchtend', 'blutig', 'stinkend')
    names = ('er Geist', 'er Goblin', 'er Zombie', 'er Sukkubus',
             'e Riesenschlange', 'es Keksmonster')

    def __init__(self, level: int):
        self.name = self.generate_name()
        self.strength = level * 30 + random.randint(level * 15 * -1,
                                                    level * 15)

    def generate_name(self) -> str:
        return random.choice(self.adjectives) + random.choice(self.names)

    def __str__(self):
        return self.name
