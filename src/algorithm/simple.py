"""A module to contain the simplest and fastest solving method of the Rubik's
cube. The downside of course being how many turns are required."""

from src.puzzle.cube import Cube


class Simple:
    """A class for solving a Rubik's cube with a lot of moves."""
    def __init__(self, cube: Cube):
        self.__cube = cube

    def solve(self) -> str:
        """A function to solve the cube step by step, layer by layer."""
        if self.__cube.isSolved():
            return ""
        moves = []

        moves += self.__top_cross()
        moves += self.__top_corners()

        return " ".join(moves)

    def __top_cross(self):
        """A function to solve the top cross of a cube."""

    def __top_corners(self):
        """A function to solve the top corners of a cube."""
