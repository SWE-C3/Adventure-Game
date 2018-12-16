"""
testing module
"""
import curses

from constants import *
from controls import Controls
from credits import Credits
from game_map import GameMap
from inventory import Inventory
from main_menu import MainMenu, NewGameWindow, EndGameWindow
from pause_menu import PauseMenu
from story import StoryScreen


def initialize(standard_screen):
    global MAIN, MAP, INVENTORY, PAUSE, STORY, CONTROLS_MAP, CONTROLS_INVENTORY, CREDITS, NEW_GAME, QUIT_GAME
    MAIN = MainMenu(standard_screen)
    NEW_GAME = NewGameWindow(standard_screen)
    QUIT_GAME = EndGameWindow(standard_screen)
    MAP = GameMap(standard_screen)
    CONTROLS_MAP = Controls(standard_screen, 'game_map')
    CONTROLS_INVENTORY = Controls(standard_screen, 'inventory')
    CREDITS = Credits(standard_screen)
    PAUSE = PauseMenu(standard_screen)
    INVENTORY = Inventory(standard_screen)
    STORY = StoryScreen(standard_screen)


if __name__ == '__main__':
    STDSCR = curses.initscr()
    curses.cbreak()
    curses.noecho()
    curses.curs_set(0)
    STDSCR.keypad(True)
    initialize(STDSCR)

    previous = None
    current = MAIN
    while True:
        current.print()
        key = STDSCR.getch()
        current, previous = current.handle(key, previous), current

