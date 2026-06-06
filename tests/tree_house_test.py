import pytest

from kt1.tree_house import (
    get_good_coordinates,
)

type Matrix = list[list[int]]


def sorted_points(point_list):
    return sorted(point_list, key=lambda p: (p["row"], p["column"]))


def test_can_identify_single_good_coordinate():
    matrix: Matrix = [[9, 8, 7], [5, 3, 2], [6, 6, 7]]
    assert sorted_points(get_good_coordinates(matrix)) == sorted_points(
        [{"row": 2, "column": 1}]
    )


def test_empty_matrix_has_no_good_coordinates():
    matrix: Matrix = []
    assert sorted_points(get_good_coordinates(matrix)) == sorted_points([])


def test_no_good_coordinates():
    matrix: Matrix = [[1, 2, 3], [3, 1, 2], [2, 3, 1]]
    assert sorted_points(get_good_coordinates(matrix)) == sorted_points([])


def test_can_identify_multiple_good_coordinates():
    matrix: Matrix = [[4, 5, 4], [3, 5, 5], [1, 5, 4]]
    assert sorted_points(get_good_coordinates(matrix)) == sorted_points(
        [
            {"row": 1, "column": 2},
            {"row": 2, "column": 2},
            {"row": 3, "column": 2},
        ]
    )


def test_multiple_good_coordinates_in_a_row():
    matrix: Matrix = [[6, 7, 8], [5, 5, 5], [7, 5, 6]]
    assert sorted_points(get_good_coordinates(matrix)) == sorted_points(
        [
            {"row": 2, "column": 1},
            {"row": 2, "column": 2},
            {"row": 2, "column": 3},
        ]
    )


def test_good_coordinate_in_bottom_right_corner():
    matrix: Matrix = [[8, 7, 9], [6, 7, 6], [3, 2, 5]]
    assert sorted_points(get_good_coordinates(matrix)) == sorted_points(
        [{"row": 3, "column": 3}]
    )


def test_non_square_matrix():
    matrix: Matrix = [[3, 1, 3], [3, 2, 4]]
    assert sorted_points(get_good_coordinates(matrix)) == sorted_points(
        [{"row": 1, "column": 3}, {"row": 1, "column": 1}]
    )


def test_good_coordinates_in_a_single_column_matrix():
    matrix: Matrix = [[2], [1], [4], [1]]
    assert sorted_points(get_good_coordinates(matrix)) == sorted_points(
        [{"row": 2, "column": 1}, {"row": 4, "column": 1}]
    )


def test_good_coordinates_in_a_single_row_matrix():
    matrix: Matrix = [[2, 5, 3, 5]]
    assert sorted_points(get_good_coordinates(matrix)) == sorted_points(
        [{"row": 1, "column": 2}, {"row": 1, "column": 4}]
    )


def test_irregular_matrix():
    matrix: Matrix = [[3, 2, 1], [0, 1], [2, 1, 0]]
    with pytest.raises(ValueError) as err:
        get_good_coordinates(matrix)

    assert "irregular matrix" in str(err.value)
