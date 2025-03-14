import curses
from time import sleep

SIGN_CHAR = "*"
FPS = 0.03


def update(signs, floor_height):
    for i, sign in enumerate(signs):
        if sign[0] < floor_height[sign[1]]:
            signs[i] = (sign[0] + 1, sign[1])

        if sign[0] == floor_height[sign[1]]:
            floor_height[sign[1]] -= 1
            signs.pop(i)


def draw(stdscr, signs, floor_height, height, width):
    stdscr.clear()
    # Draw floor
    for x, h in enumerate(floor_height):
        if height != h:
            for y in range(height - h):
                stdscr.addstr(height - 1 - y, x, SIGN_CHAR)

    # Draw falling signs
    for y, x in signs:
        stdscr.addstr(y - 1, x, SIGN_CHAR)

    stdscr.refresh()


def main(stdscr):
    signs = []
    height, width = stdscr.getmaxyx()
    floor_height = [height] * width

    curses.curs_set(0)
    curses.mousemask(curses.ALL_MOUSE_EVENTS | curses.REPORT_MOUSE_POSITION)
    stdscr.nodelay(True)

    while True:
        update(signs, floor_height)
        draw(stdscr, signs, floor_height, height, width)
        sleep(FPS)
        ch = stdscr.getch()

        if ch == curses.KEY_MOUSE:
            _, x, y, _, bstate = curses.getmouse()
            if bstate & curses.BUTTON1_CLICKED:
                signs.append((y, x))


if __name__ == '__main__':
    curses.wrapper(main)
