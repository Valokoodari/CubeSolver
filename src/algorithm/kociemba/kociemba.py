from typing import Tuple, List
from src.puzzle.cube import Cube
import copy


class Kociemba:
    phase2_moves = ["U", "U'", "U2", "D", "D'", "D2", "L2", "R2", "F2", "B2"]
    phase1_moves = phase2_moves + ["L", "L'", "R", "R'", "F", "F'", "B", "B'"]
    pairs = {"U": "D", "D": "U", "L": "R", "R": "L", "F": "B", "B": "F"}

    def __init__(self, cube: Cube):
        self.__cube = cube

    def solve(self) -> Tuple[int, str]:
        if self.__cube.isSolved:
            return (0, "")
        elif self.__cube.isDomino:
            return self.__solve_domino()
        else:
            phase1 = self.__to_domino()
            if phase1[0] <= 0:
                return phase1
            print(phase1)   # DEBUG: why simple scrambles take too long
            self.__cube.twist_by_notation(phase1[1])
            return self.__solve_domino()

    def __to_domino(self) -> Tuple[int, str]:
        for depth in range(1, 20):
            print(f"Depth: {depth}")    # DEBUG: current solving depth
            result = self.__phase1([], copy.deepcopy(self.__cube), depth)
            if result[0] >= 0:
                return result
        return (-1, "")

    def __solve_domino(self) -> Tuple[int, str]:
        for depth in range(1, 12):
            print(f"Depth: {depth}")    # DEBUG: current solving depth
            result = self.__phase2([], copy.deepcopy(self.__cube), depth)
            if result[0] >= 0:
                return result
        return (-1, "")

    @staticmethod
    def __phase1(notes: List[str], cube: Cube, depth: int) -> Tuple[int, str]:
        if cube.isDomino:
            return (len(notes), " ".join(notes))
        if depth == 0:
            return (-1, "")
        for move in Kociemba.phase1_moves:
            # Skip a move which would just cancel out a previous one
            if len(notes) > 0 and move[0] == notes[-1][0]:
                continue
            if len(notes) > 1:
                if move[0] == Kociemba.pairs[notes[-1][0]] == notes[-2][0]:
                    continue
            new_cube = copy.deepcopy(cube)
            new_cube.twist_by_notation(move)
            result = Kociemba.__phase1(notes + [move], new_cube, depth-1)
            if result[0] > 0:
                return result
        return (-1, "")

    @staticmethod
    def __phase2(notes: List[str], cube: Cube, depth: int) -> Tuple[int, str]:
        if cube.isSolved:
            return (len(notes), " ".join(notes))
        if depth == 0:
            return (-1, "")
        for move in Kociemba.phase2_moves:
            # Skip a move which would just cancel out a previous one
            if len(notes) > 0 and move[0] == notes[-1][0]:
                continue
            if len(notes) > 1:
                if move[0] == Kociemba.pairs[notes[-1][0]] == notes[-2][0]:
                    continue
            new_cube = copy.deepcopy(cube)
            new_cube.twist_by_notation(move)
            result = Kociemba.__phase2(notes + [move], new_cube, depth-1)
            if result[0] > 0:
                return result
        return (-1, "")
