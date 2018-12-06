"""
Player - S -
"""


class Player:
    """
    This class defines the features and characteristics of an object Player.
    """
    DEFAULT_POSITION = [0, 0, 0]  # Default position of Player [x,y,Level]
    DEFAULT_HEALTH = 10  # Default health of Player
    DEFAULT_STRENGTH = 5  # Default strength of Player

    def __init__(self, position=None):
        if position is None:
            position = self.DEFAULT_POSITION
        self.position = position
        self.health = self.DEFAULT_HEALTH
        self.items = []  # 0: Head, 1: Chest, 2: Trousers, 3: Shoes, 4: Weapon
        self.cookies = []

    @property
    def strength(self):
        """
        This defines the strength of Player
        """
        # The actual strength calculated by list slice:
        # DEFAULT_STRENGTH + sum of the items 0 till 4(5-1)
        # Head + Chest + Trousers + Shoes + Weapon items.
        return self.DEFAULT_STRENGTH + sum(self.items)
