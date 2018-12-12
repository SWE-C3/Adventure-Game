"""
Contains CheckpointEvent class
"""

from src.save_file import SaveFile
from src.utility import option_dialog


class CheckpointEvent:
    """
    Defines methods for handling checkpoint event
    """

    def __init__(self, screen, save):
        """
        Initial output
        """
        self.screen = screen
        self.top = "--- Checkpoint-Event ---"
        self.header = [
            "Du hast einen Speicherpunkt erreicht."
        ]
        SaveFile.write_file(save)

    def print(self):
        """

        """
        dialog = option_dialog(self,
                               "Möchtest du dich ausruhen und deinen Fortschritt speichern?",
                               ["[j] Ja", "[n] Nein"])
        print(dialog)

    def check_confirmed(self, screen):
        """
        Event if checkpoint is confirmed
        """
        self.screen = screen
        self.top = "--- Checkpoint-Event ---"
        self.header = [
            "Deine HP wurden um 30 erhöht und dein Fortschritt gespeichert."
        ]
