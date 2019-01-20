import curses

from user_interface import UserInterface
from utility import option_dialog


class Dialog(UserInterface):
    def __init__(self):
        super().__init__()
        self.dialog = None
        self.question = None
        self.options = None

    def setup(self):
        self.screen = curses.newwin(0, 0)
        self.dialog = option_dialog(self.screen, self.question, self.options)

    def refresh(self):
        self.dialog.redrawwin()
        self.dialog.refresh()

    def print(self):
        """
        render dialog to terminal window
        """
        if self.resized:
            self.resized = False
            self.setup()
        self.refresh()

    def handle(self, key: int, previous: 'UserInterface'):
        raise NotImplementedError
