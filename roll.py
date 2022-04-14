""" Roll Da Dice
----------------------------------------
"""
from sys import argv
import random
def ShowHelp():
    print( 'Roll da Dice')
    print( '')
    print( 'Usage:')
    print( 'roll.py [x]d[y] [OPTIONS]')
    print( '')
    print( 'Options:')
    print( '-n [numbers]\t roll n times the dice(s)')
    print( '-h\t\tShow this help message')
    print( '')
    print( 'Example:')
    print( 'python roll.py 3d6')
    print( 'python roll.py 3d6 -n 100')
    print( '')
    exit()
def rollthadice(d):
    nbDice =int(d[0:1])
    nbFace =int(d[2:])
    output = []
    while nbDice > 0:
        roll = random.randint(1, nbFace)
        output.append(roll)
        nbDice-=1
    print(output)
if __name__ == '__main__':
    if len(argv) == 1:
        ShowHelp()
    if argv[1] == '-h':
        ShowHelp()
    else:
        if len(argv) >2 and argv[2] == '-n':
            dice = argv[1]
            num = int(argv[3])
            print('Roll\'d da Dices')
            while num > 0:
                rollthadice(dice)
                num-=1
        else:
            dice = argv[1]
            print('Roll\'d da Dice')
            rollthadice(dice)
