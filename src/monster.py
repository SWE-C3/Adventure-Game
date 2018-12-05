"""
Interfaces for Monster

from utility
"""

from collections import namedtuple
Equipment = namedtuple('Equipment', ('name', 'strength'))
Item = namedtuple('Item', ('name', 'heal_value'))


class Monster:
    """
    Interfaces class for Monster
    """
    def __init__(self, str_monst, room, item, name):
        self.str = str_monst
        self.item = item
        self.room = room
        self.name = name

        # Monsterkampf, von Monster-Event aufgerufen
    def fight(self, player, monster_event):
        if self.str <= player.str:
            Event.player_wins(monster_event, self.item)
        else:
            Event.player_lose(monster_event, self.str)
