from typing import Tuple, List
from src.puzzle.cube import Cube
import copy


class Kociemba:
    phase2_moves = ["U", "U'", "U2", "D", "D'", "D2", "L2", "R2", "F2", "B2"]
    phase1_moves = phase2_moves + ["L", "L'", "R", "R'", "F", "F'", "B", "B'"]
    pairs = {"U": "D", "L": "R", "F": "B", "D": "U", "R": "L", "B": "F"}

    def __init__(self, cube: Cube):
        self.__cube = cube

    def solve(self) -> Tuple[int, str]:
        if self.__cube.isSolved:
            return (0, "")
        elif self.__cube.isDomino:
            return self.__solve_domino()
        else:
            phase1 = self.__to_domino()
            # print(phase1)   # DEBUG: why simple scrambles take too long
            self.__cube.twist_by_notation(phase1[1])
            if self.__cube.isSolved or phase1[0] <= 0:
                return phase1
            phase2 = self.__solve_domino()
            return (phase1[0]+phase2[0], phase1[1] + " " + phase2[1])

    # TODO: __to_domino and __solve_domino are mostly copy-paste

    def __to_domino(self) -> Tuple[int, str]:
        print("-- Phase 1 --")
        for depth in range(1, 13):  # At most 12 moves are needed
            self.__checked = 0
            # DEBUG: current solving depth
            print(f"Depth: {depth:2d}", end="", flush=True)
            result = self.__search(self.__isDomino, self.phase1_moves, [],
                                   copy.deepcopy(self.__cube), depth)
            # DEBUG: cube orientations checked with current depth
            print(f", checked: {self.__checked}")
            if result[0] >= 0:
                return result
        return (-1, "")

    def __solve_domino(self) -> Tuple[int, str]:
        print("-- Phase 2 --")
        for depth in range(1, 19):  # At most 18 moves are needed
            self.__checked = 0
            # DEBUG: current solving depth
            print(f"Depth: {depth:2d}", end="", flush=True)
            result = self.__search(self.__isSolved, self.phase2_moves, [],
                                   copy.deepcopy(self.__cube), depth)
            # DEBUG: cube orientations checked with current depth
            print(f", checked: {self.__checked}")
            if result[0] >= 0:
                return result
        return (-1, "")

    def __search(self, check, moves: List[str], notes: List[str], cube: Cube,
                 depth: int) -> Tuple[int, str]:
        if depth == 0:
            if check(cube):
                return (len(notes), " ".join(notes))
            return (-1, "")
        for move in moves:
            if self.__skip_move(notes, move):
                continue
            new_cube = copy.deepcopy(cube)
            new_cube.twist_by_notation(move)
            self.__checked += 1
            result = self.__search(check, moves, notes + [move], new_cube,
                                   depth - 1)
            if result[0] > 0:
                return result
        return (-1, "")

    @staticmethod
    def __skip_move(notes: List[str], move):
        if len(notes) > 0:
            # Don't turn the same side twice in a row. E.g. don't allow F F
            if move[0] == notes[-1][0]:
                return True
            # Don't test for example both R L and L R
            if move[0] in list(Kociemba.pairs)[:3]:
                if notes[-1][0] == Kociemba.pairs[move[0]]:
                    return True
        # Don't turn the same side if the side has not changed at all
        if len(notes) > 1:
            if move[0] == Kociemba.pairs[notes[-1][0]] == notes[-2][0]:
                return True

        return False

    @staticmethod
    def __isDomino(cube: Cube) -> bool:
        return cube.isDomino

    @staticmethod
    def __isSolved(cube: Cube) -> bool:
        return cube.isSolved
