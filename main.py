""" -tc- Ajouter une docstring."""

# -tc- Attention à la PEP8, ordonner les import correctement
from labyrinth import Labyrinth
from character import Character
import constants
import cli
import pygame_
import time

# -tc- Je séparerais initialisation (méthode __init__) et démarrage du jeu (dans une méthode run ou start)
# -tc- sinon utiliser une fonction main()
class Main:
    """Class that initializes labyrinth defines game logic"""

    def __init__(self):
        """Class constructor"""

        self.lab = Labyrinth('map.txt')
        # -tc- Même classe pour MacGyver et Murdoc? MacGyver peut se déplacer, pas Murdoc
        macgyver = Character('M', 1, 3) # -tc- Attention, il me semble plus logique que la position de départ de MacGyver soit définie dans map.txt
        guardian = Character('G', 13, 13) # -tc- il me semble plus logique que la position finale soit définie dans map.txt
        self.lab.set_character_position(macgyver)
        self.lab.set_character_position(guardian)
        self.lab.set_tool_positions(constants.TOOLS)

        view = pygame_.Pygame(*self.lab.get_size())
        # view = CLI() # -tc- jeu en CLI pas possible. Votre classe Labyrinthe dépend de pygame

        view.display_lab(self.lab.lablist)

        game_loop = True

        while game_loop:
            # -tc- attention à cadencer votre boucle 30-40 tours par second à l'aide de pygame.time.Clock
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
                    break # -tc- si game_loop = False, éviter le break
                elif move['event'] == 'LOSE':
                    view.lose()
                    game_loop = False # -tc- si game_loop = False, éviter le break
                    break


if __name__ == '__main__':
    Main()
