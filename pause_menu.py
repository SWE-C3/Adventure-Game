import curses


def read_input(window):
    return window.getch()


class pause_menu:
    def __init__(self, screen):
        self.menu_items = ["[Z] Zurück zur Karte",
                           "[S] Speicherstand laden", "[Q] Spiel verlassen"]
        self.screen = screen
        self.pressed_key = ord('z')

    def print(self):
        self.screen.clear()
        size = self.screen.getmaxyx()

        menu_item_win = curses.newwin(size[0], size[1], 0, 0)
        yPosOffset = int(size[0] / 2) - 2

        for item in self.menu_items:
            menu_item_win.addstr(yPosOffset, int(
                size[1] / 2) - int(len(item) / 2), item)
            yPosOffset += 1

        menu_item_win.refresh()
        self.pressed_key = read_input(menu_item_win)


class sure_quit:
    def __init__(self, screen):
        self.menu_items = [
            "Sicher das Sie das Spiel Verlassen wollen?", "[J]Ja", "[N]Nein"]
        self.screen = screen
        self.pressed_key = 0

    def print(self):
        self.screen.clear()
        size = self.screen.getmaxyx()

        menu_item_win = curses.newwin(size[0], size[1], 0, 0)
        yPosOffset = int(size[0] / 2) - 2

        for item in self.menu_items:
            menu_item_win.addstr(yPosOffset, int(
                size[1] / 2) - int(len(item) / 2), item)
            yPosOffset += 1

        menu_item_win.refresh()
        self.pressed_key = read_input(menu_item_win)


class sure_load_savegame:
    def __init__(self, screen):
        self.menu_items = ["Sind Sie sich sicher das Sie den Spielstand laden wollen?",
                           "Der nicht gespeicherte Fortschritt geht verloren", "[J]Ja", "[N]Nein"]
        self.screen = screen
        self.pressed_key = ord('z')

    def print(self):
        self.screen.clear()
        size = self.screen.getmaxyx()

        menu_item_win = curses.newwin(size[0], size[1], 0, 0)
        yPosOffset = int(size[0] / 2) - 2

        for item in self.menu_items:
            menu_item_win.addstr(yPosOffset, int(
                size[1] / 2) - int(len(item) / 2), item)
            yPosOffset += 1

        menu_item_win.refresh()
        self.pressed_key = read_input(menu_item_win)


main_screen = curses.initscr()
pause_menu = pause_menu(main_screen)
sure_quit = sure_quit(main_screen)
sure_load_savegame = sure_load_savegame(main_screen)

curses.endwin()
