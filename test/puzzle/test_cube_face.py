from src.puzzle.cube_face import CubeFace


def test_initial_rows_are_correct_on_3x3_with_zeroes():
    face = CubeFace(3, 0)

    for line in range(3):
        assert face.getLine(line) == [0, 0, 0]


def test_initial_colums_are_correct_on_3x3_with_zeroes():
    face = CubeFace(3, 0)

    for line in range(3, 6):
        assert face.getLine(line) == [0, 0, 0]
