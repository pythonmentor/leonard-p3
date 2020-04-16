""" -tc- Ajouter une docstring."""

# -tc- Attention au respect de la PEP8 dans les imports
import os
import pygame


class Pygame:
    """Class that defines Pygame initialization and displays labyrinth """

    DIRECTIONS = {pygame.K_UP: 'UP',
                  pygame.K_DOWN: 'DOWN',
                  pygame.K_LEFT: 'LEFT',
                  pygame.K_RIGHT: 'RIGHT'}

    def _resource_path(self, file):
        """Function to access resources"""

        return os.path.join('resource', file)

    def __init__(self, lines, columns):
        """Function to initialize Pygame"""

        pygame.init()
        self.window_size = (columns * 20, lines * 20)  # (x, y)
        self.screen_surface = pygame.display.set_mode(self.window_size)
        self.cambria_font = pygame.font.SysFont('Cambria', 30)

        # -tc- utiliser des sprites pour les objets, mac et le gardien me semblerait plus approprié dans un
        # -tc- design objet et simplifierais drastiquement votre code d'interface
        self.floor = pygame.image.load(self._resource_path('floor.png')).convert_alpha()
        self.wall = pygame.image.load(self._resource_path('wall.png')).convert_alpha()
        self.needle = pygame.image.load(self._resource_path('needle.png')).convert_alpha()
        self.tube = pygame.image.load(self._resource_path('tube.png')).convert_alpha()
        self.ether = pygame.image.load(self._resource_path('ether.png')).convert_alpha()
        self.macgyver = pygame.image.load(self._resource_path('MacGyver.png')).convert_alpha()
        self.guardian = pygame.image.load(self._resource_path('Gardien.png')).convert_alpha()

    def display_lab(self, lab):
        """Function that displays labyrinth and its characters and objects"""
        self.screen_surface.blit(self.macgyver, (3 * 20, 1 * 20))
        self.screen_surface.blit(self.guardian, (13 * 20, 13 * 20))

        for x, line in enumerate(lab):
            for y, element in enumerate(line):
                if element == '#':      # If element is a wall
                    self.screen_surface.blit(self.wall, (y * 20, x * 20))
                elif element == ' ':    # If element is a free path
                    self.screen_surface.blit(self.floor, (y * 20, x * 20))
                elif element == 'M':    # If element is Mac Gyver
                    self.screen_surface.blit(self.floor, (y * 20, x * 20))  #
                    self.screen_surface.blit(self.macgyver, (y * 20, x * 20))
                elif element == 'N':    # If element is needle tool
                    self.screen_surface.blit(self.needle, (y * 20, x * 20))
                elif element == 'T':    # If element is tube tool
                    self.screen_surface.blit(self.tube, (y * 20, x * 20))
                elif element == 'E':    # If element is ether tool
                    self.screen_surface.blit(self.ether, (y * 20, x * 20))

        pygame.display.flip()

    def win(self):
        """Function that displays a 'win' message"""

        # -tc- indiquer Press any key to quit
        win_text = self.cambria_font.render("Congratulation, you win!", True, (0, 255, 0))
        self.screen_surface.blit(win_text, (150, 150))
        pygame.display.flip()
        
        # -tc- attendre que l'utilisateur appuie sur un touche pour quitter:
        # -tc- while True:
        # -tc-     for event in pygame.event.get():
        # -tc-         if event.type in (pygame.QUIT, pygame.KEYDOWN):
        # -tc-             return 

    def lose(self):
        """Function that displays a 'lose' message """

        lose_text = self.cambria_font.render("Sorry, but you died!", True, (255, 0, 0))
        self.screen_surface.blit(lose_text, (150, 150))
        pygame.display.flip()

    def get_direction(self):
        """Function that set a direction in labyrinth"""

        moves = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            elif event.type == pygame.KEYDOWN:
                if event.key in self.DIRECTIONS:
                    moves.append(self.DIRECTIONS[event.key])
        return moves
