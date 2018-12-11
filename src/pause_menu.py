"""
Interfaces for the pause menu
"""

import curses
from utility import option_dialog


class PauseMenu:
    """
    Interface class for pause menu
    """

    def __init__(self, screen):
        self.menu_items = ["[Z] Zurück zur Karte",
                           "[S] Speicherstand laden", "[Q] Spiel verlassen"]
        self.screen = screen

    def print(self):
        """
        render pause menu to terminal window
        """

        dialog = option_dialog(self.screen, 'Pause', self.menu_items)
        dialog.refresh()
