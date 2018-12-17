"""
Credits Interface
"""
import curses


def print_list(win, row, col, my_list):
    """
    print_list prints out my_list on a specific window (win)
    and in a specific (col) with 1 line between the (item)s.
    """
    for item in my_list:
        win.addstr(row, col, item)
        for i in range(0, len(my_list)):
            row += 1


class Credits:
    """
    This User Interfaces helps printing out the CREDITS screen,
    where one can see who worked on this project.
    """

    def __init__(self, screen):

        self.screen = screen
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

    def print(self):
        """
        This method prints out the current Credits object
        with help of the method print_list
        """
        # get a tuple (y, x) - height, width of the window
        screen_size = self.screen.getmaxyx()
        # create new window for credits
        credits_win = curses.newwin(screen_size[0], screen_size[1], 0, 0)

        # Print  Top:
        credits_win.addstr(screen_size[0] //
                           6, screen_size[1] //
                           2 -
                           len(self.top) //
                           2, self.top)

        col0 = screen_size[1] // 4 - len(self.header[0])
        col1 = col0 + screen_size[1] // 5
        col2 = col1 + screen_size[1] // 5
        col3 = col2 + screen_size[1] // 5

        # Print Header:
        credits_win.addstr(screen_size[0] // 4, col0, self.header[0])
        credits_win.addstr(screen_size[0] // 4 + 1,
                           col0, len(self.header[0]) * "_")
        credits_win.addstr(screen_size[0] // 4, col1, self.header[1])
        credits_win.addstr(screen_size[0] // 4 + 1,
                           col1, len(self.header[1]) * "_")
        credits_win.addstr(screen_size[0] // 4, col2, self.header[2])
        credits_win.addstr(screen_size[0] // 4 + 1,
                           col2, len(self.header[2]) * "_")
        credits_win.addstr(screen_size[0] // 4, col3, self.header[3])
        credits_win.addstr(screen_size[0] // 4 + 1,
                           col3, len(self.header[3]) * "_")

        # Print Lists:
        print_list(
            credits_win,
            screen_size[0] // 4 + 4,
            col0,
            self.projektmanagement)
        print_list(
            credits_win,
            screen_size[0] // 4 + 4,
            col1,
            self.vertriebsmanagement)
        print_list(
            credits_win,
            screen_size[0] // 4 + 4,
            col2,
            self.technologiemanagement)
        print_list(
            credits_win,
            screen_size[0] // 4 + 4,
            col3,
            self.qualitaetsmanagement)

        credits_win.refresh()

    def handle(self, key: int, previous):
        while key != 27:
            key = self.screen.getch()
            self.print()
        return previous
