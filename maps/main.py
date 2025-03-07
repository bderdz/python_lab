import curses

PANEL_HEIGHT = 10


def show_title_screen(stdscr, width, height):
    contents = ["Map maker", "version 1.0", "", "Naciśnij dowolny klawisz aby kontynuować"]
    offset_y = (height - len(contents)) // 2

    for i, content in enumerate(contents):
        offset_x = (width - len(content)) // 2
        stdscr.addstr(offset_y + i, offset_x, content)

    stdscr.getch()


def draw_separator(stdscr, width, height):
    offset_y = height - PANEL_HEIGHT - 1

    stdscr.addstr(offset_y, 0, "-" * width)


def main(stdscr):
    curses.curs_set(0)
    curses.mousemask(curses.ALL_MOUSE_EVENTS | curses.REPORT_MOUSE_POSITION)

    height, width = stdscr.getmaxyx()
    stdscr.clear()
    # stdscr.addstr(5, 10, f"* {height}x{width} *")
    show_title_screen(stdscr, width, height)
    stdscr.clear()
    draw_separator(stdscr, width, height)
    stdscr.refresh()
    stdscr.getch()


if __name__ == '__main__':
    curses.wrapper(main)
