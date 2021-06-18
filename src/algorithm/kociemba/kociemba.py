"""A module to contain the main class of Kociemba's algorithm."""

import copy

from typing import Tuple, List

# from src.algorithm.kociemba.kociemba_tables import KociembaTables
from src.puzzle.cube import Cube


class Kociemba:
    """A class for solving a Rubik's cube with almost optimal moves using
    Kociemba's algorithm."""
    phase2_moves = ["U", "U'", "U2", "D", "D'", "D2", "L2", "R2", "F2", "B2"]

    def __init__(self, cube: Cube):
        self.__cube = cube
        # self.__checked = set()
        self.__checked = 0
        # self.__tables = KociembaTables

    def solve(self) -> Tuple[int, str]:
        """A function to solve the cube with Kociemba's algorithm (two-phase)"""
        if self.__cube.is_solved:
            return (0, "")
        if self.__cube.is_domino:
            return self.__solve_phase(2)

        phase1 = self.__solve_phase(1)
        self.__cube.twist_by_notation(phase1[1])
        if self.__cube.is_solved or phase1[0] <= 0:
            return phase1
        # FIXME: debug print, how the domino state was reached
        print(f"Current steps: {phase1[1]}")
        phase2 = self.__solve_phase(2)
        return (phase1[0]+phase2[0], phase1[1] + " " + phase2[1])

    def __solve_phase(self, phase) -> Tuple[int, str]:
        """A function to handle the iterative deepening for the search."""
        print(f"\n-- Phase {phase} --")
        for depth in range(1, 13 if phase == 1 else 19):
            # self.__checked.clear()
            self.__checked = 0
            result = self.__search(phase, [], copy.deepcopy(self.__cube),
                                   depth, 0)
            # FIXME: debug print, cube orientations checked with current depth
            print(f"Depth: {depth:2d}, checked: {self.__checked:,}  ")
            if result[0] >= 0:
                return result
        return (-1, "")

    def __search(self, phase, notes: List[str], cube: Cube,
                 depth: int, distance: int) -> Tuple[int, str]:
        """A function to actually perform the search to the current search depth
        by using recursion. Also contains the pruning if the minimum distance
        increases"""
        # TODO: Add the actual pruning based on the minimum distance.
        if self.__checked % 10000 == 0:
            print(f"Depth: {depth:2d}, checked: {self.__checked:,}+", end="\r")
        if depth <= distance:
            if phase == 1 and cube.is_domino or cube.is_solved:
                return (len(notes), " ".join(notes))
            return (-1, "")
        for move in Cube.moves if phase == 1 else self.phase2_moves:
            if Cube.skip_move(notes, move):
                continue
            new_cube = copy.deepcopy(cube)
            new_cube.twist_by_notation(move)
            # if new_cube.cube_string in self.__checked:
            #     continue
            # self.__checked.add(new_cube.cube_string)
            self.__checked += 1
            result = self.__search(phase, notes + [move], new_cube,
                                   depth, distance + 1)
            if result[0] > 0:
                return result
        return (-1, "")
