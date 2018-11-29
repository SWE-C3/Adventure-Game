"""
Utility module for reusable functions
"""


def draw_table_centered(window, headers: list, items: dict):
    """
    draw a centered table in the specified window
    :param window: window to be drawn to
    :param headers: header row values
    :param items: table items as a dict, dict must have same amount of
                  key-value pairs as there are items in headers
    :return:
    """
    max_column_lengths = list()
    for header, key in zip(headers, items[0].keys()):
        max_column_lengths.append(
            max(max(len(item[key]) for item in items), len(header))
        )
    height, width = window.getmaxyx()
    y_pos = height // 2 - len(items) // 2 - 1
    x_pos = width // 2 - (sum(max_column_lengths)
                          + 3 * len(max_column_lengths)
                          + 1) // 2

    separator_top = (
        f'┌─{"─┬─".join("─" * length for length in max_column_lengths)}─┐'
    )
    separator_middle = (
        f'├─{"─┼─".join("─" * length for length in max_column_lengths)}─┤'
    )
    separator_bottom = (
        f'└─{"─┴─".join("─" * length for length in max_column_lengths)}─┘'
    )

    def template(values):
        columns = [f'{value:^{max_column_lengths[index]}}' for index,
                   value in enumerate(values)]
        return f'│ {" │ ".join(columns)} │'

    window.addstr(y_pos - 3, x_pos, separator_top)
    window.addstr(y_pos - 2, x_pos, template(headers))
    window.addstr(y_pos - 1, x_pos, separator_middle)
    for item in items:
        window.addstr(y_pos, x_pos, template(item.values()))
        y_pos += 1
    window.addstr(y_pos, x_pos, separator_bottom)
