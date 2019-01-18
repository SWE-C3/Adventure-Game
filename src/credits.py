"""
Credits Interface
"""
import curses

import constants
from user_interface import UserInterface


def print_list(win, row, col, my_list):
    """
    print_list prints out my_list on a specific window (win)
    and in a specific (col) with 1 line between the (item)s.
    """
    for item in my_list:
        win.addstr(row, col, item)
        for i in range(0, len(my_list)):
            row += 1


class Credits(UserInterface):
    """
    This User Interfaces helps printing out the CREDITS screen,
    where one can see who worked on this project.
    """

    def __init__(self):
        super().__init__()
        self.top = "--- CREDITS ---"
        self.header = [
            "Projektmanager",
            "Vertriebsmanager",
            "Technologiemanager",
            "Qualitaetsmanager"]
        self.projektmanagement = ["Knut Z.", "Max C."]
        self.vertriebsmanagement = ["Lukas S.", "Pascal T.", "Fynn B."]
        self.technologiemanagement = ["Dennis K.", "Mostafa K.", "Tim G."]
        self.qualitaetsmanagement = ["Tobias A.", "Michael L.", "Oliver O."]
        self.credits_win = None
        self.setup()

    def setup(self):
        self.screen = curses.newwin(0, 0)
        height, width = self.screen.getmaxyx()
        self.credits_win = curses.newwin(height, width, 0, 0)
        self.credits_win.addstr(height //
                                6, width //
                                2 -
                                len(self.top) //
                                2, self.top)

        col0 = width // 4 - len(self.header[0])
        col1 = col0 + width // 5
        col2 = col1 + width // 5
        col3 = col2 + width // 5

        # Print Header:
        self.credits_win.addstr(height // 4, col0, self.header[0])
        self.credits_win.addstr(height // 4 + 1,
                                col0, len(self.header[0]) * "_")
        self.credits_win.addstr(height // 4, col1, self.header[1])
        self.credits_win.addstr(height // 4 + 1,
                                col1, len(self.header[1]) * "_")
        self.credits_win.addstr(height // 4, col2, self.header[2])
        self.credits_win.addstr(height // 4 + 1,
                                col2, len(self.header[2]) * "_")
        self.credits_win.addstr(height // 4, col3, self.header[3])
        self.credits_win.addstr(height // 4 + 1,
                                col3, len(self.header[3]) * "_")

        # Print Lists:
        print_list(self.credits_win, height // 4 + 4, col0,
                   self.projektmanagement)
        print_list(self.credits_win, height // 4 + 4, col1,
                   self.vertriebsmanagement)
        print_list(self.credits_win, height // 4 + 4, col2,
                   self.technologiemanagement)
        print_list(self.credits_win, height // 4 + 4, col3,
                   self.qualitaetsmanagement)

    def refresh(self):
        self.screen.redrawwin()
        self.credits_win.redrawwin()
        self.screen.refresh()
        self.credits_win.refresh()

    def print(self):
        """
        This method prints out the current Credits object
        with help of the method print_list
        """
        if self.resized:
            self.resized = False
            self.setup()
        self.refresh()

    def handle(self, key: int, previous):
        if key == constants.ESCAPE:
            return previous
        return self
