from flood_fill import FloodFill
from flood_fill import InvalidMatrix
import pytest


def gen_empty_array():
    return [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
           ]


def gen_filled_array():
    return [
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1]
           ]


def gen_email_matrix():
    return [
            [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 0, 0],
            [1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
            [1, 0, 1, 1, 1, 1, 1, 1, 0, 0],
            [1, 1, 1, 1, 0, 1, 0, 0, 0, 0]
           ]


def gen_email_matrix_filled():
    return [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
           ]


class TestFloodFill():
    def test_flood_fill_init_errors(self):
        with pytest.raises(InvalidMatrix) as exc:
            FloodFill([], 1, 2)
        assert "Empty matrix" in str(exc.value)
        with pytest.raises(InvalidMatrix) as exc:
            FloodFill([0, 0, 0], 1, 3)
        assert "Inputted matrix is not 2D." in str(exc.value)

    def test_flood_fill_init(self):
        ff = FloodFill([[1]], 1, 1)
        assert ff.rows == 1
        assert ff.cols == 1
        ff = FloodFill([[1, 2, 3], [4, 5, 6]], 2, 3)
        assert ff.rows == 2
        assert ff.cols == 3

    def test_flood_fill_valid_point(self):
        ff = FloodFill([[1]], 1, 1)
        assert ff.is_valid_point(1, 1)
        assert not ff.is_valid_point(-1, 1)
        assert not ff.is_valid_point(1, 0)
        assert not ff.is_valid_point(1, 2)

    def test_flood_fill_can_fill_point(self):
        ff = FloodFill([[0, 0, 1]], 1, 3)
        assert ff.can_fill_point(1, 1)
        assert ff.can_fill_point(1, 2)
        assert not ff.can_fill_point(1, 3)
        ff = FloodFill([[0, 1, 0], [1, 0, 1]], 2, 3)
        assert ff.can_fill_point(1, 1)
        assert ff.can_fill_point(2, 2)
        assert not ff.can_fill_point(2, 3)

    def test_flood_fill_can_food_fill_one_row(self):
        ff = FloodFill([[0, 0, 0]], 1, 3)
        ff.flood_fill(1, 3)
        assert ff.matrix[0][0]
        assert ff.matrix[0][1]
        assert ff.matrix[0][2]

    def test_flood_fill_can_fill_one_column(self):
        ff = FloodFill([[0], [0], [0]], 3, 1)
        ff.flood_fill(3, 1)
        assert ff.matrix[0][0]
        assert ff.matrix[1][0]
        assert ff.matrix[2][0]

    def test_flood_fill_diagonals(self):
        ff = FloodFill([[0, 1], [1, 0]], 2, 2)
        ff.flood_fill(1, 1)
        assert ff.matrix == [[1, 1], [1, 0]]

    def test_flood_fill_flood_fill(self):
        ff = FloodFill(gen_empty_array(), 4, 4)
        ff.flood_fill(1, 1)
        assert ff.matrix == gen_filled_array()
        ff = FloodFill(gen_email_matrix(), 5, 10)
        assert not ff.matrix[1][1]
        assert not ff.matrix[2][1]
        assert not ff.matrix[3][1]
        ff.flood_fill(2, 2)
        assert ff.matrix[1][1]
        assert ff.matrix[2][1]
        assert ff.matrix[3][1]
        ff.flood_fill(2, 4)
        ff.flood_fill(2, 10)
        ff.flood_fill(5, 5)
        assert ff.matrix == gen_email_matrix_filled()
