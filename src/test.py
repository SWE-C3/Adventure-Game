"""
testing module
"""
import curses

from controls import Controls
from credits import Credits
from game_map import GameMap
from inventory import Inventory
from main_menu import MainMenu, NewGameWindow, EndGameWindow
from pause_menu import PauseMenu
from story import StoryScreen

if __name__ == '__main__':
    STDSCR = curses.initscr()
    curses.cbreak()
    curses.noecho()
    curses.curs_set(0)
    STDSCR.keypad(True)

    MAIN_MENU = MainMenu(STDSCR)
    NEW_GAME_DIALOG = NewGameWindow(STDSCR)
    QUIT_GAME_DIALOG = EndGameWindow(STDSCR)
    GAME_MAP = GameMap(STDSCR)
    CONTROLS_GAME_MAP = Controls(STDSCR, Controls.Type.game_map)
    CONTROLS_INVENTORY = Controls(STDSCR, Controls.Type.inventory)
    CREDITS = Credits(STDSCR)
    PAUSE_MENU = PauseMenu(STDSCR)
    INVENTORY = Inventory(STDSCR)
    STORY_SCREEN = StoryScreen(STDSCR)

    CURRENT_SCREEN = MAIN_MENU
    PREVIOUS_SCREEN = None
    STDSCR.refresh()
    MAIN_MENU.print()
    while True:
        KEY = STDSCR.getch()
        if CURRENT_SCREEN is MAIN_MENU:
            if KEY == ord('n'):
                CURRENT_SCREEN = NEW_GAME_DIALOG
            elif KEY == ord('f'):
                CURRENT_SCREEN = GAME_MAP
            elif KEY == ord('b'):
                CURRENT_SCREEN = QUIT_GAME_DIALOG
            elif KEY == ord('c'):
                CURRENT_SCREEN = CREDITS
            PREVIOUS_SCREEN = MAIN_MENU
        elif CURRENT_SCREEN is NEW_GAME_DIALOG:
            if KEY == ord('j'):
                CURRENT_SCREEN = GAME_MAP
            elif KEY == ord('n'):
                CURRENT_SCREEN = PREVIOUS_SCREEN
            PREVIOUS_SCREEN = NEW_GAME_DIALOG
        elif CURRENT_SCREEN is QUIT_GAME_DIALOG:
            if KEY == ord('j'):
                curses.endwin()
                break
            elif KEY == ord('n'):
                CURRENT_SCREEN = PREVIOUS_SCREEN
            PREVIOUS_SCREEN = QUIT_GAME_DIALOG
        elif CURRENT_SCREEN is GAME_MAP:
            if KEY == ord('h'):
                CURRENT_SCREEN = CONTROLS_GAME_MAP
            elif KEY == ord('i'):
                CURRENT_SCREEN = INVENTORY
            elif KEY == ord('s'):
                CURRENT_SCREEN = STORY_SCREEN
            elif KEY == 27:
                CURRENT_SCREEN = PAUSE_MENU
            PREVIOUS_SCREEN = GAME_MAP
        elif CURRENT_SCREEN is CONTROLS_GAME_MAP:
            if KEY == 27:
                CURRENT_SCREEN = GAME_MAP
            PREVIOUS_SCREEN = CONTROLS_GAME_MAP
        elif CURRENT_SCREEN is CONTROLS_INVENTORY:
            if KEY == 27:
                CURRENT_SCREEN = INVENTORY
            PREVIOUS_SCREEN = CONTROLS_INVENTORY
        elif CURRENT_SCREEN is INVENTORY:
            if KEY == ord('h'):
                CURRENT_SCREEN = CONTROLS_INVENTORY
            elif KEY == 27:
                CURRENT_SCREEN = GAME_MAP
            PREVIOUS_SCREEN = INVENTORY
        elif CURRENT_SCREEN is PAUSE_MENU:
            if KEY == ord('z'):
                CURRENT_SCREEN = GAME_MAP
            elif KEY == ord('s'):
                CURRENT_SCREEN = NEW_GAME_DIALOG
            elif KEY == ord('q'):
                CURRENT_SCREEN = QUIT_GAME_DIALOG
            PREVIOUS_SCREEN = PAUSE_MENU
        elif CURRENT_SCREEN is STORY_SCREEN:
            if KEY == 27:
                CURRENT_SCREEN = GAME_MAP
            PREVIOUS_SCREEN = STORY_SCREEN
        elif CURRENT_SCREEN is CREDITS:
            if KEY == 27:
                CURRENT_SCREEN = MAIN_MENU
            PREVIOUS_SCREEN = CREDITS
        CURRENT_SCREEN.print()
