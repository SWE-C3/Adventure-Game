import curses

from utility import draw_table_centered

from collections import namedtuple
Equipment = namedtuple('Equipment', ('name', 'strength'))
Item = namedtuple('Item', ('name', 'heal_value'))


class Inventory(object):
    def __init__(self, screen):
        self.screen = screen
        self.items = {}
        self.equipment = {}

    # prints Inventory (placeholder)
    def print(self):
        self.screen.clear()
        size = self.screen.getmaxyx()
        inventory_screen = curses.newwin(size[0], size[1], 0, 0)
        draw_table_centered(inventory_screen, ['Name', 'Heilungsmenge'], self.items.name)

    # adds Item(Healing) to Inventory
    def add_item(self, item):
        self.items[item.name] = item

    # adds Equipment to Inventory
    def add_equipment(self, equipment):
        self.equipment[equipment.name] = equipment
