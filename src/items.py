"""
Item class
"""
import json
import random


class Item:
    """
    Item main class
    """

    def __init__(self):
        self.name


class Healing_Item(Item):
    """
    Healing_Item is a subclass of Item with the additional attribute health
    """

    def __init__(self):
        super().__init__()
        self.health = 0

    # randomly sets a name from the given json file
    def set_random_name(self):
        with open("items.json", "r") as read_file:
            data = json.load(read_file)
        self.name = random.choice(data["Healing_name"])

    # automatically sets the values according to the level
    def set_auto(self, level_number):
        self.set_random_name()
        self.health = random.randint(
            ((level_number-1)*10), (level_number*10))  # temporary calculation


class Equipment(Item):
    """
    Equipment is a subclass of Item with the additional attribute strength
    """

    def __init__(self):
        super().__init__()
        self.strength = 0

    # randomly sets a name from the given json file
    def set_random_name(self):
        with open("items.json", "r") as read_file:
            data = json.load(read_file)
        self.name = random.choice(data["Equipment_name"])

    # automatically sets the values according to the level
    def set_auto(self, level_number):
        self.set_random_name()
        self.health = random.randint(
            ((level_number-1)*10), (level_number*10))  # temporary calculation


class Weapon(Item):
    """
    Weapon is a subclass of Item with the additional attribute strength,
    and is meant to separate weapons and equipment for the inventory
    """

    def __init__(self):
        super().__init__()
        self.strength = 0

    # randomly sets a name from the given json file
    def set_random_name(self):
        with open("items.json", "r") as read_file:
            data = json.load(read_file)
        self.name = random.choice(data["Weapon_name"])

    # automatically sets the values according to the level
    def set_auto(self, level_number):
        self.set_random_name()
        self.health = random.randint(
            ((level_number-1)*10), (level_number*10))  # temporary calculation
