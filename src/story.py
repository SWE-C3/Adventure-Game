import curses
import textwrap


def read_input(window):
    return window.getch()


class StoryScreen:
    def __init__(self, screen):
        # hold current screen
        self.screen = screen
        # hold the pressed key in the menu
        self.pressed_key = ord('z')

    # Print the Story-Screen to given screen.
    def print(self):
        self.screen.clear()
        screen_size = self.screen.getmaxyx()
        story_win = curses.newwin(screen_size[0], screen_size[1], 0, 0)
        story_win.addstr(1, 1, "Story Name")

        story_wrapper = curses.newwin(
            int(screen_size[0] * 0.66), int(screen_size[1] - 5), 2, 3)
        story_wrapper_screen_size = story_wrapper.getmaxyx()
        story_wrapper.border()

        text = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. "

        story = curses.newwin(int(
            story_wrapper_screen_size[0] * 0.80), int(story_wrapper_screen_size[1] - 7), 3, 6)
        story.addstr(1, 0, textwrap.fill(text, 750))
        #story.addstr(1,0, text)

        #story_win.addstr(map_size[0] + 2, map_size[1] - 10, "Weiter (w)")

        story_win.refresh()
        story_wrapper.refresh()
        story.refresh()

        self.pressed_key = read_input(story_win)

