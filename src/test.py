"""
testing module
"""
import curses
import sys

import constants
from controls import Controls
from credits import Credits
from game_map import GameMap
from inventory import Inventory
from main_menu import MainMenu, NewGameWindow, EndGameWindow
from pause_menu import PauseMenu
from story import StoryScreen


def initialize(standard_screen):
    constants.MAIN = MainMenu(standard_screen)
    constants.NEW_GAME = NewGameWindow(standard_screen)
    constants.QUIT_GAME = EndGameWindow(standard_screen)
    constants.MAP = GameMap(standard_screen)
    constants.CONTROLS_MAP = Controls(standard_screen, 'game_map')
    constants.CONTROLS_INVENTORY = Controls(standard_screen, 'inventory')
    constants.CREDITS = Credits(standard_screen)
    constants.PAUSE = PauseMenu(standard_screen)
    constants.INVENTORY = Inventory(standard_screen)
    constants.STORY = StoryScreen(standard_screen)


if __name__ == '__main__':
    STDSCR = curses.initscr()
    curses.cbreak()
    curses.noecho()
    curses.curs_set(0)
    STDSCR.keypad(True)
    initialize(STDSCR)

    previous = None
    current = constants.MAIN
    print(current)
    sys.exit()
    while True:
        current.print()
        key = STDSCR.getch()
        current, previous = current.handle(key, previous), current

