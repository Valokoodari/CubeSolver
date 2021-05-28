from src.algorithm.kociemba.kociemba import Kociemba
from src.puzzle.cube import Cube


def test_a_solved_cube_requires_0_moves():
    solution = Kociemba(Cube()).solve()

    assert solution == (0, "")


def test_a_cube_in_G1_with_4_moves_is_solved():
    cube = Cube()
    cube.twist_by_notation("U R2 B2 D'")

    solution = Kociemba(cube).solve()
    assert solution[0] > 0 and len(solution[1]) > 0

    cube.twist_by_notation(solution[1])
    assert cube.isSolved()


def test_cubes_in_G1_with_4_random_moves_are_solved():
    for _ in range(5):
        cube = Cube()
        cube.scramble_G1(4)

        solution = Kociemba(cube).solve()
        assert solution[0] >= 0 and len(solution[1]) >= 0

        cube.twist_by_notation(solution[1])
        assert cube.isSolved()


def test_cubes_with_one_random_move_are_solved():
    for _ in range(5):
        cube = Cube()
        print(cube.scramble(1))

        solution = Kociemba(cube).solve()
        print(solution)
        assert solution[0] >= 0 and len(solution[1]) >= 0

        cube.twist_by_notation(solution[1])
        assert cube.isSolved()
