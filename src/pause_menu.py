"""
Interfaces for the pause menu
"""

import curses

import constants
from utility import option_dialog


class PauseMenu:
    """
    Interface class for pause menu
    """

    def __init__(self, screen):
        self.menu_items = ["[Z] Zurück zur Karte",
                           "[S] Speicherstand laden",
                           "[Q] Spiel verlassen",
                           "[M] Zum Hauptmenü"]
        self.screen = screen

    def print(self):
        """
        render pause menu to terminal window
        """
        dialog = option_dialog(self.screen, 'Pause', self.menu_items)
        dialog.refresh()

    def handle(self, key: int, previous):
        while True:
            if key == ord('z'):
                return constants.MAP
            elif key == ord('s'):
                return constants.NEW_GAME
            elif key == ord('q'):
                return constants.QUIT_GAME
            elif key == ord('m'):
                return constants.MAIN
            key = self.screen.getch()
            previous.print()
            self.print()
