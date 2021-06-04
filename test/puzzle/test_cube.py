from src.puzzle.cube import Cube


solved_str = """   WWW
   WWW
   WWW
RRRBBBOOOGGG
RRRBBBOOOGGG
RRRBBBOOOGGG
   YYY
   YYY
   YYY"""

checkerboard_turns = (0, 0, 5, 5, 1, 1, 3, 3, 2, 2, 4, 4)
checkerboard_notation = "U2 D2 L2 R2 F2 B2"
checkerboard = "UDUDUDUDULRLRLRLRLFBFBFBFBFRLRLRLRLRBFBFBFBFBDUDUDUDUD"

cube_in_the_cube_notation = "F L F U' R U F2 L2 U' L' B D' B' L2 U"
cube_in_the_cube = "FFFFUUFUUDDDLLDLLDRFFRFFRRRRRURRUUUULLLLBBLBBBBBDDBDDB"
cube_in_the_cube_edges = ["UR", "UF", "DF", "FL", "UB", "BR",
                          "DL", "DB", "FR", "DR", "BL", "UL"]


def test_the_str_of_a_solved_cube_is_correct():
    assert str(Cube()) == solved_str


def test_a_solved_cube_is_solved():
    assert Cube().isSolved


def test_R2_L2_is_not_solved():
    cube = Cube()
    cube.twist_by_notation("R2 L2")

    assert not cube.isSolved


def test_a_scrambled_cube_is_not_solved():
    cube = Cube()
    cube.scramble()

    assert not cube.isSolved


def test_checkerboard_pattern_with_single_twists():
    cube = Cube()

    for turn in checkerboard_turns:
        cube.twist(turn)

    assert cube.cube_string == checkerboard


def test_checkerboard_pattern_with_notation():
    cube = Cube()
    cube.twist_by_notation(checkerboard_notation)

    assert cube.cube_string == checkerboard


def test_cube_in_the_cube_pattern():
    cube = Cube()
    cube.twist_by_notation(cube_in_the_cube_notation)

    assert cube.cube_string == cube_in_the_cube


def test_cube_is_solved_after_reset():
    cube = Cube()
    cube.scramble()
    cube.twist(2)
    cube.twist_by_notation("U2 B D'")
    cube.reset()

    assert cube.isSolved


def test_solved_cube_is_domino():
    assert Cube().isDomino


def test_checkerboard_is_domino():
    cube = Cube()
    cube.twist_by_notation(checkerboard_notation)

    assert cube.isDomino


def test_cube_in_the_cube_is_not_domino():
    cube = Cube()
    cube.twist_by_notation(cube_in_the_cube_notation)

    assert not cube.isDomino


def test_random_cubes_in_G1_are_domino():
    for _ in range(5):
        cube = Cube()
        cube.scramble_G1()
        assert cube.isDomino


def test_cube_string_of_a_solved_cube_is_correct():
    solved_string = "UUUUUUUUULLLLLLLLLFFFFFFFFFRRRRRRRRRBBBBBBBBBDDDDDDDDD"
    cube_string = Cube().cube_string

    assert solved_string == cube_string


def test_empty_notation_doesnt_affect_the_cube():
    cube = Cube()
    cube.twist_by_notation("")

    assert cube.isSolved


def test_random_scramble_has_all_corners():
    for _ in range(10):
        cube = Cube()
        cube.scramble()

        assert None not in cube.corners


def test_random_scramble_has_one_of_each_corner():
    for _ in range(10):
        cube = Cube()
        cube.scramble()

        for corner in Cube.corner_order:
            assert corner in cube.corners


def test_coordinate_corner_permutation_is_0_for_a_solved_cube():
    assert Cube().coordinate_corner_permutation == 0


def test_coordinate_corner_permutation_is_21021_after_R_turn():
    cube = Cube()
    cube.twist_by_notation("R")

    assert cube.coordinate_corner_permutation == 21021


def test_coordinate_corner_permutation_is_correct_for_checkerboard():
    cube = Cube()
    cube.twist_by_notation(checkerboard_notation)

    assert cube.coordinate_corner_permutation == 0


def test_coordinate_corner_permutation_is_correct_for_cube_in_the_cube():
    cube = Cube()
    cube.twist_by_notation(cube_in_the_cube_notation)

    assert cube.coordinate_corner_permutation == 25980


def test_edges_of_a_solved_cube_are_correct():
    assert Cube().edges == Cube.edge_order


def test_edges_of_cube_in_the_cube_are_correct():
    cube = Cube()
    cube.twist_by_notation(cube_in_the_cube_notation)

    assert cube.edges == cube_in_the_cube_edges


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


def test_coordinate_edge_permutation_is_correct_for_checkerboard():
    cube = Cube()
    cube.twist_by_notation(checkerboard_notation)

    assert cube.coordinate_edge_permutation == 35152
