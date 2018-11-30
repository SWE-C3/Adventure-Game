"""Module that handles displaying of adventure-games story"""
import curses
import textwrap


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
        story_win.addstr(1, 1, "Story Name")

        story_wrapper = curses.newwin(
            int(screen_size[0] * 0.66), int(screen_size[1] - 5), 2, 3)
        story_wrapper_screen_size = story_wrapper.getmaxyx()
        story_wrapper.border()

        text = "Lorem ipsum dolor sit amet, consetetur "
        text += "sadipscing elitr, sed diam nonumy eirmod"
        text += "tempor invidunt ut labore et"
        text += "dolore magna aliquyam erat, sed diam voluptua. At vero eos"
        text += "et accusam et justo duo dolores et"
        text += "ea rebum. Stet clita kasd gubergren, no sea takimata"
        text += "sanctus est Lorem ipsum dolor sit amet."
        text += "Lorem ipsum dolor sit amet, consetetur sadipscing"
        text += "elitr, sed diam nonumy eirmod tempor "
        text += "invidunt ut labore et dolore magna aliquyam erat,"
        text += "sed diam voluptua. At vero eos et "
        text += "accusam et justo duo dolores et ea rebum. Stet clita"
        text += "kasd gubergren, no sea takimata sanctus "
        text += "est Lorem ipsum dolor sit amet. Lorem ipsum"
        text += "dolor sit amet, consetetur sadipscing "
        text += "elitr, sed diam nonumy eirmod tempor invidunt"
        text += "ut labore et dolore magna aliquyam "
        text += "erat, sed diam voluptua. "

        story = curses.newwin(int(story_wrapper_screen_size[0] * 0.80),
                              int(story_wrapper_screen_size[1] - 7), 3, 6)
        story.addstr(1, 0, textwrap.fill(text, 750))

        story_win.refresh()
        story_wrapper.refresh()
        story.refresh()
