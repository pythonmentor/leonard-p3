from cli import CLI
from labyrinth import *
from character import *
from constants import *


class Main:
    """Class that defines game logic"""

    def __init__(self):
        self.lab = Labyrinth('map.txt')
        self.macgyver = Character('M', 1, 3)
        self.guardian = Character('G', 13, 13)
        self.view = CLI()
        self.lab.set_character_position(self.macgyver)
        self.lab.set_character_position(self.guardian)

        self.lab.set_tool_positions(TOOLS)
        self.is_running = True

        self.view.display_lab(self.lab.lab)

        while self.is_running:
            direction = self.view.get_direction()
            if direction is None:
                continue
            move = self.lab.move_macgyver(self.macgyver,
                                          self.guardian,
                                          direction)
            if not move:
                self.is_running = False
            else:
                self.view.display_lab(self.lab.lab)


if __name__ == '__main__':
    Main()
