"""
Player - S -
"""


class Player:
    """
    This class defines the features and characteristics of an object Player.
    """
    default_position = [0, 0, 0]  # Default position of Player [x,y,Level]
    default_health = 10  # Default health of Player
    default_strength = 5  # Default strength of Player

    def __init__(self, position=None):
        if position is None:
            position = self.default_position
        self.position = position
        self.health = self.default_health
        self.items = []  # 0: Head, 1: Chest, 2: Trousers, 3: Shoes, 4: Weapon
        self.cookies = []

    @property
    def strength(self):
        """
        This defines the strength of Player
        """
        # default_strength + sum of the items:
        # Head + Chest + Trousers + Shoes + Weapon
        return self.default_strength + sum(self.items)

    def move_up(self):
        self.position[0] = max(0, self.position[0] - 1)

    def move_down(self):
        self.position[0] = max(0, self.position[0] + 1)

    def move_left(self):
        self.position[1] = max(0, self.position[0] - 1)

    def move_right(self):
        self.position[1] = max(0, self.position[0] + 1)
