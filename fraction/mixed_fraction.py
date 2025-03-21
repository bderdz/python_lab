from typing import override

from fraction import Fraction


class MixedFraction(Fraction):
    @override
    def __str__(self):
        if self.is_integer():
            return f"{self.numerator}"

        whole = self.numerator // self.denominator
        if whole == 0:
            return super().__str__()

        rest = self.numerator % self.denominator
        return f"{whole} {rest}/{self.denominator}"
