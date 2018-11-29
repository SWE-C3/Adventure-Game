"""
Game map interface
"""
import curses


class GameMap:
    """
    Main User Interface to show current
    position, current map, current health,
    current power and the event log
    """
    def __init__(self, screen):
        self.screen = screen
        self.player = {}
        self.tower = {}
        self.health_bar = "||||||||||"
        # Events: - pause
        #         - inventory
        #         - help
        #         - move Player
        self.events = {}
        # Event log window
        self.event_log = curses.newwin(0, 0, 0, 0)

    # print the GameMap onto given screen
    def print(self):
        """
        print game map to window
        """
        screen_size = self.screen.getmaxyx()
        game_map_win = curses.newwin(screen_size[0], screen_size[1], 0, 0)
        # self.player.current_level.name (?)
        game_map_win.addstr(1, 3, f"Ebene <number> {self.player} {self.tower}")
        map_window = curses.newwin(int(screen_size[0] * 0.66) - 1,
                                   int(screen_size[1] - 5), 2, 3)
        map_window.border()
        map_size = map_window.getmaxyx()
        # self.player.current_level.print
        map_window.addstr(
            map_size[0] // 2, (map_size[1] // 2) - 7, "{current level}")
        # self.player.health
        health_bar_window = curses.newwin(3, 23, map_size[0] + 2, 3)
        health_bar_window.border()
        health_bar_window.addstr(1, 2, "HP: ")
        health_bar_window.addstr(1, 6, self.health_bar)
        health_bar_window.addstr(1, 17, "100")
        # self.player.power
        game_map_win.addstr(
            map_size[0] + 3, map_size[1] - 14, "Stärke: {value}")
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
    def event_handler(self, key_input):
        """
        call event based on user input
        """
        # get function from event dict
        event = self.events.get(key_input, "no event")
        # if there is any function
        if event != "no event":
            #then call event
            event()

    # Draw the health bar based on current player.health
    def update_health_bar(self, health):
        """
        update health bar based on current health
        """
        # cut one "|" off for each 10th between current life
        # and full life (rounded off)
        for index in range(0, 10 - (health // 10)):
            self.health_bar = self.health_bar[:-1]
