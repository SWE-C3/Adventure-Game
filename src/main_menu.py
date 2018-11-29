"""
Interfaces for the main menu
"""
import curses


def save_file():
    """
    save current game state to disk
    :return: true if successful, false if not
    """
    return True


class MainMenu:
    """
    Interface class for main menu
    """

    def __init__(self, screen):
        self.screen = screen
        self.pressed_key = ord('z')
        self.title = "--- Tower Explorer ---"
        self.logo = ["     |>>>  ", "     |     ", " _  _|_  _ ",
                     "|;|_|;|_|;|",
                     r"\\.    .  /", r" \\:  .  / ", "  ||:   |  ",
                     "  ||:.  |  ",
                     "  ||:  .|  ", "  ||:   |  ", "  ||: , |  ",
                     "  ||:   |  ",
                     "  ||:   |  ", "  ||: . |  ", "  ||_   |  ", " ", " "]

        if save_file():
            self.menu_items = ["[n] Neues Spiel",
                               "[f] Fortsetzen", "[b] Beenden"]
        else:
            self.menu_items = ["[n] Neues Spiel", "[b] Beenden"]
        self.credits = "[c] Credits"

    def print(self):
        """
        render main menu to terminal window
        """
        # clear current screen
        self.screen.clear()
        # get a Tupel (y, x) - height, width of the window
        size = self.screen.getmaxyx()

        # create new window for menu
        menu_item_win = curses.newwin(size[0], size[1], 0, 0)
        # y_pos_offset to set items vertical below each other
        y_pos_offset = size[0] // 7 - 2

        # add game title
        menu_item_win.addstr(
            y_pos_offset, size[1] // 2 - len(self.title) // 2, self.title)
        y_pos_offset += 3

        # for each item in menu_logo add the game logo
        for item in self.logo:
            menu_item_win.addstr(y_pos_offset,
                                 size[1] // 2 - len(item) // 2, item)
            y_pos_offset += 1

        # for each item in menu_items add the menu text
        for item in self.menu_items:
            menu_item_win.addstr(y_pos_offset,
                                 size[1] // 2 - len(item) // 2, item)
            y_pos_offset += 1

        y_pos_offset += 1
        # add credits option
        menu_item_win.addstr(y_pos_offset,
                             size[1] // 2 - len(self.credits) // 2,
                             self.credits)
        y_pos_offset += 1

        # refresh menu_item_win
        menu_item_win.refresh()
