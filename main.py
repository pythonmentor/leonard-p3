# import os
import random


def lab_surface(path):
    """Function that defines labyrinth structure"""
    lab = []
    with open(path, 'r') as file:
        for line in file:
            result = line.replace('/', ' ')
            result = result.replace('\n', '')
            result = list(result)
            lab.append(result)
    return lab


def lab_printer(val):
    """
    Function that prints your labyrinth
    :param val: List[List[str]]
    :return: None
    """
    for i in val:
        result = ''.join(i)
        print(result)
    # Ou :
    # r = map(lambda x: ''.join(x), val)
    # r = '\n'.join(r)


LABYRINTH = lab_surface('map.txt')
MACGYVER = 'M'
FIRST_LINE = 1


def pick_random_start_position(lab, x):
    """
    Function that picks a random empty cell from a row in column index in LABYRINTH
    :param lab: List[List[str]]
    :param x: int
    :return: int
    """
    possible_start_positions = []
    for i, e in enumerate(lab[x]):
        if e == ' ':
            possible_start_positions.append(i)
    picked_position = random.choice(possible_start_positions)
    return picked_position


def set_start_position(x, y):
    """
    Function that set Mac Gyver start position in the given empty cell
    from 'pick_random_start_position' function
    :param x: int
    :param y: int
    :return: None
    """
    LABYRINTH[x][y] = MACGYVER


Y_POS = pick_random_start_position(LABYRINTH, FIRST_LINE)
set_start_position(FIRST_LINE, Y_POS)
lab_printer(LABYRINTH)

# start = lab.replace(randrange(len(lab[1])+1), MACGYVER)
# print(start)


# class MacGyver:
#     """ Class that defines Mac Gyver movements """
#     M = MacGyver()
#     start_position = randrange[lab[1]]
#
#     def __init__(self):
#         self.start = start_position
#
#
# class Guardian:
#     """ Class that defines Guardian position """
