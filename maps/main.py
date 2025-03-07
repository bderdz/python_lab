import curses

PANEL_HEIGHT = 10
barracks = None


def load_structure_from_file(src):
    with open(src) as file:
        lines = file.read()
        lines = lines.splitlines()

        return lines[0], lines[1:]


def draw_structure(stdscr, structure, x, y, centered=False, labeled=False, highlighted=False):
    name, art = structure
    offset_y = y - len(art)
    color = curses.color_pair(1 if highlighted else 0) | curses.A_BOLD

    if centered:
        x -= len(art[0]) // 2

    for i, line in enumerate(art):
        stdscr.addstr(offset_y + i, x, line, color)

    if labeled:
        stdscr.addstr(y + 1, x, name, color)


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

    stdscr.getch()


def draw_map(stdscr, structures):
    global barracks
    
    for y, x in structures:
        draw_structure(stdscr, barracks, x, y, centered=True)


def draw_separator(stdscr, height, width):
    offset_y = height - PANEL_HEIGHT - 1

    stdscr.addstr(offset_y, 0, "-" * width)


def draw_scene(stdscr, structures, height, width):
    stdscr.clear()
    draw_separator(stdscr, height, width)
    draw_map(stdscr, structures)
    stdscr.refresh()


def main(stdscr):
    global barracks
    barracks = load_structure_from_file("structures/barracks.txt")

    curses.start_color()
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
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
