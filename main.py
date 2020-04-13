from labyrinth import *
from character import *
from constants import TOOLS
from cli import CLI
from pygame_ import *


class Main:
    """Class that defines game logic"""

    def __init__(self):
        """Class constructor"""

        self.lab = Labyrinth('map.txt')
        macgyver = Character('M', 1, 3)
        guardian = Character('G', 13, 13)
        self.lab.set_character_position(macgyver)
        self.lab.set_character_position(guardian)
        self.lab.set_tool_positions(TOOLS)

        view = Pygame(*self.lab.get_size())
        view.display_lab(self.lab.lablist)

        while True:
            direction = view.get_direction()

            if direction is None:  # exit key pressed
                exit()

            for d in direction:
                move = self.lab.move_macgyver(macgyver,
                                              guardian,
                                              d)
                if move['event'] in ['CONTINUE', 'ADD_TOOL']:
                    view.display_lab(self.lab.lablist)
                elif move['event'] == 'NO_MOVE':
                    continue
                elif move['event'] == 'WIN':
                    view.win()
                    time.sleep(5)
                    exit()
                elif move['event'] == 'LOSE':
                    view.lose()
                    time.sleep(5)
                    exit()


if __name__ == '__main__':
    Main()
