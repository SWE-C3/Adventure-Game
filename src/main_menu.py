"""
Interfaces for the main menu
"""
import sys

import curses
from utility import option_dialog

import constants


def save_file():
    """
    save current game state to disk
    :return: true if successful, false if not
    """
    return True


class MainMenu:
    """
    Interface class for main menu
    """

    def __init__(self, screen):
        self.screen = screen
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

        if save_file():
            self.menu_items = ["[N] Neues Spiel",
                               "[F] Fortsetzen", "[Q] Beenden"]
        else:
            self.menu_items = ["[N] Neues Spiel", "[Q] Beenden"]
        self.credits = "[C] Credits"

    def print(self):
        """
        render main menu to terminal window
        """
        # get a tuple (y, x) - height, width of the window
        height, width = self.screen.getmaxyx()

        menu_item_win = curses.newwin(height, width, 0, 0)
        # y_pos_offset to set items vertical below each other
        y_pos_offset = height // 7 - 2

        menu_item_win.addstr(
            y_pos_offset, width // 2 - len(self.top) // 2, self.top)
        y_pos_offset += 3

        for item in self.logo[:height - 12]:
            menu_item_win.addstr(y_pos_offset,
                                 width // 2 - len(item) // 2, item)
            y_pos_offset += 1

        y_pos_offset += 2

        for item in self.menu_items:
            menu_item_win.addstr(y_pos_offset,
                                 width // 2 - len(item) // 2, item)
            y_pos_offset += 1

        y_pos_offset += 1
        menu_item_win.addstr(y_pos_offset,
                             width // 2 - len(self.credits) // 2,
                             self.credits)
        y_pos_offset += 1

        menu_item_win.refresh()

    def handle(self, key: int, previous):
        while True:
            if key == ord('n'):
                return constants.NEW_GAME
            elif key == ord('f'):
                return constants.MAP
            elif key == ord('q'):
                return constants.QUIT_GAME
            elif key == ord('c'):
                return constants.CREDITS
            key = self.screen.getch()
            self.print()


class NewGameWindow:
    """
    Dialog when creating new game
    """

    def __init__(self, screen):
        self.screen = screen
        self.question = "Wenn du ein neues Spiel anfängst, " \
                        "wird dein bisheriger Fortschritt gelöscht. " \
                        "Bist du dir sicher?"
        self.options = ["[J] Ja", "[N] Nein"]

    def print(self):
        """
        render dialog to terminal window
        """
        dialog = option_dialog(self.screen, self.question, self.options)
        dialog.refresh()

    def handle(self, key: int, previous):
        while True:
            if key == ord('n'):
                return previous
            elif key == ord('j'):
                return constants.MAP
            key = self.screen.getch()
            previous.print()
            self.print()


class EndGameWindow:
    """
    Dialog when quitting the game
    """

    def __init__(self, screen):
        self.screen = screen
        self.question = "Nicht gespeicherte Fortschritte gehen verloren! Beenden?"
        self.options = ["[J] Ja", "[N] Nein"]

    def print(self):
        """
        render dialog to terminal window
        """
        dialog = option_dialog(self.screen, self.question, self.options)
        dialog.refresh()

    def handle(self, key: int, previous):
        while True:
            if key == ord('n'):
                return previous
            elif key == ord('j'):
                curses.endwin()
                sys.exit()
            key = self.screen.getch()
            previous.print()
            self.print()
