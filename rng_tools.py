"""
This class will handle adding restrictions/requirements to random number generation.
"""
import random


# Here we will have our rng options enumerated in an easier-to-read manner
INTEGERS = 1
RATIONALS = 2
REALS = 3

# currently, allows for nonzero integers from -10 to 10
NUMBER_RANGE = [*range(1, 10)] + [*range(-10, 0)]


def lsys_generator(choice, vals):
    """
    This will generate random numbers to fill in the coefficients and constants for a solvable
    linear system, according to the specified constraints
    """

    if choice == INTEGERS:
        # first, we generate random numbers for each of the coefficients/constants
        for key in vals:
            vals[key] = random.choice(NUMBER_RANGE)

    if choice == RATIONALS:
        print("Coming soon.")

    return vals
