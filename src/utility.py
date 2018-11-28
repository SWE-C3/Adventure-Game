def draw_table_centered(window, headers: list, items: dict):
    max_column_lengths = list()
    for header, key in zip(headers, items[0].keys()):
        max_column_lengths.append(
            max(max(len(item[key]) for item in items), len(header))
        )
    height, width = window.getmaxyx()
    y_pos = height // 2 - len(items) // 2 - 1
    x_pos = width // 2 - (sum(max_column_lengths) + 10) // 2

    separator = f'+-{"-+-".join("-" * length for length in max_column_lengths)}-+'

    def template(values):
        columns = [f'{value:^{max_column_lengths[index]}}' for index, value in enumerate(values)]
        return f'| {" | ".join(columns)} |'

    window.addstr(y_pos - 3, x_pos, separator)
    window.addstr(y_pos - 2, x_pos, template(headers))
    window.addstr(y_pos - 1, x_pos, separator)
    for item in items:
        window.addstr(y_pos, x_pos, template(item.values()))
        y_pos += 1
    window.addstr(y_pos, x_pos, separator)
