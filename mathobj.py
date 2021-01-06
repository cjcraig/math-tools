"""
This module will contain classes for mathematical objects that need their own methods and displays.
For example, a number in simple-radical form should have ways to display
"""
from math import floor


class RadicalNum:

    # TODO unfinished method
    def radform(input_number):
    """
    This function takes in a number, and returns it in simple radical form.
    """
    # Output format: [integer,radical]
    outpair = [1, 1]
    root = input_number**0.5

    # If we have a perfect square, might as well just return the root
    if root*root == input_number:
        outpair[0] = root
        return outpair

    # First, we need to extract any perfect square factor
    square_factors = []

    for i in range(4, floor(input_number/2), 1):
        if input_number % i == 0 and i*i == i**0.5:
            square_factors.append(i)
