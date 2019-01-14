"""
Interfaces for help menus
"""
import curses
import json
from enum import Enum
from os.path import join, abspath, dirname
from pathlib import Path

import constants
import globals
from user_interface import UserInterface
from utility import table_centered


class Controls(UserInterface):
    """
    Help menu for inventory and game map
    """

    def setup(self):
        self.screen = curses.newwin(0, 0)
        self.table = table_centered(self.screen,
                                    ['Primary', 'Secondary', 'Action'],
                                    self.items)

    def refresh(self):
        self.screen.redrawwin()
        self.table.redrawwin()
        self.screen.refresh()
        self.table.refresh()

    class Type(Enum):
        """
        Enumeration of possible types of control menus
        """
        game_map = 'game_map'
        inventory = 'inventory'

    def __init__(self, menu_type: Type):
        super().__init__()
        with (Path(__file__).parent.parent
              / 'resources' / 'controls.json').open() as items:
            self.items = json.load(items)[menu_type.value]
            self.items = [tuple(item.values()) for item in self.items]
        self.table = None
        self.setup()

    def print(self):
        """
        print interface to window
        """
        if self.resized:
            self.resized = False
            self.setup()
        self.refresh()

    def handle(self, key: int, previous):
        if key == constants.ESCAPE:
            return previous
        return self
