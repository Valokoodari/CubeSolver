from test.test_variables import TEST_SIZE, SOLVED_STR, CHECKERBOARD_TURNS, \
        CHECKERBOARD, CHECKERBOARD_NOTATION, CUBE_IN_THE_CUBE_NOTATION, \
        CUBE_IN_THE_CUBE, CUBE_IN_THE_CUBE_EDGES
from src.puzzle.cube import Cube


def test_the_str_of_a_solved_cube_is_correct():
    assert str(Cube()) == SOLVED_STR


def test_a_solved_cube_is_solved():
    assert Cube().is_solved


def test_R2_L2_is_not_solved():
    cube = Cube()
    cube.twist_by_notation("R2 L2")

    assert not cube.is_solved


def test_a_scrambled_cube_is_not_solved():
    cube = Cube()
    cube.scramble()

    assert not cube.is_solved


def test_CHECKERBOARD_pattern_with_single_twists():
    cube = Cube()

    for turn in CHECKERBOARD_TURNS:
        cube.twist(turn)

    assert cube.cube_string == CHECKERBOARD


def test_CHECKERBOARD_pattern_with_notation():
    cube = Cube()
    cube.twist_by_notation(CHECKERBOARD_NOTATION)

    assert cube.cube_string == CHECKERBOARD


def test_CUBE_IN_THE_CUBE_pattern():
    cube = Cube()
    cube.twist_by_notation(CUBE_IN_THE_CUBE_NOTATION)

    assert cube.cube_string == CUBE_IN_THE_CUBE


def test_cube_is_solved_after_reset():
    cube = Cube()
    cube.scramble()
    cube.twist(2)
    cube.twist_by_notation("U2 B D'")
    cube.reset()

    assert cube.is_solved


def test_solved_cube_is_domino():
    assert Cube().is_domino


def test_CHECKERBOARD_is_domino():
    cube = Cube()
    cube.twist_by_notation(CHECKERBOARD_NOTATION)

    assert cube.is_domino


def test_CUBE_IN_THE_CUBE_is_not_domino():
    cube = Cube()
    cube.twist_by_notation(CUBE_IN_THE_CUBE_NOTATION)

    assert not cube.is_domino


def test_random_cubes_in_G1_are_domino():
    for _ in range(5):
        cube = Cube()
        cube.scramble_g1()
        assert cube.is_domino


def test_cube_string_of_a_solved_cube_is_correct():
    SOLVED_STRing = "UUUUUUUUULLLLLLLLLFFFFFFFFFRRRRRRRRRBBBBBBBBBDDDDDDDDD"
    cube_string = Cube().cube_string

    assert SOLVED_STRing == cube_string


def test_empty_notation_doesnt_affect_the_cube():
    cube = Cube()
    cube.twist_by_notation("")

    assert cube.is_solved


def test_random_scramble_has_all_corners():
    for _ in range(10):
        cube = Cube()
        cube.scramble()

        assert None not in cube.corners


def test_random_scramble_has_one_of_each_corner():
    for _ in range(10):
        cube = Cube()
        cube.scramble()
        corners = cube.corners

        for corner in Cube.corner_order:
            assert corner in corners


def test_edges_of_a_solved_cube_are_correct():
    assert Cube().edges == Cube.edge_order


def test_edges_of_CUBE_IN_THE_CUBE_are_correct():
    cube = Cube()
    cube.twist_by_notation(CUBE_IN_THE_CUBE_NOTATION)

    assert cube.edges == CUBE_IN_THE_CUBE_EDGES


def test_random_scramble_has_one_of_each_edge():
    for _ in range(10):
        cube = Cube()
        cube.scramble()
        edges = cube.edges

        for edge in Cube.edge_order:
            assert edge in edges


# Properties of the cube for Kociemba's algorithm

def test_triple_is_0_for_a_solved_cube():
    assert Cube().triple == (0, 0, 0)


def test_triple_is_always_0_for_a_cube_in_G1():
    for _ in range(TEST_SIZE):
        cube = Cube()
        cube.scramble_g1()

        assert cube.triple == (0, 0, 0)


def test_triple_is_never_0_for_a_cube_not_in_G1():
    for _ in range(TEST_SIZE):
        cube = Cube()
        while cube.is_domino:
            cube.scramble()

        assert cube.triple != (0, 0, 0)


def test_coordinate_corner_orientation_is_0_for_a_solved_cube():
    assert Cube().coordinate_corner_orientation == 0


def test_coordinate_corner_orientation_of_cube_in_G1_is_always_0():
    for _ in range(TEST_SIZE):
        cube = Cube()
        cube.scramble_g1()

        assert cube.coordinate_corner_orientation == 0


def test_coordinate_corner_orientation_is_always_between_0_and_2186():
    for _ in range(TEST_SIZE):
        cube = Cube()
        cube.scramble()

        assert 0 <= cube.coordinate_corner_orientation <= 2186


def test_coordinate_corner_orientation_is_correct_after_R():
    cube = Cube()
    cube.twist_by_notation("R")

    assert cube.coordinate_corner_orientation == 1494


def test_coordinate_edge_orientation_is_0_for_a_solved_cube():
    assert Cube().coordinate_edge_orientation == 0


def test_coordinate_edge_orientation_of_cube_in_G1_is_always_0():
    for _ in range(TEST_SIZE):
        cube = Cube()
        cube.scramble_g1()

        assert cube.coordinate_edge_orientation == 0


def test_coordinate_edge_orientation_is_not_0_after_rB_rR():
    cube = Cube()
    cube.twist_by_notation("B' R'")

    assert cube.coordinate_edge_orientation != 0


def test_coordinate_edge_orientation_is_always_between_0_and_2047():
    for _ in range(TEST_SIZE):
        cube = Cube()
        cube.scramble()

        assert 0 <= cube.coordinate_edge_orientation <= 2047


def test_coordinate_ud_slice_of_a_solved_cube_is_0():
    assert Cube().coordinate_ud_slice == 0


def test_coordinate_ud_slice_of_cube_in_G1_is_always_0():
    for _ in range(TEST_SIZE):
        cube = Cube()
        cube.scramble_g1()

        assert cube.coordinate_ud_slice == 0


def test_coordinate_ud_slice_is_correct_after_R_L_D_F2_B2():
    cube = Cube()
    cube.twist_by_notation("R L D F2 B2")

    assert cube.coordinate_ud_slice == 494


def test_coordinate_ud_slice_is_always_between_0_and_494():
    for _ in range(TEST_SIZE):
        cube = Cube()
        cube.scramble()

        assert 0 <= cube.coordinate_ud_slice <= 494


def test_triple2_is_0_for_a_solved_cube():
    assert Cube().triple2 == (0, 0, 0)


def test_triple_is_never_0_for_an_unsolved_cube():
    for _ in range(TEST_SIZE):
        cube = Cube()
        while cube.is_solved:
            cube.scramble()

        assert cube.triple != (0, 0, 0)


def test_coordinate_corner_permutation_is_0_for_a_solved_cube():
    assert Cube().coordinate_corner_permutation == 0


def test_coordinate_corner_permutation_is_21021_after_R_turn():
    cube = Cube()
    cube.twist_by_notation("R")

    assert cube.coordinate_corner_permutation == 21021


def test_coordinate_corner_permutation_is_correct_for_CHECKERBOARD():
    cube = Cube()
    cube.twist_by_notation(CHECKERBOARD_NOTATION)

    assert cube.coordinate_corner_permutation == 0


def test_coordinate_corner_permutation_is_correct_for_CUBE_IN_THE_CUBE():
    cube = Cube()
    cube.twist_by_notation(CUBE_IN_THE_CUBE_NOTATION)

    assert cube.coordinate_corner_permutation == 25980


def test_coordinate_corner_permutation_is_always_between_0_and_40319():
    for _ in range(TEST_SIZE):
        cube = Cube()
        cube.scramble_g1()

        assert 0 <= cube.coordinate_corner_permutation <= 40319


def test_coordinate_edge_permutation_is_0_for_a_solved_cube():
    assert Cube().coordinate_edge_permutation == 0


def test_coordinate_edge_permutation_is_correct_after_R2_turn():
    cube = Cube()
    cube.twist_by_notation("R2")

    assert cube.coordinate_edge_permutation == 105


def test_coordinate_edge_permutation_is_correct_after_R2_U2_R2():
    cube = Cube()
    cube.twist_by_notation("R2 U2 R2")

    assert cube.coordinate_edge_permutation == 60


def test_coordinate_edge_permutation_is_correct_for_CHECKERBOARD():
    cube = Cube()
    cube.twist_by_notation(CHECKERBOARD_NOTATION)

    assert cube.coordinate_edge_permutation == 35152


def test_coordinate_edge_permutation_is_always_between_0_and_40319():
    for _ in range(TEST_SIZE):
        cube = Cube()
        cube.scramble_g1()

        assert 0 <= cube.coordinate_edge_permutation <= 40319


def test_coordinate_ud_slice_phase2_is_0_for_a_solved_cube():
    assert Cube().coordinate_ud_slice_phase2 == 0


def test_coordinate_ud_slice_phase2_is_correct_after_R2_L2():
    cube = Cube()
    cube.twist_by_notation("R2 L2")

    assert cube.coordinate_ud_slice_phase2 == 23


def test_coordinate_ud_slice_phase2_of_CHECKERBOARD_is_correct():
    cube = Cube()
    cube.twist_by_notation(CHECKERBOARD_NOTATION)

    assert cube.coordinate_ud_slice_phase2 == 16


def test_coordinate_ud_slice_phase2_is_always_between_0_and_23():
    for _ in range(TEST_SIZE):
        cube = Cube()
        cube.scramble_g1()

        assert 0 <= cube.coordinate_ud_slice_phase2 <= 23


def test_all_coordinates_of_a_solved_cube_are_0():
    cube = Cube()

    assert cube.coordinate_corner_orientation == 0
    assert cube.coordinate_edge_orientation == 0
    assert cube.coordinate_ud_slice == 0
    assert cube.coordinate_corner_permutation == 0
    assert cube.coordinate_edge_permutation == 0
    assert cube.coordinate_ud_slice_phase2 == 0


def test_all_phase1_coordinates_of_cube_in_G1_are_always_0():
    for _ in range(TEST_SIZE):
        cube = Cube()
        cube.scramble_g1()

        assert cube.coordinate_corner_orientation == 0
        assert cube.coordinate_edge_orientation == 0
        assert cube.coordinate_ud_slice == 0


def test_all_phase1_coordinates_of_cube_not_in_G1_are_never_0():
    for _ in range(TEST_SIZE):
        cube = Cube()
        while cube.is_domino:
            cube.scramble()

        x1 = cube.coordinate_corner_orientation
        x2 = cube.coordinate_edge_orientation
        x3 = cube.coordinate_ud_slice

        assert (x1, x2, x3) != (0, 0, 0)


def test_all_coordinates_of_a_not_solved_cube_are_never_0():
    for _ in range(TEST_SIZE):
        cube = Cube()
        while cube.is_solved:
            cube.scramble()

        x1 = cube.coordinate_corner_orientation
        x2 = cube.coordinate_edge_orientation
        x3 = cube.coordinate_ud_slice
        x4 = cube.coordinate_corner_permutation
        x5 = cube.coordinate_edge_permutation
        x6 = cube.coordinate_ud_slice_phase2

        assert (x1, x2, x3, x4, x5, x6) != (0, 0, 0, 0, 0, 0)
