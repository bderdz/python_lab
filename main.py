from math import sin, cos, radians

GRAVITY = 9.81
DISTANCE = 100
IMPACT_RADIUS = 5


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
        print(f"tura gracza {player}")
        angle, velocity = get_input()
        z = calculate_impact(angle, velocity)

        if player == 1:
            if (check_victory(DISTANCE, z)):
                break
        else:
            z = DISTANCE - z

            if (check_victory(0, z)):
                break

        print(z)

        player = 3 - player

    print(f"Zwyciężył gracz: {player}")


if __name__ == '__main__':
    main()
