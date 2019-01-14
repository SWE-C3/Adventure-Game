"""Module that handles displaying of adventure-games story"""
import curses
import textwrap

from user_interface import UserInterface


class StoryScreen(UserInterface):
    """Story Screen Class, can display parts of the games' story"""

    def __init__(self):
        """StoryScreen's init function"""
        super().__init__()
        self.text = "Lorem ipsum dolor sit amet, consetetur "
        self.text += "et accusam et justo duo dolores et"
        self.text += "ea rebum. Stet clita kasd gubergren, no sea takimata"
        self.text += "sanctus est Lorem ipsum dolor sit amet."
        self.text += "Lorem ipsum dolor sit amet, consetetur sadipscing"
        self.text += "elitr, sed diam nonumy eirmod tempor "
        self.text += "invidunt ut labore et dolore magn"
        self.story_name = "Story Name"
        self.story_content = None
        self.story = None
        self.story_image = None
        self.story_win = None
        self.setup()

    def setup(self):
        self.screen = curses.newwin(0, 0)
        screen_size = self.screen.getmaxyx()
        self.story_win = curses.newwin(screen_size[0], screen_size[1], 0, 0)

        self.story_image = curses.newwin(
            int(screen_size[0] * 0.50), int(screen_size[1] - 5), 2, 3)
        self.story_image.border()
        self.story_win.addstr(
            int(screen_size[0] * 0.92), int(screen_size[1] * 0.845),
            "Weiter (W)")

        self.story = curses.newwin(int(screen_size[0] * 0.35),
                                   int(screen_size[1] - 5),
                                   int(1 + screen_size[0] * 0.55), 3)
        story_size = self.story.getmaxyx()
        self.story.border()

        self.story_content = curses.newwin(
            int(story_size[0] * 0.74), int(story_size[1] * 0.95),
            int(screen_size[0] * 0.63), 5)

    def refresh(self):
        self.screen.redrawwin()
        self.story_win.redrawwin()
        self.story_image.redrawwin()
        self.story.redrawwin()
        self.story_content.redrawwin()
        self.screen.refresh()
        self.story_win.refresh()
        self.story_image.refresh()
        self.story.refresh()
        self.story_content.refresh()

    # Print the Story-Screen to given screen.
    def print(self):
        """Prints story-screen"""
        if self.resized:
            self.resized = False
            self.setup()
        self.story_win.addstr(1, 4, self.story_name)
        self.story_content.addstr(1, 0, textwrap.fill(self.text, 750))
        self.refresh()

    def handle(self, key: int, previous):
        if key == ord('w'):
            return previous
        return self
