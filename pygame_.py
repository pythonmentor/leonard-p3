import os
import pygame
from pygame.locals import *

class Pygame:
    """Class that defines Pygame initialization """
    DIRECTIONS = {K_UP: 'UP',
                  K_DOWN: 'DOWN',
                  K_LEFT: 'LEFT',
                  K_RIGHT: 'RIGHT'}

    def resource_path(self, file):
        """Function to access resources"""
        return os.path.join('resource', file)

    def __init__(self, lines, columns):
        """Function to initialize Pygame"""

        pygame.init()
        self.window_size = (columns * 20, lines * 20)  # (x, y)
        self.screen_surface = pygame.display.set_mode(self.window_size)
        self.cambria_font = pygame.font.SysFont('Cambria', 30)

        self.floor = pygame.image.load(self.resource_path('floor.png')).convert_alpha()
        self.wall = pygame.image.load(self.resource_path('wall.png')).convert_alpha()
        self.needle = pygame.image.load(self.resource_path('needle.png')).convert_alpha()
        self.tube = pygame.image.load(self.resource_path('tube.png')).convert_alpha()
        self.ether = pygame.image.load(self.resource_path('ether.png')).convert_alpha()
        self.macgyver = pygame.image.load(self.resource_path('MacGyver.png')).convert_alpha()
        self.guardian = pygame.image.load(self.resource_path('Gardien.png')).convert_alpha()

    def display_lab(self, lab):
        """Function that displays labyrinth and its characters and objects"""
        self.screen_surface.blit(self.macgyver, (3 * 20, 1 * 20))
        self.screen_surface.blit(self.guardian, (13 * 20, 13 * 20))

        for x, line in enumerate(lab):
            for y, element in enumerate(line):
                if element == '#':
                    self.screen_surface.blit(self.wall, (y * 20, x * 20))
                elif element == ' ':
                    self.screen_surface.blit(self.floor, (y * 20, x * 20))
                elif element == 'M':
                    self.screen_surface.blit(self.floor, (y * 20, x * 20))
                    self.screen_surface.blit(self.macgyver, (y * 20, x * 20))
                elif element == 'N':
                    self.screen_surface.blit(self.needle, (y * 20, x * 20))
                elif element == 'T':
                    self.screen_surface.blit(self.tube, (y * 20, x * 20))
                elif element == 'E':
                    self.screen_surface.blit(self.ether, (y * 20, x * 20))

        pygame.display.flip()

    def win(self):
        win_text = self.cambria_font.render("Congratulation, you win!", True, (0, 255, 0))
        self.screen_surface.blit(win_text, (150, 150))
        pygame.display.flip()

    def lose(self):
        lose_text = self.cambria_font.render("Sorry, but you died!", True, (255, 0, 0))
        self.screen_surface.blit(lose_text, (150, 150))
        pygame.display.flip()

    def get_direction(self):
        moves = []
        for event in pygame.event.get():
            if event.type == QUIT:
                return None
            elif event.type == KEYDOWN:
                if event.key in self.DIRECTIONS:
                    moves.append(self.DIRECTIONS[event.key])
        return moves
