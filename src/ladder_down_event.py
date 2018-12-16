"""
Event for moving one level down via ladder
"""


class LadderDownEvent:
    """
    This class defines the ladder down event
    """

    def __init__(self, screen):
        self.screen = screen
        self.top = "--- Leiter-runter-Event ---"
        self.header = [
            "Du hast eine Leiter nach unten gefunden."
        ]

    @classmethod
    def change_level(cls, player):
        """
        changes the current Level
        """
        current_position = player.get_postion()
        current_position[2] -= 1
        player.set_postition(current_position)
