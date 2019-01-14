"""
Game map interface
"""
import curses
import random
from pathlib import Path

import constants
import globals
from dialog import Dialog
from player import Player, Position
from tower import Tower
from user_interface import UserInterface
from utility import color, option_dialog


class GameMap(UserInterface):
    """
    Main User Interface to show current
    position, current map, current health,
    current power and the event log
    """

    def __init__(self):
        super().__init__()
        self.tower = Tower()
        self.health_bar = "||||||||||"
        self.event_log = None
        self.map = None
        self.status_info = None
        self.levels = list()
        with (Path(__file__).parent.parent
              / 'resources'
              / 'levelfile.txt').open() as levels:
            content = levels.read()
            content = content.replace('-', constants.HORIZONTAL)
            content = content.replace('|', constants.VERTICAL)
            content = content.replace('+', constants.CROSS)
            content = content.split('\n\n')
            for level in content:
                level = level.split('\n')
                self.levels.append(level)
        self.player = Player(Position(33, 13, layouts=self.levels))
        self._last_position = (self.player.position.x, self.player.position.y)
        self.current_position = (
            self.player.position.x, self.player.position.y)
        self.discovered = set()
        self.setup()

    def setup(self):
        self.screen = curses.newwin(0, 0)
        height, width = self.screen.getmaxyx()
        self.map = curses.newwin(13, 34, 2, width // 2 - 33 // 2)
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
        self.screen.addstr(1, 3, f"Ebene {self.player.position.level}")
        for y_index, row in enumerate(self.levels[self.player.position.level]):
            for x_index, value in enumerate(row):
                if (x_index, y_index) not in self.discovered:
                    self.map.addstr(y_index, x_index, ' ',
                                    color(background=curses.COLOR_CYAN))
                else:
                    self.map.addstr(y_index, x_index, value)
        self.map.addstr(self.player.position.y, self.player.position.x, "x",
                        color(foreground=curses.COLOR_YELLOW))
        self.status_info.addstr(1, 2, "HP: ")
        self.status_info.addstr(1, 6, self.health_bar,
                                color(foreground=curses.COLOR_RED))
        self.status_info.addstr(1, 17, "100")
        self.status_info.addstr(1, 22, f"Stärke: {self.player.strength}")

        self.refresh()

    def discover(self, x_index: int, y_index: int):
        for vertical in (-1, 0, 1):
            for horizontal in (-1, 0, 1):
                self.discovered.add((x_index + horizontal, y_index + vertical))

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
        self._last_position, self.current_position = self.current_position, (
            self.player.position.x,
            self.player.position.y)
        self.discover(self.current_position[0], self.current_position[1])
        current = \
            self.levels[self.player.position.level][self.player.position.y][
                self.player.position.x]
        if self._last_position != self.current_position:
            if current == 'M':
                self.log_event("You are fighting a monster")
                return globals.MONSTER
            elif current == 'I':
                self.log_event('You have found an item')
            elif current == 'S':
                return globals.SAVE_GAME
            elif current == '=':
                self.log_event('You found the ladder')
            elif current == 'O':
                self.log_event('You fell through a hole')

        return self


class SaveGameDialog(Dialog):
    """
    Dialog when creating new game
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
    Dialog when creating new game
    """

    def __init__(self):
        super().__init__()
        self.success = random.randint(0, 10) < 3
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
                self.question = 'Du kaempfst gegen ein Monster! ' \
                                'Und du besiegst es!'
            else:
                globals.MAP.log_event('The monster overpowered you...')
                self.question = 'Du kaempfst gegen ein Monster! ' \
                                'Und das Monster besiegt dich...'
            self.success = random.randint(0, 10) < 3
            return globals.MAP
        globals.MAP.print()
        return self
