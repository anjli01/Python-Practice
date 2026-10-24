"""
NeetCode 150 - Module 1.2: Verification & Test Suite
Unit tests with comprehensive edge cases for all 5 Two Pointers solutions.
"""

from solutions import (
    SolutionValidPalindrome,
    SolutionTwoSumII,
    Solution3Sum,
    SolutionContainerWithMostWater,
    SolutionTrappingRainWater,
)


def test_valid_palindrome():
    sol = SolutionValidPalindrome()
    # Standard cases
    assert sol.isPalindrome("A man, a plan, a canal: Panama") is True
    assert sol.isPalindrome("race a car") is False
    # Edge cases
    assert sol.isPalindrome(" ") is True
    assert sol.isPalindrome(".,") is True
    assert sol.isPalindrome("a.") is True
    assert sol.isPalindrome("0P") is False
    print("PASS: 1. Valid Palindrome")


def test_two_sum_ii():
    sol = SolutionTwoSumII()
    # Standard cases (1-indexed output)
    assert sol.twoSum([2, 7, 11, 15], 9) == [1, 2]
    assert sol.twoSum([2, 3, 4], 6) == [1, 3]
    assert sol.twoSum([-1, 0], -1) == [1, 2]
    # Edge cases with duplicate numbers and negative values
    assert sol.twoSum([0, 0, 3, 4], 0) == [1, 2]
    assert sol.twoSum([-5, -3, -1, 0, 2], -8) == [1, 2]
    print("PASS: 2. Two Sum II - Input Array Is Sorted")


def test_three_sum():
    sol = Solution3Sum()
    # Standard case
    res1 = sol.threeSum([-1, 0, 1, 2, -1, -4])
    sorted_res1 = sorted([sorted(t) for t in res1])
    expected1 = sorted([[-1, -1, 2], [-1, 0, 1]])
    assert sorted_res1 == expected1
    # Edge cases
    assert sol.threeSum([0, 1, 1]) == []
    assert sol.threeSum([0, 0, 0]) == [[0, 0, 0]]
    assert sol.threeSum([0, 0, 0, 0]) == [[0, 0, 0]]
    assert sol.threeSum([-2, 0, 1, 1, 2]) == [[-2, 0, 2], [-2, 1, 1]]
    print("PASS: 3. 3Sum")


def test_container_with_most_water():
    sol = SolutionContainerWithMostWater()
    # Standard cases
    assert sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert sol.maxArea([1, 1]) == 1
    # Edge cases: descending, ascending, flat
    assert sol.maxArea([4, 3, 2, 1, 4]) == 16
    assert sol.maxArea([1, 2, 1]) == 2
    assert sol.maxArea([5, 5, 5, 5]) == 15
    print("PASS: 4. Container With Most Water")


def test_trapping_rain_water():
    sol = SolutionTrappingRainWater()
    # Standard cases
    assert sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert sol.trap([4, 2, 0, 3, 2, 5]) == 9
    # Edge cases: flat, strictly descending, strictly ascending, empty, single bar
    assert sol.trap([]) == 0
    assert sol.trap([3]) == 0
    assert sol.trap([1, 2]) == 0
    assert sol.trap([5, 4, 3, 2, 1]) == 0
    assert sol.trap([1, 2, 3, 4, 5]) == 0
    assert sol.trap([3, 0, 2, 0, 4]) == 7
    print("PASS: 5. Trapping Rain Water")


if __name__ == "__main__":
    print("\n================ RUNNING TWO POINTERS VERIFICATION ================\n")
    test_valid_palindrome()
    test_two_sum_ii()
    test_three_sum()
    test_container_with_most_water()
    test_trapping_rain_water()
    print("\n================ ALL 5 TESTS PASSED! (100% VERIFIED) ================\n")
