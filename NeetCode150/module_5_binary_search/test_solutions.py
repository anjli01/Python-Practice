"""
NeetCode 150 - Module 2.1: Verification & Test Suite
Unit tests with comprehensive edge cases for all 7 Binary Search solutions.
"""

from solutions import (
    SolutionBinarySearch,
    SolutionSearch2DMatrix,
    SolutionKokoEatingBananas,
    SolutionFindMinRotatedSortedArray,
    SolutionSearchRotatedSortedArray,
    TimeMap,
    SolutionMedianOfTwoSortedArrays,
)


def test_binary_search():
    sol = SolutionBinarySearch()
    assert sol.search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert sol.search([-1, 0, 3, 5, 9, 12], 2) == -1
    # Edge cases
    assert sol.search([5], 5) == 0
    assert sol.search([5], 3) == -1
    assert sol.search([], 1) == -1
    print("PASS: 1. Binary Search")


def test_search_2d_matrix():
    sol = SolutionSearch2DMatrix()
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    assert sol.searchMatrix(matrix, 3) is True
    assert sol.searchMatrix(matrix, 13) is False
    # Edge cases
    assert sol.searchMatrix([[1]], 1) is True
    assert sol.searchMatrix([[1]], 2) is False
    assert sol.searchMatrix([[1, 3]], 3) is True
    print("PASS: 2. Search a 2D Matrix")


def test_koko_eating_bananas():
    sol = SolutionKokoEatingBananas()
    assert sol.minEatingSpeed([3, 6, 7, 11], 8) == 4
    assert sol.minEatingSpeed([30, 11, 23, 4, 20], 5) == 30
    assert sol.minEatingSpeed([30, 11, 23, 4, 20], 6) == 23
    # Edge cases: single pile, h == len(piles)
    assert sol.minEatingSpeed([312884470], 312884470) == 1
    assert sol.minEatingSpeed([10], 2) == 5
    print("PASS: 3. Koko Eating Bananas")


def test_find_min_rotated_sorted_array():
    sol = SolutionFindMinRotatedSortedArray()
    assert sol.findMin([3, 4, 5, 1, 2]) == 1
    assert sol.findMin([4, 5, 6, 7, 0, 1, 2]) == 0
    assert sol.findMin([11, 13, 15, 17]) == 11
    # Edge cases: single element, two elements
    assert sol.findMin([1]) == 1
    assert sol.findMin([2, 1]) == 1
    assert sol.findMin([1, 2]) == 1
    print("PASS: 4. Find Minimum in Rotated Sorted Array")


def test_search_rotated_sorted_array():
    sol = SolutionSearchRotatedSortedArray()
    assert sol.search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert sol.search([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert sol.search([1], 0) == -1
    # Edge cases: pivot at edges, 2 elements
    assert sol.search([1], 1) == 0
    assert sol.search([3, 1], 1) == 1
    assert sol.search([5, 1, 3], 5) == 0
    print("PASS: 5. Search in Rotated Sorted Array")


def test_time_based_key_value_store():
    time_map = TimeMap()
    time_map.set("foo", "bar", 1)
    assert time_map.get("foo", 1) == "bar"
    assert time_map.get("foo", 3) == "bar"
    time_map.set("foo", "bar2", 4)
    assert time_map.get("foo", 4) == "bar2"
    assert time_map.get("foo", 5) == "bar2"
    assert time_map.get("foo", 0) == ""
    assert time_map.get("unknown", 10) == ""
    print("PASS: 6. Time Based Key-Value Store")


def test_median_of_two_sorted_arrays():
    sol = SolutionMedianOfTwoSortedArrays()
    # Standard cases
    assert sol.findMedianSortedArrays([1, 3], [2]) == 2.0
    assert sol.findMedianSortedArrays([1, 2], [3, 4]) == 2.5
    # Edge cases: one empty array, disjoint arrays, single elements
    assert sol.findMedianSortedArrays([], [1]) == 1.0
    assert sol.findMedianSortedArrays([2], []) == 2.0
    assert sol.findMedianSortedArrays([100001], [100000]) == 100000.5
    assert sol.findMedianSortedArrays([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]) == 5.5
    print("PASS: 7. Median of Two Sorted Arrays")


if __name__ == "__main__":
    print("\n================ RUNNING BINARY SEARCH VERIFICATION ================\n")
    test_binary_search()
    test_search_2d_matrix()
    test_koko_eating_bananas()
    test_find_min_rotated_sorted_array()
    test_search_rotated_sorted_array()
    test_time_based_key_value_store()
    test_median_of_two_sorted_arrays()
    print("\n================ ALL 7 TESTS PASSED! (100% VERIFIED) ================\n")
