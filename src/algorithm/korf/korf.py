from src.puzzle.cube import Cube
from src.algorithm.korf.korf_tables import KorfTables


class Korf:
    def __init__(self, cube: Cube):
        self.__cube = cube
        self.__tables = KorfTables()

    def solve(self) -> str:
        pass
