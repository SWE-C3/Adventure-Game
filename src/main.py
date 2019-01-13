"""
testing module
"""
import curses
import logging
from pathlib import Path

import constants
from controls import Controls
from credits import Credits
from game_map import GameMap, SaveGameDialog, MonsterDialog
from inventory import Inventory
from main_menu import MainMenu, NewGameWindow, EndGameWindow
from pause_menu import PauseMenu
from story import StoryScreen


def initialize(standard_screen):
    constants.STDSCR = standard_screen
    constants.MAIN = MainMenu(standard_screen)
    constants.NEW_GAME = NewGameWindow(standard_screen)
    constants.QUIT_GAME = EndGameWindow(standard_screen)
    constants.MAP = GameMap()
    constants.CONTROLS_MAP = Controls(standard_screen, Controls.Type.game_map)
    constants.CONTROLS_INVENTORY = Controls(standard_screen,
                                            Controls.Type.inventory)
    constants.CREDITS = Credits(standard_screen)
    constants.PAUSE = PauseMenu(standard_screen)
    constants.INVENTORY = Inventory(standard_screen)
    constants.STORY = StoryScreen(standard_screen)
    constants.SAVE_GAME = SaveGameDialog(standard_screen)
    constants.MONSTER = MonsterDialog(standard_screen)


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
    previous = None
    current = constants.MAIN
    while True:
        current.print()
        key = STDSCR.getch()
        current, previous = current.handle(key, previous), current
