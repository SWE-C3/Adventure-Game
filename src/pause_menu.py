"""
Interfaces for the pause menu
"""

import curses


class PauseMenu:
    """
    Interface class for pause menu
    """

    def __init__(self, screen):
        self.menu_items = ["[Z] Zurück zur Karte",
                           "[S] Speicherstand laden", "[Q] Spiel verlassen"]
        self.screen = screen
        self.pressed_key = ord('z')

    def print(self):
        """
        render pause menu to terminal window
        """

        # get a Tupel (y, x) - height, width of the window
        size = self.screen.getmaxyx()

        # create new window for menu
        menu_item_win = curses.newwin(size[0], size[1], 0, 0)
        # y_pos_offset to set items vertical below each other
        ypos = (size[0] // 2) - 2

        # for each item in menu_items add the menu text
        for item in self.menu_items:
            menu_item_win.addstr(ypos, (
                size[1] // 2) - (len(item) // 2), item)
            ypos += 1

        # refresh menu_item_win
        menu_item_win.refresh()
