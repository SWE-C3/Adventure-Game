"""
Player - S -
"""


class Player:
    """
    This class defines the features and characteristics of an object Player.
    """
    DEFAULT_POSITION = [0, 0]  # Default position of Player [x,y]
    DEFAULT_HEALTH = 10  # Default health of Player
    DEFAULT_STRENGTH = 5  # Default strength of Player

    def __init__(self, position=None):
        if position is None:
            position = self.DEFAULT_POSITION
        self.position = position
        # Item Array of Player,0: Head,1: Chest, 2: Trousers,
        # 3: Shoes, 4: Weapon, 5-7: Cookies
        self.items = ["", "", "", "", "", "", "", ""]

    @property
    def strength(self):
        """
        This defines the strength of Player
        """
        # The actual strength calculated by list slice:
        # DEFAULT_STRENGTH + sum of the items 0 till 4(5-1)
        # Head + Chest + Trousers + Shoes + Weapon items.
        return self.DEFAULT_STRENGTH + sum(self.items[0:5])

    @property
    def health(self):
        """
        This defines the health of Player
        """
        # The actual health calculated by list slice:
        # DEFAULT_HEALTH + sum of the items 5 till 7(8-1)
        # items.Cookies
        return self.DEFAULT_HEALTH + sum(self.items[5:8])

    def update_pos(self, x_axis, y_axis):
        """
        set_pos helps setting the current coordinates of Player position.
        :param x_axis: horizontal position of Player
        :param y_axis: vertical position of Player
        :return:
        """
        self.position[0] = x_axis
        self.position[1] = y_axis
