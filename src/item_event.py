"""
Item Events
"""


class ItemEvent:
    """
    This class defines all Events related to items
    """

    def __init__(self, screen):
        self.screen = screen
        self.top = "--- Item-Event ---"

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
        self.header = [
            "Du hast " + item.toString() + " gefunden"
        ]
        if inventory.add_item(item):
            self.header = [
                "Du hast " + item.toString() +
                "erfolgreich deinem Inventar hinzugefügt"
            ]
        else:
            self.header = self.header + [
                "Dein Inventar ist voll"
            ]

    def equipment_pick_up(self, equipment, inventory, screen):
        """
        Event for picking up an Equipment-Item
        :param equipment:
        :param inventory:
        :param screen:
        :return:
        """

        self.screen = screen
        self.top = "--- Item-Event ---"
        if inventory.add_equipment(equipment):
            self.header = [
                equipment.name +
                "wurde erfolgreich ausgerüstet."
            ]
        else:
            self.header = [
                "Dein Inventar ist voll"
            ]
