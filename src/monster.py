"""
Monster - S -
"""


class Monster:
    """
    This class defines the features and characteristics of an object Monster.
    """
    default_position = [0, 0, 0]  # Default position of Monster [x,y,Level]
    default_health = 10  # Default health of Monster
    default_strength = 5  # Default strength of Monster

    def __init__(self, position=None):
        if position is None:
            position = self.default_position
        self.position = position
        self.health = self.default_health
        self.items = []  # 0: Head, 1: Chest, 2: Trousers, 3: Shoes, 4: Weapon

    @property
    def strength(self):
        """
        This defines the strength of Monster
        """
        # default_strength + sum of the items:
        # Head + Chest + Trousers + Shoes + Weapon
        return self.default_strength + sum(self.items)
