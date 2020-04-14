from labyrinth import Labyrinth
from character import Character
import constants
import cli
import pygame_
import time


class Main:
    """Class that initializes labyrinth defines game logic"""

    def __init__(self):
        """Class constructor"""

        self.lab = Labyrinth('map.txt')
        macgyver = Character('M', 1, 3)
        guardian = Character('G', 13, 13)
        self.lab.set_character_position(macgyver)
        self.lab.set_character_position(guardian)
        self.lab.set_tool_positions(constants.TOOLS)

        view = pygame_.Pygame(*self.lab.get_size())
        # view = CLI()

        view.display_lab(self.lab.lablist)

        game_loop = True

        while game_loop:
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
                    game_loop = False
                    break
                elif move['event'] == 'LOSE':
                    view.lose()
                    game_loop = False
                    break


if __name__ == '__main__':
    Main()
