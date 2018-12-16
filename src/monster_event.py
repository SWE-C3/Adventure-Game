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

        # Monsterkampf, von Monster-Event aufgerufen

    def fight(self, player, monster, screen):
        """
        This defines how the Player wins or looses
        and what event will be triggered
        """

        if monster.get_str() <= player.str:
            self.player_win(self, player, monster, screen)
        else:
            self.player_lose(self, monster, screen, player)

    def player_win(self, player, monster, screen):
        """
        Event for winning Player
        """
        self.screen = screen
        self.top = "--- Monster-Event ---"
        self.header = [
            "Du konntest " + monster.name + " besiegen."
            ]
        if monster.item is not None:
            self.screen = screen
            self.top = "--- Monster-Event ---"
            self.header = [monster.name + " hat " + monster.item]
            player.get_item(monster.item)

    def player_lose(self, monster, screen, player):
        """
        Event for loosing Player
        """
        self.screen = screen
        self.top = "--- Monster-Event ---"
        self.header = [
            monster.name + " hat dich besiegt. ", "----------",
            "- " + monster.get_str() + " HP"
            ]
        player.death()
