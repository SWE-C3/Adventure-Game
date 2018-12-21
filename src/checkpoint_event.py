"""
Contains CheckpointEvent class
"""

import curses
from player import Player
from save_file import SaveFile
from utility import option_dialog


class CheckpointEvent:
    """
    Defines methods for checkpoint event
    """

    def __init__(self, screen):
        self.screen = screen
        self.top = "--- Checkpoint-Event ---"

        self.playerinstance = Player()
        self.savefileinstance = SaveFile()
        self.savedialoginstance = SaveDialog(self)

    def checkpoint(self):
        """
        Initial output
        """
        header = "Du hast einen Speicherpunkt erreicht."

        height, width = self.screen.getmaxyx()

        event_log = curses.newwin(height, width, 0, 0)
        y_pos_offset = height // 7 - 2

        event_log.addstr(
            y_pos_offset, width // 2 - len(self.top) // 2, self.top)
        event_log.addstr(
            y_pos_offset + 1, width // 2 - len(header) // 2, header)

        self.savedialoginstance.print()

    def saved_state(self):
        """
        Heals the player, saves game progress and creates output
        if user wanted to save progress
        """

        self.playerinstance.health += 3
        self.savefileinstance.write_file()

        header = "Deine HP wurden um 3 erhöht und " \
                 "dein Fortschritt gespeichert."

        height, width = self.screen.getmaxyx()

        event_log = curses.newwin(height, width, 0, 0)
        y_pos_offset = height // 7 - 2

        event_log.addstr(
            y_pos_offset, width // 2 - len(self.top) // 2, self.top)
        event_log.addstr(
            y_pos_offset + 1, width // 2 - len(header) // 2, header)


class SaveDialog:
    """
    Dialog asking the user to save game progress
    when reaching checkpoint event
    """

    def __init__(self, screen):
        self.screen = screen
        self.question = "Möchtest du dich ausruhen und " \
                        "deinen Fortschritt speichern?"
        self.options = ["[J] Ja", "[N] Nein"]
        self.checkpointeventinstance = CheckpointEvent(self)

    def print(self):
        """
        Renders dialog to terminal window
        """
        dialog = option_dialog(self.screen, self.question, self.options)
        dialog.refresh()

    def handle(self, key: int, previous):
        """
        Handles user input
        """
        while True:
            if key == ord('j'):
                self.checkpointeventinstance.saved_state()
            elif key == ord('n'):
                return previous
            key = self.screen.getch()
            previous.print()
            self.print()
