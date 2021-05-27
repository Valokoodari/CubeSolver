from typing import Tuple
from src.puzzle.cube import Cube
import copy


class Kociemba:
    phase2_moves = ["U", "U'", "U2", "D", "D'", "D2", "L2", "R2", "F2", "B2"]

    def __init__(self, cube: Cube):
        self.__cube = cube

    def solve(self) -> Tuple[int, str]:
        if self.__cube.isSolved():
            return ""
        elif self.__cube.isDomino():
            return self.__solve_domino()
        else:
            return (-1, "The cube is not in G1!!!")

    def __solve_domino(self) -> Tuple[int, str]:
        for depth in range(1, 12):
            count, notes = self.__search("", copy.deepcopy(self.__cube), depth)
            if count != -1:
                return (count, notes)
        return (-1, "")

    @staticmethod
    def __search(notation: str, cube: Cube, depth: int) -> Tuple[int, str]:
        if cube.isSolved():
            return (len(notation.trim().split(" ")), notation)
        if depth == 0:
            return (-1, "")
        for m in Kociemba.phase2_moves:
            new_cube = copy.deepcopy(cube)
            new_cube.twist_by_notation(m)
            count,notes = Kociemba.__search(f"{notation} {m}", new_cube, depth-1)
            if count != -1: return (count, notes)
        return (-1, "")
