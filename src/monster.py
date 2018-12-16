"""
Interfaces for Monster

from utility
"""


class Monster:
    """
    Interfaces class for Monster
    """
    def __init__(self, str_monster, room, item, name):
        self.str = str_monster
        self.item = item
        self.room = room
        self.name = name

    def get_str(self):
        return self.str
    """
    Getter method for Monster strength
    """
