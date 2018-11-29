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

        # print Cookies
        inventory_screen.addstr(0, 4, 'Cookies')
        inventory_screen.addstr(1, 1, '\t'.join(['Name', 'Heilungswert']))
        i = 2
        for item in self.items.values():
            inventory_screen.addstr(i, 2, '\t'.join([str(x) for x in [item.name, item.heal_value]]))
            i = i + 1

        # print Equipment
        inventory_screen.addstr(0, 44, 'Equipment')
        inventory_screen.addstr(1, 41, '\t'.join(['Name', 'Stärke']))
        i = 2
        for equipment in self.equipment.values():
            inventory_screen.addstr(i, 42, '\t'.join([str(x) for x in [equipment.name, equipment.strength]]))
            i = i + 1

        inventory_screen.refresh()
        inventory_screen.getch()

    # adds Item(Healing) to Inventory
    def add_item(self, item):
        self.items[item.name] = item

    # adds Equipment to Inventory
    def add_equipment(self, equipment):
        self.equipment[equipment.name] = equipment
