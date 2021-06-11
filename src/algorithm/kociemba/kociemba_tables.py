from pathlib import Path

from src.puzzle.cube import Cube


class KociembaTables:
    def __init__(self):
        self.__path = Path(__file__).parent
        self.__phase1 = [-1]*140_908_410
        self.__phase2 = [-1]*111_605_760

    def generate_tables(self):
        pass

    def save_tables(self) -> None:
        with open(f"{self.__path}/tables/phase1.txt", 'w') as file:
            for distance in self.__phase1:
                file.write(f"{distance}\n")
        with open(f"{self.__path}/tables/phase2.txt", 'w') as file:
            for distance in self.__phase2:
                file.write(f"{distance}\n")

    def load_tables(self):
        with open(f"{self.__path}/tables/phase1.txt", 'w') as file:
            self.__phase1 = [int(line) for line in file.readlines()]
        with open(f"{self.__path}/tables/phase2.txt", 'w') as file:
            self.__phase2 = [int(line) for line in file.readlines()]

    def get_distance(self, phase: int, cube: Cube) -> int:
        pass
