# import os
# from random import randrange
# from typing import List, Any


def lab_surface(path):
    """ Function that defines labyrinth structure """
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
    :param val: List[List[char]]
    :return: None
    """
    for i in val:
        result = ''.join(i)
        print(result)
    # Ou :
    # r = map(lambda x: ''.join(x), val)
    # r = '\n'.join(r)


LAB = lab_surface('map.txt')

lab_printer(LAB)


# class MacGyver:
#     """ Class that defines Mac Gyver movements """
#     M = MacGyver()
#     start_position = randrange[LAB[1]]
#
#     def __init__(self):
#         self.start = start_position
#
#
# class Guardian:
#     """ Class that defines Guardian position """
