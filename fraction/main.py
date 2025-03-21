from fraction import Fraction


def main():
    fraction1 = Fraction(5, 7)
    fraction2 = Fraction(8, 6)

    fraction3 = fraction1 * 5
    fraction4 = 5 * fraction2

    try:
        fraction5 = fraction2 / Fraction(1, 0)
    except (ZeroDivisionError, ValueError) as e:
        print(e)


if __name__ == '__main__':
    main()
