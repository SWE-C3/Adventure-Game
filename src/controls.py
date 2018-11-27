"""
Interfaces for help menus
"""
import curses
import json
from os.path import join, abspath, dirname

from utility import draw_table_centered


class Controls:
    """
    Help menu for inventory and game map
    """

    def __init__(self, stdscr, menu_type: str):
        self.stdscr = stdscr
        with open(join(dirname(abspath(__file__)), '..', 'resources',
                       'controls.json')) as items:
            self.items = json.load(items)[menu_type]

    def print_screen(self):
        """
        print interface to window
        """
        self.stdscr.clear()
        height, width = self.stdscr.getmaxyx()
        window = curses.newwin(height, width, 0, 0)
        draw_table_centered(window, ['Primary', 'Secondary', 'Action'],
                            self.items)
        window.addstr(1, 1, 'Keymap')
        window.refresh()
        window.getch()
