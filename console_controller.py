"""
ConsoleController: User interface for manually solving
Anne Hoy's problems from the console.
"""


# Copyright 2014, 2017 Dustin Wehr, Danny Heap, Bogdan Simion,
# Jacqueline Smith, Dan Zingaro
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 1, CSC148, Winter 2017.
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.


from toah_model import TOAHModel, IllegalMoveError


def move(model, origin, dest):
    """ Apply move from origin to destination in model.

    May raise an IllegalMoveError.

    @param TOAHModel model:
        model to modify
    @param int origin:
        stool number (index from 0) of cheese to move
    @param int dest:
        stool number you want to move cheese to
    @rtype: None
    """
    model.move(origin, dest)


class ConsoleController:
    """ Controller for text console.
    """

    def __init__(self, number_of_cheeses, number_of_stools):
        """ Initialize a new ConsoleController self.

        @param ConsoleController self:
        @param int number_of_cheeses:
        @param int number_of_stools:
        @rtype: None
        """
        self.number_of_cheeses = number_of_cheeses
        self.number_of_stools = number_of_stools
        self._model = TOAHModel(number_of_stools)
        self._model.fill_first_stool(number_of_cheeses)

    def play_loop(self):
        """ Play Console-based game.

        @param ConsoleController self:
        @rtype: None

        TODO:
        -Start by giving instructions about how to enter moves (which is up to
        you). Be sure to provide some way of exiting the game, and indicate
        that in the instructions.
        -Use python's built-in function input() to read a potential move from
        the user/player. You should print an error message if the input does
        not meet the specifications given in your instruction or if it denotes
        an invalid move (e.g. moving a cheese onto a smaller cheese).
        You can print error messages from this method and/or from
        ConsoleController.move; it's up to you.
        -After each valid move, use the method TOAHModel.__str__ that we've
        provided to print a representation of the current state of the game.
        """
        print("INSTRUCTIONS ---Type initial stool and the destination to move "
              "the topmost cheese in the order - ''start stool(int)',"
              "'destination stool(int)''. And, to exit the function type 'e'"
              ". The initial stool's index is 0 and the fourth stool's index "
              "is 3""")
        pot_move = input("enter move: ")
        while pot_move != 'e':
            try:
                check_comma(pot_move[1])
                self._model.check_move(int(pot_move[0]), int(pot_move[2]))
                move(self._model, int(pot_move[0]), int(pot_move[2]))
                print(self._model)
                pot_move = input("enter move: ")
            except IndexError as ie:
                print(ie)
                print("index should be in range.")
                pot_move = input("enter move: ")
            except SyntaxError as ilme:
                print(ilme)
                print("Invalid syntax.")
                pot_move = input("enter move: ")
            except IllegalMoveError as ilme:
                print(ilme)
                print("enter again.")
                pot_move = input("enter move: ")
            except ValueError as ve:
                print(ve)
                print("enter again.")
                pot_move = input("enter move: ")


def check_comma(comma):
    """
    Returns True iff s is a comma. Otherwise, raise an Exception.

    @param str comma: string comma
    @rtype: bool

    >>> check_comma(',')
    True
    >>> check_comma('*')
    False
    """
    if comma != ',':
        raise SyntaxError("should be a comma there")
    else:
        return True


if __name__ == '__main__':
    # TODO:
    # You should initiate game play here. Your game should be playable by
    # running this file.
    game = ConsoleController(5, 4)
    game.play_loop()
    # Leave lines below as they are, so you will know what python_ta checks.
    # You will need consolecontroller_pyta.txt in the same folder.
    import python_ta
    python_ta.check_all(config="consolecontroller_pyta.txt")
