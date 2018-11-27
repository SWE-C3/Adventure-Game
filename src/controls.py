import curses
import json
from os.path import join, abspath, dirname

from utility import draw_table_centered


class ControlsInventory:

    def __init__(self, stdscr):
        self.stdscr = stdscr
        with open(join(dirname(abspath(__file__)), '..', 'resources',
                       'controls.json')) as items:
            self.items = json.load(items)['inventory']

    def print_screen(self):
        self.stdscr.clear()
        height, width = self.stdscr.getmaxyx()
        window = curses.newwin(height, width, 0, 0)
        draw_table_centered(window, ['Primary', 'Secondary', 'Action'],
                            self.items)
        window.addstr(1, 1, 'Keymap')
        window.refresh()
        window.getch()
