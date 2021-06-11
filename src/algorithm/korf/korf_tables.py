from pathlib import Path

from src.puzzle.cube import Cube


class KorfTables:
    def __init__(self):
        self.__path = Path(__file__).parent
        self.__corner_distances = [-1]*88_179_840
        self.__edge_first_distances = [-1]*42_577_920
        self.__edge_second_distances = [-1]*42_577_920

    def generate_tables(self):
        pass

    def save_tables(self) -> None:
        with open(f"{self.__path}/tables/corners.txt", 'w') as file:
            for distance in self.__corner_distances:
                file.write(f"{distance}\n")
        with open(f"{self.__path}/tables/edges1.txt", 'w') as file:
            for distance in self.__edge_first_distances:
                file.write(f"{distance}\n")
        with open(f"{self.__path}/tables/edges2.txt", 'w') as file:
            for distance in self.__edge_second_distances:
                file.write(f"{distance}\n")

    def load_tables(self):
        with open(f"{self.__path}/tables/corners.txt", "r") as file:
            self.__corner_distances = [int(line) for line in file.readlines()]
        with open(f"{self.__path}/tables/edges1.txt", "r") as file:
            self.__edge_first_distances = \
                    [int(line) for line in file.readlines()]
        with open(f"{self.__path}/tables/edges2.txt", "r") as file:
            self.__edge_second_distances = \
                    [int(line) for line in file.readlines()]

    def get_distance(self, cube: Cube) -> int:
        corner = cube.corner_pattern
        edge_first = cube.edge_pattern_first
        edge_second = cube.edge_pattern_second

        corner_dist = self.__corner_distances[corner]
        edge_first_dist = self.__edge_second_distances[edge_first]
        edge_second_dist = self.__edge_second_distances[edge_second]

        return max(corner_dist, edge_first_dist, edge_second_dist)
