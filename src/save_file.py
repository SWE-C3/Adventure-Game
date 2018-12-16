"""
Contains SaveFile class
"""

import json
from src.player import Player


class SaveFile:
    """
    Defines methods for transferring information between
    player class attributes and a JSON file
    """

    def __init__(self):
        self.playerinstance = Player()

    def write_file(self):
        """
        Write player class information into a JSON file
        """
        with open("save_file.json", "w") as file:
            file.write(json.dumps(vars(self.playerinstance), indent=4))

    def read_file(self):
        """
        Read player class information from a JSON file
        """
        with open("save_file.json") as file:
            self.playerinstance.__dict__ = json.load(file)
