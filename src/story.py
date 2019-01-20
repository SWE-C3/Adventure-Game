import curses
import textwrap
from pathlib import Path

import constants
import globals
from user_interface import UserInterface


class StoryScreen(UserInterface):

    def __init__(self):
        super().__init__()
        self.stories = dict()
        for story in (Path(__file__).parent.parent
                      / 'resources' / 'story').glob('*.story'):
            with story.open() as file:
                self.stories[story.stem] = file.read()
        self._upper = 0
        self.story_height = 0
        self._text = ''
        self.lines = 0
        self.story_content = None
        self.setup()

    @property
    def lower(self):
        return self.upper + self.story_height

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        width = self.story_content.getmaxyx()[1] - 4
        self._text = textwrap.wrap(value, width)

    @property
    def upper(self):
        return self._upper

    @upper.setter
    def upper(self, value):
        self._upper = max(0, min(len(self.text) - self.story_height, value))

    def setup(self):
        self.screen = curses.newwin(0, 0)
        height, width = self.screen.getmaxyx()
        self.story_content = curses.newwin(height - 4, width - 3, 2, 2)
        self.story_height = height - 5
        self.screen.addstr(1, 4, 'Geschichte')
        self.screen.addstr(1, width - 15, '[ENTER] Weiter')

    def refresh(self):
        self.screen.redrawwin()
        self.story_content.redrawwin()
        self.screen.refresh()
        self.story_content.refresh()

    def print(self):
        if self.resized:
            self.resized = False
            self.setup()
        self.story_content.clear()
        wrapped_text = self.text[self.upper:self.lower]
        for index, line in enumerate(wrapped_text):
            self.story_content.addstr(index + 1, 0, line)
        self.refresh()

    def handle(self, key: int, previous):
        if key == constants.ENTER:
            if self.text == self.stories['outro']:
                self.text = ''
                return globals.MAIN
            self.text = ''
            return globals.MAP
        elif key in (constants.DOWN, ord('s')):
            self.upper += 1
        elif key in (constants.UP, ord('w')):
            self.upper -= 1
        return self
