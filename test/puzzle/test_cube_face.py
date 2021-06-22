from random import choices

from test.test_variables import TEST_SIZE
from src.puzzle.cube_face import CubeFace


def test_3x3_face_has_9_facelets():
    face = CubeFace(0)
    for i in range(9):
        assert face.get_facelet(i)


def test_initial_rows_are_correct_on_3x3_with_zeroes():
    face = CubeFace(0)

    for line in range(3):
        assert face.get_line(line) == (0, 0, 0)


def test_initial_colums_are_correct_on_3x3_with_zeroes():
    face = CubeFace(0)

    for line in range(6):
        assert face.get_line(line) == (0, 0, 0)


def test_initial_rows_and_lines_are_correct_on_3x3_with_fives():
    face = CubeFace(5)

    for line in range(6):
        assert face.get_line(line) == (5, 5, 5)


def test_initial_facelets_are_correct_on_3x3_with_twos():
    face = CubeFace(2)

    assert face.facelets == [[2, 2, 2], [2, 2, 2], [2, 2, 2]]


def test_cube_string_is_correct_on_solved_face():
    for i in range(6):
        face = CubeFace(i)

        assert face.cube_string == face.sides[i]*9


def test_cube_string_is_correct_with_a_row_replaced():
    face = CubeFace(0)
    face.set_line(2, (2, 5, 3))

    assert face.cube_string == "UUUUUUFDR"


# FIXME: Implement set_line for middle lines
# def test_cube_string_is_correct_with_a_column_replaced():
#     face = CubeFace(2)
#     face.set_line(4, (1, 4, 0))

#     assert face.cube_string == "FLFFBFFUF"


def test_the_face_is_initially_solved():
    for i in range(6):
        face = CubeFace(i)

        assert face.is_solved


def test_face_with_a_facelet_replaced_is_not_solved():
    face = CubeFace(4)
    face.set_line(3, (2, 4, 4))

    assert not face.is_solved


def test_a_rotated_face_is_still_solved():
    face = CubeFace(3)
    face.rotate()

    assert face.is_solved

    face.rotate(False)
    face.rotate(False)

    assert face.is_solved


def test_an_unsolved_rotated_face_is_still_unsolved():
    face = CubeFace(5)
    face.set_line(0, (5, 3, 2))

    for _ in range(4):
        face.rotate()

        assert not face.is_solved


def test_top_face_is_domino():
    face = CubeFace(0)

    assert face.is_domino


def test_bottom_face_is_domino():
    face = CubeFace(5)

    assert face.is_domino


def test_side_faces_are_not_domino():
    for i in range(1, 5):
        face = CubeFace(i)

        assert not face.is_domino


# FIXME: Implement set_line for middle lines.
def test_top_and_bottom_mixed_face_is_domino():
    for _ in range(TEST_SIZE):
        face = CubeFace(0)
        for row in (0, 2):
            face.set_line(row, choices([0, 5], k=3))

        assert face.is_domino


def test_top_face_with_a_side_facelet_is_not_domino():
    face = CubeFace(0)
    face.set_line(2, [0, 2, 0])

    assert not face.is_domino


def test_bottom_face_with_a_side_facelet_is_not_domino():
    face = CubeFace(5)
    face.set_line(0, [4, 5, 5])

    assert not face.is_domino
