import random as r

MACGYVER = 'M'
TOOLS = [
    'N',  # Needle
    'T',  # Tube
    'E'  # Ether
]
GUARDIAN = 'G'
FIRST_LINE = 1

state = {'labyrinth': None,
         'picked_tools': [],
         'game_running': True
         }


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


state['labyrinth'] = lab_surface('map.txt')


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


# Initialization
Y_MAC_POS = pick_random_position(state['labyrinth'], FIRST_LINE)
set_position(state['labyrinth'], FIRST_LINE, Y_MAC_POS, MACGYVER)

X_GUARDIAN_POS = len(state['labyrinth']) - 2  # Second to last line
Y_GUARDIAN_POS = pick_random_position(state['labyrinth'], X_GUARDIAN_POS)
set_position(state['labyrinth'], X_GUARDIAN_POS, Y_GUARDIAN_POS, GUARDIAN)

set_tool_positions(state['labyrinth'])


# Game loop
while state['game_running']:
    lab = state['labyrinth']

    lab_printer(lab)
    direction = input("Select direction 'Z, Q, S or D' : ")
    if direction not in ['Z', 'Q', 'S', 'D']:
        print("Please enter a valid direction")
        continue

    x1, y1 = get_macgyver_position(lab)  # Present Mac Gyver position

    # https://stackoverflow.com/questions/60208/replacements-for-switch-statement-in-python
    x2, y2 = {
        'Z': (x1 - 1, y1),
        'Q': (x1, y1 - 1),
        'S': (x1 + 1, y1),
        'D': (x1, y1 + 1)
        }[direction]                  # Future Mac Gyver position

    if lab[x2][y2] in TOOLS:
        state['picked_tools'].append(lab[x2][y2])

    if lab[x2][y2] == ' ' or lab[x2][y2] in TOOLS:
        lab[x2][y2] = MACGYVER
        lab[x1][y1] = ' '
    else:
        print("Mac Gyver cannot go through walls !")
        continue

    if GUARDIAN in [lab[x2 - 1][y2], lab[x2 + 1][y2], lab[x2][y2 + 1], lab[x2][y2 - 1]]:
        if len(state['picked_tools']) == len(TOOLS):
            print("Congratulation, you win!")
        else:
            print("Sorry, but you died!")
        state['game_running'] = False
