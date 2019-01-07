"""
Interfaces for Monster

from utility
"""


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
        """
        This defines how the Player wins or looses
        and what event will be triggered
        """
        if self.str <= player.str:
            monster_event.player_win(self.item)
        else:
            monster_event.player_loose(self.item)
