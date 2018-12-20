"""
Interfaces for Monster
"""
import curses


class MonsterEvent:
    """
    This class defines all Events related to Monster
    """
    def __init__(self, screen):
        self.screen = screen

    def fight(self, player, monster):
        """
        This defines how the Player wins or looses
        """
        top = "--- Monster-Event ---"
        header = "Ein " + monster.name + " " + str(monster.str) + " greift an."

        size = self.screen.getmaxyx()

        # create new window for menu
        event_log = curses.newwin(size[0], size[1], 0, 0)
        # y_pos_offset to set items vertical below each other
        y_pos_offset = size[0] // 7 - 2

        #
        event_log.addstr(
            y_pos_offset, size[1] // 2 - len(top) // 2, top)
        event_log.addstr(
            y_pos_offset + 1, size[1] // 2 - len(header) // 2, header)

        # player win
        if monster.str <= player.strength:
            outcome = "Du konntest " + monster.name + " besiegen."
            if monster.item is not None:
                player.inv.add_item(monster.item)
        # player loose
        else:
            outcome = monster.name + " hat dich besiegt. (-1 HP)"
            player.health -= 1
            # player dies
            if player.health == 0:
                player.death()
            # player survives
            else:
                player.respawn()

        event_log.addstr(y_pos_offset + 2, size[1] // 2 - len(outcome) // 2, outcome)
        event_log.refresh()
