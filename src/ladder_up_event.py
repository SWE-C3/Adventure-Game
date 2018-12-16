"""
Event for moving one level up via ladder
"""


class LadderUpEvent:
    """
    This class defines the ladder down event
    """

    def __init__(self, player, screen):
        self.screen = screen
        self.top = "--- Leiter-hoch-Event ---"
        self.header = [
            "Du hast eine Leiter nach oben gefunden."
        ]
        self.change_level(player)

    @classmethod
    def change_level(player):
        """
        changes the current Level
        """
        current_position = player.get_postion()
        current_position[2] += 1
        player.set_postition(current_position)
