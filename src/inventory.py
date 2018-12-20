"""
Interfaces for inventory
"""
import curses


from collections import namedtuple
Equipment = namedtuple('Equipment', ('name', 'strength'))
Item = namedtuple('Item', ('name', 'heal_value'))


class Inventory:
    """
    Interfaces class for inventory
    """

    def __init__(self):
        self.cookies = {}
        self.items = {}

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
        for cookie in self.cookies.values():
            inventory_screen.addstr(i,
                                    2,
                                    '\t'
                                    .join([str(x)
                                           for x in [cookie.name,
                                                     cookie.heal_value]]))
            i = i + 1

        # print Equipment
        inventory_screen.addstr(0, 44, 'Equipment')
        inventory_screen.addstr(1, 41, '\t'.join(['Name', 'Stärke']))
        i = 2
        for item in self.items.values():
            inventory_screen.addstr(i,
                                    42,
                                    '\t'
                                    .join([str(x)
                                           for x in [item.name,
                                                     item.strength]]))
            i = i + 1

        inventory_screen.refresh()

    # adds Cookie(Healing) to Inventory
    def add_cookie(self, cookie):
        """
        adds item to inventory
        """
        self.cookies[cookie.name] = cookie

    # adds Equipment to Inventory
    def add_item(self, item):
        """
        adds equipment to inventory
        """
        self.items[item.name] = item
