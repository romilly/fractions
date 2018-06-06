"""
Test the Fraction class

These tests *will not run* under MicroPython, since they require
the unittest and hamcrest modules
"""
from unittest import TestCase

from hamcrest import assert_that, equal_to
from hamcrest.core.base_matcher import BaseMatcher

from fractions import Fraction


class FractionMatcher(BaseMatcher):
    def describe_to(self, description):
        description.append('a Fraction(%d/%d)' % (self._fraction.numerator, self._fraction.denominator))

    def __init__(self, num, denom):
        self._fraction = Fraction(num, denom)

    def _matches(self, item):
        if not isinstance(item, Fraction):
            return False
        return self._fraction.numerator == item.numerator and self._fraction.denominator == item.denominator


def equals_fraction(num, denom):
    return FractionMatcher(num, denom)


class FractionTest(TestCase):
    def test_reduces_to_lcd(self):
        assert_that(Fraction(2,4).reduce(), equals_fraction(1,2))
        assert_that(Fraction(2,5).reduce(), equals_fraction(2,5))
        assert_that(Fraction(2,2).reduce(), equal_to(1))

    def test_addition(self):
        assert_that(Fraction(1,2)+Fraction(1,3), equals_fraction(5,6))
        assert_that(Fraction(1,2)+Fraction(1,2), equal_to(1))
        assert_that(1+Fraction(1,2), equals_fraction(3,2))

    def test_subtraction(self):
        assert_that(Fraction(1,2)-Fraction(1,3), equals_fraction(1,6))

    def test_multiplication(self):
        assert_that(Fraction(1,2)*Fraction(1,3), equals_fraction(1,6))
        assert_that(Fraction(1,2)*2, equal_to(1))
        assert_that(2*Fraction(1,2), equal_to(1))

    def test_division(self):
        assert_that(Fraction(1,2) / Fraction(2,3), equals_fraction(3,4))
        assert_that(Fraction(1,2) / 1, equals_fraction(1,2))
        assert_that(Fraction(1,2) / Fraction(1,2), equal_to(1))









