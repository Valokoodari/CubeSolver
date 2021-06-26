from test.test_variables import TEST_SIZE
from src.algorithm.simple import Simple
from src.puzzle.cube import Cube


def test_a_solved_cube_requires_0_moves():
    solution = Simple(Cube()).solve()
    assert solution == (0, "")


def test_any_cube_with_just_one_move_is_solved():
    for move in Cube.moves:
        cube = Cube()
        cube.twist_by_notation(move)
        result = Simple(cube).solve()
        cube.twist_by_notation(result[1])
        assert cube.is_solved


def test_any_random_cube_is_solved():
    for _ in range(TEST_SIZE):
        cube = Cube()
        cube.scramble()
        result = Simple(cube).solve()
        cube.twist_by_notation(result[1])
        assert cube.is_solved
