from math import gcd


class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

        self.__reduce()

    def is_integer(self):
        return self.denominator == 1

    def __reduce(self):
        gcd_value = gcd(self.numerator, self.denominator)

        self.numerator //= gcd_value
        self.denominator //= gcd_value

    def __mul__(self, other):
        num = self.numerator * other.numerator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __imul__(self, other):
        self.numerator *= other.numerator
        self.denominator *= other.denominator
        return self

    def __float__(self):
        return float(self.numerator / self.denominator)

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
