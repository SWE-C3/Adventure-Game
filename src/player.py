"""
Player - S -
"""
import curses


# Default Position sinnvoll?
# default_position = [0, 0]  -> [x,y] oder [y,x] wie getmaxyx() in curses ?
# Health, Strength und Item sind konstant, wenn ein neues Objekt Spieler
# erzeugt wird (Neues Spiel)

class Player:
    """
    This class defines the features and characteristics of an object Player.
    """

    def __init__(self, position=None):
        if position is None:
            position = [0, 0]
        self.position = position
        self.health = 10
        self.strength = 0  # Default Stärke wv?
        self.item = ""  # Default Item wäre?

    def set_pos(self, x, y):
        """
        set_pos sets the current position of Player.
        :param x
        :param y:
        :return:
        """
        self.position[0] = x
        self.position[1] = y
