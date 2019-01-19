"""
Game map interface
"""
import curses
import json
import logging
import random
from pathlib import Path
from pprint import pformat
from typing import List, Set, Tuple

import constants
import globals
from dialog import Dialog
from items import Consumable, Equipment, Weapon
from monster import Monster
from player import Player, Position
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
        self.event_log = None
        self.map = None
        self.status_info = None
        self.levels = list()
        self.level_width = 51
        self.level_height = 15
        self.levels = list()
        self.items = dict()
        self.monsters = dict()
        self.starting_positions = list()
        self.stories_shown = set()
        for index, file in enumerate(
                sorted(
                    (Path(__file__).parent.parent / 'resources' / 'levels')
                            .glob('*.level'),
                    key=lambda x: int(x.stem)
                )
        ):
            with file.open() as level:
                self.levels.append(self.parse_level(level.read(), index))
        self.player = Player(Position(self.level_width, self.level_height,
                                      layouts=self.levels))
        self.player.position.x, self.player.position.y = \
            self.starting_positions[0]
        self._last_position = self.current_position
        self.visited: List[Set[Tuple[int, int]]] = [set() for _ in
                                                    range(len(self.levels))]
        self.seen: List[Set[Tuple[int, int]]] = [set() for _ in
                                                 range(len(self.levels))]
        self.setup()

    @property
    def health_bar(self):
        health_bar = int(10 * (self.player.current_health
                               / self.player.max_health)) * constants.HEALTH
        return health_bar

    @property
    def current_value(self) -> str:
        return self.levels[self.player.level][self.player.y][self.player.x]

    @current_value.setter
    def current_value(self, value: str):
        self.levels[self.player.level][self.player.y][self.player.x] = value

    @property
    def current_position(self):
        return self.player.x, self.player.y

    def save_game(self):
        data = {
            'monsters': {str(key): vars(monster) for key, monster in
                         self.monsters.items()},
            'items': {str(key): vars(item) for key, item in
                      self.items.items()},
            'starting_positions': [list(position) for position in
                                   self.starting_positions],
            'levels': self.levels,
            'player_items': {
                'head': vars(self.player.head) if self.player.head else None,
                'chest': vars(self.player.chest)
                if self.player.chest else None,
                'legs': vars(self.player.legs) if self.player.legs else None,
                'feet': vars(self.player.feet) if self.player.feet else None,
                'weapon': vars(self.player.weapon)
                if self.player.weapon else None,
                'cookies': [vars(cookie) for cookie in self.player.cookies
                            if cookie]
            },
            'damage': self.player.damage,
            'last_position': list(self._last_position),
            'level': self.player.level,
            'current_position': list(self.current_position),
            'visited': [[list(position) for position in level] for level in
                        self.visited],
            'seen': [[list(position) for position in level] for level in
                     self.seen],
            'stories_shown': list(self.stories_shown)
        }
        with (Path(__file__).parent.parent / 'savegame.json').open(mode='w') \
                as file:
            logging.info(pformat(data))
            json.dump(data, file, default=lambda x: vars(x))

    def load_game(self, filename: str):
        with (Path(__file__).parent.parent / filename).open() as file:
            data = json.load(file)
        for position, monster_data in data['monsters'].items():
            position = tuple(int(i) for i in position[1:-1].split(', '))
            monster = Monster(1)
            monster.strength = monster_data['strength']
            monster.name = monster_data['name']
            self.monsters[position] = monster
        for position, item_data in data['items'].items():
            position = tuple(int(i) for i in position[1:-1].split(', '))
            item = Consumable(1) if item_data['type'] == 'Keks' \
                else Equipment(1)
            item.name = item_data['name']
            item.factor = item_data['factor']
            item.type = item_data['type']
            self.items[position] = item
        self.starting_positions = [tuple(position) for position in
                                   data['starting_positions']]
        self.levels = data['levels']
        head = data['player_items']['head']
        chest = data['player_items']['chest']
        legs = data['player_items']['legs']
        feet = data['player_items']['feet']
        weapon = data['player_items']['weapon']
        cookies = data['player_items']['cookies']
        self.player.head = head if not head else Equipment(1)
        if head:
            self.player.head.factor = head['factor']
            self.player.head.name = head['name']
            self.player.head.type = head['type']
        self.player.chest = chest if not chest else Equipment(1)
        if chest:
            self.player.chest.factor = chest['factor']
            self.player.chest.name = chest['name']
            self.player.chest.type = chest['type']
        self.player.legs = legs if not legs else Equipment(1)
        if legs:
            self.player.legs.factor = legs['factor']
            self.player.legs.name = legs['name']
            self.player.legs.type = legs['type']
        self.player.feet = feet if not feet else Equipment(1)
        if feet:
            self.player.feet.factor = feet['factor']
            self.player.feet.name = feet['name']
            self.player.feet.type = feet['type']
        self.player.weapon = weapon if not weapon else Weapon(1)
        if weapon:
            self.player.weapon.factor = weapon['factor']
            self.player.weapon.name = weapon['name']
            self.player.weapon.type = weapon['type']
        self.player.cookies = list()
        for cookie_data in cookies:
            cookie = Consumable(1)
            cookie.factor = cookie_data['factor']
            cookie.name = cookie_data['name']
            cookie.type = cookie_data['type']
            self.player.cookies.append(cookie)
        self.player.position._level = data['level']
        self.player.damage = data['damage']
        self._last_position = (data['last_position'][0],
                               data['last_position'][1])
        self.player.position._x = data['current_position'][0]
        self.player.position._y = data['current_position'][1]
        self.visited = [set(tuple(position) for position in level) for level in
                        data['visited']]
        self.seen = [set(tuple(position) for position in level) for level in
                     data['seen']]
        self.stories_shown = set(data['stories_shown'])

    def parse_level(self, level: str, level_number: int) -> List[List[str]]:
        level = level.replace('-', constants.HORIZONTAL)
        level = level.replace('|', constants.VERTICAL)
        level = level.replace('+', constants.CROSS)
        level = [[char for char in row]
                 for row in level.split('\n')]
        for y_index, row in enumerate(level):
            for x_index, value in enumerate(row):
                if x_index == 0 and y_index == 0:
                    level[y_index][x_index] = constants.BOTTOM_RIGHT
                elif x_index == 0 and y_index == len(level) - 1:
                    level[y_index][x_index] = constants.TOP_RIGHT
                elif x_index == len(row) - 1 and y_index == len(level) - 1:
                    level[y_index][x_index] = constants.TOP_LEFT
                elif x_index == len(row) - 1 and y_index == 0:
                    level[y_index][x_index] = constants.BOTTOM_LEFT
                elif y_index == 0 and value == constants.CROSS:
                    level[y_index][x_index] = constants.TOP_OUT
                elif y_index == len(level) - 1 and value == constants.CROSS:
                    level[y_index][x_index] = constants.BOTTOM_OUT
                elif x_index == 0 and value == constants.CROSS:
                    level[y_index][x_index] = constants.LEFT_OUT
                elif x_index == len(row) - 1 and value == constants.CROSS:
                    level[y_index][x_index] = constants.RIGHT_OUT
                if value == 'I':
                    self.items[(level_number, x_index, y_index)] = \
                        random.choice((Consumable, Equipment,
                                       Weapon))(level_number + 1)
                elif value == 'M':
                    self.monsters[(level_number, x_index, y_index)] = \
                        Monster(level_number + 1)
                elif value == '%':
                    self.starting_positions.append((x_index, y_index))
                    if level_number == 0:
                        level[y_index][x_index] = ' '
        return level

    def level_value(self, x_index: int, y_index: int) -> str:
        return self.levels[self.player.level][y_index][x_index]

    def visit(self, x_index: int, y_index: int):
        for vertical in range(-1, 2):
            for horizontal in range(-1, 2):
                self.visited[self.player.level].add((x_index + horizontal,
                                                     y_index + vertical))
                self.seen[self.player.level].add((x_index + horizontal,
                                                  y_index + vertical))

    def see(self, x_index: int, y_index: int):
        for vertical in range(-1, 2):
            for horizontal in range(-1, 2):
                self.seen[self.player.level].add((x_index + horizontal,
                                                  y_index + vertical))

    def log_event(self, message):
        self.event_log.move(1, 1)
        self.event_log.deleteln()
        self.event_log.move(self.event_log.getmaxyx()[0] - 2, 1)
        self.event_log.insertln()
        self.event_log.border()
        self.event_log.addstr(self.event_log.getmaxyx()[0] - 2, 1,
                              message, color(foreground=curses.COLOR_YELLOW))

    def setup(self):
        self.screen = curses.newwin(0, 0)
        height, width = self.screen.getmaxyx()
        self.map = curses.newwin(self.level_height, self.level_width + 1,
                                 2, width // 2 - self.level_width // 2)
        map_height, _ = self.map.getmaxyx()
        self.status_info = curses.newwin(3, width - 5, map_height + 2, 3)
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
        self.screen.addstr(1, 20, f'Position: {self.current_position}')

        self.visit(*self.current_position)
        for i in (-1, 1):
            if self.level_value(self.current_position[0] + i,
                                self.current_position[1]) == ' ':
                self.see(self.current_position[0] + i,
                         self.current_position[1])
            if self.level_value(self.current_position[0],
                                self.current_position[1] + i) == ' ':
                self.see(self.current_position[0],
                         self.current_position[1] + i)

        for y_index, row in enumerate(self.levels[self.player.level]):
            for x_index, value in enumerate(row):
                if (x_index, y_index) not in self.seen[self.player.level]:
                    self.map.addstr(y_index, x_index, '#',
                                    color(foreground=curses.COLOR_BLUE))
                elif (x_index, y_index) \
                        not in self.visited[self.player.level] \
                        and value in ('M', 'O', 'I'):
                    self.map.addstr(y_index, x_index, constants.UNKNOWN,
                                    color(foreground=curses.COLOR_MAGENTA))
                elif value == 'I':
                    self.map.addstr(y_index, x_index, constants.ITEM,
                                    color(foreground=curses.COLOR_CYAN))
                elif value == 'X':
                    self.map.addstr(y_index, x_index, constants.SAVEPOINT,
                                    color(foreground=curses.COLOR_BLUE))
                elif value == '=':
                    self.map.addstr(y_index, x_index, constants.LADDER_UP,
                                    color(foreground=curses.COLOR_GREEN))
                elif value == '%':
                    self.map.addstr(y_index, x_index, constants.LADDER_DOWN,
                                    color(foreground=curses.COLOR_GREEN))
                elif value == 'M':
                    self.map.addstr(y_index, x_index, constants.MONSTER,
                                    color(foreground=curses.COLOR_RED))
                elif value == 'O':
                    self.map.addstr(y_index, x_index, constants.HOLE)
                else:
                    self.map.addstr(y_index, x_index, value)

        self.map.addstr(self.current_position[1], self.current_position[0],
                        constants.PLAYER, color(foreground=curses.COLOR_YELLOW))

        self.status_info.addstr(1, 2, "HP: ")
        self.status_info.addstr(1, 6, 10 * ' ',
                                color(foreground=curses.COLOR_RED))
        self.status_info.addstr(1, 6, self.health_bar,
                                color(foreground=curses.COLOR_RED))

        self.status_info.addstr(1, 17,
                                f'{self.player.current_health:3}/{self.player.max_health:3}')
        self.status_info.addstr(1, 27, f"Staerke: {self.player.strength}")

        self.refresh()

    def handle(self, key: int, previous=None):
        self._last_position = self.current_position

        if self.player.current_health < 1:
            return globals.GAME_OVER
        elif key == constants.ESCAPE:
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

        if self._last_position != self.current_position:
            if self.current_value == 'M':
                self.visit(*self.current_position)
                return globals.MONSTER
            elif self.current_value == 'I':
                return globals.ITEM
            elif self.current_value == 'X':
                return globals.SAVE_GAME
            elif self.current_value == '=':
                self.visit(*self.current_position)
                globals.LADDER.upwards = True
                return globals.LADDER
            elif self.current_value == '%':
                self.visit(*self.current_position)
                globals.LADDER.upwards = False
                return globals.LADDER
            elif self.current_value == 'O':
                self.visit(*self.current_position)
                self.log_event('Du bist durch ein Loch gefallen')
                self.player.position.level -= 1
        return self


class LadderDialog(Dialog):

    def __init__(self):
        super().__init__()
        self.upwards = True
        self.question = ''
        self.options = ['[J] Ja', '[N] Nein']
        self.initialized = False
        self.setup()

    def print(self):
        if not self.initialized:
            if self.upwards:
                self.question = 'Du hast eine Leiter nach oben gefunden. ' \
                                'Willst du sie herauf klettern?'
            else:
                self.question = 'Du hast eine Leiter nach unten gefunden. ' \
                                'Willst du sie hinab kletern?'
            self.setup()
            self.initialized = True
        super().print()

    def handle(self, key: int, previous: 'UserInterface'):
        if key == ord('j'):
            self.initialized = False
            if self.upwards:
                globals.MAP.log_event('Du bist eine Leiter hinaufgestiegen')
                globals.MAP.player.position.level += 1
                if globals.MAP.player.level == 10:
                    globals.STORY.text = globals.STORY.stories['outro']
                    return globals.STORY
                elif globals.MAP.player.level not in globals.MAP.stories_shown:
                    globals.MAP.stories_shown.add(globals.MAP.player.level)
                    globals.STORY.text = \
                        globals.STORY.stories[str(globals.MAP.player.level)]
                    return globals.STORY
                return globals.MAP
            else:
                globals.MAP.log_event('Du bist eine Leiter hinabgestiegen')
                globals.MAP.player.position.level -= 1
                return globals.MAP
        elif key == ord('n'):
            self.initialized = False
            return globals.MAP
        previous.print()
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
            globals.MAP.log_event('Du hast das Spiel nicht gespeichert')
            return globals.MAP
        elif key == ord('j'):
            globals.MAP.save_game()
            globals.MAP.log_event('Du hast das Spiel gespeichert')
            return globals.MAP
        globals.MAP.print()
        return self


class MonsterDialog(Dialog):
    """
    Dialog when encountering a monster
    """

    def __init__(self):
        super().__init__()
        self.initialized = False
        self.question = ''
        self.options = ["[ENTER] OK"]
        self.setup()

    def print(self):
        if not self.initialized:
            self.initialize()
            self.initialized = True
        super().print()

    def handle(self, key: int, previous=None):
        if key == constants.ENTER:
            self.initialized = False
            return globals.MAP
        globals.MAP.print()
        return self

    def initialize(self):
        player = globals.MAP.player
        monster = globals.MAP.monsters[(player.level,
                                        *globals.MAP.current_position)]

        self.question = f'Du kaempfst gegen das Monster:\n{monster}\n' \
            f'Staerke: {monster.strength}'

        if player.strength >= monster.strength:
            self.question += '\nUnd du besiegst es!'
            globals.MAP.log_event(f'{monster.name.title()} wurde besiegt!')
            globals.MAP.current_value = ' '
            globals.MAP.levels[player.level][globals.MAP._last_position[1]][
                globals.MAP._last_position[0]] = 'I'
            globals.MAP.items[(player.level, *globals.MAP._last_position)] = \
                random.choice((Consumable, Equipment,
                               Weapon))(player.level + 1)
        else:
            damage = int(player.strength/monster.strength * player.strength)
            self.question += '\nUnd das Monster besiegt dich...'
            self.question += f'\nDu hast {damage} Schaden ausgeteilt'
            globals.MAP.log_event(f'{monster.name.title()} '
                                  f'hat dich besiegt...')
            globals.MAP.player.damage += monster.strength - player.strength
            globals.MAP.monsters[(player.level, player.x,
                                  player.y)].strength -= damage

            globals.MAP.player.position._x, globals.MAP.player.position._y = \
                globals.MAP.starting_positions[player.level]
        self.setup()


class ItemDialog(Dialog):

    def __init__(self):
        super().__init__()
        self.initialized = False
        self.question = ''
        self.item = None
        self.options = ['[J] Aufnehmen', '[N] Liegen lassen']
        self.setup()

    def print(self):
        if not self.initialized:
            self.initialize()
            self.initialized = True
        super().print()

    def handle(self, key: int, previous: 'UserInterface'):
        if key == ord('j'):
            self.initialized = False
            globals.MAP.player.add_item(self.item)
            globals.MAP.current_value = ' '
            globals.MAP.log_event(f'Du hast {self.item} aufgenommen')
            return previous
        if key == ord('n'):
            self.initialized = False
            globals.MAP.log_event(f'Du hast {self.item} liegen lassen')
            return previous
        previous.print()
        return self

    def initialize(self):
        self.item = globals.MAP.items[(globals.MAP.player.level,
                                       *globals.MAP.current_position)]

        self.question = 'Du hast einen Gegenstand gefunden!\n' \
            f'Name: {self.item}\n' \
            f'Staerke: {self.item.factor}'
        self.options = ['[J] Aufnehmen', '[N] Liegen lassen']
        other_item = None
        if self.item.type == 'Kopf':
            other_item = globals.MAP.player.head
        elif self.item.type == 'Brust':
            other_item = globals.MAP.player.chest
        elif self.item.type == 'Beine':
            other_item = globals.MAP.player.legs
        elif self.item.type == 'Fuesse':
            other_item = globals.MAP.player.feet
        elif self.item.type == 'Waffe':
            other_item = globals.MAP.player.weapon
        elif self.item.type == 'Keks' and len(globals.MAP.player.cookies) > 2:
            other_item = globals.MAP.player.cookies[0]
        if other_item:
            self.question += f'\nDu hast bereits diesen Gegenstand:\n' \
            f'Name: {other_item}\n' \
            f'Staerke: {other_item.factor}'
            self.options[0] = '[J] Austauschen'
        self.setup()


class GameOverDialog(Dialog):
    def __init__(self):
        super().__init__()
        self.question = 'Du bist gestorben\nGame Over'
        self.options = ['[O] OK']
        self.setup()

    def handle(self, key: int, previous: 'UserInterface'):
        if key == ord('o'):
            globals.MAP = GameMap()
            return globals.MAIN
        previous.print()
        return self
