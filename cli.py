""" -tc- Ajouter une docstring."""

class CLI:
    """Class that defines CLI init"""

    DIRECTIONS = {'Z': 'UP',
                  'Q': 'LEFT',
                  'S': 'DOWN',
                  'D': 'RIGHT'}

    # -tc- si la méthode d'initialisation ne fait rien, ne pas la mettre
    def __init__(self, lines, columns):
        """ -tc- Ajouter une docstring."""
        pass

    def display_lab(self, lab):
        """Function that displays labyrinth"""

        for i in lab:
            result = ''.join(i)
            print(result)
            # Ou :
            # r = map(lambda x: ''.join(x), val)
            # r = '\n'.join(r)

    def win(self):
        """Function that returns a 'win' message"""
        return "Congratulation, you win!"

    def lose(self):
        """Function that returns a 'lose' message"""
        return "Sorry but you died!"

    def get_direction(self):
        """Function that set a direction in labyrinth"""

        direction = input("Select direction 'Z, Q, S or D' : ").upper()
        if direction == "X":
            return None
        elif direction in ['Z', 'Q', 'S', 'D']:
            return [self.DIRECTIONS[direction]]

        print("Please enter a valid direction")
        return self.get_direction()
