from math import sin, cos, radians
from time import sleep
import os
from shutil import get_terminal_size

GRAVITY = 9.81
DISTANCE = 100
IMPACT_RADIUS = 5
COLS, ROWS = get_terminal_size()

ASPECT_RATIO = COLS / DISTANCE


def draw_scene(x, y):
    for _ in range(y - 2):
        print()

    if 0 <= x < COLS and 0 <= y < ROWS:
        for _ in range(x - 1):
            print(" ", end="")
        print("o")
    else:
        print()

    for _ in range(y, ROWS - 1):
        print()

    print("(@)" + "-" * (COLS - 6) + "(#)")


def draw_scene_adjusted(x, y):
    x_t = x * ASPECT_RATIO
    y_t = ROWS - (y * ASPECT_RATIO / 2)

    draw_scene(round(x_t), round(y_t))


def animate_shot(velocity, angle, player):
    t_c = 2 * velocity * sin(angle) / GRAVITY
    d_t = 0.016
    v_x = velocity * cos(angle) * (-1 if player == 2 else 1)
    v_y = velocity * sin(angle)

    t = 0

    while t < t_c:
        x = v_x * t + (COLS if player == 2 else 0)
        y = v_y * t - GRAVITY * t ** 2 / 2

        os.system("clear")
        draw_scene_adjusted(x, y)

        t += d_t
        sleep(d_t)


def get_input():
    angle = None

    while angle is None or not (angle >= 0 and angle <= 90):
        angle = float(input("Podaj kąt: "))

    velocity = float(input("Podaj prędkość: "))
    angle = radians(angle)

    return angle, velocity


def calculate_impact(angle, velocity):
    return (velocity ** 2 * sin(2 * angle)) / GRAVITY


def check_victory(distance, z):
    return abs(distance - z) < IMPACT_RADIUS


def main():
    player = 1

    while True:
        print(f"\ntura gracza {player}")
        angle, velocity = get_input()
        z = calculate_impact(angle, velocity)

        animate_shot(velocity, angle, player)

        if player == 1:
            if (check_victory(DISTANCE, z)):
                break
        else:
            z = DISTANCE - z

            if (check_victory(0, z)):
                break

        player = 3 - player

    print(f"Zwyciężył gracz: {player}")


if __name__ == '__main__':
    main()
