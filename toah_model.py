"""
TOAHModel:  Model a game of Tour of Anne Hoy
Cheese:   Model a cheese with a given (relative) size
IllegalMoveError: Type of exceptions thrown when an illegal move is attempted
MoveSequence: Record of a sequence of (not necessarily legal) moves. You will
need to return MoveSequence object after solving an instance of the 4-stool
Tour of Anne Hoy game, and we will use that to check the correctness of your
algorithm.
"""


# Copyright 2013, 2014, 2017 Gary Baumgartner, Danny Heap, Dustin Wehr,
# Bogdan Simion, Jacqueline Smith, Dan Zingaro, Ritu Chaturvedi, Samar Sabie
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
#


class TOAHModel:
    """ Model a game of Tour Of Anne Hoy.

    Model stools holding stacks of cheese, enforcing the constraint
    that a larger cheese may not be placed on a smaller one.
    """

    def __init__(self, number_of_stools):
        """ Create new TOAHModel with empty stools
        to hold stools of cheese.

        @param TOAHModel self:
        @param int number_of_stools:
        @rtype: None

        >>> M = TOAHModel(4)
        >>> M.fill_first_stool(5)
        >>> (M.get_number_of_stools(), M.number_of_moves()) == (4,0)
        True
        >>> M.get_number_of_cheeses()
        5
        """
        # you must have _move_seq as well as any other attributes you choose
        s = list(range(number_of_stools))
        self._stools = {}
        for x in s:
            self._stools[x] = []
        self.number_of_stools = number_of_stools
        self._move_seq = MoveSequence([])

    def fill_first_stool(self, number_of_cheeses):
        """ Add the number_of_cheeses to the first stool in the TOAHModel.

        @param TOAHModel self:
        @param int number_of_cheeses:
        @rtype None

        >>> M = TOAHModel(4)
        >>> M.fill_first_stool(5)
        >>> M.get_number_of_cheeses()
        5
        >>> N = TOAHModel(4)
        >>> N.fill_first_stool(6)
        >>> N.get_number_of_cheeses()
        6
        """

        s = list(range(number_of_cheeses))
        a = len(s)
        for i in s:
            self._stools[0].append(Cheese(a - i))

    def get_number_of_stools(self):
        """Return the number of stools in self.

        @param TOAHModel self:
        @rtype int

        >>> M = TOAHModel(4)
        >>> M.fill_first_stool(5)
        >>> M.get_number_of_stools()
        4
        >>> N = TOAHModel(5)
        >>> N.fill_first_stool(4)
        >>> N.get_number_of_stools()
        5
        """

        return self.number_of_stools

    def number_of_moves(self):
        """Return the number of moves that have been made to the TOAHModel
        self.

        @param TOAHModel self:
        @rtype int

        >>> m1 = TOAHModel(4)
        >>> m1.fill_first_stool(7)
        >>> m1.move(0, 1)
        >>> m1.move(0, 2)
        >>> m1.move(1, 2)
        >>> m1.number_of_moves()
        3
        >>> m2 = TOAHModel(4)
        >>> m2.fill_first_stool(7)
        >>> m2.move(0, 3)
        >>> m2.move(0, 2)
        >>> m2.move(3, 2)
        >>> m2.number_of_moves()
        3
        """

        return self._move_seq.length()

    def move(self, start_stool, dest_stool):
        """Move the topmost cheese from the start_stool to the dest_stool.

        @param TOAHModel self:
        @param int start_stool:
        @param int dest_stool:
        @rtype None

        >>> m1 = TOAHModel(4)
        >>> m1.fill_first_stool(7)
        >>> m1.move(0, 1)
        >>> m1.move(0, 2)
        >>> m1.move(1, 2)
        >>> m2 = TOAHModel(4)
        >>> m2.fill_first_stool(7)
        >>> m2.move(0, 3)
        >>> m2.move(0, 2)
        >>> m2.move(3, 2)
        >>> m1 == m2
        True
        """
        if self.check_move(start_stool, dest_stool):
            self._stools[dest_stool].append(self._stools[start_stool].pop())
            self._move_seq.add_move(start_stool, dest_stool)

    def check_move(self, start_stool, dest_stool):
        """Return True if it's a valid move. Otherwise, raise an exception.

        @param TOAHModel self:
        @param int start_stool:
        @param int dest_stool :
        @rtype : bool

        >>> m1 = TOAHModel(4)
        >>> m1.fill_first_stool(7)
        >>> m1.check_move(0, 1)
        True
        >>> m1.check_move(0, 2)
        True
        """
        if start_stool in self._stools and dest_stool in self._stools:
            if self._cheese_at(dest_stool, len(self._stools[dest_stool]) -
                               1) is None:
                if len(self._stools[start_stool]) > 0:
                    return True
                else:
                    raise IllegalMoveError("source stool doesn't have any "
                                           "cheese")
            elif self._cheese_at(start_stool, len(self._stools[start_stool])
                                 - 1) is not None and self._cheese_at(
                                     start_stool, len(self._stools[
                                         start_stool]) - 1).size < \
                    self._cheese_at(dest_stool, len(self._stools[dest_stool])
                                    - 1).size:
                return True
            else:
                if self._cheese_at(start_stool, len(self._stools[start_stool])
                                   - 1) is None:
                    raise IllegalMoveError("source stool is empty")
                else:
                    raise IllegalMoveError("Cannot stack larger cheese on top "
                                           "of a smaller one")
        else:
            if start_stool not in self._stools:
                raise IllegalMoveError("source stool index is not correct")
            else:
                raise IllegalMoveError("destination stool index is not "
                                       "correct")

    def add(self, cheese, stool):
        """Add cheese to the top of the stool.

        @param TOAHModel self:
        @param Cheese cheese:
        @param int stool:
        @rtype None
        """
        self._stools[stool].append(cheese)

    def get_cheese_location(self, cheese):
        """Return the location of the cheese in self.

        @param TOAHModel self:
        @param Cheese cheese:
        @rtype : int

        """
        for i in self._stools:
            if cheese in self._stools[i]:
                return i
        return 0

    def get_top_cheese(self, stool_index):
        """Return the top cheese at the stool stool_index."""
        if len(self._stools[stool_index]) > 0:
            return self._stools[stool_index][-1]
        else:
            return None

    def get_move_seq(self):
        """ Return the move sequence

        @type self: TOAHModel
        @rtype: MoveSequence

        >>> toah = TOAHModel(2)
        >>> toah.get_move_seq() == MoveSequence([])
        True
        """

        return self._move_seq

    def get_number_of_cheeses(self):
        """Return the total number of cheeses in the TOAHModel self.
        @param TOAHModel self:
        @rtype int

        >>> m1 = TOAHModel(4)
        >>> m1.fill_first_stool(7)
        >>> m1.get_number_of_cheeses()
        7
        >>> m2 = TOAHModel(4)
        >>> m2.fill_first_stool(7)
        >>> m2.get_number_of_cheeses()
        7
        """
        number = 0
        for i in self._stools:
            number = number + len(self._stools[i])
        return number

    def __eq__(self, other):
        """ Return whether TOAHModel self is equivalent to other.

        Two TOAHModels are equivalent if their current
        configurations of cheeses on stools look the same.
        More precisely, for all h,s, the h-th cheese on the s-th
        stool of self should be equivalent the h-th cheese on the s-th
        stool of other

        @type self: TOAHModel
        @type other: TOAHModel
        @rtype: bool

        >>> m1 = TOAHModel(4)
        >>> m1.fill_first_stool(7)
        >>> m1.move(0, 1)
        >>> m1.move(0, 2)
        >>> m1.move(1, 2)
        >>> m2 = TOAHModel(4)
        >>> m2.fill_first_stool(7)
        >>> m2.move(0, 3)
        >>> m2.move(0, 2)
        >>> m2.move(3, 2)
        >>> m1 == m2
        True
        """
        return isinstance(self, TOAHModel) and isinstance(other, TOAHModel) \
            and self._stools == other._stools

    def _cheese_at(self, stool_index, stool_height):
        # """ Return (stool_height)th from stool_index stool, if possible.
        #
        # @type self: TOAHModel
        # @type stool_index: int
        # @type stool_height: int
        # @rtype: Cheese | None
        #
        # >>> M = TOAHModel(4)
        # >>> M.fill_first_stool(5)
        # >>> M._cheese_at(0,3).size
        # 2
        # >>> M._cheese_at(0,0).size
        # 5
        # """
        if 0 <= stool_height < len(self._stools[stool_index]):
            return self._stools[stool_index][stool_height]
        else:
            return None

    def __str__(self):
        """
        Depicts only the current state of the stools and cheese.

        @param TOAHModel self:
        @rtype: str
        """
        all_cheeses = []
        for height in range(self.get_number_of_cheeses()):
            for stool in range(self.get_number_of_stools()):
                if self._cheese_at(stool, height) is not None:
                    all_cheeses.append(self._cheese_at(stool, height))
        max_cheese_size = max([c.size for c in all_cheeses]) \
            if len(all_cheeses) > 0 else 0
        stool_str = "=" * (2 * max_cheese_size + 1)
        stool_spacing = "  "
        stools_str = (stool_str + stool_spacing) * self.get_number_of_stools()

        def _cheese_str(size):
            # helper for string representation of cheese
            if size == 0:
                return " " * len(stool_str)
            cheese_part = "-" + "--" * (size - 1)
            space_filler = " " * int((len(stool_str) - len(cheese_part)) / 2)
            return space_filler + cheese_part + space_filler

        lines = ""
        for height in range(self.get_number_of_cheeses() - 1, -1, -1):
            line = ""
            for stool in range(self.get_number_of_stools()):
                c = self._cheese_at(stool, height)
                if isinstance(c, Cheese):
                    s = _cheese_str(int(c.size))
                else:
                    s = _cheese_str(0)
                line += s + stool_spacing
            lines += line + "\n"
        lines += stools_str

        return lines


class Cheese:
    """ A cheese for stacking in a TOAHModel

    === Attributes ===
    @param int size: width of cheese
    """

    def __init__(self, size):
        """ Initialize a Cheese to diameter size.

        @param Cheese self:
        @param int size:
        @rtype: None

        >>> c = Cheese(3)
        >>> isinstance(c, Cheese)
        True
        >>> c.size
        3
        """
        self.size = size

    def __eq__(self, other):
        """ Is self equivalent to other?

        We say they are if they're the same
        size.

        @param Cheese self:
        @param Cheese|Any other:
        @rtype: bool

        >>> c = Cheese(3)
        >>> a = Cheese(3)
        >>> c == a
        True
        >>> d = Cheese(4)
        >>> e = Cheese(5)
        >>> d == e
        False
        """
        return isinstance(self, Cheese) and isinstance(other, Cheese) and \
            self.size == other.size


class IllegalMoveError(Exception):
    """ Exception indicating move that violate TOAHModel
    """
    pass


class MoveSequence(object):
    """ Sequence of moves in TOAH game
    """

    def __init__(self, moves):
        """ Create a new MoveSequence self.

        @param MoveSequence self:
        @param list[tuple[int]] moves:
        @rtype: None
        """
        # moves - a list of integer pairs, e.g. [(0,1),(0,2),(1,2)]
        self._moves = moves

    def __eq__(self, other):
        """Return True iff self and other are equal.
        @param MoveSequence self:
        @param MoveSequence other:
        @rtype : bool

        >>> ms = MoveSequence([(1, 2)])
        >>> ns = MoveSequence([(1, 2)])
        >>> ms == ns
        True
        >>> ms = MoveSequence([(1, 2)])
        >>> ns = MoveSequence([(0, 2)])
        >>> ms == ns
        False
        """
        return isinstance(self, MoveSequence) and isinstance(other,
                                                             MoveSequence) \
            and self._moves == other._moves

    def get_move(self, i):
        """ Return the move at position i in self

        @param MoveSequence self:
        @param int i:
        @rtype: tuple[int]

        >>> ms = MoveSequence([(1, 2)])
        >>> ms.get_move(0) == (1, 2)
        True
        """
        # Exception if not (0 <= i < self.length)
        return self._moves[i]

    def add_move(self, src_stool, dest_stool):
        """ Add move from src_stool to dest_stool to MoveSequence self.

        @param MoveSequence self:
        @param int src_stool:
        @param int dest_stool:
        @rtype: None
        """
        self._moves.append((src_stool, dest_stool))

    def length(self):
        """ Return number of moves in self.

        @param MoveSequence self:
        @rtype: int

        >>> ms = MoveSequence([(1, 2)])
        >>> ms.length()
        1
        """
        return len(self._moves)

    def generate_toah_model(self, number_of_stools, number_of_cheeses):
        """ Construct TOAHModel from number_of_stools and number_of_cheeses
         after moves in self.

        Takes the two parameters for
        the game (number_of_cheeses, number_of_stools), initializes the game
        in the standard way with TOAHModel.fill_first_stool(number_of_cheeses),
        and then applies each of the moves in this move sequence.

        @param MoveSequence self:
        @param int number_of_stools:
        @param int number_of_cheeses:
        @rtype: TOAHModel

        >>> ms = MoveSequence([])
        >>> toah = TOAHModel(2)
        >>> toah.fill_first_stool(2)
        >>> toah == ms.generate_toah_model(2, 2)
        True
        """
        model = TOAHModel(number_of_stools)
        model.fill_first_stool(number_of_cheeses)
        for move in self._moves:
            model.move(move[0], move[1])
        return model

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
    # Leave lines below to see what python_ta checks.
    # File toahmodel_pyta.txt must be in same folder.
    import python_ta
    python_ta.check_all(config="toahmodel_pyta.txt")
