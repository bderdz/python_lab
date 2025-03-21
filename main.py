class Fraction:
    numerator = None
    denominator = None

    def is_integer(self):
        return self.numerator % self.denominator == 0


def main():
    fraction = Fraction()
    fraction.numerator = 1
    fraction.denominator = 2

    fraction2 = Fraction()
    fraction2.numerator = 4
    fraction2.denominator = 4

    print(f"{fraction.numerator}/{fraction.denominator}")
    print(f"{fraction2.numerator}/{fraction2.denominator}")

    print(f"1 - {fraction.is_integer()}")
    print(f"2 - {fraction2.is_integer()}")


if __name__ == '__main__':
    main()
