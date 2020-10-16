"""
This is the starting/main location for starting the math generating methods.
"""

import os
import rng_tools

NEWLINE = os.linesep


def start_menu():
    """
    User will start here to make a selection of which tool they wish to initialize
    """
    print(
        '1. Create two-variable system\n' +
        '2. More to be added...'
    )


def switcher(inbound):
    """
    This method will take in the input from the main menu,
    and direct it to the appropriate method
    """
    #print("inbound is: "+inbound)
    if int(inbound) == 1:
        print("Selected two-variable system...")
        twovarsys()


# method for creating two equations in two variables, format
# ax+by=e
# cx+dy=f
def twovarsys():
    """
    This method will provide the user with randomized two linear equations in two variables
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
              "3. Real Solutions" + NEWLINE +
              "Enter anthing else to exit.")
        selection = input()

        # if we don't get an integer input, don't try everything else
        if (not selection.isnumeric()) or (int(selection) > 3):
            selection = -1
            continue

        # initialize loop control variable
        finished = False
        if int(selection) == 1:

            while not finished:
                # first, we generate random numbers for each of the coefficients/constants
                coeffs = rng_tools.lsys_generator(rng_tools.INTEGERS, coeffs)

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
        elif selection == 2:
            # commence loop until we get what we want
            while not finished:
                # first, we generate random numbers for each of the coefficients/constants
                coeffs = rng_tools.lsys_generator(rng_tools.INTEGERS, coeffs)

                # we'll use determinant a lot, might as well only compute it once
                det = coeffs['a']*coeffs['d']-coeffs['b']*coeffs['c']

                # Next, we check for nonzero determinant of {{a,b},{c,d}}. If fails, regenerate.
                if det == 0:
                    continue

                # now check for divisibility, since we want rational solutions
                # TODO mostly integers, occasionally an "over 2" or "over 4", not really rationals.
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
                solns[0] = (coeffs['d']*coeffs['e'] -
                            coeffs['b']*coeffs['f']) / det
                solns[1] = (coeffs['a']*coeffs['f'] -
                            coeffs['c']*coeffs['e']) / det
                finished = True

            print("System is: " + str(coeffs['a']) + "x + " + str(coeffs['b']) + "y = "
                  + str(coeffs['e'])
                  + NEWLINE + str(coeffs['c']) + "x + " +
                  str(coeffs['d']) + "y = "
                  + str(coeffs['f']))
            print("Solution is:" + NEWLINE + "x = " +
                  str(solns[0]) + NEWLINE + "y = " + str(solns[1]))
            return 0
        elif selection == 3:
            return 0
        else:
            selection = -1
            continue

    print("Thank you for using this program, please come again soon!")
    return 0


print('Welcome! Please select an option below...')
start_menu()
choice = input()
switcher(choice)
