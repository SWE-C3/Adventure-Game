"""
Interfaces for help menus
"""
import json
from os.path import join, abspath, dirname

from utility import table_centered


class Controls:
    """
    Help menu for inventory and game map
    """

    def __init__(self, screen, menu_type: str):
        self.screen = screen
        with open(join(dirname(abspath(__file__)), '..', 'resources',
                       'controls.json')) as items:
            self.items = json.load(items)[menu_type]
            self.items = [tuple(item.values()) for item in self.items]

    def print(self):
        """
        print interface to window
        """
        table = table_centered(self.screen,
                               ['Primary', 'Secondary', 'Action'],
                               self.items)
        table.refresh()

    def handle(self, key: int, previous):
        while key != 27:
            key = self.screen.getch()
        return previous
