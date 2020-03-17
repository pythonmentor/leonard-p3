# import os
import random as r

MACGYVER = 'M'
TOOLS = [
    'N',  # Needle
    'T',  # Tube
    'E'  # Ether
]
GUARDIAN = 'G'
FIRST_LINE = 1
# LINE = r.randrange(2, 13)

# Labyrinth = List[List[str]]

# Position = Tuple[int, int]


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


LABYRINTH = lab_surface('map.txt')


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


def pick_random_start_position(lab, x):
    """
    Function that picks a random empty cell from a row in column index in LABYRINTH
    :param lab: List[List[str]]
    :param x: int
    :return: int
    """
    possible_start_positions = []
    for index, element in enumerate(lab[x]):
        if element == ' ':
            possible_start_positions.append(index)
    picked_position = r.choice(possible_start_positions)
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


def pick_random_tool_positions(lab):
    """
    Function that picks a random empty cell from a row in column index in LABYRINTH
    :param lab: List[List[str]]
    :return: Tuple[int, int]
    """
    possible_tool_positions = []
    for x, line in enumerate(lab):
        for y, element in enumerate(line):
            if element == ' ':
                possible_tool_positions.append((x, y))
    picked_position = r.choice(possible_tool_positions)
    return picked_position


# def set_tool_positions(x, y):
    # LABYRINTH[x][y] = TOOLS


pick_random_tool_positions(LABYRINTH)


Y_MAC_POS = pick_random_start_position(LABYRINTH, FIRST_LINE)
set_start_position(FIRST_LINE, Y_MAC_POS)

# Y_TOOLS_POS = pick_random_tool_position(LABYRINTH, LINE)
# set_tools_position(LINE, Y_TOOLS_POS)

# lab_printer(LABYRINTH)

# def move():

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
