"""
This module will contain classes for mathematical objects that need their own methods and displays.
For example, a number in simple-radical form should have ways to display
"""

from math import ceil
from fractions import Fraction


class RadicalNum:
    """
    Class to handle numbers in simple radical form.
    Numbers are stored as a pair of values rat_part and rad_part,
    where rat_part is the Fraction value outside of the square root,
    and rad_part is the integer within the square root.
    """

    def __init__(self, input_number):
        # We should make sure we are starting with a rational number
        if not isinstance(input_number, (Fraction, int)):
            raise TypeError(
                "Simple radical form only makes sense applied to rationals!")

        # To start, we assume the entire given number is inside the square root.
        # Other functions will fix this.
        self.rat_part = 1
        self.rad_part = Fraction(input_number)
        self.simplify()

    def __str__(self):
        rootstring = ''
        if self.rad_part != 1:
            rootstring = '*sqrt('+str(self.rad_part)+')'

        return rational_string(self.rat_part) + rootstring

    def __mul__(self, other):
        """
        Multiplies together according to the process in radical_multiplication,
        overloading the * operator
        """
        # need to handle a few cases:

        # rational * rational
        if(isinstance(other, RadicalNum)):
            return self.radical_multiplication(self, other)
        # rational * fraction or rational * integer
        if(isinstance(other, Fraction) or isinstance(other, int)):
            # in this case need to convert to a radical number before multiplying
            return self.radical_multiplication(self, RadicalNum(other*other))

    def __rmul__(self, other):
        return self.__mul__(other)

    def simplify(self):
        """
        This function takes in a number, and returns it in simple radical form.
        The radical part will represent the square root of an integer,
        and the radical part will have no square factors.
        """
        # Outpair format: [rational part,radical part]
        outpair = [1, 1]

        # We will handle the top and bottom factors separately,
        # since denominator radicals need to be moved.
        # Note each of these is a pair of the form [integer part, radical part]
        top_vals = integer_root(self.rad_part.numerator)
        bot_vals = integer_root(self.rad_part.denominator)

        # For simple radical form, we will
        # remove square roots from the denominator by multiplying...

        # Multiply the radical from bottom into top
        top_vals[1] *= bot_vals[1]
        # Multiply radical from bottom into bottom
        # (squaring the radical making it integer, and removing the radical)
        bot_vals[0] *= bot_vals[1]
        bot_vals[1] = 1

        # Now bring it all together:
        self.rat_part = Fraction(top_vals[0], bot_vals[0])
        self.rad_part = top_vals[1]
        return outpair

    @staticmethod
    def radical_multiplication(num1, num2):
        """
        Multiplies two radical numbers of the type RadicalNum.
        Static here so it can be used without * needed (for whatever reason)
        """
        if not isinstance(num1, RadicalNum) or not isinstance(num2, RadicalNum):
            raise TypeError(
                "radical_multiplication is only for two objects of type RadicalNum")

        # First we find the product of the non-rooted parts
        prod = num1.rat_part * num2.rat_part
        # now we square it to put it 'back' into a square root
        prod = prod * prod
        # now multiply the radical we just made with the radicals from each number
        prod = prod * num1.rad_part * num2.rad_part

        return RadicalNum(prod)


def integer_root(in_root):
    """
    Takes in an integer and returns it's square root in simple radical form.
    Example: sqrt[540] = sqrt[2*2*3*3*3*5] = 2*3*sqrt[(2*2*2*3*3*3*5) / (2^2 * 3^2)] = 6*sqrt[15]
    """
    # First, get our list of factors
    factors = get_prime_factors(in_root)

    # This will store
    out_root = 1

    i = 0
    while i < len(factors)-1:
        # Check if there is a repeated factor; if so, we can take the square root of that pair
        if factors[i] == factors[i+1]:
            out_root *= factors[i]
            del factors[i+1]
            del factors[i]
            continue
        i += 1

    # At this point, repeated roots will have been reduced
    # and multiplied to the 'front' of the radical.
    # However, we have not reduced the inside of the radical! We need to do that now.
    # Since a factor outside of the radical was 'rooted',
    # we need to re-square when reducing the interior.
    # We could have reduced the interior as we removed factors,
    # but this way we only need to do one division and one squaring instead of many.
    in_root = int(in_root / (out_root**2))

    return [out_root, in_root]


def rational_string(number):
    """
    Turns numbers into strings, and converts fractions with denominator 1 into an integer.
    """
    output = str(number)
    if isinstance(number, Fraction):
        if number.denominator == 1:
            output = str(number.numerator)

    return output


def get_prime_factors(number):
    """
    Method to get a list of factors given an integer, repeated values allowed.
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
