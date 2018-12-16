"""
Item classes
"""

import json
import random
from os.path import join, abspath, dirname
from enum import Enum


class Item:
    """
    Item main class
    """

    def __init__(self):
        self.name = None

    def set(self, name):
        """
        need that because nametuple is not mutable
        """
        self.name = name


class Healing(Item):
    """
    Healing_Item is a subclass of Item with the additional attribute health
    """

    def __init__(self):
        super().__init__()
        self.health = None

    def set_random_name(self):
        """
        randomly sets a name from the given json file
        """
        with open(join(dirname(abspath(__file__)), '..',
                       'resources', 'items.json')) as items:
            data = json.load(items)
        self.name = random.choice(data["Healing_name"])

    def set_auto(self, level_number):
        """
        automatically sets the values according to the level
        """
        self.set_random_name()
        self.health = random.randint(
            ((level_number-1)*10), (level_number*10))  # temporary calculation


class Equipment(Item):
    """
    Equipment is a subclass of Item with the additional attribute strength, 
    you have to set a predefined part for initialization
    """

    def __init__(self):
        super().__init__()
        self.strength = None
        self.part = Enum("Part", "Weapon Helmet Body Pants Shoes")

    def set_random_name(self):
        """
        randomly sets a name from the given json file
        """
        with open(join(dirname(abspath(__file__)), '..',
                       'resources', 'items.json')) as items:
            data = json.load(items)
        file_name = self.part + "_name"
        self.name = random.choice(data[file_name])

    def set_auto(self, level_number):
        """
        automatically sets the values according to the level
        """
        self.set_random_name()
        self.strength = random.randint(
            ((level_number-1)*10), (level_number*10))  # temporary calculation
