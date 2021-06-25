"""A module to contain the simplest and fastest solving method of the Rubik's
cube. The downside of course being how many turns are required."""

import copy
from typing import Tuple, List

from src.puzzle.cube import Cube


class Simple:
    """A class for solving a Rubik's cube with a lot of moves."""
    def __init__(self, cube: Cube):
        self.__cube = cube

    def set_cube(self, cube) -> None:
        """A function to copy a cube into this class."""
        self.__cube = copy.deepcopy(cube)

    def solve(self) -> Tuple[int, str]:
        """A function to solve the cube step by step, layer by layer."""
        if self.__cube.is_solved:
            return (0, "")
        moves = []

        moves += self.__top_cross()
        moves += self.__top_corners()

        if len(moves) == 0:
            return (-1, "")

        return (len(moves), " ".join(moves))

    def __top_edges(self) -> List[str]:
        return [edge if "U" in edge else "--"
                for edge in self.__cube.unoriented_edges]

    def __top_cross(self) -> List[str]:
        """A function to solve the top cross of a cube."""
        moves = self.__top_cross_clear_top()
        moves += self.__top_cross_clear_equator()
        moves += self.__top_cross_clear_top()
        moves += self.__top_cross_orient()
        moves += self.__top_cross_to_top()

        return moves

    def __top_cross_clear_top(self) -> List[str]:
        moves, sides = [], ["R", "F", "L", "B"]
        for i in range(4):
            if "U" in self.__top_edges()[i]:
                moves += self.__top_cross_rotate_bottom(i+4)
                moves.append(sides[i] + "2")
                self.__cube.twist_by_notation(moves[-1])
        return moves

    def __top_cross_clear_equator(self) -> List[str]:
        moves = []
        if "U" in self.__top_edges()[8] or "U" in self.__top_edges()[9]:
            moves += self.__top_cross_rotate_bottom(5)
            moves.append("F")
            self.__cube.twist_by_notation(moves[-1])
        if "U" in self.__top_edges()[10] or "U" in self.__top_edges()[11]:
            moves += self.__top_cross_rotate_bottom(7)
            moves.append("B")
            self.__cube.twist_by_notation(moves[-1])
        return moves

    def __top_cross_orient(self) -> List[str]:
        moves, sides, edges = [], ["R", "F", "L", "B"], self.__top_edges()
        for i in range(4):
            if edges[i+4][1] == "U":
                moves.append(sides[i])
                moves.append("D'")
                moves.append(sides[(i+1) % 4])
                moves.append("D")
        self.__cube.twist_by_notation(" ".join(moves))
        return moves

    def __top_cross_to_top(self) -> List[str]:
        moves, sides = [], ["R", "F", "L", "B"]
        for i in range(4):
            while self.__top_edges()[i+4][1] != sides[i]:
                moves.append("D")
                self.__cube.twist_by_notation(moves[-1])
            moves.append(sides[i]+"2")
            self.__cube.twist_by_notation(moves[-1])
        return moves

    def __top_cross_rotate_bottom(self, edge) -> List[str]:
        moves = []
        while "U" in self.__top_edges()[edge]:
            moves.append("D")
            self.__cube.twist_by_notation(moves[-1])
        return moves

    def __top_corners(self) -> List[str]:
        """A function to solve the top corners of a cube."""
        return []
