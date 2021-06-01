from src.puzzle.cube_face import CubeFace
from random import choices


def test_initial_rows_are_correct_on_3x3_with_zeroes():
    face = CubeFace(3, 0)

    for line in range(3):
        assert face.getLine(line) == [0, 0, 0]


def test_initial_colums_are_correct_on_3x3_with_zeroes():
    face = CubeFace(3, 0)

    for line in range(3, 6):
        assert face.getLine(line) == [0, 0, 0]


def test_initial_rows_and_lines_are_correct_on_3x3_with_fives():
    face = CubeFace(3, 5)

    for line in range(6):
        assert face.getLine(line) == [5, 5, 5]


def test_initial_facelets_are_correct_on_3x3_with_twos():
    face = CubeFace(3, 2)

    assert face.facelets == [[2, 2, 2], [2, 2, 2], [2, 2, 2]]


def test_cube_string_is_correct_on_solved_face():
    for i in range(6):
        face = CubeFace(3, i)

        assert face.cube_string == face.sides[i]*9


def test_cube_string_is_correct_with_a_row_replaced():
    face = CubeFace(3, 0)
    face.setLine(2, [2, 5, 3])

    assert face.cube_string == "UUUUUUFDR"


def test_cube_string_is_correct_with_a_column_replaced():
    face = CubeFace(3, 2)
    face.setLine(4, [1, 4, 0])

    assert face.cube_string == "FLFFBFFUF"


def test_the_face_is_initially_solved():
    for i in range(6):
        face = CubeFace(3, i)

        assert face.isSolved


def test_face_with_a_facelet_replaced_is_not_solved():
    face = CubeFace(3, 4)
    face.setLine(3, [2, 4, 4])

    assert not face.isSolved


def test_a_rotated_face_is_still_solved():
    face = CubeFace(3, 3)
    face.rotate()

    assert face.isSolved

    face.rotate(False)
    face.rotate(False)

    assert face.isSolved


def test_an_unsolved_rotated_face_is_still_unsolved():
    face = CubeFace(3, 5)
    face.setLine(0, [5, 3, 2])

    for _ in range(4):
        face.rotate()

        assert not face.isSolved


def test_top_face_is_domino():
    face = CubeFace(3, 0)

    assert face.isDomino


def test_bottom_face_is_domino():
    face = CubeFace(3, 5)

    assert face.isDomino


def test_side_faces_are_not_domino():
    for i in range(1, 5):
        face = CubeFace(3, i)

        assert not face.isDomino


def test_top_and_bottom_mixed_face_is_domino():
    for _ in range(5):
        face = CubeFace(3, 0)
        for row in range(3):
            face.setLine(row, choices([0, 5], k=3))

        assert face.isDomino


def test_top_face_with_a_side_facelet_is_not_domino():
    face = CubeFace(3, 0)
    face.setLine(2, [0, 2, 0])

    assert not face.isDomino


def test_bottom_face_with_a_side_facelet_is_not_domino():
    face = CubeFace(3, 5)
    face.setLine(0, [4, 5, 5])

    assert not face.isDomino
