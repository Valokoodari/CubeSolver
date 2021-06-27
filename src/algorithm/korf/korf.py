"""A module to contain the main class of Korf's algorithm."""

import copy
import os

from typing import Tuple, List
from math import factorial

from src.puzzle.cube import Cube
from src.algorithm.korf.korf_tables import KorfTables


class Korf:
    """A class for solving a Rubik's cube with optimal moves using Korf's
    algorithm."""
    def __init__(self, cube: Cube):
        self.__cube = copy.deepcopy(cube)
        self.__tables = KorfTables()
        self.__checked = 0
        self.__skipped = 0
        if "NO_TABLES" not in os.environ:
            try:    # Try to load already generated pruning tables
                self.__tables.load_tables()
            except FileNotFoundError:   # Generate the pruning tables
                print("\nGenerating pruning tables...\n")
                self.generate_tables()
                self.__tables.save_tables()

    def set_cube(self, cube) -> None:
        """A function to copy a cube into this class."""
        self.__cube = copy.deepcopy(cube)

    def solve(self) -> Tuple[int, str]:
        """A function to solve the cube with Korf's algorithm (IDA*)."""
        if self.__cube.is_solved:
            return (0, "")
        estimate = self.__tables.get_distance(self.coordinate(self.__cube))
        for depth in range(estimate if estimate >= 0 else 1, 21):
            self.__checked, self.__skipped = 0, 0
            if estimate < 0:
                estimate = 21
            result = self.__search([], self.__cube, depth, estimate)
            print(f"Depth: {depth:2d}, checked: {self.__checked:,}, " +
                  f"(pruned: {self.__skipped:,}+)    ")
            if result[0] != -1:
                return result

        return (-1, "")

    def __search(self, notes: List[str], cube: Cube, depth: int,
                 estimate: int) -> Tuple[int, str]:
        """A function to actually perform the search to the current search depth
        by using recursion. Also contains the pruning if the minimum distance
        increases"""
        if self.__checked % 10000 == 0:
            print(f"Depth: {depth:2d}, checked: {self.__checked:,}+, " +
                  f"(pruned: {self.__skipped:,}+)", end="\r")
        if len(notes) >= depth or estimate <= 0:
            if cube.is_solved:
                return (len(notes), " ".join(notes))
            return (-1, "")
        for move in cube.moves:
            if Cube.skip_move(notes, move):
                self.__skipped += 1
                continue
            new_cube = copy.deepcopy(cube)
            new_cube.twist_by_notation(move)
            new_estimate = self.__tables.get_distance(self.coordinate(cube))
            if new_estimate != -1:
                if estimate < new_estimate:
                    self.__skipped += 1
                    continue
                estimate = new_estimate + 1
            self.__checked += 1
            result = self.__search(notes + [move], new_cube, depth, estimate-1)
            if result[0] > 0:
                return result
        return (-1, "")

    def generate_tables(self) -> None:
        """A function to generate the pruning tables for Korf's algorithm by
        iterating through search depths from 0 to 20."""
        cube = Cube()

        for depth in range(0, 8):   # FIXME: Should be 0..20 range(0, 21)
            print(f"Generation Depth: {depth}")
            self.generation_search([], cube, depth, 0)
            if self.__tables.is_complete:
                break
            self.__tables.print_completeness()

    def generation_search(self, notes: List[str], cube: Cube, depth: int,
                          distance: int) -> None:
        """A function to search all of the patterns indexes to generate the
        pruning tables required by the Korf's algorithm to solve any cube in
        less than about 10^12 years.

        Unfortunately this function currently takes about 10^13 years with depth
        20 to finish on a modern desktop computer."""
        # FIXME: Optimize to run in less than a week.
        # FIXME: Pruning while generating doesn't seem to work correctly.
        if distance >= depth:
            self.__tables.set_distance(self.coordinate(cube), distance)
            return
        for move in cube.moves:
            if Cube.skip_move(notes, move):
                continue
            new_cube = copy.deepcopy(cube)
            new_cube.twist_by_notation(move)
            estimate = self.__tables.get_distance(self.coordinate(new_cube))
            if estimate != -1 and estimate-depth < distance:
                # print(f"Depth: {depth}, distance: {distance}, move: {move}")
                continue
            self.generation_search(notes+[move], new_cube, depth, distance+1)

    @classmethod
    def coordinate(cls, cube: Cube) -> Tuple[int, int, int]:
        """A function to return a single tuple containing all of the pattern
        indexes used by Korf's algorithm."""
        return (
            cls.corner_pattern(cube),
            cls.edge_pattern_first(cube),
            cls.edge_pattern_second(cube)
        )

    @staticmethod
    def corner_pattern(cube: Cube) -> int:
        """A function to calculate the corner pattern index of a cube for the
        Korf's algorithm.

        The pattern is a combination of the corner orientation (0..2,086) and
        permutation indexes (0..40,319) which means that the value is always
        between 0 and 88,179,839."""
        coordinate = cube.coordinate_corner_orientation * 40_320
        return coordinate + cube.coordinate_corner_permutation

    @classmethod
    def edge_pattern_first(cls, cube: Cube) -> int:
        """A function to calculate the edge pattern index for the first six
        edges of a cube for Korf's algorithm.

        The pattern is a combination of the orientation (0..63) and the
        permutation (0..665,219) of the first six edges of the cube. Which
        means that the value of index of the pattern is always between 0 and
        42,577,919."""
        order = cube.edge_order[:6]
        edges = [edge if edge in order or edge[::-1] in order else "-"
                 for edge in cube.unoriented_edges]

        return cls.__edge_pattern(order, edges)

    @classmethod
    def edge_pattern_second(cls, cube: Cube) -> int:
        """A function to calculate the edge pattern index for the last six
        edges of a cube for Korf's algorithm.

        The pattern is a combination of the orientation (0..63) and the
        permutation (0..665,219) of the last six edges of the cube. Which
        means that the value of index of the pattern is always between 0 and
        42,577,919."""
        order = Cube().edge_order[6:][::-1]
        edges = [edge if edge in order or edge[::-1] in order else "-"
                 for edge in cube.unoriented_edges][::-1]

        return cls.__edge_pattern(order, edges)

    @staticmethod
    def __edge_pattern(edge_order, edges) -> int:
        """A function to calculate the edge pattern index for the given edges.
        This is only intended for use by the functions edge_pattern_first and
        edge_pattern_second."""
        count, orientation = 0, 0
        for i, edge in enumerate(edges):
            if edge == "-":
                continue
            if edge not in edge_order:
                edges[i] = edge[::-1]
                orientation += 2 ** count
            count += 1

        permutation = 0
        for i, edge_name in enumerate(edge_order):
            order = 0
            for edge in edges[:edges.index(edge_name)]:
                if edge in edge_order[i:] or edge == "-":
                    order += 1
            permutation += order * (factorial(11-i) / factorial(6))

        return int(orientation * 665_280 + permutation)
