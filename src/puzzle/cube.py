from .cube_face import CubeFace
from math import factorial, comb
from random import choice
from typing import List


class Cube:
    """Neighbors, the affected line number, and -1 if the line should be
    flipped for every possible turn.
    """
    __turns = (((1, 0, 1), (2, 0, 1), (3, 0, 1), (4, 0, 1)),
               ((0, 3, 1), (4, 5, -1), (5, 3, 1), (2, 3, 1)),
               ((0, 2, -1), (1, 5, 1), (5, 0, 1), (3, 3, -1)),
               ((0, 5, 1), (2, 5, 1), (5, 5, 1), (4, 3, -1)),
               ((0, 0, -1), (3, 5, -1), (5, 2, 1), (1, 3, 1)),
               ((4, 2, 1), (3, 2, 1), (2, 2, 1), (1, 2, 1)))

    corner_order = ["URF", "UFL", "ULB", "UBR", "DFR", "DLF", "DBL", "DRB"]
    edge_order = ["UR", "UF", "UL", "UB", "DR", "DF",
                  "DL", "DB", "FR", "FL", "BL", "BR"]

    def __init__(self):
        self.__faces = [CubeFace(3, i) for i in range(6)]

    def twist(self, face_number: int, clockwise: bool = True) -> None:
        self.__faces[face_number].rotate(clockwise)

        lines = []
        direction = 1 if clockwise else -1
        for i in range(4):
            face, line, flip = self.__turns[face_number][(i + direction) % 4]
            lines.append(self.__faces[face].getLine(line)[::flip])
        for i in range(4):
            face, line, flip = self.__turns[face_number][i]
            self.__faces[face].setLine(line, lines[i][::flip])

    def twist_by_notation(self, notation: str) -> None:
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
        faces = ["R", "L", "U", "D", "F", "B"]
        options = ["", "'", "2"]
        moves = [choice(faces) + choice(options) for _ in range(count)]
        notation = " ".join(moves)
        self.twist_by_notation(notation)
        return notation

    def scramble_G1(self, count: int = 18) -> None:
        notes = ["U", "U'", "U2", "D", "D'", "D2", "L2", "R2", "F2", "B2"]
        moves = [choice(notes) for _ in range(count)]
        notation = " ".join(moves)
        self.twist_by_notation(notation)
        return notation

    def reset(self) -> None:
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
        return "".join([face.cube_string for face in self.__faces])

    @property
    def corners(self) -> List[str]:
        coords = {   # (face, facelet)
            "URF": ((0, 8), (3, 0), (2, 2)),
            "UFL": ((0, 6), (2, 0), (1, 2)),
            "ULB": ((0, 0), (1, 0), (4, 2)),
            "UBR": ((0, 2), (4, 0), (3, 2)),
            "DFR": ((5, 2), (2, 8), (3, 6)),
            "DLF": ((5, 0), (1, 8), (2, 6)),
            "DBL": ((5, 6), (4, 8), (1, 6)),
            "DRB": ((5, 8), (3, 8), (4, 6))
        }

        corners = [""]*8
        for i, corner in enumerate(self.corner_order):
            for face, facelet in coords[corner]:
                corners[i] += self.__faces[face].getFacelet(facelet)
            if corners[i] not in coords:
                corners[i] = self.__fix_corner_name(corners[i])

        return corners

    @property
    def edges(self) -> List[str]:
        coords = {
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

        edges = [""]*12
        for i, edge in enumerate(self.edge_order):
            for face, facelet in coords[edge]:
                edges[i] += self.__faces[face].getFacelet(facelet)
            if edges[i] not in self.edge_order:
                edges[i] = edges[i][::-1]

        return edges

    @property
    def isSolved(self) -> bool:     # Group G_2 {1}
        for face in self.__faces:
            if not face.isSolved:
                return False
        return True

    @property
    def isDomino(self) -> bool:     # Group G_1 <U, D, L2, R2, F2, B2>
        return self.__faces[0].isDomino and self.__faces[5].isDomino

    # Coordinates for Kociemba's phase 1
    @property
    def coordinate_corner_orientation(self) -> int:     # 0..2186
        pass

    @property
    def coordinate_edge_orientation(self) -> int:       # 0..2047
        pass

    @property
    def coordinate_ud_slice(self) -> int:               # 0..494
        edges, k, coordinate = self.edges, 3, 0

        for n in reversed(range(12)):
            if edges[n] in self.edge_order[8:]:
                k -= 1
            else:
                coordinate += comb(n, k)
            if k < 0:
                break

        return coordinate

    # Coordinates for Kociemba's phase 2
    @property
    def coordinate_corner_permutation(self) -> int:     # 0..40319
        coordinate, corners = 0, self.corners

        for i, corner in enumerate(corners[1:]):
            order, i = 0, i+1
            for c in corners[:i]:
                if c in self.corner_order[self.corner_order.index(corner)+1:]:
                    order += 1
            coordinate += order * factorial(i)

        return coordinate

    @property
    def coordinate_edge_permutation(self) -> int:       # 0..40319
        coordinate, edges = 0, self.edges[:8]

        for i, edge in enumerate(edges[1:]):
            order, i = 0, i+1
            for e in edges[:i]:
                if e in self.edge_order[self.edge_order.index(edge)+1:]:
                    order += 1
            coordinate += order * factorial(i)

        return coordinate

    @property
    def coordinate_ud_slice_phase2(self) -> int:        # 0..23
        coordinate, edges = 0, self.edges[8:]

        for i, edge in enumerate(edges[1:]):
            order, i = 0, i+1
            for e in edges[:i]:
                if e in self.edge_order[self.edge_order.index(edge)+1:]:
                    order += 1
            coordinate += order * factorial(i)

        return coordinate

    @classmethod
    def __fix_corner_name(self, corner: str) -> str:
        for name in self.corner_order:
            if sum([1 for char in corner if char in name]) == 3:
                return name
