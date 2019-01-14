from typing import List

from user_interface import UserInterface

STDSCR = None
MAIN = None
MAP = None
INVENTORY = None
PAUSE = None
STORY = None
CONTROLS_MAP = None
CONTROLS_INVENTORY = None
CREDITS = None
NEW_GAME = None
QUIT_GAME = None
SAVE_GAME = None
MONSTER = None

INTERFACES: List[UserInterface] = (MAIN, MAP, INVENTORY, PAUSE, STORY,
                                   CONTROLS_MAP, CONTROLS_INVENTORY, CREDITS,
                                   NEW_GAME, QUIT_GAME, SAVE_GAME, MONSTER)
