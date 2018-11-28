import curses

class PascalCase:
    def __init__(self, screen):
        self.menu_items = ["[Z] Zurück zur Karte",
                           "[S] Speicherstand laden", "[Q] Spiel verlassen"]
        self.screen = screen
        self.pressed_key = ord('z')

    def print(self):
        self.screen.clear()
        size = self.screen.getmaxyx()

        menu_item_win = curses.newwin(size[0], size[1], 0, 0)
        yPosOffset = (size[0] // 2) - 2

        for item in self.menu_items:
            menu_item_win.addstr(yPosOffset, int(
                size[1] / 2) - (len(item) // 2), item)
            yPosOffset += 1

        menu_item_win.refresh()
