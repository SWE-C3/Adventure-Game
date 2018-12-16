"""
Game map interface
"""
import curses

from constants import PAUSE, INVENTORY, CONTROLS_MAP, UP, DOWN, LEFT, RIGHT
from player import Player
from tower import Tower


class GameMap:
    """
    Main User Interface to show current
    position, current map, current health,
    current power and the event log
    """

    def __init__(self, screen):
        self.screen = screen
        self.player = Player()
        self.tower = Tower()
        self.health_bar = "||||||||||"
        # Event log window
        self.event_log = curses.newwin(0, 0, 0, 0)

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
            map_size[0] // 2, (map_size[1] // 2) - 7, f"Position: {self.player.position}")
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

    def update_health_bar(self, health):
        """
        update health bar based on current health
        """
        # cut one "|" off for each 10th between current life
        # and full life (rounded off)
        for index in range(0, 10 - (health // 10)):
            self.health_bar = self.health_bar[:-1]

    def handle(self, key: int, previous = None):
        while True:
            if key == 27:
                return PAUSE
            elif key == ord('i'):
                return INVENTORY
            elif key == ord('h'):
                return CONTROLS_MAP
            elif key in (ord('w'), UP):
                self.player.move_up()
            elif key in (ord('s'), DOWN):
                self.player.move_down()
            elif key in (ord('a'), LEFT):
                self.player.move_left()
            elif key in (ord('d'), RIGHT):
                self.player.move_right()
            self.print()
            self.screen.getch()
