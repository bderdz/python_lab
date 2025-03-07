import curses

PANEL_HEIGHT = 10


def load_structure_from_file(src):
    with open(src) as file:
        lines = file.read()
        lines = lines.splitlines()

        return lines[0], lines[1:]


def draw_structure(stdscr, structure):
    name, art = structure

    for i, line in enumerate(art):
        stdscr.addstr(i, 0, line)


def add_structure(structures, y, x, height):
    y_max = height - PANEL_HEIGHT - 1

    if y < y_max:
        structures.append((y, x))


def show_title_screen(stdscr, height, width):
    contents = ["Map maker", "version 1.0", "", "Naciśnij dowolny klawisz aby kontynuować"]
    offset_y = (height - len(contents)) // 2

    for i, content in enumerate(contents):
        offset_x = (width - len(content)) // 2
        stdscr.addstr(offset_y + i, offset_x, content)

    barracks = load_structure_from_file("structures/barracks.txt")
    draw_structure(stdscr, barracks)

    stdscr.getch()


def draw_map(stdscr, structures):
    for y, x in structures:
        stdscr.addstr(y, x, "X")


def draw_separator(stdscr, height, width):
    offset_y = height - PANEL_HEIGHT - 1

    stdscr.addstr(offset_y, 0, "-" * width)


def draw_scene(stdscr, structures, height, width):
    stdscr.clear()
    draw_separator(stdscr, height, width)
    draw_map(stdscr, structures)
    stdscr.refresh()


def main(stdscr):
    curses.curs_set(0)
    curses.mousemask(curses.ALL_MOUSE_EVENTS | curses.REPORT_MOUSE_POSITION)

    structures = [(10, 5), (8, 9), (15, 20)]
    height, width = stdscr.getmaxyx()
    stdscr.clear()
    show_title_screen(stdscr, height, width)
    draw_scene(stdscr, structures, height, width)

    while (True):
        ch = stdscr.getch()

        if ch == curses.KEY_MOUSE:
            _, x, y, _, bstate = curses.getmouse()

            if bstate & curses.BUTTON1_CLICKED:
                add_structure(structures, y, x, height)
                draw_scene(stdscr, structures, height, width)


if __name__ == '__main__':
    curses.wrapper(main)
