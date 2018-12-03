"""
Player - S -
"""
import curses


# Default Position sinnvoll?
# default_position = [0, 0]  -> [x,y] oder [y,x] wie getmaxyx() in curses ?
# Health, Strength und Item sind konstant, wenn ein neues Objekt Spieler
# erzeugt wird (Neues Spiel)

default_strength = 5 #Default strength of Player
default_health = 10 # Default health of Player

class Player:
    """
    This class defines the features and characteristics of an object Player.
    """

    def __init__(self, position=None):
        if position is None:
            position = [0, 0]
        self.position = position
        self.health = default_health
        self.strength = default_strength
        self.items = ["","","","","","","",""] #Item Array of Player,0: Head,1: Chest, 2: Trousers, 3: Shoes, 4: weapon, 5-7: Cookies



    def set_pos(self, x, y):
        """
        set_pos sets the current position of Player.
        :param x: horizontal position of Player
        :param y: vertical position of Player
        :return:
        """
        self.position[0] = x
        self.position[1] = y


    def set_strength(self,item):
        """
        set_strength sets the strength of Player
        :param:Items Item Array of Player,0: Head,1: Chest, 2: Trousers, 3: Shoes, 4: weapon, 5-7: Cookies
        """

        for i in items:
            self.strength += items[i]#.Item_strength
