import curses, os.path

def read_input(window):
    return window.getch()

def Story():
    return "Story"

def GameMap():
    return "Continue"

def Credits():
    return "Credits"

def SaveFile():
    return True

class main_menu:
    def __init__(self, screen):
        self.screen = screen
        self.pressed_key = ord('z')
        self.top = "--- Tower Explorer ---"
        self.logo = ["     |" + ">>>  ", "     |     ", " _  _|_  _ ", "|;|_|;|_|;|",
                     "\\\.    .  /", " \\\:  .  / ", "  ||:   |  ", "  ||:.  |  ",
                     "  ||:  .|  ", "  ||:   |  ", "  ||: , |  ", "  ||:   |  ",
                     "  ||:   |  ", "  ||: . |  ", "  ||_   |  ", " ", " "]

        if SaveFile():
            self.menu_items = ["[n] Neues Spiel", "[f] Fortsetzen", "[b] Beenden"]
        else:
            self.menu_items = ["[n] Neues Spiel", "[b] Beenden"]
        self.credits = "[c] Credits"

    def print(self):
        self.screen.clear()                                          # clear current screen
        size = self.screen.getmaxyx()                                # get a Tupel (y, x) - height, width of the window

        menu_item_win = curses.newwin(size[0], size[1], 0, 0)        # create new window for menu
        yPosOffset = int(size[0] / 7) - 2                            # yPosOffset to set items vertical below each other

        menu_item_win.addstr(yPosOffset, int(size[1] / 2) - int(len(self.top) / 2), self.top)
        yPosOffset += 3

        for item in self.logo:                                 # for each item in menu_items add the menu text
            menu_item_win.addstr(yPosOffset, int(size[1] / 2) - int(len(item) / 2), item)
            yPosOffset += 1                                          # increment yPosOffset by one

        for item in self.menu_items:                                 # for each item in menu_items add the menu text
            menu_item_win.addstr(yPosOffset, int(size[1] / 2) - int(len(item) / 2), item)
            yPosOffset += 1                                          # increment yPosOffset by one

        yPosOffset += 1
        menu_item_win.addstr(yPosOffset, int(size[1] / 2) - int(len(self.credits) / 2), self.credits)
        yPosOffset += 1

        menu_item_win.refresh()                                      # refresh menu_item_win
        self.pressed_key = read_input(menu_item_win)                 # wait for pressing a key


class new_game_window:
    def __init__(self, screen):
        self.screen = screen
        self.pressed_key = ord('z')
        self.text1 = "Wenn du ein neues Spiel anfängst, wird dein bisheriger Fortschritt gelöscht."
        self.text2 = "Bist du dir sicher?"
        self.text3 = "--------------------------"
        self.menu_items = ["[j] Ja", "[n] Nein"]

    def print(self):
        self.screen.clear()
        size = self.screen.getmaxyx()

        new_item_win = curses.newwin(size[0], size[1], 0, 0)        # create new window for menu
        yPosOffset = int(size[0] / 2) - 2                            # yPosOffset to set items vertical below each other

        new_item_win.addstr(yPosOffset, int(size[1] / 2) - int(len(self.text1) / 2), self.text1)
        yPosOffset += 1
        new_item_win.addstr(yPosOffset, int(size[1] / 2) - int(len(self.text2) / 2), self.text2)
        yPosOffset += 1
        new_item_win.addstr(yPosOffset, int(size[1] / 2) - int(len(self.text3) / 2), self.text3)
        yPosOffset += 1

        for item in self.menu_items:                                 # for each item in menu_items add the menu text
            new_item_win.addstr(yPosOffset, int(size[1] / 2) - int(len(item) / 2), item)
            yPosOffset += 1                                          # increment yPosOffset by one

        new_item_win.refresh()                                      # refresh menu_item_win
        self.pressed_key = read_input(new_item_win)                 # wait for pressing a key

class end_game_window:
    def __init__(self, screen):
        self.screen = screen
        self.pressed_key = ord('z')
        self.text1 = "Nicht gespeicherte Fortschritte gehen verloren!"
        self.text2 = "Beenden?"
        self.text3 = "--------------"
        self.menu_items = ["[j] Ja", "[n] Nein"]

    def print(self):
        self.screen.clear()
        size = self.screen.getmaxyx()

        end_item_win = curses.newwin(size[0], size[1], 0, 0)        # create new window for menu
        yPosOffset = int(size[0] / 2) - 2                            # yPosOffset to set items vertical below each other

        end_item_win.addstr(yPosOffset, int(size[1] / 2) - int(len(self.text1) / 2), self.text1)
        yPosOffset += 1
        end_item_win.addstr(yPosOffset, int(size[1] / 2) - int(len(self.text2) / 2), self.text2)
        yPosOffset += 1
        end_item_win.addstr(yPosOffset, int(size[1] / 2) - int(len(self.text3) / 2), self.text3)
        yPosOffset += 1

        for item in self.menu_items:                                 # for each item in menu_items add the menu text
            end_item_win.addstr(yPosOffset, int(size[1] / 2) - int(len(item) / 2), item)
            yPosOffset += 1                                          # increment yPosOffset by one

        end_item_win.refresh()                                      # refresh menu_item_win
        self.pressed_key = read_input(end_item_win)                 # wait for pressing a key