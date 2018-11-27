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
    return "SaveFile.txt"

saveExists = os.path.exists("SaveFile.txt")

class main_menu:
    def __init__(self, screen):
        self.screen = screen
        self.pressed_key = ord('z')
        self.top = "--- Tower Explorer ---"
        self.logo = ["     |" + ">>>  ", "     |     ", " _  _|_  _ ", "|;|_|;|_|;|",
                     "\\\.    .  /", " \\\:  .  / ", "  ||:   |  ", "  ||:.  |  ",
                     "  ||:  .|  ", "  ||:   |  ", "  ||: , |  ", "  ||:   |  ",
                     "  ||:   |  ", "  ||: . |  ", "  ||_   |  ", " ", " "]

        if saveExists:
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

main_screen = curses.initscr()
m_menu = main_menu(main_screen)
n_game = new_game_window(main_screen)
e_game = end_game_window(main_screen)

# look which key is pressed in m_menu
while m_menu.pressed_key != ord('q'):								 # check pressed key in main_menu
    m_menu.print()													 # print main_menu
    if m_menu.pressed_key == ord('n'):
        if saveExists:
            n_game.print()
            while n_game.pressed_key != ord('n'):                        # check pressed key in new_game_window
                n_game.print()                                           # print new_game_window
                if n_game.pressed_key == ord('j'):                       # if 'j' is pressed in new_game_window
                    Story()
        else:
            Story()
    elif m_menu.pressed_key == ord('b'):							 # else if 'c' pressed in test_menu
        e_game.print()												 # then print test_con_window
        while e_game.pressed_key != ord('n'):                        # check pressed key in new_game_window
            e_game.print()                                           # print end_game_window
            if e_game.pressed_key == ord('j'):                       # if 'n' is pressed in new_game_window
                exit()                                               # then print main_menu
    elif m_menu.pressed_key == ord('c'):
        Credits()
    elif saveExists:
        if m_menu.pressed_key == ord('f'):						     # if 'p' pressed in test_menu
            GameMap()                                            # then go to Game Map