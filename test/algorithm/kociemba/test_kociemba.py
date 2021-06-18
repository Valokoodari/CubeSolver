from src.algorithm.kociemba.kociemba import Kociemba
from src.puzzle.cube import Cube
import copy


def test_a_solved_cube_requires_0_moves():
    solution = Kociemba(Cube()).solve()

    assert solution == (0, "")


def test_a_cube_in_G1_with_4_moves_is_solved():
    cube = Cube()
    cube.twist_by_notation("U R2 B2 D'")

    solution = Kociemba(copy.deepcopy(cube)).solve()
    assert solution[0] > 0 and len(solution[1]) > 0

    cube.twist_by_notation(solution[1])
    assert cube.is_solved


def test_cubes_in_G1_with_4_random_moves_are_solved():
    for _ in range(5):
        cube = Cube()
        cube.scramble_g1(4)

        solution = Kociemba(copy.deepcopy(cube)).solve()
        assert solution[0] >= 0 and len(solution[1]) >= 0

        cube.twist_by_notation(solution[1])
        assert cube.is_solved


def test_all_cubes_with_one_move_are_solved():
    for move in Cube.moves:
        cube = Cube()
        cube.twist_by_notation(move)

        solution = Kociemba(copy.deepcopy(cube)).solve()
        assert solution[0] >= 1

        cube.twist_by_notation(solution[1])
        assert cube.is_solved


def test_checkerboard_is_solved_with_6_moves():
    cube = Cube()
    cube.twist_by_notation("U2 D2 F2 B2 L2 R2")

    solution = Kociemba(copy.deepcopy(cube)).solve()
    assert solution[0] == 6

    cube.twist_by_notation(solution[1])
    assert cube.is_solved
