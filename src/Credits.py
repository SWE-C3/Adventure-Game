import curses

# Interface Class for Credits
class Credits:
    def __init__(self, screen):
        self.screen = screen
        self.top = "--- CREDITS ---"
        self.header = ["Projektmanager", "Vertriebsmanager", "Technologiemanager", "Qualitaetsmanager"]
        self.projektmanagement = ["Knut Z.", "Max C."]
        self.vertriebsmanagement = ["Lukas S.", "Pascal T.", "Fynn B."]
        self.technologiemanagement = ["Dennis K.", "Mostafa K.", "Tim G."]
        self.qualitaetsmanagement = ["Tobias A.", "Michael L.", "Oliver O."]

    def print_list(self, win, row, col, list):
        for x in list:
            win.addstr(row, col, x)
            for i in range(0, len(list)):
                row += 1

    def print_screen(self):
        # clear current screen
        self.screen.clear()
        # get a Tupel (y, x) - height, width of the window
        screen_size = self.screen.getmaxyx()
        # create new window for credits
        credits_win = curses.newwin(screen_size[0], screen_size[1], 0, 0)

        # Print  Top:
        credits_win.addstr(screen_size[0] // 6, screen_size[1] // 2 - len(self.top) // 2, self.top)

        col0 = screen_size[1] // 4 - len(self.header[0])
        col1 = col0 + screen_size[1] // 5
        col2 = col1 + screen_size[1] // 5
        col3 = col2 + screen_size[1] // 5

        # Print Header:
        credits_win.addstr(screen_size[0] // 4, col0, self.header[0])
        credits_win.addstr(screen_size[0] // 4 + 1, col0, len(self.header[0])*"_")
        credits_win.addstr(screen_size[0] // 4, col1, self.header[1])
        credits_win.addstr(screen_size[0] // 4 + 1, col1, len(self.header[1])*"_")
        credits_win.addstr(screen_size[0] // 4, col2, self.header[2])
        credits_win.addstr(screen_size[0] // 4 + 1, col2, len(self.header[2])*"_")
        credits_win.addstr(screen_size[0] // 4, col3, self.header[3])
        credits_win.addstr(screen_size[0] // 4 + 1, col3, len(self.header[3])*"_")

        # Print Lists:
        self.print_list(credits_win, screen_size[0] // 4 + 4, col0, self.projektmanagement)
        self.print_list(credits_win, screen_size[0] // 4 + 4, col1, self.vertriebsmanagement)
        self.print_list(credits_win, screen_size[0] // 4 + 4, col2, self.technologiemanagement)
        self.print_list(credits_win, screen_size[0] // 4 + 4, col3, self.qualitaetsmanagement)

        credits_win.refresh()
        credits_win.getch()



'''
stdscr = curses.initscr()
c = Credits(stdscr)
c.print_screen()

    def print_header(self, win, row, col, header):
        for x in header:
            win.addstr(row, col, x)
            win.addstr(row + 2, col, len(x) * "_")
            for i in range(0, 3):
                col += col + self.screen.getmaxyx()[1] // 5
                
self.print_header(credits_win, screen_size[0] // 4, col0, self.header)
'''
