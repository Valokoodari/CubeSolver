"""A module to contain the class KorfTables"""
import os

from typing import Tuple
from pathlib import Path


class KorfTables:
    """A class to handle the short and long term storage for the pruning tables
    of the Korf's algorithm and also the checking of the minimum distance to
    solved."""
    def __init__(self):
        self.__path = f"{Path(__file__).parent}/tables"
        self.__corner_distances = [-1]*88_179_840
        self.__edge_first_distances = [-1]*42_577_920
        self.__edge_second_distances = [-1]*42_577_920
        self.__corner_distances[0] = 0
        self.__edge_first_distances[0] = 0
        self.__edge_second_distances[0] = 0

    def save_tables(self) -> None:
        if not os.path.exists(self.__path):
            os.makedirs(self.__path)
        """A function to save the pruning tables to files."""
        with open(f"{self.__path}/corners.txt", 'w') as file:
            for distance in self.__corner_distances:
                file.write(f"{distance}\n")
        with open(f"{self.__path}/edges1.txt", 'w') as file:
            for distance in self.__edge_first_distances:
                file.write(f"{distance}\n")
        with open(f"{self.__path}/edges2.txt", 'w') as file:
            for distance in self.__edge_second_distances:
                file.write(f"{distance}\n")

    def load_tables(self) -> None:
        """A function to load the pruning tables from files."""
        with open(f"{self.__path}/corners.txt", "r") as file:
            self.__corner_distances = [int(line) for line in file.readlines()]
        with open(f"{self.__path}/edges1.txt", "r") as file:
            self.__edge_first_distances = \
                    [int(line) for line in file.readlines()]
        with open(f"{self.__path}/edges2.txt", "r") as file:
            self.__edge_second_distances = \
                    [int(line) for line in file.readlines()]

    def set_distance(self, coordinate: Tuple[int, int, int], distance: int) \
            -> None:
        """A function to save the minimum distances to a solved cube by the
        coordinate of a cube."""
        if self.__corner_distances[coordinate[0]] == -1:
            self.__corner_distances[coordinate[0]] = distance
        if self.__edge_first_distances[coordinate[1]] == -1:
            self.__edge_first_distances[coordinate[1]] = distance
        if self.__edge_second_distances[coordinate[1]] == -1:
            self.__edge_second_distances[coordinate[1]] = distance

    def get_distance(self, coordinate: Tuple[int, int, int]) -> int:
        """A function to check the minimum distance to a solved cube by the
        given coordinates of a cube."""
        corner_dist = self.__corner_distances[coordinate[0]]
        edge_first_dist = self.__edge_second_distances[coordinate[1]]
        edge_second_dist = self.__edge_second_distances[coordinate[2]]

        if min(corner_dist, edge_first_dist, edge_second_dist) == -1:
            return -1

        return max(corner_dist, edge_first_dist, edge_second_dist)

    @property
    def is_complete(self) -> bool:
        """A property to tell if there are still any coordinates without known
        minimum distances to a solved cube."""
        if self.__corner_distances.count(-1) > 0:
            return False
        if self.__edge_first_distances.count(-1) > 0:
            return False
        return self.__edge_second_distances.count(-1) == 0

    def print_completeness(self) -> None:
        """A function to print the current completeness state of the pruning
        tables. This is to see the actual progress when generating the tables.
        """
        size = len(self.__corner_distances)
        missing = self.__corner_distances.count(-1)
        print(f"Corners: {size - missing} / {size}")
        size = len(self.__edge_first_distances)
        missing = self.__edge_first_distances.count(-1)
        print(f"Edges 1: {size - missing} / {size}")
        size = len(self.__edge_second_distances)
        missing = self.__edge_second_distances.count(-1)
        print(f"Edges 2: {size - missing} / {size}\n")
