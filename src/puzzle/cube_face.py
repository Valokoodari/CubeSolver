"""A module for the CubeFace class."""

from typing import List


class CubeFace:
    """A class to store and manipulate a face of a Rubik's cube.

    Lines om a 3x3 are 0: top, 1: middle (horizontal), 2: bottom, 3: right,
    4: middle, 5: left."""
    sides = ('U', 'L', 'F', 'R', 'B', 'D')

    def __init__(self, size: int, color: int):
        self.__size = size
        self.__facelets = [[color]*size for _ in range(size)]

    def rotate(self, clockwise: bool = True) -> None:
        """A function to rotate the face 90 degrees clockwise or
        counterclockwise."""
        if clockwise:
            self.__facelets = list(zip(*self.__facelets[::-1]))
        else:
            self.__facelets = list(zip(*self.__facelets))[::-1]

        self.__facelets = [list(row) for row in self.__facelets]

    def set_line(self, line_number: int, line: List[int]) -> None:
        """A function to replace a line of facelets on the face. Intended to be
        used to move facelets from one face to an another face when a layer is
        rotated."""
        if line_number < self.__size:
            self.__facelets[line_number] = line
            return
        for row in range(self.__size):
            self.__facelets[row][line_number-self.__size] = line[row]

    def get_facelet(self, number: int) -> str:
        """A function to get a single facelet on the face.

        On a 3x3 face the facelets are 0-2 on the top line, 3-5, on the middle
        line and 6-8 on the bottom line. (Horizontal lines)"""
        return CubeFace.sides[self.__facelets[number // 3][number % 3]]

    def get_line(self, line_number: int) -> List[int]:
        """A function to get a list of facelets on a line."""
        line = [0, 0, 0]

        if line_number < self.__size:
            line = self.__facelets[line_number][:]
        else:
            for row in range(self.__size):
                line[row] = self.__facelets[row][line_number-self.__size]

        return line

    @property
    def facelets(self) -> List[List[int]]:
        """A property to get a two-dimensional list of all the facelets on the
        face."""
        return self.__facelets[:]

    @property
    def cube_string(self) -> str:
        """A property to get the cube string representation for the face.

        For example: "UUUUUUUUU" for the top face of a solved cube or
        "UDUDUDUDU" for the bottom face on a checkerboard pattern."""
        facelets = []
        for row in range(self.__size):
            for col in range(self.__size):
                facelets.append(self.sides[self.__facelets[row][col]])
        return "".join(facelets)

    @property
    def is_solved(self) -> bool:
        """A property to check if the face is valid on a solved Rubik's cube or
        not. Return true when all of the facelets are equal to each other."""
        cube_string = self.cube_string
        return cube_string.count(cube_string[0]) == len(cube_string)

    @property
    def is_domino(self) -> bool:
        """A property to check if the face is valid on a Rubik's cube which can
        be solved with only the moves possible on the Domino Cube (also known as
        the 2x3x3 Rubik's cube)."""
        for face_number in range(1, 5):
            for row in self.__facelets:
                if face_number in row:
                    return False
        return True
