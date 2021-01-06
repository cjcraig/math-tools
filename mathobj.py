"""
This module will contain classes for mathematical objects that need their own methods and displays.
For example, a number in simple-radical form should have ways to display
"""

from math import ceil
from fractions import Fraction


class RadicalNum:
    """
    Class to handle numbers in simple radical form.
    """

    def __init__(self, input_number):
        # We should make sure we are starting with a rational number
        if not isinstance(input_number, (Fraction, int)):
            raise TypeError(
                "Simple radical form only makes sense applied to rationals!")

        self.ratpart = Fraction(input_number)

        self.radpart = 1

    # TODO finish this method

    def radform(self):
        """
        This function takes in a number, and returns it in simple radical form.
        """

        # Output format: [integer,radical]
        outpair = [1, 1]
        root = self.number**0.5

        # If we have a perfect square, might as well just return the root
        if root*root == self.number:
            outpair[0] = root
            return outpair

        # First, we need to extract any perfect square factor
        square_factors = []

        # Here we will run through the factors of numerator and denominator,
        # reducing by repeated factors

        return outpair


def get_prime_factors(number):
    """
    Method to get a list of factors, repeated values allowed.
    """
    factor_list = []
    while number % 2 == 0:
        factor_list.append(2)
        number = number/2

    for factor in range(3, ceil(number/2), 2):
        while number % factor == 0:
            factor_list.append(factor)
            number = number/factor
        if number == 1:
            break
    if number != 1:
        factor_list.append(number)
    return factor_list
