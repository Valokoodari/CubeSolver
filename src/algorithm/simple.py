"""A module to contain the simplest and fastest solving method of the Rubik's
cube. The downside of course being how many turns are required."""

import copy
from typing import Tuple, List

from src.puzzle.cube import Cube


class Simple:
    __sides = ["R", "F", "L", "B"]
    """A class for solving a Rubik's cube with a lot of moves."""
    def __init__(self, cube: Cube):
        self.__cube = cube
        self.__moves = []

    def set_cube(self, cube) -> None:
        """A function to copy a cube into this class."""
        self.__cube = copy.deepcopy(cube)
        self.__moves = []

    def solve(self) -> Tuple[int, str]:
        """A function to solve the cube step by step, layer by layer."""
        if self.__cube.is_solved:
            return (0, "")

        self.__moves += self.__top_cross()
        self.__top_corners()

        if len(self.__moves) == 0:
            return (-1, "")

        return (len(self.__moves), " ".join(self.__moves))

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
        moves = []
        for i in range(4):
            if "U" in self.__top_edges()[i]:
                moves += self.__top_cross_rotate_bottom(i+4)
                moves.append(self.__sides[i] + "2")
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
        moves, edges = [], self.__top_edges()
        for i in range(4):
            if edges[i+4][1] == "U":
                moves.append(self.__sides[i])
                moves.append("D'")
                moves.append(self.__sides[(i+1) % 4])
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

    def __top_corners(self) -> None:
        """A function to solve the top corners of a cube."""
        self.__clear_top_corners()
        self.__place_top_corners()

    def __clear_top_corners(self) -> None:
        for i in range(4):
            if "U" in self.__cube.corners[i]:
                self.__top_corners_rotate_bottom(i+4)
                moves = [self.__sides[i]+"'", "D'", self.__sides[i], "D"]
                self.__cube.twist_by_notation(" ".join(moves))
                self.__moves += moves

    def __place_top_corners(self) -> None:
        for i, corner in enumerate(Cube.corner_order[:4]):
            self.__top_corners_rotate_bottom(4+i, corner)
            moves, side = [], self.__sides[i]
            if self.__cube.unoriented_corners[4+i][0] == "U":
                moves = [side+"'", "D2", side, "D", side+"'", "D'", side]
            elif self.__cube.unoriented_corners[4+i][1] == "U":
                moves = ["D'", side+"'", "D", side]
            else:
                moves = [side+"'", "D'", side]
            self.__cube.twist_by_notation(" ".join(moves))
            self.__moves += moves

    def __top_corners_rotate_bottom(self, corner: int,
                                    target: str = None) -> None:
        while True:
            if "U" not in self.__cube.corners[corner] and target is None:
                break
            if target == self.__cube.corners[corner]:
                break
            print(target, self.__cube.corners[corner])
            self.__moves.append("D")
            self.__cube.twist_by_notation(self.__moves[-1])
