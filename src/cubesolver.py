from src.puzzle.cube import Cube
from src.algorithm.kociemba.kociemba import Kociemba
import copy
import time

class CubeSolver:
    def __init__(self):
        self.__cube = Cube()

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
            elif method == "0":
                print("Not implemented yet.")
            elif method == "1":
                startTime = time.time()
                solution = Kociemba(copy.deepcopy(self.__cube)).solve()
                totalTime = time.time()-startTime
                if solution[0] < 0:
                    print(f"Couldn't find a solution in {totalTime:.3f} seconds.")
                else:
                    print(f"Found solution: {solution[1]} in {totalTime:.3f} seconds.")
            elif method == "2":
                print("Not implemented yet.")
            else:
                print("Invalid option")

    def __play(self):
        print("\nMoves should be given with the basic cube notation.")
        print("r or q will return to the main menu.\n")
        print(f"{self.__cube}\n")
        while True:
            notation = input("Next move(s): ").strip()
            if notation in ["r", "q"]:
                print()
                break

            if self.__check_notation(notation):
                self.__cube.twist_by_notation(notation)
            else:
                print("Invalid notation!")

            print(f"\n{self.__cube}\n")

    def __check_notation(self, notation: str) -> bool:
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

    def __list_commands(self) -> None:
        print("Available commands:")
        print("0 - scramble (or 'g' for scramble in <U,D,L2,R2,F2,B2>")
        print("1 - solve")
        print("2 - play")
        print("3 - reset")
        print("q - quit")

    def start(self) -> None:
        while True:
            print(f"{self.__cube}\n")
            self.__list_commands()

            command = input("\nCommand: ").lower()

            if command == 'q':
                break
            elif command == '0':
                scramble = self.__cube.scramble()
                print(f"\nScramble: {scramble}\n")
            elif command == 'g':
                scramble = self.__cube.scramble_G1()
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
