import curses


class Item(object):
    def __init__(self, name, heal_value):
        self.name = name
        self.heal_value = heal_value


class Equipment(object):
    def __init__(self, name, strength):
        self.name = name
        self.strength = strength


class Inventory(object):
    def __init__(self):
        self.items = {}
        self.equipment = {}

    # prints Inventory (placeholder)
    def __str__(self):
        out_item = '\t'.join(['Name: ', 'Heilungsmenge: '])
        for item in self.items.values():
            out_item += '\n' + \
                   '\t'.join([str(x) for x in [item.name, item.heal_value]])

        out_equipment = '\t'.join(['Name: ', 'Stärke: '])
        for equipment in self.equipment.values():
            out_equipment += '\n' + \
                   '\t'.join([str(x) for x in [equipment.name, equipment.strength]])
        return out_item + '\n' + out_equipment

    # adds Item(Healing) to Inventory
    def add_item(self, item):
        self.items[item.name] = item

    # adds Equipment to Inventory
    def add_equipment(self, equipment):
        self.equipment[equipment.name] = equipment
