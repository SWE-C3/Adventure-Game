"""
Game map interface
"""
import curses

import constants
from player import Player, Position
from tower import Tower


class GameMap:
    """
    Main User Interface to show current
    position, current map, current health,
    current power and the event log
    """

    def __init__(self, screen):
        self.screen = screen
        self.player = Player(Position(13 * 3, 13))
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
        game_map_win.addstr(1, 3, f"Ebene {self.player.position.level}")
        map_window = curses.newwin(13 + 2, 13 * 3 + 2, 2, screen_size[1] // 2 - (13 * 3 + 2) // 2)
        map_window.border()
        map_size = map_window.getmaxyx()
        map_window.addstr(self.player.position.y, self.player.position.x, "x")
        health_bar_window = curses.newwin(3, 23, map_size[0] + 2, 3)
        health_bar_window.border()
        health_bar_window.addstr(1, 2, "HP: ")
        health_bar_window.addstr(1, 6, self.health_bar)
        health_bar_window.addstr(1, 17, "100")
        game_map_win.addstr(map_size[0] + 3, map_size[1] - 14,
                            f"Stärke: {self.player.strength}")
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
        cut one "|" off for each 10th between current life
        and full life (rounded off)
        """
        for index in range(0, 10 - (health // 10)):
            self.health_bar = self.health_bar[:-1]

    def handle(self, key: int, previous=None):
        while True:
            if key == 27:
                return constants.PAUSE
            elif key == ord('i'):
                return constants.INVENTORY
            elif key == ord('h'):
                return constants.CONTROLS_MAP
            elif key in (ord('w'), constants.UP):
                self.player.position.y -= 1
            elif key in (ord('s'), constants.DOWN):
                self.player.position.y += 1
            elif key in (ord('a'), constants.LEFT):
                self.player.position.x -= 3
            elif key in (ord('d'), constants.RIGHT):
                self.player.position.x += 3
            elif key == ord('z'):
                return constants.STORY
            self.print()
            key = self.screen.getch()
