from src.puzzle.cube import Cube


class Simple:
    def __init__(self, cube: Cube):
        self.__cube = cube

    def solve(self) -> str:
        if self.__cube.isSolved():
            return ""
        moves = []

        moves += self.__top_cross()
        moves += self.__top_corners()

        return " ".join(moves)

    def __top_cross(self):
        pass

    def __top_corners(self):
        pass
