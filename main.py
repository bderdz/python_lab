class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def is_integer(self):
        return self.numerator % self.denominator == 0

    def __float__(self):
        return float(self.numerator / self.denominator)

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"


def main():
    fraction1 = Fraction(1, 2)
    fraction2 = Fraction(4, 4)

    print(fraction1)
    print(fraction2)

    print(float(fraction1))

    print(f"1 - {fraction1.is_integer()}")
    print(f"2 - {fraction2.is_integer()}")


if __name__ == '__main__':
    main()
