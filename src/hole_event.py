"""
HoleEvent Class
"""


class HoleEvent:
    """
    This class handles the event Hole.
    """

    def __init__(self, screen, hole_room):
        self.screen = screen
        self.top = "--- Loch-Event ---"
        self.header = [
            "Du bist durch ein Loch eine Ebene tiefer gefallen.",
            "----------"]
        self.room = hole_room

    def fall(self, player):
        """
        This method drops the player into the lower level.
        """
        # Level = position[2]
        player.position[2] -= 1
        self.header.append("- [ANZAHL] HP")
        