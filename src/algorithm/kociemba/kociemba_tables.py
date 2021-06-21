"""A module to contain the class KociembaTables."""

from pathlib import Path
from typing import Tuple


class KociembaTables:
    """A class to handle the short and long term storage for the pruning tables
    of the Kociemba's algorithm. Also handles the checking of the minimum
    distance to the next group (Totally scrambled -> Domino -> Solved)."""
    def __init__(self):
        self.__path = Path(__file__).parent
        self.__phase1 = [-1]*140_908_410
        self.__phase2 = [-1]*111_605_760

    def set_distance(self, phase: int, coord: Tuple[int, int, int]) -> bool:
        """A function to set the minimum distance values to the pruning tables
        based on the given cube."""
        # TODO: implement this setter, requires the calculation of
        # the sym-coordinates first

    def save_tables(self) -> None:
        """A function to save the current state of the pruning tables in memory
        to files.
        """
        with open(f"{self.__path}/tables/phase1.txt", 'w') as file:
            for distance in self.__phase1:
                file.write(f"{distance}\n")
        with open(f"{self.__path}/tables/phase2.txt", 'w') as file:
            for distance in self.__phase2:
                file.write(f"{distance}\n")

    def load_tables(self):
        """A function to load the pruning tables to memory from files."""
        with open(f"{self.__path}/tables/phase1.txt", 'w') as file:
            self.__phase1 = [int(line) for line in file.readlines()]
        with open(f"{self.__path}/tables/phase2.txt", 'w') as file:
            self.__phase2 = [int(line) for line in file.readlines()]

    def get_distance(self, phase: int, coord: Tuple[int, int, int]) -> int:
        """A function to get the minimum distance to the next group for the
        given Cube."""
        # TODO: implement this getter, requires the calculation of
        # the sym-coordinates first
