"""
Interfaces for the main menu
"""
import curses
import sys

import globals
from dialog import Dialog
from game_map import GameMap
from inventory import Inventory
from user_interface import UserInterface


def save_file():
    """
    save current game state to disk
    :return: true if successful, false if not
    """
    return True


class MainMenu(UserInterface):
    """
    Interface class for main menu
    """

    def __init__(self):
        super().__init__()
        self.top = "--- Tower Explorer ---"
        self.logo = ["     |>>>  ",
                     "     |     ",
                     " _  _|_  _ ",
                     "|;|_|;|_|;|",
                     r"\\.    .  /",
                     r" \\:  .  / ",
                     "  ||:   |  ",
                     "  ||:.  |  ",
                     "  ||:  .|  ",
                     "  ||:   |  ",
                     "  ||: , |  ",
                     "  ||:   |  ",
                     "  ||:   |  ",
                     "  ||: . |  ",
                     "  ||_   |  "]
        self.menu_items = ["[N] Neues Spiel", "[Q] Beenden"]
        self.credits = "[C] Credits"
        self.menu_item_win = None
        self.setup()

    def setup(self):
        self.screen = curses.newwin(0, 0)
        height, width = self.screen.getmaxyx()
        self.menu_item_win = curses.newwin(height, width, 0, 0)
        y_pos_offset = height // 7 - 2
        self.menu_item_win.addstr(y_pos_offset,
                                  width // 2 - len(self.top) // 2, self.top)
        y_pos_offset += 3
        for item in self.logo[:height - 12]:
            self.menu_item_win.addstr(y_pos_offset,
                                      width // 2 - len(item) // 2, item)
            y_pos_offset += 1

    def refresh(self):
        self.screen.redrawwin()
        self.menu_item_win.redrawwin()
        self.screen.refresh()
        self.menu_item_win.refresh()

    def print(self):
        """
        render main menu to terminal window
        """
        if self.resized:
            self.resized = False
            self.setup()
        if save_file():
            self.menu_items = ["[N] Neues Spiel",
                               "[F] Fortsetzen", "[Q] Beenden"]
        else:
            self.menu_items = ["[N] Neues Spiel", "[Q] Beenden"]
        height, width = self.screen.getmaxyx()
        y_pos_offset = height // 7 + 2 + len(self.logo[:height - 12])
        for item in self.menu_items:
            y_pos_offset += 1
            self.menu_item_win.addstr(y_pos_offset,
                                      width // 2 - len(item) // 2, item)
        y_pos_offset += 1
        self.menu_item_win.addstr(y_pos_offset,
                                  width // 2 - len(self.credits) // 2,
                                  self.credits)
        self.refresh()

    def handle(self, key: int, previous):
        if key == ord('n'):
            return globals.NEW_GAME
        elif key == ord('f'):
            return globals.MAP
        elif key == ord('q'):
            return globals.QUIT_GAME
        elif key == ord('c'):
            return globals.CREDITS
        return self


class NewGameDialog(Dialog):
    """
    Dialog when creating new game
    """

    def __init__(self):
        super().__init__()
        self.question = "Wenn du ein neues Spiel anfängst, " \
                        "wird dein bisheriger Fortschritt gelöscht. " \
                        "Bist du dir sicher?"
        self.options = ["[J] Ja", "[N] Nein"]
        self.setup()

    def handle(self, key: int, previous):
        if key == ord('n'):
            return previous
        elif key == ord('j'):
            globals.MAP = GameMap()
            globals.INVENTORY = Inventory()
            return globals.MAP
        previous.print()
        return self


class EndGameDialog(Dialog):
    """
    Dialog when quitting the game
    """

    def __init__(self):
        super().__init__()
        self.question = "Nicht gespeicherte Fortschritte gehen verloren! " \
                        "Beenden?"
        self.options = ["[J] Ja", "[N] Nein"]
        self.setup()

    def handle(self, key: int, previous):
        if key == ord('n'):
            return previous
        elif key == ord('j'):
            curses.endwin()
            sys.exit()
        previous.print()
        return self
