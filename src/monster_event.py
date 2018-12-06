"""
Interfaces for Monster
"""
from monster import Monster

from collections import namedtuple
Equipment = namedtuple('Equipment', ('name', 'strength'))
Item = namedtuple('Item', ('name', 'heal_value'))


class MonsterEvent:
    """
    Interfaces class for Monster Event
    """

    def __init__(self, monster, screen):
        self.screen = screen
        self.top = "--- Monster-Event ---"
        self.header = [
            "Ein " + monster.name + " " + monster.str + " greift an."
            ]
        Monster.fight(monster, player, self)

    def player_win(self, item):
        self.screen = screen
        self.top = "--- Monster-Event ---"
        self.header = [
            "Du konntest " + monster.name + " besiegen."
           ]
        if item != NULL:
            self.screen = screen
            self.top = "--- Monster-Event ---"
            self.header = [
            monster.name + " hat " + monster.item
            ]
            player.get_item(monster.item)

    def player_lose(self, str):
        self.screen = screen
        self.top = "--- Monster-Event ---"
        self.header = [
            monster.name + " hat dich besiegt. ",
           "----------",
           "- " + monster.str + " HP"
            ]
        player.death()

