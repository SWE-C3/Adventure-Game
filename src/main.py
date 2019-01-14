"""
testing module
"""
import curses
import logging
from pathlib import Path

import globals
from controls import Controls
from credits import Credits
from game_map import GameMap, SaveGameDialog, MonsterDialog
from inventory import Inventory
from main_menu import MainMenu, NewGameDialog, EndGameDialog
from pause_menu import PauseMenu
from story import StoryScreen


def initialize(standard_screen):
    globals.STDSCR = standard_screen
    globals.MAIN = MainMenu()
    globals.NEW_GAME = NewGameDialog()
    globals.QUIT_GAME = EndGameDialog()
    globals.MAP = GameMap()
    globals.CONTROLS_MAP = Controls(Controls.Type.game_map)
    globals.CONTROLS_INVENTORY = Controls(Controls.Type.inventory)
    globals.CREDITS = Credits()
    globals.PAUSE = PauseMenu()
    globals.INVENTORY = Inventory()
    globals.STORY = StoryScreen()
    globals.SAVE_GAME = SaveGameDialog()
    globals.MONSTER = MonsterDialog()


if __name__ == '__main__':
    logging.basicConfig(
        filename=str((Path(__file__).parent / 'game.log').absolute())
    )
    STDSCR = curses.initscr()
    curses.cbreak()
    curses.noecho()
    curses.curs_set(0)
    curses.start_color()
    STDSCR.keypad(True)
    STDSCR.refresh()
    STDSCR.timeout(500)
    initialize(STDSCR)

    screen_size = STDSCR.getmaxyx()
    current = globals.MAIN
    previous = None
    temp = None
    while True:
        if screen_size != STDSCR.getmaxyx():
            screen_size = STDSCR.getmaxyx()
            for interface in globals.INTERFACES:
                interface.resized = True
        current.print()
        key = STDSCR.getch()
        temp = current.handle(key, previous)
        if temp is not current:
            previous, current = current, temp
