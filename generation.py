"""
This module will contain the functions that generate problems and solutions.
"""

import os
from fractions import Fraction
import rng_tools


# Nice, consistent newline characters
NEWLINE = os.linesep


def twovarsys():
    """
    This method will provide the user with randomized two linear equations in two variables.
    ax+by=e
    cx+dy=f
    """
    # initialize array to store coefficients for
    # ax+by=e |and| cx+dy=f
    coeffs = {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0,
        'e': 0,
        'f': 0
    }

    # initialize array to store x,y in that order
    solns = [0, 0]
    selection = 1
    while int(selection) > 0:
        # prompt the user for what types of solutions are desired
        print("Please select first option (integer inputs only, please):")
        print("Set of solutions desired?" + NEWLINE +
              "1. Integer Solutions" + NEWLINE +
              "2. Rational Solutions" + NEWLINE +
              "Enter anthing else to exit.")
        selection = input()

        # if we don't get an integer input, don't try everything else
        if (not selection.isnumeric()) or (int(selection) > 2):
            selection = -1
            continue

        # initialize loop control variable
        finished = False

        if int(selection) == 1:

            while not finished:
                # first, we generate random numbers for each of the coefficients/constants
                coeffs = rng_tools.spec_generator(rng_tools.INTEGERS, coeffs)

                # we'll use determinant a lot, might as well only compute it once
                det = coeffs['a']*coeffs['d']-coeffs['b']*coeffs['c']

                # Next, we check for nonzero determinant of {{a,b},{c,d}}. If fails, regenerate.
                if det == 0:
                    continue

                # now check for divisibility, since we want integer solutions
                if (
                    ((coeffs['d']*coeffs['e'] - coeffs['b']*coeffs['f']) % det) != 0 or
                    ((coeffs['a']*coeffs['f'] -
                      coeffs['c']*coeffs['e']) % det) != 0
                ):
                    continue

                # if we made it here, it means we have integer solutions,
                # so we can output the information:
                solns[0] = (coeffs['d']*coeffs['e'] -
                            coeffs['b']*coeffs['f']) / det
                solns[1] = (coeffs['a']*coeffs['f'] -
                            coeffs['c']*coeffs['e']) / det
                finished = True

            print("System is: " +
                  str(coeffs['a']) + "x + " + str(coeffs['b']) + "y = "+str(coeffs['e']) +
                  NEWLINE + str(coeffs['c']) + "x + " +
                  str(coeffs['d']) + "y = "
                  + str(coeffs['f']))
            print("Solution is:" + "x = " +
                  str(solns[0]) + NEWLINE + "y = "
                  + str(solns[1]) + NEWLINE
                  + "=====================================")

            twovarsys()

        # if user wants rational solutions
        elif int(selection) == 2:
            # commence loop until we get what we want
            while not finished:
                # first, we generate random numbers for each of the coefficients/constants
                coeffs = rng_tools.spec_generator(rng_tools.RATIONALS, coeffs)

                # we'll use determinant a lot, might as well only compute it once
                det = Fraction(
                    Fraction(coeffs['a']*coeffs['d']) - Fraction(coeffs['b']*coeffs['c']))

                # Next, we check for nonzero determinant of {{a,b},{c,d}}. If fails, regenerate.
                if det == 0:
                    continue

                # now check for divisibility, since we want rational solutions
                # only just copied it from the unfinished integer one,
                # need to change these conditions here, maybe coeffs also?
                if (
                    (coeffs['d']*coeffs['e'] - coeffs['b']*coeffs['f'] % det) != 0 and
                    (coeffs['a']*coeffs['f'] -
                     coeffs['c']*coeffs['e'] % det) != 0
                ):
                    continue

                # if we made it here, it means we have integer solutions,
                # so we can output the information:
                solns[0] = Fraction((coeffs['d']*coeffs['e'] -
                                     coeffs['b']*coeffs['f']) / det)
                solns[1] = Fraction((coeffs['a']*coeffs['f'] -
                                     coeffs['c']*coeffs['e']) / det)
                finished = True

            print("System is: " + str((coeffs['a'])) + "x + " + str(coeffs['b']) + "y = "
                  + str(coeffs['e'])
                  + NEWLINE + str(coeffs['c']) + "x + " +
                  str(coeffs['d']) + "y = "
                  + str(coeffs['f']))
            print("Solution is:" + NEWLINE + "x = " +
                  str((solns[0])) + NEWLINE + "y = " + str((solns[1])))

        else:
            selection = -1
            continue

    print("Thank you for using this program, please come again soon!")
    return 0


def quadratics():
    """
    This method will create problems that involve second degree polynomials
    ax^2+bx+c=0
    """
    coeffs = {
        'a': 0,
        'b': 0,
        'c': 0
    }

    selection = 1

    while int(selection) > 0:

        roots = []

        # prompt the user for what types of solutions are desired
        print("Set of solutions desired?" + NEWLINE +
              "1. Integer Coefficients and Rational Solutions" + NEWLINE +
              "2. Rational Coefficients and Real Solutions" + NEWLINE +
              # TODO allow for mismatch of solution type and coefficient type
              # TODO allow decisions between displaying roots as decimals and radicals
              "Enter larger number to exit.")
        selection = input()

        if int(selection) < 1:
            selection = -1
            break
        if int(selection) > 2:
            selection = -1
            break

        print(
            "Number of real roots desired?" +
            "(0, 1, or 2, note that 0 will result in complex solutions)")
        rootnum = input()

        finished = False

        while not finished:
            # first we generate random coefficients
            if int(selection) == 1:
                coeffs = rng_tools.spec_generator(
                    rng_tools.INTEGERS, coeffs)

            elif int(selection) == 2:
                # first we generate random rational coefficients
                coeffs = rng_tools.spec_generator(
                    rng_tools.RATIONALS, coeffs)

            # calculate discriminant: b^2 - 4ac
            disc = (coeffs['b']*coeffs['b']) - \
                (4 * coeffs['a'] * coeffs['c'])

            if int(rootnum) == 0:
                # if we want no real roots
                finished = (disc < 0)
            elif int(rootnum) == 1:
                # one real root means discriminant is zero
                finished = (disc == 0)
            else:
                # two real roots means positive discriminant
                finished = (disc > 0)

        # TODO force rational output?
        roots.append(((-1)*coeffs['b'] + disc**(0.5))/(2*coeffs['a']))
        roots.append(((-1)*coeffs['b'] - disc**(0.5))/(2*coeffs['a']))

        # TODO properly sign b and c
        print("Polynomial is: " + str(coeffs['a']) + "x^2 + " +
              str(coeffs['b']) + "x + " + str(coeffs['c']))

        print("Factored form: " + str(coeffs['a']) +
              "(x" + str_rt_sub(str(roots[0])) + ")(x"+str_rt_sub(str(roots[1]))+")")
        print(NEWLINE)

    print("Ending program...")


def str_rt_sub(inbound_num):
    """
    Method to format subtracting roots. If the incoming number is already negative,
    we should add the positive of the root. Otherwise, we want to subtract.
    """

    if inbound_num[0] == '-':
        return inbound_num.replace('-', '+')

    return '-'+inbound_num
