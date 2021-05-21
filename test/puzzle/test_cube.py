from src.puzzle.cube import Cube


solved = """   WWW
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
checkerboard = """   WYW
   YWY
   WYW
RORBGBOROGBG
OROGBGRORBGB
RORBGBOROGBG
   YWY
   WYW
   YWY"""

cube_in_the_cube_notation = "F L F U' R U F2 L2 U' L' B D' B' L2 U"
cube_in_the_cube = """   BBB
   BWW
   BWW
YYYOBBOOWRRR
RRYOBBOOWRGG
RRYOOOWWWRGG
   GGG
   YYG
   YYG"""


def test_an_untwisted_cube_is_solved():
    cube = Cube()

    assert str(cube) == solved


def test_a_solved_cube_is_solved():
    cube = Cube()

    assert cube.isSolved()


def test_a_scrambled_cube_is_not_solved():
    cube = Cube()
    cube.scramble()

    assert not cube.isSolved()


def test_checkerboard_pattern_with_single_twists():
    cube = Cube()

    for turn in checkerboard_turns:
        cube.twist(turn)

    assert str(cube) == checkerboard


def test_checkerboard_pattern_with_notation():
    cube = Cube()
    cube.twist_by_notation(checkerboard_notation)

    assert str(cube) == checkerboard


def test_cube_in_the_cube_pattern():
    cube = Cube()
    cube.twist_by_notation(cube_in_the_cube_notation)

    assert str(cube) == cube_in_the_cube


def test_cube_is_solved_after_reset():
    cube = Cube()
    cube.scramble()
    cube.twist(2)
    cube.twist_by_notation("U2 B D'")
    cube.reset()

    assert cube.isSolved()
