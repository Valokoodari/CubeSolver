"""The main module of the CubeSolver application.

The purpose for this program is to compare different methods of solving the
Rubik's cube in terms of turns and time required."""

import time

from src.puzzle.cube import Cube
from src.algorithm.simple import Simple
from src.algorithm.korf.korf import Korf
from src.algorithm.kociemba.kociemba import Kociemba


class CubeSolver:
    """A class providing the UI of the CubeSolver application.

    The method check_notation can be used to check if a string of simple cube
    notations is valid. And the UI itself can be started by running the method
    start."""
    def __init__(self):
        print("Initializing...", end="", flush=True)
        self.__cube = Cube()
        self.__simple = Simple(self.__cube)
        self.__kociemba = Kociemba(self.__cube)
        self.__korf = Korf(self.__cube)
        print(" Done.\n")

    def __choose_method(self):
        print("\nAvailable solving methods:")
        print("0 - Simple method (fast, a lot of moves)")
        print("1 - Kociemba's algorithm (slower, fewer moves")
        print("2 - Korf's algorithm (slowest, fewest moves")
        print("(r or q - return to the main menu)")

        while True:
            method = input("\nMethod: ")

            if method in ["r", "q"]:
                print()
                break

            start_time = time.time()
            solution = (-1, "")
            if method == "0":
                self.__simple.set_cube(self.__cube)
                solution = self.__simple.solve()
            elif method == "1":
                self.__kociemba.set_cube(self.__cube)
                solution = self.__kociemba.solve()
            elif method == "2":
                print()
                self.__korf.set_cube(self.__cube)
                solution = self.__korf.solve()
            else:
                print("Invalid option")
                return
            total_time = time.time()-start_time
            if solution[0] < 0:
                print(f"\nCouldn't find a solution in {total_time:.3f}" +
                      " seconds.")
            else:
                print(f"\nFound solution: {solution[1]} with {solution[0]} " +
                      f"turns in {total_time:.3f} seconds.")

    def __play(self):
        print("\nMoves should be given with the basic cube notation.")
        print("r or q will return to the main menu.\n")
        print(f"{self.__cube}\n")
        while True:
            notation = input("Next move(s): ").strip()
            if notation in ["r", "q"]:
                print()
                break

            if self.check_notation(notation):
                self.__cube.twist_by_notation(notation)
            else:
                print("Invalid notation!")

            print(f"\n{self.__cube}\n")

    @staticmethod
    def check_notation(notation: str) -> bool:
        """A function to check the validity of a string containing cube
        notation.

        For example the notation 'F2 B2 L2 R2 D2 U2' is valid but 'U3', 'U-1',
        'M', 'X', 'Y', or 'Z' are not valid."""
        if len(notation) == 0:
            return False
        for note in notation.split(" "):
            if note[0] not in ["U", "R", "F", "L", "B", "D"]:
                return False
            if len(note) > 2:
                return False
            if len(note) == 2 and note[1] not in ["'", "2"]:
                return False
        return True

    @staticmethod
    def __list_commands() -> None:
        print("Available commands:")
        print("0 - scramble (or 'g' for scramble in <U,D,L2,R2,F2,B2>")
        print("1 - solve")
        print("2 - play")
        print("3 - reset")
        print("q - quit")

    def start(self) -> None:
        """A function containing the main loop for the programs UI."""
        while True:
            print(f"{self.__cube}\n")
            self.__list_commands()

            command = input("\nCommand: ").lower()

            if command == 'q':
                break
            if command == '0':
                scramble = self.__cube.scramble()
                print(f"\nScramble: {scramble}\n")
            elif command == 'g':
                scramble = self.__cube.scramble_g1()
                print(f"\nScramble: {scramble}\n")
            elif command == '1':
                self.__choose_method()
            elif command == '2':
                self.__play()
            elif command == '3':
                print()
                self.__cube.reset()
            else:
                print("\nInvalid command!\n")


if __name__ == "__main__":
    CubeSolver().start()
