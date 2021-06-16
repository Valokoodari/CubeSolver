"""A module for the Cube class."""

from math import factorial, comb
from random import choice
from typing import List, Tuple

from src.puzzle.cube_face import CubeFace


class Cube:
    """A class to store and manipulate a normal 3x3x3 Rubik's cube."""

    # Neighbors, the affected line number, and -1 if the line should be
    # flipped for every possible turn.
    __turns = (((1, 0, 1), (2, 0, 1), (3, 0, 1), (4, 0, 1)),
               ((0, 3, 1), (4, 5, -1), (5, 3, 1), (2, 3, 1)),
               ((0, 2, -1), (1, 5, 1), (5, 0, 1), (3, 3, -1)),
               ((0, 5, 1), (2, 5, 1), (5, 5, 1), (4, 3, -1)),
               ((0, 0, -1), (3, 5, -1), (5, 2, 1), (1, 3, 1)),
               ((4, 2, 1), (3, 2, 1), (2, 2, 1), (1, 2, 1)))

    corner_order = ["URF", "UFL", "ULB", "UBR", "DFR", "DLF", "DBL", "DRB"]
    edge_order = ["UR", "UF", "UL", "UB", "DR", "DF",
                  "DL", "DB", "FR", "FL", "BL", "BR"]

    corner_coords = {   # (face, facelet)
        "URF": ((0, 8), (3, 0), (2, 2)),
        "UFL": ((0, 6), (2, 0), (1, 2)),
        "ULB": ((0, 0), (1, 0), (4, 2)),
        "UBR": ((0, 2), (4, 0), (3, 2)),
        "DFR": ((5, 2), (2, 8), (3, 6)),
        "DLF": ((5, 0), (1, 8), (2, 6)),
        "DBL": ((5, 6), (4, 8), (1, 6)),
        "DRB": ((5, 8), (3, 8), (4, 6))
    }

    edge_coords = {
        "UR": ((0, 5), (3, 1)),
        "UF": ((0, 7), (2, 1)),
        "UL": ((0, 3), (1, 1)),
        "UB": ((0, 1), (4, 1)),
        "DR": ((5, 5), (3, 7)),
        "DF": ((5, 1), (2, 7)),
        "DL": ((5, 3), (1, 7)),
        "DB": ((5, 7), (4, 7)),
        "FR": ((2, 5), (3, 3)),
        "FL": ((2, 3), (1, 5)),
        "BL": ((4, 5), (1, 3)),
        "BR": ((4, 3), (3, 5))
    }

    moves = [
        move + modifier
        for move in ["U", "L", "F", "R", "B", "D"]
        for modifier in ["", "'", "2"]
    ]

    def __init__(self):
        self.__faces = [CubeFace(3, i) for i in range(6)]

    def twist(self, face_number: int, clockwise: bool = True) -> None:
        """A method to twist a single layer of the cube 90 degress clockwise or
        anticlockwise."""
        self.__faces[face_number].rotate(clockwise)

        lines = []
        direction = 1 if clockwise else -1
        for i in range(4):
            face, line, flip = self.__turns[face_number][(i + direction) % 4]
            lines.append(self.__faces[face].get_line(line)[::flip])
        for i in range(4):
            face, line, flip = self.__turns[face_number][i]
            self.__faces[face].set_line(line, lines[i][::flip])

    def twist_by_notation(self, notation: str) -> None:
        """A method to twist the cube one or multiple times based on a simple
        cube notation.

        Only supports the notation listed in the moves property of this class.
        This means that notations like 'X', 'Y', and 'Z' are not allowed."""
        face = ("U", "L", "F", "R", "B", "D")
        if len(notation) < 1:
            return
        for move in notation.strip().split(" "):
            if len(move) == 1:
                self.twist(face.index(move))
            else:
                if move[1] == "2":
                    self.twist(face.index(move[0]))
                    self.twist(face.index(move[0]))
                else:
                    self.twist(face.index(move[0]), False)

    def scramble(self, count: int = 20) -> str:
        """A function to scramble the cube to any possible orientation."""
        moves = [choice(self.moves) for _ in range(count)]
        notation = " ".join(moves)
        self.twist_by_notation(notation)
        return notation

    def scramble_g1(self, count: int = 18) -> None:
        """A function to scramble the cube to any possible orientation allowed
        by the turns possible on a Domino Cube (2x3x3)."""
        notes = ["U", "U'", "U2", "D", "D'", "D2", "L2", "R2", "F2", "B2"]
        moves = [choice(notes) for _ in range(count)]
        notation = " ".join(moves)
        self.twist_by_notation(notation)
        return notation

    def reset(self) -> None:
        """A function to reset the state of the cube. Kind of like just peeling
        and reapplying the stickers except a lot faster..."""
        self.__init__()

    def __str__(self) -> str:
        colors = ('W', 'R', 'B', 'O', 'G', 'Y')
        string = ""

        for row in self.__faces[0].facelets:
            string += f"\n   {''.join([colors[color] for color in row])}"

        for row_number in range(3):
            string += "\n"
            for face_number in range(1, 5):
                row = self.__faces[face_number].facelets[row_number]
                string += ''.join([colors[color] for color in row])

        for row in self.__faces[5].facelets:
            string += f"\n   {''.join([colors[color] for color in row])}"

        return string[1:]

    @property
    def cube_string(self) -> str:
        """A property to get the cube string representation of the cube.

        For example "UUUUUUUUULLLLLLLLLFFFFFFFFFRRRRRRRRRBBBBBBBBBDDDDDDDDD"
        for a solved cube or
        "UDUDUDUDULRLRLRLRLFBFBFBFBFRLRLRLRLRBFBFBFBFBDUDUDUDUD" for a
        checkerboard pattern."""
        return "".join([face.cube_string for face in self.__faces])

    @property
    def corners(self) -> List[str]:
        """List of all of the corners of the cube ordered by the position in
        order of the corner_order property of this class."""
        corners = [""]*8
        for i, corner in enumerate(self.corner_order):
            for face, facelet in self.corner_coords[corner]:
                corners[i] += self.__faces[face].get_facelet(facelet)
            if corners[i] not in self.corner_coords:
                corners[i] = self.__fix_corner_name(corners[i])

        return corners

    @property
    def edges(self) -> List[str]:
        """List of all the edges of the cube ordered by the position in order
        of the edge_order property of this class."""
        edges = self.unoriented_edges
        for i, edge in enumerate(edges):
            if edge not in self.edge_order:
                edges[i] = edge[::-1]
        return edges

    @property
    def unoriented_edges(self) -> List[str]:
        """List of the edges of the cube in order without the name correction.

        This is used to calculate the edge orientation indexes."""
        edges = [""]*12
        for i, edge in enumerate(self.edge_order):
            for face, facelet in self.edge_coords[edge]:
                edges[i] += self.__faces[face].get_facelet(facelet)
        return edges

    @property
    def is_solved(self) -> bool:     # Group G_2 {1}
        """A property to check if the cube is a valid solved cube or not."""
        for face in self.__faces:
            if not face.is_solved:
                return False
        return True

    @property
    def is_domino(self) -> bool:     # Group G_1 <U, D, L2, R2, F2, B2>
        """A property to check if the cube can be solved with only moves
        possible on a Domino Cube. Assuming that the cube is valid at all."""
        return self.__faces[0].is_domino and self.__faces[5].is_domino

    # Coordinates for Kociemba's phase 1
    @property
    def triple(self) -> Tuple[int, int, int]:
        """A coordinate triple which is (0, 0, 0) if and only if the cube is
        solvable with the moves allowed on a Domino Cube and there has only
        been valid moves been made."""
        corner_orientation = self.coordinate_corner_orientation
        edge_orientation = self.coordinate_edge_orientation
        ud_slice = self.coordinate_ud_slice

        return (corner_orientation, edge_orientation, ud_slice)

    @property
    def coordinate_corner_orientation(self) -> int:
        """Corner orientation index coordinate for the phase 1 of Kociemba's
        algorithm.

        The value is always in range from 0 to 2186."""
        coordinate, corners = 0, [""]*8
        for i, corner in enumerate(self.corner_order[:-1]):
            for face, facelet in self.corner_coords[corner]:
                corners[i] += self.__faces[face].get_facelet(facelet)
            if corners[i] not in self.corner_coords:
                correct = self.__fix_corner_name(corners[i])
                if corners[i][0] == correct[2]:
                    coordinate += 3**(6-i)
                elif corners[i][0] == correct[1]:
                    coordinate += 2*3**(6-i)

        return coordinate

    @property
    def coordinate_edge_orientation(self) -> int:
        """Edge orientation index coordinate for the phase 1 of Kociemba's
        algorithm.

        The value is always in range from 0 to 2047."""
        edges, coordinate = [""]*12, 0
        for i, edge in enumerate(self.edge_order):
            for face, facelet in self.edge_coords[edge]:
                edges[i] += self.__faces[face].get_facelet(facelet)
            if edges[i] not in self.edge_order:
                coordinate += i

        return coordinate

    @property
    def coordinate_ud_slice(self) -> int:
        """UD Slice index coordinate for the phase 1 of Kociemba's algorithm.

        The value in always in range from 0 to 494."""
        edges, k, coordinate = self.edges, 3, 0

        for i in reversed(range(12)):
            if edges[i] in self.edge_order[8:]:
                k -= 1
            else:
                coordinate += comb(i, k)
            if k < 0:
                break

        return coordinate

    # Coordinates for Kociemba's phase 2
    @property
    def triple2(self) -> Tuple[int, int, int]:
        """A coordinate triple which is (0, 0, 0) if and only if the cube is
        solved."""
        corner_permutation = self.coordinate_corner_permutation
        edge_permutation = self.coordinate_edge_permutation
        ud_slice_phase2 = self.coordinate_ud_slice_phase2

        return (corner_permutation, edge_permutation, ud_slice_phase2)

    @property
    def coordinate_corner_permutation(self) -> int:
        """Corner permutation index coordinate for the phase 2 of Kociemba's
        algorithm.

        The value is always in range from 0 to 40319."""
        coordinate, corners = 0, self.corners

        for i, corner in enumerate(corners[1:]):
            order, i = 0, i+1
            for other_corner in corners[:i]:
                index = self.corner_order.index(corner)+1
                if other_corner in self.corner_order[index:]:
                    order += 1
            coordinate += order * factorial(i)

        return coordinate

    @property
    def coordinate_edge_permutation(self) -> int:
        """Edge permutation index coordinate for the phase 2 of Kociemba's
        algorithm.

        The value is always in range from 0 to 40319."""
        return self.__phase2_edge_coordinate(self.edges[:8])

    @property
    def coordinate_ud_slice_phase2(self) -> int:        # 0..23
        """UD Slice index coordinate for the phase 2 of Kociemba's algorithm.

        The value in always in range from 0 to 23."""
        return self.__phase2_edge_coordinate(self.edges[8:])

    def __phase2_edge_coordinate(self, edges) -> int:
        coordinate = 0

        for i, edge in enumerate(edges[1:]):
            order, i = 0, i+1
            for other_edge in edges[:i]:
                index = self.edge_order.index(edge)+1
                if other_edge in self.edge_order[index:]:
                    order += 1
            coordinate += order * factorial(i)

        return coordinate

    @classmethod
    def __fix_corner_name(cls, corner: str) -> str:
        for name in cls.corner_order:
            if sum([1 for char in corner if char in name]) == 3:
                return name
        return ""
