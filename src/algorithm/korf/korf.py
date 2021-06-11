from math import factorial

from src.puzzle.cube import Cube
# from src.algorithm.korf.korf_tables import KorfTables


class Korf:
    def __init__(self, cube: Cube):
        self.__cube = cube
        # self.__tables = KorfTables()

    def solve(self) -> str:
        pass

    @property
    def corner_pattern(self) -> int:      # 0..88,179,839
        # 2187 orientations, 40320 permutations -> 88,179,840 states
        coordinate = self.__cube.coordinate_corner_orientation * 40_320
        return coordinate + self.__cube.coordinate_corner_permutation

    @property
    def edge_pattern_first(self) -> int:       # 0..42,577,919
        # 2^6 = 64 orientations, 12!/6! = 665,280 permutations -> 42,577,920
        order = Cube().edge_order[:6]
        edges = [edge if edge in order or edge[::-1] in order else "-"
                 for edge in self.__cube.unoriented_edges]

        return self.__edge_pattern(order, edges)

    @property
    def edge_pattern_second(self) -> int:       # 0..42,577,919
        # 2^6 = 64 orientations, 12!/6! = 665,280 permutations -> 42,577,920
        order = Cube().edge_order[6:][::-1]
        edges = [edge if edge in order or edge[::-1] in order else "-"
                 for edge in self.__cube.unoriented_edges][::-1]

        return self.__edge_pattern(order, edges)

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
