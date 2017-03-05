class EmptyListException(Exception):
    pass


class InvalidTarget(Exception):
    pass


class MissingTarget(Exception):
    pass


def binary_search(arr, left, right, target):
    if left > right:
        raise MissingTarget("'{}' is not in input list.".format(target))
    midpoint = (left+right)/2
    if arr[midpoint] == target:
        return midpoint
    if arr[midpoint] > target:
        return binary_search(arr, left, midpoint-1, target)
    else:
        return binary_search(arr, midpoint+1, right, target)


class SortedRotationSearcher(object):
    def __init__(self):
        pass

    @staticmethod
    def _find_rotation_point_helper(arr, left, right):
        if left > right:
            return 0
        mid_point = (left + right) / 2
        if arr[mid_point + 1] < arr[mid_point]:
            return mid_point + 1
        if arr[left] > arr[mid_point]:
            return SortedRotationSearcher._find_rotation_point_helper(arr, left, mid_point - 1)
        else:
            return SortedRotationSearcher._find_rotation_point_helper(arr, mid_point + 1, right)

    @staticmethod
    def find_rotation_point(arr):
        if not arr:
            raise EmptyListException("Cannot find rotation point of empty list.")
        # List is one element or already sorted
        if len(arr) == 1 or arr[0] < arr[len(arr)-1]:
            return 0
        return SortedRotationSearcher._find_rotation_point_helper(arr, 0, len(arr)-1)

    @staticmethod
    def find_target(arr, target):
        if not target:
            raise InvalidTarget("No target provided for search.")
        rotation_point = SortedRotationSearcher.find_rotation_point(arr)
        # can I simplify this condition?
        if rotation_point != 0 and target >= arr[0] and target <= arr[rotation_point-1]:
            return binary_search(arr, 0, rotation_point-1, target)
        else:
            return binary_search(arr, rotation_point, len(arr)-1, target)