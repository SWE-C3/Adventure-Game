"""
Player - S -
"""


class Player:
    """
    This class defines the features and characteristics of an object Player.
    """
    default_health = 10  # Default health of Player
    default_strength = 5  # Default strength of Player

    def __init__(self, position=None):
        self.position = position or Position()
        self.max_health = self.default_health
        self.current_health = self.default_health
        self.items = []
        self.cookies = []

    @property
    def strength(self):
        """
        This defines the strength of Player
        """
        # default_strength + sum of the items:
        # Head + Chest + Trousers + Shoes + Weapon
        return self.default_strength + sum(self.items)


class Position:

    def __init__(self, max_x: int = 30, max_y: int = 30, max_level: int = 10,
                 layouts: list = None):
        self._x = 1
        self._y = 1
        self._level = 0
        self.max_x = max_x
        self.max_y = max_y
        self.max_level = max_level
        self.layouts = layouts

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if (value > self.x and
                self.layouts[self.level][self.y][self.x + 1] == ' '):
            self._x = max(1, min(self.max_x, value))
        elif (value < self.x and
              self.layouts[self.level][self.y][self.x - 1] == ' '):
            self._x = max(1, min(self.max_x, value))

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if (value > self.y and
                self.layouts[self.level][self.y + 1][self.x] == ' '):
            self._y = max(1, min(self.max_y, value))
        elif (value < self.y and
              self.layouts[self.level][self.y - 1][self.x] == ' '):
            self._y = max(1, min(self.max_y, value))

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = max(1, min(self.max_level, value))

    def __repr__(self):
        return f"Position(x={self.x}, y={self.y}, level={self.level})"
