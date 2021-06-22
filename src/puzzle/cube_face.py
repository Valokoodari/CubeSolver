"""A module for the CubeFace class."""

from typing import Tuple, List


class CubeFace:
    """A class to store and manipulate a face of a Rubik's cube.
    Lines om a 3x3 are 0: top, 1: middle (horizontal), 2: bottom, 3: right,
    4: middle (vertical), 5: left."""
    sides = ('U', 'L', 'F', 'R', 'B', 'D')
    __remap = (0, 1, 2, 7, 3, 6, 5, 4)
    __lines = ((0, 1, 2), (7, -1, 3), (6, 5, 4),
               (0, 7, 6), (1, -1, 5), (2, 3, 4))

    def __init__(self, side: int):
        self.__side = side
        self.__facelets = sum([side << 28-4*i for i in range(8)])

    def rotate(self, clockwise: bool = True) -> None:
        """A function to rotate the face 90 degrees clockwise or
        counterclockwise."""
        if clockwise:
            self.__facelets = self.__facelets << 24 & 0xFF000000 \
                              | self.__facelets >> 8
        else:
            self.__facelets = self.__facelets << 8 & 0xFFFFFF00 \
                              | self.__facelets >> 24

    def __get_facelet(self, facelet_number: int) -> int:
        if not 0 <= facelet_number <= 8:
            raise ValueError("The value must be in range from 0 to 8.")

        if facelet_number == 4:
            return self.__side
        if facelet_number > 4:
            facelet_number -= 1

        return self.__facelets >> (4*(7-CubeFace.__remap[facelet_number])) & 0xF

    def get_facelet(self, facelet_number: int) -> str:
        """A function to get a single facelet on the face.
        On a 3x3 face the facelets are 0-2 on the top line, 3-5, on the middle
        line and 6-8 on the bottom line. (Horizontal lines)"""
        return CubeFace.sides[self.__get_facelet(facelet_number)]

    def get_line(self, line_number) -> Tuple[int, int, int]:
        """A function to get a list of facelets on a line."""
        if not 0 <= line_number <= 5:
            raise ValueError("The line number must be in range from 0 to 5.")

        if line_number < 3:
            return tuple(self.__get_facelet(i+3*line_number) for i in range(3))
        return tuple(self.__get_facelet(3*i+line_number-3) for i in range(3))

    def set_line(self, line_number: int, line: Tuple[int, int, int]) -> None:
        """A function to replace a line of facelets on the face. Intended to be
        used to move facelets from one face to an another face when a layer is
        rotated."""
        if not 0 <= line_number <= 5:
            raise ValueError("The line number must be in range from 0 to 5.")
        if line_number in (1, 4):   # FIXME: Implement for middle lines
            raise NotImplementedError("Not implemented for middle lines.")

        for i, side in enumerate(line):
            self.__facelets &= ~(0xF << 4*(7-CubeFace.__lines[line_number][i]))
            self.__facelets |= side << 4*(7-CubeFace.__lines[line_number][i])

    @property
    def facelets(self) -> List[List[int]]:
        """A property to get a two-dimensional list of all the facelets on the
        face."""
        return [[self.__get_facelet(col + 3*row) for col in range(3)]
                for row in range(3)]

    @property
    def cube_string(self) -> str:
        """A property to get the cube string representation for the face.
        For example: "UUUUUUUUU" for the top face of a solved cube or
        "UDUDUDUDU" for the bottom face on a checkerboard pattern."""
        return "".join([self.get_facelet(i) for i in range(9)])

    @property
    def is_solved(self) -> bool:
        """A property to check if the face is valid on a solved Rubik's cube or
        not. Return true when all of the facelets are equal to each other."""
        first = self.get_facelet(0)
        for i in range(1, 9):
            if self.get_facelet(i) != first:
                return False
        return True

    @property
    def is_domino(self) -> bool:
        """A property to check if the face is valid on a Rubik's cube which can
        be solved with only the moves possible on the Domino Cube (also known as
        the 2x3x3 Rubik's cube)."""
        for i in range(9):
            if self.get_facelet(i) not in ('U', 'D'):
                return False
        return True
