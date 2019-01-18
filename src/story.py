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
        self.text = ''
        self.story_content = None
        self.setup()

    def setup(self):
        self.screen = curses.newwin(0, 0)
        height, width = self.screen.getmaxyx()

        self.story_content = curses.newwin(height - 2, width - 3, 2, 2)
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
        width = self.story_content.getmaxyx()[1] - 4
        self.story_content.clear()
        self.story_content.addstr(1, 0, textwrap.fill(self.text, width))
        self.refresh()

    def handle(self, key: int, previous):
        if key == constants.ENTER:
            if self.text == self.stories['outro']:
                self.text = ''
                return globals.MAIN
            self.text = ''
            return globals.MAP
        return self
