from labyrinth import *
from constants import TOOLS


class CLI:
    """Class that defines CLI init"""

    DIRECTIONS = {'Z': 'UP',
                  'Q': 'LEFT',
                  'S': 'DOWN',
                  'D': 'RIGHT'}

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

        direction = input("Select direction 'Z, Q, S or D' : ").upper()
        if direction == "X":
            return None
        elif direction in ['Z', 'Q', 'S', 'D']:
            return list(self.DIRECTIONS[direction])

        print("Please enter a valid direction")
        return self.get_direction()



