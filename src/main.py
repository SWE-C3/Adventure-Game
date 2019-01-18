"""
testing module
"""
import curses
import logging
from pathlib import Path

import globals
from controls import Controls
from credits import Credits
from game_map import GameMap, SaveGameDialog, MonsterDialog, ItemDialog, \
    GameOverDialog, LadderDialog
from inventory import Inventory
from main_menu import MainMenu, NewGameDialog, EndGameDialog
from pause_menu import PauseMenu
from story import StoryScreen


def initialize(standard_screen):
    globals.STDSCR = standard_screen
    globals.MAIN = MainMenu()
    globals.INTERFACES.append(globals.MAIN)
    globals.MAP = GameMap()
    globals.INTERFACES.append(globals.MAP)
    globals.INVENTORY = Inventory()
    globals.INTERFACES.append(globals.INVENTORY)
    globals.PAUSE = PauseMenu()
    globals.INTERFACES.append(globals.PAUSE)
    globals.STORY = StoryScreen()
    globals.INTERFACES.append(globals.STORY)
    globals.CONTROLS_MAP = Controls(Controls.Type.game_map)
    globals.INTERFACES.append(globals.CONTROLS_MAP)
    globals.CONTROLS_INVENTORY = Controls(Controls.Type.inventory)
    globals.INTERFACES.append(globals.CONTROLS_INVENTORY)
    globals.CREDITS = Credits()
    globals.INTERFACES.append(globals.CREDITS)
    globals.NEW_GAME = NewGameDialog()
    globals.INTERFACES.append(globals.NEW_GAME)
    globals.QUIT_GAME = EndGameDialog()
    globals.INTERFACES.append(globals.QUIT_GAME)
    globals.SAVE_GAME = SaveGameDialog()
    globals.INTERFACES.append(globals.SAVE_GAME)
    globals.MONSTER = MonsterDialog()
    globals.INTERFACES.append(globals.MONSTER)
    globals.ITEM = ItemDialog()
    globals.INTERFACES.append(globals.ITEM)
    globals.GAME_OVER = GameOverDialog()
    globals.INTERFACES.append(globals.GAME_OVER)
    globals.LADDER = LadderDialog()
    globals.INTERFACES.append(globals.LADDER)


if __name__ == '__main__':
    logging.basicConfig(
        filename=str((Path(__file__).parent.parent / 'game.log').absolute()),
        level=logging.INFO,
        filemode='w'
    )
    try:
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
                logging.info(globals.INTERFACES)
                for interface in globals.INTERFACES:
                    interface.resized = True
            current.print()
            key = STDSCR.getch()
            temp = current.handle(key, previous)
            if temp is not current:
                previous, current = current, temp
    except Exception as e:
        curses.endwin()
        raise e
