"""
This class will handle adding restrictions/requirements to random number generation.
"""
import random
from fractions import Fraction


# Here we will have our rng options enumerated in an easier-to-read manner
INTEGERS = 1
RATIONALS = 2
REALS = 3

# currently, allows for nonzero integers from -10 to 10
NUMBER_RANGE = [*range(1, 10)] + [*range(-10, 0)]


def spec_generator(choice, vals):
    """
    This will generate random numbers to fill in the coefficients and constants for math problems, 
    according to the specified constraints.
    """

    if choice == INTEGERS:
        for key in vals:
            vals[key] = random.choice(NUMBER_RANGE)

    if choice == RATIONALS:
        for key in vals:
            vals[key] = Fraction(random.choice(
                NUMBER_RANGE), random.choice(NUMBER_RANGE))

    return vals
