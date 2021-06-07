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
            return self.__solve_phase(2)
        else:
            phase1 = self.__solve_phase(1)
            self.__cube.twist_by_notation(phase1[1])
            if self.__cube.isSolved or phase1[0] <= 0:
                return phase1
            # DEBUG: how the domino state was reached
            print(f"Current steps: {phase1[1]}")
            phase2 = self.__solve_phase(2)
            return (phase1[0]+phase2[0], phase1[1] + " " + phase2[1])

    def __solve_phase(self, phase) -> Tuple[int, str]:
        print(f"-- Phase {phase} --")
        for depth in range(1, 13 if phase == 1 else 19):
            # TODO: Takes way too much memory and is slowish but still
            # better than nothing when there are no pruning tables.
            self.__checked = []
            # DEBUG: current solcing depth
            print(f"Depth: {depth:2d}", end="", flush=True)
            result = self.__search(phase, [], copy.deepcopy(self.__cube), depth)
            # DEBUG: cube orientations checked with current depth
            print(f", checked: {len(self.__checked)}")
            if result[0] >= 0:
                return result
        return (-1, "")

    def __search(self, phase, notes: List[str], cube: Cube,
                 depth: int) -> Tuple[int, str]:
        if depth == 0:
            if phase == 1 and cube.isDomino or cube.isSolved:
                return (len(notes), " ".join(notes))
            return (-1, "")
        for move in self.phase1_moves if phase == 1 else self.phase2_moves:
            if self.__skip_move(notes, move):
                continue
            new_cube = copy.deepcopy(cube)
            new_cube.twist_by_notation(move)
            if new_cube.cube_string in self.__checked:
                break
            self.__checked.append(new_cube.cube_string)
            result = self.__search(phase, notes + [move], new_cube, depth - 1)
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
