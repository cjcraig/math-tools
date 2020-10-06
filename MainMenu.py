import random

print('Welcome! Please select an option below...')
startMenu()
choice  = input()
switcher(choice)


def startMenu():
    print(
        '1. Create two-variable system\n'+ \
        '2. More to be added...'\
    )

def switcher(inbound):
    if(inbound == 1):
        twovarsys()


#method for creating two equations in two variables, format
#ax+by=e
#cx+dy=f
def twovarsys():
    #initialize array to store a,b,c,d,e,f in that order
    coeffs = [0,0,0,0,0,0]
    #initialize array to store x,y in that order
    solns=[0,0]
    print("Please select first option:")
    print("Set of solutions desired?" + \
        "1. Integer Solutions"+\
        "2. Rational Solutions"+\
        "3. Real Solutions")
    selection = input()

    if(selection==1):
        return 0
    elif(selection==2):
        return 0
    elif(selection==3):
        return 0
    else:
        print("Invalid option selected")
        return 0

