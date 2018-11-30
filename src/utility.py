"""
Utility module for reusable functions
"""
import curses
import textwrap
from typing import List, Tuple


def draw_table_centered(window, headers: List[str], items: List[Tuple[str]]):
    """
    draw a centered table in the specified window
    :param window: window to be drawn to
    :param headers: header row values
    :param items: table items as a list of tuples, tuples must have same length
                  as headers
    """
    max_column_lengths = list()
    for index, header in enumerate(headers):
        max_column_lengths.append(
            max(max(len(item[index]) for item in items), len(header))
        )
    height, width = window.getmaxyx()
    table_height = len(items) + 5
    table_width = sum(max_column_lengths) + 3 * len(headers) + 1
    y_position = height // 2 - table_height // 2
    x_position = width // 2 - table_width // 2
    table = curses.newwin(table_height, table_width, y_position, x_position)

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
        columns = [f'{value:^{max_length}}'
                   for value, max_length in zip(values, max_column_lengths)]
        return f'│ {" │ ".join(columns)} │'

    table.addstr(0, 0, separator_top)
    table.addstr(1, 0, template(headers))
    table.addstr(2, 0, separator_middle)
    y_position = 3
    for item in items:
        table.addstr(y_position, 0, template(item))
        y_position += 1
    table.addstr(y_position, 0, separator_bottom)
    return table


def option_dialog(window, question: str, options: List[str],
                  dialog_width: int = 40):
    assert max(len(option) for option in options) <= dialog_width
    height, width = window.getmaxyx()
    question_lines = textwrap.wrap(question, dialog_width - 2)
    dialog_height = len(question_lines) + len(options) + 3
    dialog = curses.newwin(dialog_height,
                           dialog_width,
                           height // 2 - dialog_height // 2,
                           width // 2 - dialog_width // 2)
    y_position = 1
    for question_line in question_lines:
        dialog.addstr(y_position, dialog_width // 2 - len(question_line) // 2,
                      question_line)
        y_position += 1
    for option in options:
        y_position += 1
        dialog.addstr(y_position, dialog_width // 2 - len(option) // 2,
                      option)
    dialog.border()
    return dialog
