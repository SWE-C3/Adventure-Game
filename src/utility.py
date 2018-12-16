"""
Utility module for reusable functions
"""
import curses
import textwrap
from typing import List, Tuple


def table_centered(window, headers: List[str], items: List[Tuple[str]]):
    """
    create a window with a centered table centered in the specified window
    :param window: window to be centered on
    :param headers: header row values
    :param items: table items as a list of tuples, tuples must have same length
                  as headers
    :return window object containing a table
    """
    max_column_lengths = list()
    for index, header in enumerate(headers):
        max_column_lengths.append(
            max(max(len(item[index]) for item in items), len(header))
        )
    height, width = window.getmaxyx()
    table_height = len(items) + 5
    table_width = sum(max_column_lengths) + 3 * len(headers) + 1
    table = curses.newwin(table_height, table_width,
                          height // 2 - table_height // 2,
                          width // 2 - table_width // 2)

    def template(values):
        columns = [f'{value:^{max_length}}'
                   for value, max_length in zip(values, max_column_lengths)]
        return f'│ {" │ ".join(columns)} │'

    table.addstr(
        0, 0,
        f'┌─{"─┬─".join("─" * length for length in max_column_lengths)}─┐'
    )
    table.addstr(1, 0, template(headers))
    table.addstr(
        2, 0,
        f'├─{"─┼─".join("─" * length for length in max_column_lengths)}─┤'
    )
    y_position = 3
    for item in items:
        table.addstr(y_position, 0, template(item))
        y_position += 1
    table.addstr(
        y_position, 0,
        f'└─{"─┴─".join("─" * length for length in max_column_lengths)}─┘'
    )
    return table


def option_dialog(window, question: str, options: List[str],
                  dialog_width: int = 40):
    """
    create a dialog with multiple options centered in the specified window
    :param window: window to be centered on
    :param question: question to be asked
    :param options: options to be provided, options are required to be shorter
                    than dialog_width
    :param dialog_width: width of the dialog window, question will be wrapped
                         to fit the width
    :return: a window object containing the dialog
    """
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
