"""
Game map interface
"""
import curses
import random
from pathlib import Path
from typing import List, Set, Tuple

import constants
import globals
from dialog import Dialog
from player import Player, Position
from tower import Tower
from user_interface import UserInterface
from utility import color


class GameMap(UserInterface):
    """
    Main User Interface to show current
    position, current map, current health,
    current power and the event log
    """

    def __init__(self):
        super().__init__()
        self.tower = Tower()
        self.health_bar = "\u2764" * 10
        self.event_log = None
        self.map = None
        self.status_info = None
        self.levels = list()
        self.level_width = 51
        self.level_height = 15
        self.levels = list()
        for file in sorted((Path(__file__).parent.parent
                            / 'resources' / 'levels').glob('*.level'),
                           key=lambda x: int(x.stem)):
            with file.open() as level:
                self.levels.append(self.parse_level(level.read()))
        self.player = Player(Position(self.level_width, self.level_height,
                                      layouts=self.levels))
        self._last_position = self.current_position
        self.discovered: List[Set[Tuple[int, int]]] = [set() for _ in
                                                       range(len(self.levels))]
        self.setup()

    @property
    def current_value(self) -> str:
        return self.levels[self.player.level][self.player.y][self.player.x]

    @current_value.setter
    def current_value(self, value: str):
        self.levels[self.player.level][self.player.y][self.player.x] = value

    @property
    def current_position(self):
        return self.player.x, self.player.y

    @staticmethod
    def parse_level(level: str) -> List[List[str]]:
        level = level.replace('-', constants.HORIZONTAL)
        level = level.replace('|', constants.VERTICAL)
        level = level.replace('+', constants.CROSS)
        return [[char for char in row]
                for row in level.split('\n')]

    def level_value(self, x_index: int, y_index: int) -> str:
        return self.levels[self.player.level][y_index][x_index]

    def setup(self):
        self.screen = curses.newwin(0, 0)
        height, width = self.screen.getmaxyx()
        self.map = curses.newwin(self.level_height, self.level_width + 1,
                                 2, width // 2 - self.level_width // 2)
        map_height, _ = self.map.getmaxyx()
        self.status_info = curses.newwin(3, 35, map_height + 2, 3)
        self.event_log = curses.newwin(height - (map_height + 6), width - 5,
                                       map_height + 5, 3)
        self.status_info.border()
        self.event_log.border()

    def refresh(self):
        self.screen.redrawwin()
        self.map.redrawwin()
        self.status_info.redrawwin()
        self.event_log.redrawwin()
        self.screen.refresh()
        self.map.refresh()
        self.status_info.refresh()
        self.event_log.refresh()

    def print(self):
        """
        print game map to window
        """
        if self.resized:
            self.resized = False
            self.setup()

        self.screen.addstr(1, 3, f"Ebene {self.player.level}")
        for y_index, row in enumerate(self.levels[self.player.level]):
            for x_index, value in enumerate(row):
                if (x_index, y_index) not in \
                        self.discovered[self.player.level]:
                    self.map.addstr(y_index, x_index, ' ',
                                    color(background=curses.COLOR_BLACK))
                elif value == 'M':
                    self.map.addstr(y_index, x_index, '\u2620',
                                    color(foreground=curses.COLOR_RED))
                elif value == 'I':
                    self.map.addstr(y_index, x_index, '\u2734',
                                    color(foreground=curses.COLOR_CYAN))
                elif value == 'S':
                    self.map.addstr(y_index, x_index, '\u2602',
                                    color(foreground=curses.COLOR_BLUE))
                elif value == '=':
                    self.map.addstr(y_index, x_index, '\u2195',
                                    color(foreground=curses.COLOR_GREEN))
                else:
                    self.map.addstr(y_index, x_index, value)
        self.map.addstr(self.current_position[1], self.current_position[0],
                        '\u265f', color(foreground=curses.COLOR_YELLOW))
        self.status_info.addstr(1, 2, "HP: ")
        self.status_info.addstr(1, 6, self.health_bar,
                                color(foreground=curses.COLOR_RED))
        self.status_info.addstr(1, 17, "100")
        self.status_info.addstr(1, 22, f"Stärke: {self.player.strength}")

        self.refresh()

    def discover(self, x_index: int, y_index: int):
        for vertical in range(-1, 2):
            for horizontal in range(-1, 2):
                self.discovered[self.player.level].add((x_index + horizontal,
                                                        y_index + vertical))

    def update_health_bar(self, health):
        """
        update health bar based on current health
        cut one "|" off for each 10th between current life
        and full life (rounded off)
        """
        for index in range(0, 10 - (health // 10)):
            self.health_bar = self.health_bar[:-1]

    def log_event(self, message):
        self.event_log.move(1, 1)
        self.event_log.deleteln()
        self.event_log.move(self.event_log.getmaxyx()[0] - 2, 1)
        self.event_log.insertln()
        self.event_log.border()
        self.event_log.addstr(self.event_log.getmaxyx()[0] - 2, 1,
                              message, color(foreground=curses.COLOR_YELLOW))

    def handle(self, key: int, previous=None):
        self._last_position = self.current_position

        if key == constants.ESCAPE:
            return globals.PAUSE
        elif key == ord('i'):
            return globals.INVENTORY
        elif key == ord('h'):
            return globals.CONTROLS_MAP
        elif key in (ord('w'), constants.UP):
            self.player.position.y -= 2
        elif key in (ord('s'), constants.DOWN):
            self.player.position.y += 2
        elif key in (ord('a'), constants.LEFT):
            self.player.position.x -= 2
        elif key in (ord('d'), constants.RIGHT):
            self.player.position.x += 2
        elif key == ord('z'):
            return globals.STORY

        self.discover(*self.current_position)
        for i in (-1, 1):
            if self.level_value(self.current_position[0] + i,
                                self.current_position[1]) == ' ':
                self.discover(self.current_position[0] + i,
                              self.current_position[1])
            if self.level_value(self.current_position[0],
                                self.current_position[1] + i) == ' ':
                self.discover(self.current_position[0],
                              self.current_position[1] + i)

        if self._last_position != self.current_position:
            if self.current_value == 'M':
                self.current_value = ' '
                self.log_event("You are fighting a monster")
                return globals.MONSTER
            elif self.current_value == 'I':
                self.log_event('You have found an item')
            elif self.current_value == 'S':
                return globals.SAVE_GAME
            elif self.current_value == '=':
                self.log_event('You found the ladder')
                self.player.position.level += 1
                return globals.STORY
            elif self.current_value == 'O':
                self.log_event('You fell through a hole')
                self.player.position.level -= 1

        return self


class SaveGameDialog(Dialog):
    """
    Dialog when accessing a save point
    """

    def __init__(self):
        super().__init__()
        self.question = "Du kannst deinen Spielstand speichern. " \
                        "Dein vorheriger Spielstand wird ueberschrieben. " \
                        "Bist du dir sicher?"
        self.options = ["[J] Ja", "[N] Nein"]
        self.setup()

    def handle(self, key: int, previous=None):
        if key == ord('n'):
            globals.MAP.log_event('You did not save the game')
            return globals.MAP
        elif key == ord('j'):
            globals.MAP.log_event('You saved the game')
            return globals.MAP
        globals.MAP.print()
        return self


class MonsterDialog(Dialog):
    """
    Dialog when encountering a monster
    """

    def __init__(self):
        super().__init__()
        self.success = random.randint(0, 10) < 5
        if self.success:
            self.question = 'Du kaempfst gegen ein Monster! ' \
                            'Und du besiegst es!'
        else:
            self.question = 'Du kaempfst gegen ein Monster! ' \
                            'Und das Monster besiegt dich...'
        self.options = ["[O] OK"]
        self.setup()

    def handle(self, key: int, previous=None):
        if key == ord('o'):
            if self.success:
                globals.MAP.log_event('You bested the monster!')
            else:
                globals.MAP.log_event('The monster overpowered you...')
            self.success = random.randint(0, 10) < 5
            if self.success:
                self.question = 'Du kaempfst gegen ein Monster! ' \
                                'Und du besiegst es!'
            else:
                self.question = 'Du kaempfst gegen ein Monster! ' \
                                'Und das Monster besiegt dich...'
            return globals.MAP
        globals.MAP.print()
        return self
