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
        # get a Tupel (y, x) - height, width of the window
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
        self.pressed_key = ord('z')
        self.text1 = "Wenn du ein neues Spiel anfängst, " \
                     "wird dein bisheriger Fortschritt gelöscht."
        self.text2 = "Bist du dir sicher?"
        self.text3 = "--------------------------"
        self.menu_items = ["[j] Ja", "[n] Nein"]

    def print(self):
        """
        render dialog to terminal window
        """
        size = self.screen.getmaxyx()

        # create new window for menu
        new_item_win = curses.newwin(size[0], size[1], 0, 0)
        # y_pos_offset to set items vertical below each other
        y_pos_offset = size[0] // 2 - 2

        new_item_win.addstr(y_pos_offset,
                            size[1] // 2 - len(self.text1) // 2, self.text1)
        y_pos_offset += 1
        new_item_win.addstr(y_pos_offset,
                            size[1] // 2 - len(self.text2) // 2, self.text2)
        y_pos_offset += 1
        new_item_win.addstr(y_pos_offset,
                            size[1] // 2 - len(self.text3) // 2, self.text3)
        y_pos_offset += 1

        # for each item in menu_items add the menu text
        for item in self.menu_items:
            new_item_win.addstr(y_pos_offset,
                                size[1] // 2 - len(item) // 2, item)
            # increment y_pos_offset by one
            y_pos_offset += 1

        # refresh menu_item_win
        new_item_win.refresh()


class EndGameWindow:
    """
    Dialog when quitting the game
    """

    def __init__(self, screen):
        self.screen = screen
        self.pressed_key = ord('z')
        self.text1 = "Nicht gespeicherte Fortschritte gehen verloren!"
        self.text2 = "Beenden?"
        self.text3 = "--------------"
        self.menu_items = ["[j] Ja", "[n] Nein"]

    def print(self):
        """
        render dialog to terminal window
        """
        size = self.screen.getmaxyx()

        # create new window for menu
        end_item_win = curses.newwin(size[0], size[1], 0, 0)
        # yposoffset to set items vertical below each other
        yposoffset = size[0] // 2 - 2

        end_item_win.addstr(yposoffset,
                            size[1] // 2 - len(self.text1) // 2, self.text1)
        yposoffset += 1
        end_item_win.addstr(yposoffset,
                            size[1] // 2 - len(self.text2) // 2, self.text2)
        yposoffset += 1
        end_item_win.addstr(yposoffset,
                            size[1] // 2 - len(self.text3) // 2, self.text3)
        yposoffset += 1

        # for each item in menu_items add the menu text
        for item in self.menu_items:
            end_item_win.addstr(yposoffset,
                                size[1] // 2 - len(item) // 2, item)
            # increment yposoffset by one
            yposoffset += 1

        # refresh menu_item_win
        end_item_win.refresh()
