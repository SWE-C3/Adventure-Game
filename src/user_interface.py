"""
Abstract class for user interfaces defining basic methods
"""


class UserInterface:
    """
    Abstract super class for any user interface.
    Attributes:
        resized     Should be set whenever the terminal screen size was changed
        screen      Blank 'background' for the interface
                    Used to draw over previous interfaces
    """

    def __init__(self):
        self.resized = False
        self.screen = None

    def setup(self):
        """
        Creates all windows of this interface. Should be called on init and
        after resizing
        """
        raise NotImplementedError

    def refresh(self):
        """
        Calls refresh methods for all windows of this interface in the desired
        order. Should also call `redrawwin` methods so windows are not
        overwritten because they weren't updated
        """
        raise NotImplementedError

    def print(self):
        """
        Update all windows of this interface. `refresh` should be called at the
        very end of this method
        """
        raise NotImplementedError

    def handle(self, key: int, previous: 'UserInterface'):
        """
        Handles behavior of interface on key input.
        :param key: user input
        :param previous: previously displayed interface
        :return: The next interface to be displayed
        """
        raise NotImplementedError
