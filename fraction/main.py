from fraction import Fraction


def main():
    fraction1 = Fraction(5, 7)
    fraction2 = Fraction(8, 6)

    # fraction1 *= fraction2
    # print(fraction1)
    fraction3 = fraction1 * 5
    fraction4 = 5 * fraction2
    fraction5 = fraction2 / Fraction(2, 1)
    print(fraction5)
    # print(str(fraction1))


# print(str(fraction2))
# print(float(fraction2))
# print(fraction1.is_integer())


if __name__ == '__main__':
    main()
