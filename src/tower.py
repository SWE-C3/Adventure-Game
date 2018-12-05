"""
tower class
"""


class Tower:
    """
    tower class
    with all levels
    """
    def __init__(self):
        self.levels = []

    def print(self, window):
        """
        print all levels
        :param window: window to print
        :return:
        """
        for level in self.levels:
            level.print(window)
