"""
Item Events
"""


class ItemEvent:
    """
    This class defines all Events related to items
    """

    def __init__(self, item, screen):
        self.screen = screen
        self.top = "--- Item-Event ---"
        self.header = [
            "Du hast " + item.name + " gefunden!"
        ]

    def item_pick_up(self, item, inventory, screen):
        """
        Event for picking up an Item
        :param item:
        :param inventory:
        :param screen:
        :return:
        """

        self.screen = screen
        self.top = "--- Item-Event ---"
        if inventory.add_item(item):
            self.header = [
                "Du hast " + item.name +
                "erfolgreich deinem Inventar hinzugefügt"
            ]
        else:
            self.header = [
                "Dein Inventar ist voll"
            ]
