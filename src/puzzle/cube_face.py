from typing import List


class CubeFace:
    colors = ('W', 'R', 'B', 'O', 'G', 'Y')

    def __init__(self, size: int, color: int):
        self.__size = size
        self.__facelets = [[color]*size for _ in range(size)]

    @property
    def facelets(self) -> List[List[int]]:
        return self.__facelets[:]

    def getLine(self, line_number: int) -> List[int]:
        line = [0, 0, 0]

        if line_number < self.__size:
            line = self.__facelets[line_number][:]
        else:
            for row in range(self.__size):
                line[row] = self.__facelets[row][line_number-self.__size]

        return line

    def setLine(self, line_number: int, line: List[int]) -> None:
        if line_number < self.__size:
            self.__facelets[line_number] = line
            return
        for row in range(self.__size):
            self.__facelets[row][line_number-self.__size] = line[row]

    def rotate(self, clockwise: bool = True) -> None:
        if clockwise:
            self.__facelets = list(zip(*self.__facelets[::-1]))
        else:
            self.__facelets = list(zip(*self.__facelets))[::-1]

        self.__facelets = [list(row) for row in self.__facelets]

    def isSolved(self) -> bool:
        return self.__facelets.count(self.__facelets[0]) == len(self.__facelets)

    def isDomino(self) -> bool:
        for n in range(1, 5):
            for row in self.__facelets:
                if n in row:
                    return False
        return True

    @property
    def cube_string(self) -> str:
        colors = []
        for row in range(self.__size):
            for col in range(self.__size):
                colors.append(self.colors[self.__facelets[row][col]])
        return "".join(colors)
