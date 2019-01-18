"""
Interfaces for the pause menu
"""

import globals
from dialog import Dialog


class PauseMenu(Dialog):
    """
    Interface class for pause menu
    """

    def __init__(self):
        super().__init__()
        self.question = 'Pause'
        self.options = ["[Z] Zurueck zur Karte",
                        "[S] Speicherstand laden",
                        "[Q] Spiel verlassen",
                        "[M] Zum Hauptmenue"]
        self.setup()

    def handle(self, key: int, previous):
        if key == ord('z'):
            return globals.MAP
        elif key == ord('s'):
            globals.MAP.load_game('savegame.json')
            return globals.MAP
        elif key == ord('q'):
            return globals.QUIT_GAME
        elif key == ord('m'):
            return globals.MAIN
        previous.print()
        return self
