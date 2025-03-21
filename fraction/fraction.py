from math import gcd


class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("The denominator is 0")

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
        if isinstance(other, Fraction):
            nom = self.numerator * other.numerator
            den = self.denominator * other.denominator
            return Fraction(nom, den)
        elif isinstance(other, int):
            nom = self.numerator * other
            dem = self.denominator
            return Fraction(nom, dem)
        else:
            return NotImplemented

    def __common(self, other, operator):
        nom = operator(self.numerator * other.denominator, other.numerator * self.denominator)
        dem = self.denominator * other.denominator
        return self.__class__(nom, dem)

    def __add__(self, other):
        return self.__common(other, lambda x, y: x + y)

    def __sub__(self, other):
        return self.__common(other, lambda x, y: x - y)

    def __imul__(self, other: "Fraction"):
        self.numerator *= other.numerator
        self.denominator *= other.denominator
        return self

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if other.numerator == 0:
            raise ZeroDivisionError("The numerator is 0")

        return self.__mul__(Fraction(other.denominator, other.numerator))

    def __float__(self):
        return float(self.numerator / self.denominator)

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
