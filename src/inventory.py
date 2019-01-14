"""
Interfaces for inventory
"""
import curses

import constants
import globals
from user_interface import UserInterface


class Inventory(UserInterface):
    """
    Interfaces class for inventory
    """

    def __init__(self):
        super().__init__()
        self.cookies = [None, None, None]
        self.equipment = {
            'head': None,
            'chest': None,
            'arms': None,
            'legs': None,
            'feet': None
        }
        self.cookie_window = None
        self.equipment_window = None
        self.setup()

    def setup(self):
        self.screen = curses.newwin(0, 0)
        height, width = self.screen.getmaxyx()

        cookie_window_height = 4
        cookie_window_width = 25
        self.cookie_window = curses.newwin(cookie_window_height,
                                           cookie_window_width,
                                           height - cookie_window_height,
                                           width // 2 -
                                           cookie_window_width // 2)
        self.cookie_window.border()

        equipment_window_height = 16
        equipment_window_width = 20
        self.equipment_window = curses.newwin(equipment_window_height,
                                              equipment_window_width, 0,
                                              width // 2 -
                                              cookie_window_width // 2)
        self.equipment_window.border()

    def refresh(self):
        self.screen.redrawwin()
        self.cookie_window.redrawwin()
        self.equipment_window.redrawwin()
        self.screen.refresh()
        self.cookie_window.refresh()
        self.equipment_window.refresh()

    def print(self):
        """
        render inventory to terminal window
        """
        if self.resized:
            self.resized = False
            self.setup()
        for index, (name, item) in enumerate(self.equipment.items()):
            self.equipment_window.addstr(index * 3 + 1, 1, "Name: name")
            self.equipment_window.addstr(index * 3 + 2, 1,
                                         "Strength: strength")
        for index, cookie in enumerate(self.cookies):
            self.cookie_window.addstr(1, index * 8, "Name")
            self.cookie_window.addstr(2, index * 8, "+Amount")
        self.refresh()

    def handle(self, key: int, previous):
        if key == constants.ESCAPE:
            return globals.MAP
        elif key == ord('h'):
            return globals.CONTROLS_INVENTORY
        return self
