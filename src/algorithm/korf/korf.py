import copy

from typing import Tuple
from math import factorial

from src.puzzle.cube import Cube
from src.algorithm.korf.korf_tables import KorfTables


class Korf:
    def __init__(self, cube: Cube):
        self.__cube = cube
        self.__tables = KorfTables()
        try:
            self.__tables.load_tables()
        except FileNotFoundError:
            print("\nGenerating pruning tables...\n")
            self.generate_tables()
            self.__tables.save_tables()

    def solve(self) -> Tuple[int, str]:
        # TODO: Implement the search
        return (-1, "Solving not implemented yet!")

    def generate_tables(self) -> None:
        cube = Cube()

        for depth in range(0, 21):
            print(f"Generation Depth: {depth}")
            self.generation_search(cube, depth, 0)
            if self.__tables.is_complete:
                break
            self.__tables.print_completeness()

    def generation_search(self, cube: Cube, depth: int, distance: int) -> None:
        if depth <= 0:
            self.__tables.set_distance(self.coordinate(cube), distance)
            return
        for move in cube.moves:
            distance += 1
            new_cube = copy.deepcopy(cube)
            new_cube.twist_by_notation(move)
            self.generation_search(new_cube, depth-1, distance+1)

    @classmethod
    def coordinate(cls, cube: Cube) -> Tuple[int, int, int]:
        return (
            cls.corner_pattern(cube),
            cls.edge_pattern_first(cube),
            cls.edge_pattern_second(cube)
        )

    @staticmethod
    def corner_pattern(cube: Cube) -> int:      # 0..88,179,839
        # 2187 orientations, 40320 permutations -> 88,179,840 states
        coordinate = cube.coordinate_corner_orientation * 40_320
        return coordinate + cube.coordinate_corner_permutation

    @classmethod
    def edge_pattern_first(cls, cube: Cube) -> int:       # 0..42,577,919
        # 2^6 = 64 orientations, 12!/6! = 665,280 permutations -> 42,577,920
        order = cube.edge_order[:6]
        edges = [edge if edge in order or edge[::-1] in order else "-"
                 for edge in cube.unoriented_edges]

        return cls.__edge_pattern(order, edges)

    @classmethod
    def edge_pattern_second(cls, cube: Cube) -> int:       # 0..42,577,919
        # 2^6 = 64 orientations, 12!/6! = 665,280 permutations -> 42,577,920
        order = Cube().edge_order[6:][::-1]
        edges = [edge if edge in order or edge[::-1] in order else "-"
                 for edge in cube.unoriented_edges][::-1]

        return cls.__edge_pattern(order, edges)

    @staticmethod
    def __edge_pattern(edge_order, edges) -> int:
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
