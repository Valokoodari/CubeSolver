"""A module to contain the simplest and fastest solving method of the Rubik's
cube. The downside of course being how many turns are required."""

import copy
from typing import Tuple, List

from src.puzzle.cube import Cube


class Simple:
    __sides = ["R", "F", "L", "B"]
    __ud_edges = ["FR", "LF", "BL", "RB"]
    __states = ([False, True, True, False],
                [False, False, True, True],
                [True, False, False, True],
                [True, True, False, False])

    """A class for solving a Rubik's cube with a lot of moves."""
    def __init__(self, cube: Cube):
        self.__cube = copy.deepcopy(cube)
        self.__moves = []

    def set_cube(self, cube) -> None:
        """A function to copy a cube into this class."""
        self.__cube = copy.deepcopy(cube)
        self.__moves = []

    def solve(self) -> Tuple[int, str]:
        """A function to solve the cube step by step, layer by layer."""
        if self.__cube.is_solved:
            return (0, "")

        self.__moves += self.__solve_top_cross()
        self.__solve_top_corners()
        self.__solve_ud_slice()
        self.__solve_bottom_layer()

        if len(self.__moves) == 0:
            return (-1, "")

        return (len(self.__moves), " ".join(self.__moves))

    def __top_edges(self) -> List[str]:
        return [edge if "U" in edge else "--"
                for edge in self.__cube.unoriented_edges]

    def __solve_top_cross(self) -> List[str]:
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

    def __solve_top_corners(self) -> None:
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
            self.__moves.append("D")
            self.__cube.twist_by_notation(self.__moves[-1])

    def __solve_ud_slice(self) -> None:
        self.__clear_ud_slice()
        self.__place_ud_slice()

    def __clear_ud_slice(self) -> None:
        for i in range(4):
            if self.__cube.edges[i+8] not in Cube.edge_order[8:]:
                continue
            sides = (self.__sides[i], self.__sides[(i+1) % 4])
            self.__ud_slice_rotate_bottom((i+2) % 4 + 4)
            moves = [sides[0]+"'", "D", sides[0], "D",
                     sides[1], "D'", sides[1]+"'"]
            self.__moves += moves
            self.__cube.twist_by_notation(" ".join(moves))

    def __place_ud_slice(self) -> None:
        for i in range(4):
            moves, sides = [], (self.__sides[i], self.__sides[(i+1) % 4])
            self.__ud_slice_rotate_bottom(i+4, Cube.edge_order[i+8])
            if self.__cube.unoriented_edges[i+4] in self.__ud_edges:
                moves = ["D", sides[1], "D'", sides[1]+"'",
                         "D'", sides[0]+"'", "D", sides[0]]
            else:
                moves = ["D2", sides[0]+"'", "D", sides[0],
                         "D", sides[1], "D'", sides[1]+"'"]
            self.__moves += moves
            self.__cube.twist_by_notation(" ".join(moves))

    def __ud_slice_rotate_bottom(self, edge: int, target: str = None) -> None:
        while True:
            current = self.__cube.edges[edge]
            if current == target:
                break
            if target is None and current not in Cube.edge_order[8:]:
                break
            self.__moves.append("D")
            self.__cube.twist_by_notation("D")

    def __bottom_cross_orientation(self) -> List[bool]:
        bottom_edges = self.__cube.unoriented_edges[4:8]
        return [edge[0] == "D" for edge in bottom_edges]

    def __bottom_cross_permutation(self) -> List[bool]:
        bottom_edges = self.__cube.unoriented_edges[4:8]
        order = Cube.edge_order[4:8]
        return [edge == order[i] for i, edge in enumerate(bottom_edges)]

    def __solve_bottom_layer(self) -> None:
        self.__orient_bottom_cross()
        self.__rotate_bottom_cross()
        self.__place_bottom_corners()
        self.__orient_bottom_corners()

    def __orient_bottom_cross(self) -> None:
        sequence = ["F", "L", "D", "L'", "D'", "F'"]
        moves, cross = [], self.__bottom_cross_orientation()

        if cross == [False]*4:  # no cross at all (.)
            moves = [*sequence, *sequence, "D", *sequence]
        elif cross in ([True, False]*2, [False, True]*2):   # line (I)
            moves = [*sequence]
            if cross == [False, True]*2:
                moves = ["D", *moves]
        elif cross != [True]*4:     # corner (L)
            moves = ["D"]*Simple.__states.index(cross)
            moves = [*moves, *sequence, "D", *sequence]

        self.__cube.twist_by_notation(" ".join(moves))
        self.__moves += moves

    def __rotate_bottom_cross(self) -> None:
        sequence = ["L", "D2", "L'", "D'", "L", "D'", "L'"]
        self.__turn_bottom_cross(2)

        cross = self.__bottom_cross_permutation()
        if cross == [True]*4:
            return
        if cross in ([False, True]*2, [True, False]*2):
            self.__moves += sequence
            self.__cube.twist_by_notation(" ".join(sequence))
            self.__turn_bottom_cross(2)
            cross = self.__bottom_cross_permutation()
        self.__turn_bottom_cross(2)

        moves = ["D"]*((Simple.__states.index(cross)+2) % 4)
        moves += sequence
        self.__moves += moves
        self.__cube.twist_by_notation(" ".join(moves))

        self.__turn_bottom_cross(4)

    def __turn_bottom_cross(self, limit: int) -> None:
        while self.__bottom_cross_permutation().count(True) < limit:
            self.__moves.append("D")
            self.__cube.twist_by_notation("D")

    def __bottom_corner_permutation(self) -> List[bool]:
        corners, correct = self.__cube.corners[4:8], Cube.corner_order[4:8]
        return [corner == correct[i] for i, corner in enumerate(corners)]

    def __place_bottom_corners(self) -> None:
        sequence = ["R'", "D", "L", "D'", "R", "D", "L'", "D'"]
        corners = self.__bottom_corner_permutation()
        if corners == [False]*4:
            self.__moves += sequence
            self.__cube.twist_by_notation(" ".join(sequence))

        while self.__bottom_corner_permutation() != [True]*4:
            corners = self.__bottom_corner_permutation()
            moves = ["D"]*((corners.index(True)+3) % 4)
            moves += sequence
            self.__moves += moves
            self.__cube.twist_by_notation(" ".join(moves))
            self.__turn_bottom_cross(4)

    def __orient_bottom_corners(self) -> None:
        sequence = ["R", "U", "R'", "U'"]*2
        for _ in range(4):
            while self.__cube.unoriented_corners[4] not in Cube.corner_order:
                self.__moves += sequence
                self.__cube.twist_by_notation(" ".join(sequence))
            self.__moves.append("D")
            self.__cube.twist_by_notation("D")
