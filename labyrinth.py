import random as r


class Labyrinth:
    """Class that defines a labyrinth, characterised by:
    - Mac Gyver, Guardian and tools positions
    - movements of Mac Gyver
    - logic to win or to lose"""

    def __init__(self, path):
        """Function that initializes a labyrinth"""

        self.lab = []
        with open(path) as file:
            for line in file:
                result = line.replace('/', ' ')
                result = result.replace('\n', '')
                result = list(result)
                self.lab.append(result)

    def get_random_position(self):
        """Function that gets a random empty cell from a row in column index in labyrinth"""

        possible_positions = []
        for x, line in enumerate(self.lab):
            for y, element in enumerate(line):
                if element == ' ':
                    possible_positions.append((x, y))
        return r.choice(possible_positions)

    def set_character_position(self, x, y, character):
        """Function that sets a character position in the given empty cell
        from 'get_random_position'"""

        self.lab[x][y] = character

    def set_random_position_on_line(self, character, line):
        """Function that sets a random position in a random empty cell
        for a given line"""

        possible_positions = []
        for y, element in enumerate(self.lab[line]):
            if element == ' ':
                possible_positions.append((line, y))
        x, y = r.choice(possible_positions)
        self.lab[x][y] = character.name

    def get_number_of_lines(self):
        """Function that returns the number of lines contained in labyrinth"""

        return len(self.lab)

    def set_tool_positions(self, tools):
        """Function that sets tools random positions"""

        for tool in tools:
            x, y = self.get_random_position()
            self.lab[x][y] = tool

    def get_character_position(self, character):
        """Function that return current character position"""

        for x, line in enumerate(self.lab):
            for y, element in enumerate(line):
                if element == character.name:
                    return x, y

    def move_macgyver(self, macgyver, guardian, tools, direction):
        """Function that allow macgyver to move in the labyrinth,
        accordinf to walls, guardian and tools positions"""

        position = self.get_character_position(macgyver)
        x, y = position
        if direction == 'UP':
            next_position = (x - 1, y)
        elif direction == 'DOWN':
            next_position = (x + 1, y)
        elif direction == 'LEFT':
            next_position = (x, y - 1)
        elif direction == 'RIGHT':
            next_position = (x, y + 1)

        x2, y2 = next_position
        element = self.lab[x2][y2]
        if element == ' ':
            self.lab[x2][y2] = macgyver.name
            self.lab[x][y] = ' '
        elif element in tools:
            tool = self.lab[x2][y2]
            macgyver.add_tool(tool)
            self.lab[x2][y2] = macgyver.name
            self.lab[x][y] = ' '
        elif element == guardian.name:
            if len(macgyver.tools) == len(tools):
                print("Congratulations, you win!")
            else:
                print("Sorry, but you died!")
            return False
        elif element == '#':
            print("Mac Gyver cannot go through walls!")
        return True
