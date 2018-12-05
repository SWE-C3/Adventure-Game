
import curses
import json
import random

class Item:
    """
    Item main class
    """
    
    def __init__(self):
        self.name

    def create(self,name):
        self.name = name
    
    # automatically sets the values according to the level
    def create_auto(self,level_number):
        set_random_name()
        self.health = random.randint(((level_number-1)*10),(level_number*10)) # temporary calculation
        
class Healing_Item(Item):
    """
    Healing_Item is a subclass of Item with the additional attribute health
    """

    def __init__(self):
        super().__init__
        self.health = 0

    def create(self,name,health):
        super.create(name)
        self.health = health
    
    # randomly sets a name from the given json file
    def set_random_name(self):
        with open("items.json", "r") as read_file:
            data = json.load(read_file)
        self.name = random.choice(data["Healing_name"])

class Equipment(Item):
    """
    Equipment is a subclass of Item with the additional attribute strength
    """

    def __init__(self):
        super().__init__
        self.strength = 0

    def create(name,strength):
        super.create(name)
        self.strength = strength

    def set_random_name(self):
        with open("items.json", "r") as read_file:
            data = json.load(read_file)
        self.name = random.choice(data["Equipment_name"])


class Weapon(Item):
    """
    Weapon is a subclass of Item with the additional attribute strength,
    and is meant to separate weapons and equipment for the inventory
    """

    def __init__(self):
        super().__init__
        self.strength = 0

    def create(self,name,strength):
        super.create(name)
        self.strength = strength

    def set_random_name(self):
        with open("items.json", "r") as read_file:
            data = json.load(read_file)
        self.name = random.choice(data["Weapon_name"])




        




