"""
Interfaces for inventory
"""
import curses

from collections import namedtuple

import constants


class Inventory:
    """
    Interfaces class for inventory
    """

    def __init__(self, screen):
        self.screen = screen
        self.cookies = list(None for _ in range(3))
        self.equipment = {
            'head': None,
            'chest': None,
            'arms': None,
            'legs': None,
            'feet': None
        }

    def print(self):
        """
        render inventory to terminal window
        """
        height, width = self.screen.getmaxyx()
        inventory_window = curses.newwin(height, width, 0, 0)

        cookie_window_height = 4
        cookie_window_width = 25
        cookie_window = curses.newwin(cookie_window_height, cookie_window_width, height - cookie_window_height,
                                      width // 2 - cookie_window_width // 2)
        cookie_window.border()
        for index, cookie in enumerate(self.cookies):
            cookie_window.addstr(1, index * 8, "Name")
            cookie_window.addstr(2, index * 8, "+Amount")

        equipment_window_height = 16
        equipment_window_width = 20
        equipment_window = curses.newwin(equipment_window_height, equipment_window_width, 0,
                                         width // 2 - cookie_window_width // 2)
        equipment_window.border()
        for index, (name, item) in enumerate(self.equipment.items()):
            equipment_window.addstr(index * 3 + 1, 1, "Name: name")
            equipment_window.addstr(index * 3 + 2, 1, "Strength: strength")

        inventory_window.refresh()
        cookie_window.refresh()
        equipment_window.refresh()

    def handle(self, key: int, previous):
        while True:
            if key == constants.ESCAPE:
                return constants.MAP
            elif key == ord('h'):
                return constants.CONTROLS_INVENTORY
            key = self.screen.getch()
            self.print()
