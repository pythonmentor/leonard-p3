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

# Labyrinth = List[List[str]]

# Position = Tuple[int, int]


def lab_surface(path):
    """Function that defines labyrinth structure"""
    lab = []
    with open(path) as file:
        for line in file:
            result = line.replace('/', ' ')
            result = result.replace('\n', '')
            result = list(result)
            lab.append(result)
    return lab


LABYRINTH = lab_surface('map.txt')


# class CLI:
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


def pick_random_position(lab, x):
    """
    Function that picks a random empty cell from a row in column index in LABYRINTH
    :param lab: List[List[str]]
    :param x: int
    :return: int
    """
    possible_positions = []
    for index, element in enumerate(lab[x]):
        if element == ' ':
            possible_positions.append(index)
    picked_position = r.choice(possible_positions)
    return picked_position


def set_position(lab, x, y, character):
    """
    Function that set a character position in the given empty cell
    from 'pick_random_start_position' function
    :param lab: List[List[str]]
    :param x: int
    :param y: int
    :param character: str
    :return: None
    """
    lab[x][y] = character


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


def set_tool_positions(lab):
    """
    Function that sets tools positions in the labyrinth
    :param lab: List[List[str]]
    :return: None
    """
    for tool in TOOLS:
        x, y = pick_random_tool_positions(lab)
        lab[x][y] = tool


def get_macgyver_position(lab):
    """
    "Function that returns Mac Gyver position"
    :param lab: List[List[str]]
    :return: Tuple or None
    """
    for x, line in enumerate(lab):
        for y, element in enumerate(line):
            if element == MACGYVER:
                return x, y
    return None


def move_macgyver(lab):
    """
    Function that moves Mac Gyver in the labyrinth
    :param lab: List[List[str]]
    :return: List[List[str]]
    """
    direction = input("Select direction 'Z, Q, S or D' : ")
    x, y = get_macgyver_position(lab)
    if direction == 'Z' and (lab[x - 1][y] == ' ' or lab[x - 1][y] in TOOLS):
        lab[x][y] = ' '
        lab[x - 1][y] = MACGYVER
    elif direction == 'Q' and (lab[x][y - 1] == ' ' or lab[x][y - 1] in TOOLS):
        lab[x][y] = ' '
        lab[x][y - 1] = MACGYVER
    elif direction == 'S' and (lab[x + 1][y] == ' ' or lab[x + 1][y] in TOOLS):
        lab[x][y] = ' '
        lab[x + 1][y] = MACGYVER
    elif direction == 'D' and (lab[x][y + 1] == ' ' or lab[x][y + 1] in TOOLS):
        lab[x][y] = ' '
        lab[x][y + 1] = MACGYVER
    else:
        print("Mac Gyver cannot go through walls !")
    return lab


# def win_game(x, y, lab):
#     x, y = get_macgyver_position(lab)
#     if TOOLS not in lab and lab[x-1][y] == GUARDIAN:
#         print("Congratulations, you win!")
#     elif TOOLS not in lab and lab[x][y - 1] == GUARDIAN:
#         print("Congratulations, you win!")
#         elif lab[x + 1][y] == GUARDIAN:
#             print("Congratulations, you win!")
#         elif lab[x][y + 1] == GUARDIAN:
#             print("Congratulations, you win!")






Y_MAC_POS = pick_random_position(LABYRINTH, FIRST_LINE)
set_position(LABYRINTH, FIRST_LINE, Y_MAC_POS, MACGYVER)

X_GUARDIAN_POS = len(LABYRINTH) - 2  # Second to last line
Y_GUARDIAN_POS = pick_random_position(LABYRINTH, X_GUARDIAN_POS)
set_position(LABYRINTH, X_GUARDIAN_POS, Y_GUARDIAN_POS, GUARDIAN)


set_tool_positions(LABYRINTH)

lab_printer(LABYRINTH)

move_macgyver(LABYRINTH)

lab_printer(LABYRINTH)



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
