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
        self.name = None


class HealingItem(Item):
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
        with open("items.json", "r") as read_file:
            data = json.load(read_file)
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
    Equipment is a subclass of Item with the additional attribute strength
    """

    def __init__(self):
        super().__init__()
        self.strength = None

    def set_random_name(self):
        """
        randomly sets a name from the given json file
        """
        with open("items.json", "r") as read_file:
            data = json.load(read_file)
        self.name = random.choice(data["Equipment_name"])

    def set_auto(self, level_number):
        """
        automatically sets the values according to the level
        """
        self.set_random_name()
        self.strength = random.randint(
            ((level_number-1)*10), (level_number*10))  # temporary calculation


class Weapon(Item):
    """
    Weapon is a subclass of Item with the additional attribute strength,
    and is meant to separate weapons and equipment for the inventory
    """

    def __init__(self):
        super().__init__()
        self.strength = None

    def set_random_name(self):
        """
        randomly sets a name from the given json file
        """
        with open("items.json", "r") as read_file:
            data = json.load(read_file)
        self.name = random.choice(data["Weapon_name"])

    def set_auto(self, level_number):
        """
        automatically sets the values according to the level
        """
        self.set_random_name()
        self.strength = random.randint(
            ((level_number-1)*10), (level_number*10))  # temporary calculation
