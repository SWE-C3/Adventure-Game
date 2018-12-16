import curses

if __name__ == '__main__':

    STDSCR = curses.initscr()
    curses.cbreak()
    curses.noecho()
    curses.curs_set(0)
    STDSCR.keypad(True)

    while True:
        key = STDSCR.getch()
        STDSCR.clear()
        STDSCR.addstr(1, 1, str(key))
