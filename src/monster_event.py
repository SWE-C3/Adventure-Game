"""
Interfaces for Monster
"""


class MonsterEvent:
    """
    This class defines all Events related to Monster
    """

    def __init__(self, monster, screen):
        self.screen = screen
        self.top = "--- Monster-Event ---"
        self.header = [
            "Ein " + monster.name + " " + monster.str + " greift an."
            ]

    def player_win(self, item, player, monster, screen):
        """
        Event for winning Player
        """
        self.screen = screen
        self.top = "--- Monster-Event ---"
        self.header = [
            "Du konntest " + monster.name + " besiegen."
            ]
        if item is not None:
            self.screen = screen
            self.top = "--- Monster-Event ---"
            self.header = [monster.name + " hat " + monster.item]
            player.get_item(monster.item)

    def player_lose(self, monster, player, screen):
        """
        Event for loosing Player
        """
        self.screen = screen
        self.top = "--- Monster-Event ---"
        self.header = [
            monster.name + " hat dich besiegt. ", "----------",
            "- " + monster.str + " HP"
            ]
        player.death()
