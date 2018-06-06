def hcf(x, y):
    while (y):
        x, y = y, x % y
    return x


def make_fraction(value):
    if isinstance(value, int):
        value = Fraction(value, 1)
    return value


class Fraction():
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def reduce(self):
        factor = self.hcf()
        if factor == 1:
            result = self
        else:
            result = Fraction(self.numerator//factor, self.denominator//factor)
        if result.denominator == 1:
            return result.numerator
        if result.denominator < 0:
            result = Fraction(-result.numerator, -result.denominator)
        return result

    def hcf(self):
        return hcf(self.numerator, self.denominator)

    def __add__(self, other):
        other = make_fraction(other)
        return Fraction(self.numerator*other.denominator + self.denominator*other.numerator,
                        self.denominator*other.denominator).reduce()

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        return self + -other

    def __neg__(self):
        return Fraction(-self.numerator, self.denominator)

    def __mul__(self, other):
        other = make_fraction(other)
        return Fraction(self.numerator*other.numerator, self.denominator*other.denominator).reduce()

    def __rmul__(self, other):
        return self*other

    def __truediv__(self, other):
        return Fraction(self.numerator*other.denominator, self.denominator*other.numerator).reduce()

    def __rdiv__(self, other):
        return Fraction(self.denominator*other, self.numerator).reduce()

    def __repr__(self):
        return 'Fraction(%d/%d)' % (self.numerator, self.denominator)

print(Fraction(1,2)*2)