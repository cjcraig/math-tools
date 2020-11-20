"""
This is the starting/main location for starting the math generating methods.
"""

from fractions import Fraction
import generation


def start_menu():
    """
    Displays all currently available options from the start of main menu
    """
    print(
        '1. Create two-variable system' + generation.NEWLINE +
        '2. Create quadratic polynomial...' + generation.NEWLINE +
        '3+. Not yet implemented.'
    )


def switcher(inbound):
    """
    This method will take in the input from the main menu,
    and direct it to the appropriate method
    """
    #print("inbound is: "+inbound)
    if int(inbound) == 1:
        print("Selected two-variable system..." + generation.NEWLINE)
        generation.twovarsys()

    elif int(inbound) == 2:
        print("Selected quadratic..." + generation.NEWLINE)
        generation.quadratics()


print('Welcome! Please select an option below...')
start_menu()
choice = input()
switcher(choice)
