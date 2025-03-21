from fraction import Fraction


def main():
    fraction1 = Fraction(0, 2)
    fraction2 = Fraction(8, 6)

    print(fraction1)
    print(fraction2)
    print(float(fraction2))
    print(f"1 - {fraction1.is_integer()}")


if __name__ == '__main__':
    main()
