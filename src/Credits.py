# coding=utf-8
import curses

from utility import draw_table_centered

#Interface Class for Credits
class Credits:
    def __init__(self, screen):
        self.screen = screen
        self.top = "--- CREDITS ---"
        self.projektmanagement = ["Knut Z.", "Max C."]
        self.vertriebsmanagement = ["Lukas S.", "Pascal T.", "Fynn B."]
        self.technologiemanagement = ["Dennis K.", "Mostafa K.", "Tim G."]
        self.qualitaetsmanagement = ["Tobias A.", "Michael L.", "Oliver O."]
        self.team = [
            {
                "Projektmanager": "Knut Z.",
                "Vertriebsmanager": "Lukas S.",
                "Technologiemanager": "Dennis K.",
                "Qualitätsmanager": "Tobias A."
            },
            {
                "Projektmanager": "Max C.",
                "Vertriebsmanager": "Pascal T.",
                "Technologiemanager": "Mostafa K.",
                "Qualitätsmanager": "Michael L."
            },
            {
                "Projektmanager": "",
                "Vertriebsmanager": "Fynn B.",
                "Technologiemanager": "Tim G.",
                "Qualitätsmanager": "Oliver O."
            }
        ]

    def print(self):
        # clear current screen
        self.screen.clear()
        # get a Tupel (y, x) - height, width of the window
        screen_size = self.screen.getmaxyx()
        # create new window for credits
        credits_win = curses.newwin(screen_size[0], screen_size[1], 0, 0)

        credits_win.addstr(
            screen_size[0] // 7 - 2, screen_size[1] // 2 - len(self.top) // 2, self.top)

        draw_table_centered(credits_win, ['Projektmanager', 'Vertriebsmanager', 'Technologiemanager', 'Qualitätsmanager'],
                        self.team)

        credits_win.refresh()
        credits_win.getch()
