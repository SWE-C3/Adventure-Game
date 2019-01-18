class Player:
    default_health = 100
    default_strength = 5

    def __init__(self, position=None):
        self.position = position or Position()
        self.head = None
        self.chest = None
        self.legs = None
        self.feet = None
        self.weapon = None
        self.cookies = []
        self._damage = 0

    def add_item(self, item):
        if item.type == 'Kopf':
            self.head = item
        elif item.type == 'Brust':
            self.chest = item
        elif item.type == 'Beine':
            self.legs = item
        elif item.type == 'Fuesse':
            self.feet = item
        elif item.type == 'Waffe':
            self.weapon = item
        elif item.type == 'Keks':
            self.cookies.append(item)
            if len(self.cookies) > 3:
                del self.cookies[0]

    @property
    def damage(self):
        return self._damage

    @damage.setter
    def damage(self, value):
        self._damage = min(max(0, value), self.max_health)

    @property
    def max_health(self):
        return self.default_health + sum(item.factor for item
                                         in (self.head, self.chest,
                                             self.legs, self.feet)
                                         if item)

    @property
    def current_health(self):
        return min(max(0, self.max_health - self.damage), self.max_health)

    @property
    def strength(self):
        return self.default_strength + (self.weapon.factor
                                        if self.weapon else 0)

    @property
    def x(self):
        return self.position.x

    @property
    def y(self):
        return self.position.y

    @property
    def level(self):
        return self.position.level


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
        self._level = max(0, min(self.max_level, value))
