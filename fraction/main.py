from fraction import Fraction


def main():
    fraction1 = Fraction(1, 2)
    fraction2 = Fraction(3, 4)

    fraction3 = fraction1 * 5
    fraction4 = 5 * fraction2

    try:
        fraction5 = fraction2 / Fraction(1, 0)
    except (ZeroDivisionError, ValueError) as e:
        print(e)

    fraction6 = fraction1 - fraction2
    print(fraction6)


if __name__ == '__main__':
    main()
