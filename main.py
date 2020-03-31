from labyrinth import *
from character import *
from constants import *


class CLI:
    """Class that defines CLI init"""

    def display_lab(self, lab):
        """Function that displays labyrinth"""

        for i in lab:
            result = ''.join(i)
            print(result)
            # Ou :
            # r = map(lambda x: ''.join(x), val)
            # r = '\n'.join(r)

    def get_direction(self):
        """Function that set a direction in labyrinth"""

        direction = input("Select direction 'Z, Q, S or D' : ")
        if direction not in ['Z', 'Q', 'S', 'D']:
            print("Please enter a valid direction")
            return None
        else:
            return direction


class Pygame:
    """Class that defines Pygame initialization """

    def __init__(self):
        pass

    def display_lab(self, lab):
        """Function that displays labyrinth"""

        for i in lab:
            result = ''.join(i)
            print(result)
            # Ou :
            # r = map(lambda x: ''.join(x), val)
            # r = '\n'.join(r)

    def get_direction(self):
        """Function that set a direction in labyrinth"""

        direction = input("Select direction 'Z, Q, S or D' : ")
        if direction not in ['Z', 'Q', 'S', 'D']:
            print("Please enter a valid direction")
            return None
        else:
            return direction


class Main:
    """Class that defines game logic"""

    def __init__(self):
        self.view = Pygame()
        self.lab = Labyrinth('map.txt')
        self.macgyver = Character('M')
        self.guardian = Character('G')
        self.view = CLI()
        self.lab.set_random_position_on_line(self.macgyver, FIRST_LINE)
        self.lab.set_random_position_on_line(self.guardian,
                                             self.lab.get_number_of_lines() - 2)
                                             # Second to last line
        self.lab.set_tool_positions(TOOLS)
        self.is_running = True
        self.keyboard = {'Z': 'UP',
                         'Q': 'LEFT',
                         'S': 'DOWN',
                         'D': 'RIGHT'}

        while self.is_running:
            self.view.display_lab(self.lab.lab)
            direction = input("Select direction 'Z, Q, S, D': ")
            if direction not in ['Z', 'Q', 'S', 'D']:
                print("Please enter a valid direction")
                continue
            move = self.lab.move_macgyver(self.macgyver,
                                          self.guardian,
                                          TOOLS,
                                          self.keyboard[direction])
            if not move:
                self.is_running = False


if __name__ == '__main__':
    Main()
