"""
Room on a Level
with print method
"""


class Room:
    """
    Represents a single room
    on a Level in the Tower
    """
    def __init__(self, doors, event=None):
        """
        Initialise a new room
        :param doors: north,east,south,west doors
        :param event: room event
        """
        self.doors = doors
        self.event = event

    def print(self, window, y_pos, x_pos):
        """
        Print a single room
        :param window: window to be drawn to
        :param y_pos: y position in the window
        :param x_pos: x position in the window
        :return:
        """
        if not self.doors['n']:
            window.addstr(y_pos, x_pos, "┼─┼")
        else:
            window.addstr(y_pos, x_pos, "┼ ┼")

        mid = ""
        if not self.doors['w']:
            mid += "│"
        else:
            mid += " "

        if self.event is None:
            mid += " "
        else:
            mid += self.event
        if not self.doors['e']:
            mid += "│"
        else:
            mid += " "
        window.addstr(y_pos + 1, x_pos, mid)

        if self.doors['s'] is False:
            window.addstr(y_pos + 2, x_pos, "┼─┼")
        else:
            window.addstr(y_pos + 2, x_pos, "┼ ┼")
