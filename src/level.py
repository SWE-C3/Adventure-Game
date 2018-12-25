"""
represents a whole level in the tower
with a print method
"""


class Level:
    """
    represents a whole level in the tower
    with height, width and containing rooms
    """
    def __init__(self, height, width):
        self.rooms = []
        self.height = height
        self.width = width

    def print(self, window):
        """
        Print a level on the window
        :param window: window to be drawn to
        :return:
        """
        y_pos = 1
        x_pos = 1
        counter = 0
        for room in self.rooms:
            room.print(window, y_pos, x_pos)
            x_pos += 2
            counter += 1
            if counter == self.width:
                counter = 0
                y_pos += 2
                x_pos = 1
