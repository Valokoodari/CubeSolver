from test.test_variables import TEST_SIZE, CHECKERBOARD_NOTATION

from src.algorithm.korf.korf import Korf
from src.puzzle.cube import Cube


# Calculation of the indexes

def test_corner_pattern_is_0_for_a_solved_cube():
    assert Korf(Cube()).corner_pattern == 0


def test_corner_patter_is_always_in_the_correct_range():
    for _ in range(TEST_SIZE):
        cube = Cube()
        cube.scramble()

        assert 0 <= Korf(cube).corner_pattern <= 88_179_839


def test_edge_pattern_first_is_0_for_a_solved_cube():
    assert Korf(Cube()).edge_pattern_first == 0


def test_edge_pattern_first_is_correct_for_checkerboard():
    cube = Cube()
    cube.twist_by_notation(CHECKERBOARD_NOTATION)

    assert Korf(cube).edge_pattern_first == 365136


def test_edge_pattern_first_is_always_in_the_correct_range():
    for _ in range(TEST_SIZE):
        cube = Cube()
        cube.scramble()

        assert 0 <= Korf(cube).edge_pattern_first <= 42_577_919


def test_edge_pattern_second_is_0_for_a_solved_cube():
    assert Korf(Cube()).edge_pattern_second == 0


def test_edge_pattern_second_is_correct_for_checkerboard():
    cube = Cube()
    cube.twist_by_notation(CHECKERBOARD_NOTATION)

    assert Korf(cube).edge_pattern_second == 121008


def test_edge_pattern_second_is_always_in_the_correct_range():
    for _ in range(TEST_SIZE):
        cube = Cube()
        cube.scramble()

        assert 0 <= Korf(cube).edge_pattern_second <= 42_577_919
