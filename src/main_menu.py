"""
Interfaces for the main menu
"""
import curses
from utility import option_dialog


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
        self.top = "--- Tower Explorer ---"
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
        # get a tuple (y, x) - height, width of the window
        size = self.screen.getmaxyx()

        # create new window for menu
        menu_item_win = curses.newwin(size[0], size[1], 0, 0)
        # y_pos_offset to set items vertical below each other
        y_pos_offset = size[0] // 7 - 2

        #
        menu_item_win.addstr(
            y_pos_offset, size[1] // 2 - len(self.top) // 2, self.top)
        # increment y_pos_offset by one
        y_pos_offset += 3

        # for each item in menu_logo add the menu text
        for item in self.logo:
            menu_item_win.addstr(y_pos_offset,
                                 size[1] // 2 - len(item) // 2, item)
            y_pos_offset += 1

        # for each item in menu_items add the menu text
        for item in self.menu_items:
            menu_item_win.addstr(y_pos_offset,
                                 size[1] // 2 - len(item) // 2, item)
            # increment y_pos_offset by one
            y_pos_offset += 1

        y_pos_offset += 1
        menu_item_win.addstr(y_pos_offset,
                             size[1] // 2 - len(self.credits) // 2,
                             self.credits)
        y_pos_offset += 1

        # refresh menu_item_win
        menu_item_win.refresh()


class NewGameWindow:
    """
    Dialog when creating new game
    """

    def __init__(self, screen):
        self.screen = screen
        self.question = "Wenn du ein neues Spiel anfängst, " \
                     "wird dein bisheriger Fortschritt gelöscht. " \
                     "Bist du dir sicher?"
        self.options = ["[j] Ja", "[n] Nein"]

    def print(self):
        """
        render dialog to terminal window
        """
        dialog = option_dialog(self.screen, self.question, self.options)
        dialog.refresh()


class EndGameWindow:
    """
    Dialog when quitting the game
    """

    def __init__(self, screen):
        self.screen = screen
        self.question = "Nicht gespeicherte Fortschritte gehen verloren! " \
                     "Beenden?"
        self.options = ["[j] Ja", "[n] Nein"]

    def print(self):
        """
        render dialog to terminal window
        """
        dialog = option_dialog(self.screen, self.question, self.options)
        dialog.refresh()
