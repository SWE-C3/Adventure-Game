"""Module that handles displaying of adventure-games story"""
import curses
import textwrap

import constants


class StoryScreen:
    """Story Screen Class, can display parts of the games' story"""

    def __init__(self, screen):
        """StoryScreen's init function"""
        # hold current screen
        self.screen = screen

    # Print the Story-Screen to given screen.
    def print(self):
        """Prints story-screen"""
        screen_size = self.screen.getmaxyx()
        story_win = curses.newwin(screen_size[0], screen_size[1], 0, 0)
        story_win.addstr(1, 4, "Story Name")

        story_image = curses.newwin(
            int(screen_size[0] * 0.50), int(screen_size[1] - 5), 2, 3)
        story_image.border()
        story_win.addstr(
            int(screen_size[0] * 0.92), int(screen_size[1]*0.845),
            "Weiter (w)")

        text = "Lorem ipsum dolor sit amet, consetetur "
        text += "et accusam et justo duo dolores et"
        text += "ea rebum. Stet clita kasd gubergren, no sea takimata"
        text += "sanctus est Lorem ipsum dolor sit amet."
        text += "Lorem ipsum dolor sit amet, consetetur sadipscing"
        text += "elitr, sed diam nonumy eirmod tempor "
        text += "invidunt ut labore et dolore magn"

        story = curses.newwin(int(screen_size[0] * 0.35),
                              int(screen_size[1] - 5),
                              int(1 + screen_size[0] * 0.55), 3)
        story_size = story.getmaxyx()
        story.border()

        story_content = curses.newwin(
            int(story_size[0] * 0.74), int(story_size[1]*0.95),
            int(screen_size[0] * 0.63), 5)
        story_content.addstr(1, 0, textwrap.fill(text, 750))
        self.screen.clear()
        story_win.refresh()
        story_image.refresh()
        story.refresh()
        story_content.refresh()

    def handle(self, key: int, previous):
        while True:
            if key == constants.ESCAPE:
                return previous
            key = self.screen.getch()