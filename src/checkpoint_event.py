"""
Contains CheckpointEvent class
"""

from src.utility import option_dialog


class CheckpointEvent:
    """
    Defines methods for checkpoint event
    """

    def __init__(self, screen):
        """
        Initial output
        """
        self.screen = screen
        self.top = "--- Checkpoint-Event ---"
        self.header = [
            "Du hast einen Speicherpunkt erreicht."
        ]

    def save_dialog(self):
        """
        Prints a dialog asking the user to save game progress
        """
        dialog = option_dialog(self,
                               "Möchtest du dich ausruhen und " +
                               "deinen Fortschritt speichern?",
                               ["[j] Ja", "[n] Nein"])
        dialog.refresh()

    def saved_progress(self, screen):
        """
        If user wants to save progress
        """
        self.screen = screen
        self.top = "--- Checkpoint-Event ---"
        self.header = [
            "Deine HP wurden um 3 erhöht und dein Fortschritt gespeichert."
        ]
