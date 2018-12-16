import json
import test
import random

from enum import Enum


class Item:
    """
    Item main class
    """

    def __init__(self):
        self.name = None

    def set(self, name):
        self.name = name


class Healing_Item(Item):
    """
    Healing_Item is a subclass of Item with the additional attribute health
    """

    def __init__(self):
        self.name = None
        self.health = None

    def set(self, name, health):
        super.set(name)
        self.health = health

    # randomly sets a name from the given json file
    def set_random_name(self):
        with open("../resources/items.json", "r") as read_file:
            data = json.load(read_file)
        self.name = random.choice(data["Healing_name"])

    # automatically sets the values according to the level
    def set_auto(self, level_number):
        self.set_random_name()
        self.health = random.randint(
            ((level_number-1)*10), (level_number*10))  # temporary calculation


class Equipment(Item):
    """
    Equipment is a subclass of Item with the additional attribute strength, 
    you have to set a predefined part for initialization
    """

    def __init__(self):
        super().__init__
        self.strength = 0
        self.part = Enum("Part", "Weapon Helmet Body Pants Shoes")

    def set_random_name(self):
        with open("../resources/items.json", "r") as read_file:
            data = json.load(read_file)
        file_name = self.part + "_name"
        self.name = random.choice(data[file_name])

    # automatically sets the values according to the level
    def set_auto(self, level_number):
        self.set_random_name()
        self.health = random.randint(
            ((level_number-1)*10), (level_number*10))  # temporary calculation
