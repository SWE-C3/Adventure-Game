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

    def print(self, window, level_index):
        """
        print all levels
        :param window: window to print
        :param level_index: index of to print level
        :return:
        """

        self.level[level_index].print(window)
