from .cube_face import CubeFace
from random import choice


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

        for move in notation.strip().split(" "):
            if len(move) == 1:
                self.twist(face.index(move))
            else:
                if move[1] == "2":
                    self.twist(face.index(move[0]))
                    self.twist(face.index(move[0]))
                else:
                    self.twist(face.index(move[0]), False)

    def scramble(self) -> str:
        faces = ["R", "L", "U", "D", "F", "B"]
        options = ["", "'", "2"]
        moves = [choice(faces) + choice(options) for _ in range(20)]
        notation = " ".join(moves)
        self.twist_by_notation(notation)
        return notation

    def scramble_G1(self) -> None:
        notes = ["U", "U'", "U2", "D", "D'", "D2", "L2", "R2", "F2", "B2"]
        moves = [choice(notes) for _ in range(12)]
        notation = " ".join(moves)
        self.twist_by_notation(notation)
        return notation

    def isSolved(self) -> bool:     # Group G_2 {1}
        for face in self.__faces:
            if not face.isSolved():
                return False
        return True

    def isDomino(self) -> bool:     # Group G_1 <U, D, L2, R2, F2, B2>
        return self.__faces[0].isDomino() and self.__faces[5].isDomino()

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
