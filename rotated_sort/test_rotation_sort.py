from rotation_sort import SortedRotationSearcher
from rotation_sort import binary_search
from rotation_sort import EmptyListException
from rotation_sort import InvalidTarget
from rotation_sort import MissingTarget
import pytest


class TestBinarySearch:
    def test_binary_search_single_item_list(self):
        assert binary_search([1], 0, 0, 1) == 0

    def test_binary_search(self):
        assert binary_search([1, 2, 3, 4, 5, 6], 0, 5, 6) == 5
        assert binary_search([1, 2, 3, 4, 5, 6], 0, 5, 1) == 0
        assert binary_search([1, 2, 3, 4, 5, 6], 0, 5, 3) == 2

class TestFindRotationPoint:
    def test_find_rotation_point_empty_list(self):
        with pytest.raises(EmptyListException) as exc:
            SortedRotationSearcher.find_rotation_point([])
        assert 'Cannot find rotation point of empty list.' in str(exc.value)

    def test_find_rotation_point_one_item_list(self):
        assert SortedRotationSearcher.find_rotation_point([5]) == 0

    def test_find_rotation_point_sorted_lists(self):
        assert SortedRotationSearcher.find_rotation_point([5, 10]) == 0
        assert SortedRotationSearcher.find_rotation_point([1, 2, 3, 4, 5]) == 0
        assert SortedRotationSearcher.find_rotation_point([10, 20, 100, 1000]) == 0

    def test_find_rotation_point_rotated_sorted_lists(self):
        assert SortedRotationSearcher.find_rotation_point([10, 5]) == 1
        assert SortedRotationSearcher.find_rotation_point([10, 5, 9]) == 1
        assert SortedRotationSearcher.find_rotation_point([10, 11, 12, 5, 9]) == 3
        assert SortedRotationSearcher.find_rotation_point([9, 10, 11, 12, 1]) == 4
        assert SortedRotationSearcher.find_rotation_point([10, 11, 20, 1, 5, 9]) == 3


class TestFindTargetFromRotatedSorted:
    def test_get_target_index_empty_list(self):
        with pytest.raises(EmptyListException) as exc:
            SortedRotationSearcher.find_target([], 1)
        assert 'Cannot find rotation point of empty list.' in str(exc.value)

    def test_get_target_index_empty_list(self):
        with pytest.raises(InvalidTarget) as exc:
            SortedRotationSearcher.find_target([1, 2], None)
        assert 'No target provided for search.' in str(exc.value)

    def test_get_target_index_missing_from_list(self):
        with pytest.raises(MissingTarget) as exc:
            SortedRotationSearcher.find_target([1, 2], 5)
        assert "'5' is not in input list." in str(exc.value)
        with pytest.raises(MissingTarget) as exc:
            SortedRotationSearcher.find_target([2, 1, 3, 4], 10)
        assert "'10' is not in input list." in str(exc.value)

    def test_get_target_index_in_non_rotated_list(self):
        SortedRotationSearcher.find_target([1], 1) == 0
        SortedRotationSearcher.find_target([1, 2], 2) == 1
        SortedRotationSearcher.find_target([1, 2], 1) == 0
        SortedRotationSearcher.find_target([1, 2, 3, 4, 5, 6, 7, 8], 5) == 4
        SortedRotationSearcher.find_target([1, 2, 3, 4, 5, 6, 7, 8], 1) == 0
        SortedRotationSearcher.find_target([1, 2, 3, 4, 5, 6, 7, 100], 100) == 7

    def test_get_target_index_in_rotated_list(self):
        SortedRotationSearcher.find_target([2, 1], 1) == 1
        SortedRotationSearcher.find_target([2, 1], 2) == 0
        SortedRotationSearcher.find_target([9, 10, 11, 1, 6, 8], 8) == 5
        SortedRotationSearcher.find_target([9, 10, 11, 1, 6, 8], 9) == 0
        SortedRotationSearcher.find_target([9, 10, 11, 1, 6, 8], 11) == 2
        SortedRotationSearcher.find_target([25, 1, 2, 3, 4], 25) == 0
        SortedRotationSearcher.find_target([25, 100, 200, 201, 4], 4) == 4