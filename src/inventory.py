"""
Interfaces for inventory
"""
import curses


from collections import namedtuple

import constants

Equipment = namedtuple('Equipment', ('name', 'strength'))
Item = namedtuple('Item', ('name', 'heal_value'))


class Inventory:
    """
    Interfaces class for inventory
    """

    def __init__(self, screen):
        self.screen = screen
        self.items = {}
        self.equipment = {}

    # prints Inventory (placeholder)
    def print(self):
        """
        render inventory to terminal window
        """
        size = self.screen.getmaxyx()
        inventory_screen = curses.newwin(size[0], size[1], 0, 0)

        # print Cookies
        inventory_screen.addstr(0, 4, 'Cookies')
        inventory_screen.addstr(1, 1, '\t'.join(['Name', 'Heilungswert']))
        i = 2
        for item in self.items.values():
            inventory_screen.addstr(i,
                                    2,
                                    '\t'
                                    .join([str(x)
                                           for x in [item.name,
                                                     item.heal_value]]))
            i = i + 1

        # print Equipment
        inventory_screen.addstr(0, 44, 'Equipment')
        inventory_screen.addstr(1, 41, '\t'.join(['Name', 'Stärke']))
        i = 2
        for equipment in self.equipment.values():
            inventory_screen.addstr(i,
                                    42,
                                    '\t'
                                    .join([str(x)
                                           for x in [equipment.name,
                                                     equipment.strength]]))
            i = i + 1

        inventory_screen.refresh()

    def handle(self, key: int, previous):
        while True:
            if key == constants.ESCAPE:
                return constants.MAP
            elif key == ord('h'):
                return constants.CONTROLS_INVENTORY
            key = self.screen.getch()

    # adds Item(Healing) to Inventory
    def add_item(self, item):
        """
        adds item to inventory
        """
        self.items[item.name] = item

    # adds Equipment to Inventory
    def add_equipment(self, equipment):
        """
        adds equipment to inventory
        """
        self.equipment[equipment.name] = equipment
