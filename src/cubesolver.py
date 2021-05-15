from puzzle.cube import Cube


class CubeSolver:
    def start(self):
        cube = Cube()
        cube.scramble()

        print(f"{cube}\n")
        while True:
            move = input("Next move: ")
            if move == "-1":
                break

            cube.twist_by_notation(move)
            print(f"\n{cube}\n")


if __name__ == "__main__":
    CubeSolver().start()
