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
        self.cookie_window = None
        self.equipment_window = None
        self.setup()

    def setup(self):
        self.screen = curses.newwin(0, 0)
        height, width = self.screen.getmaxyx()

        cookie_window_height = 9
        cookie_window_width = 40
        self.cookie_window = curses.newwin(cookie_window_height,
                                           cookie_window_width,
                                           height - cookie_window_height,
                                           width // 2 -
                                           cookie_window_width // 2)
        self.cookie_window.border()

        equipment_window_height = 16
        equipment_window_width = 40
        self.equipment_window = curses.newwin(equipment_window_height,
                                              equipment_window_width, 0,
                                              width // 2 -
                                              equipment_window_width // 2)
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
        player = globals.MAP.player
        for y in range(3, 12, 2):
            self.equipment_window.addstr(y, 1, 38 * ' ')
        for y in range(3, 8, 2):
            self.cookie_window.addstr(y, 1, 38 * ' ')
        self.equipment_window.addstr(1, 1, 'Name')
        self.equipment_window.addstr(1, 32, 'Staerke')
        self.equipment_window.addstr(2, 1, 38 * '-')
        if player.head:
            self.equipment_window.addstr(3, 1, player.head.name)
            self.equipment_window.addstr(3, 39 - len(str(player.head.factor)),
                                         str(player.head.factor))
        if player.chest:
            self.equipment_window.addstr(5, 1, player.chest.name)
            self.equipment_window.addstr(5, 39 - len(str(player.chest.factor)),
                                         str(player.chest.factor))
        if player.legs:
            self.equipment_window.addstr(7, 1, player.legs.name)
            self.equipment_window.addstr(7, 39 - len(str(player.legs.factor)),
                                         str(player.legs.factor))
        if player.feet:
            self.equipment_window.addstr(9, 1, player.feet.name)
            self.equipment_window.addstr(9, 39 - len(str(player.feet.factor)),
                                         str(player.feet.factor))
        if player.weapon:
            self.equipment_window.addstr(11, 1, player.weapon.name)
            self.equipment_window.addstr(11,
                                         39 - len(str(player.weapon.factor)),
                                         str(player.weapon.factor))
        self.cookie_window.addstr(1, 1, 'Name')
        self.cookie_window.addstr(1, 32, 'Heilung')
        self.cookie_window.addstr(2, 1, 38 * '-')
        for index, cookie in enumerate(globals.MAP.player.cookies):
            self.cookie_window.addstr((index + 1) * 2 + 1, 1, cookie.name)
            self.cookie_window.addstr((index + 1) * 2 + 1,
                                      39 - len(str(cookie.factor)),
                                      str(cookie.factor))
        self.refresh()

    def handle(self, key: int, previous):
        player = globals.MAP.player
        if key in (constants.ESCAPE, constants.TAB ,ord('i')):
            return globals.MAP
        elif key == ord('h'):
            return globals.CONTROLS_INVENTORY
        elif key == ord('1') and len(player.cookies) > 0:
            globals.MAP.log_event(f'Du hast {player.cookies[0]} gegessen und'
                                  f' hast {player.cookies[0].factor} Heilung'
                                  f' erhalten')
            globals.MAP.player.damage -= player.cookies[0].factor
            del globals.MAP.player.cookies[0]
        elif key == ord('2') and len(player.cookies) > 1:
            globals.MAP.log_event(f'Du hast {player.cookies[1]} gegessen und'
                                  f' hast {player.cookies[1].factor} Heilung'
                                  f' erhalten')
            globals.MAP.player.damage -= player.cookies[1].factor
            del globals.MAP.player.cookies[1]
        elif key == ord('3') and len(player.cookies) > 2:
            globals.MAP.log_event(f'Du hast {player.cookies[2]} gegessen und'
                                  f' hast {player.cookies[2].factor} Heilung'
                                  f' erhalten')
            globals.MAP.player.damage -= player.cookies[2].factor
            del globals.MAP.player.cookies[2]
        return self
