import curses


class GameMap:
    def __init__(self, player, tower):
        self.player = player
        self.tower = tower
        # TODO: read events from file (?)
        # Events: - pause
        #         - inventory
        #         - help
        #         - move Player
        self.events = { }
        # Event log window
        self.event_log = ""

    # print the GameMap onto given screen
    def print(self, window):
        screen_size = window.getmaxyx()
        game_map_win = curses.newwin(screen_size[0], screen_size[1], 0, 0)
        # self.player.current_level.name (?)
        game_map_win.addstr(1, 3, "Ebene {number}" + self.player + self.tower)
        map_window = curses.newwin(int(screen_size[0] * 0.66) - 1,
                            int(screen_size[1] - 5), 2, 3)
        map_window.border()
        map_size = map_window.getmaxyx()
        # self.player.current_level.print
        map_window.addstr(int(map_size[0] / 2), int(map_size[1] / 2) - 7, "{current level}")
        # self.player.health
        health_bar_window = curses.newwin(3, 23, map_size[0] + 2, 3)
        health_bar_window.border()
        health_bar_window.addstr(1, 2, "HP: ")
        health_bar_window.addstr(1, 6, self.DrawHealthBar(40))
        health_bar_window.addstr(1, 17, "100")
        # game_map_win.addstr(map_size[0] + 2, 3, "HP: " + self.DrawHealthBar(50) + " 50")
        # self.player.power
        game_map_win.addstr(map_size[0] + 3, map_size[1] - 14, "Stärke: {value}")
        self.event_log = curses.newwin(screen_size[0] - (map_size[0] + 6),
                                       screen_size[1] - 5,
                                       map_size[0] + 5,
                                       3)
        self.event_log.border()

        game_map_win.refresh()
        map_window.refresh()
        self.event_log.refresh()
        health_bar_window.refresh()

    # Call Event based on key_input
    def EventHandler(self, key_input):
        # get function from event dict
        event = self.events.get(key_input, "no event")
        # if there is any function
        if event is not "no event":
            # then call event
            event()

    # Draw the health bar based on current player.health
    def DrawHealthBar(self, health):
        # start with full life
        health_bar = "||||||||||"
        # cut one "|" off for each 10th between current life and full life (rounded off)
        for index in range(0, 10 - int(health / 10)):
            health_bar = health_bar[:-1]

        return health_bar

    # refresh window with new player and new tower (?)
    def Refresh(self, window, player):
        self.player = player
        self.print(window)
