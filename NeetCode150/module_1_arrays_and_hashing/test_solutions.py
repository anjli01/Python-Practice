"""
NeetCode 150 - Module 1.1: Verification & Test Suite
Unit tests with comprehensive edge cases for all 9 Arrays & Hashing solutions.
"""

import sys
from solutions import (
    SolutionContainsDuplicate,
    SolutionValidAnagram,
    SolutionTwoSum,
    SolutionGroupAnagrams,
    SolutionTopKFrequent,
    Codec,
    SolutionProductExceptSelf,
    SolutionValidSudoku,
    SolutionLongestConsecutive,
)


def test_contains_duplicate():
    sol = SolutionContainsDuplicate()
    # Standard cases
    assert sol.containsDuplicate([1, 2, 3, 1]) is True
    assert sol.containsDuplicate([1, 2, 3, 4]) is False
    assert sol.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True
    # Edge cases
    assert sol.containsDuplicate([]) is False
    assert sol.containsDuplicate([42]) is False
    assert sol.containsDuplicate([-1, -1]) is True
    print("PASS: 1. Contains Duplicate")


def test_valid_anagram():
    sol = SolutionValidAnagram()
    # Standard cases
    assert sol.isAnagram("anagram", "nagaram") is True
    assert sol.isAnagram("rat", "car") is False
    # Edge cases
    assert sol.isAnagram("a", "a") is True
    assert sol.isAnagram("a", "b") is False
    assert sol.isAnagram("ab", "a") is False
    assert sol.isAnagram("", "") is True
    print("PASS: 2. Valid Anagram")


def test_two_sum():
    sol = SolutionTwoSum()
    # Standard cases
    assert sorted(sol.twoSum([2, 7, 11, 15], 9)) == [0, 1]
    assert sorted(sol.twoSum([3, 2, 4], 6)) == [1, 2]
    assert sorted(sol.twoSum([3, 3], 6)) == [0, 1]
    # Edge cases with negative numbers and zero
    assert sorted(sol.twoSum([-3, 4, 3, 90], 0)) == [0, 2]
    assert sorted(sol.twoSum([-1, -2, -3, -4, -5], -8)) == [2, 4]
    print("PASS: 3. Two Sum")


def test_group_anagrams():
    sol = SolutionGroupAnagrams()
    # Standard cases
    input_strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    res = sol.groupAnagrams(input_strs)
    sorted_res = sorted([sorted(group) for group in res])
    expected = sorted([["ate", "eat", "tea"], ["bat"], ["nat", "tan"]])
    assert sorted_res == expected
    # Edge cases
    assert sol.groupAnagrams([""]) == [[""]]
    assert sol.groupAnagrams(["a"]) == [["a"]]
    print("PASS: 4. Group Anagrams")


def test_top_k_frequent():
    sol = SolutionTopKFrequent()
    # Standard cases
    assert set(sol.topKFrequent([1, 1, 1, 2, 2, 3], 2)) == {1, 2}
    assert sol.topKFrequent([1], 1) == [1]
    # Edge cases with negative values and distinct counts
    assert set(sol.topKFrequent([-1, -1, 2], 1)) == {-1}
    assert set(sol.topKFrequent([4, 1, -1, 2, -1, 2, 3], 2)) == {-1, 2}
    print("PASS: 5. Top K Frequent Elements")


def test_encode_and_decode_strings():
    codec = Codec()
    # Standard cases
    sample1 = ["lint", "code", "love", "you"]
    assert codec.decode(codec.encode(sample1)) == sample1
    # Tricky edge cases: empty strings, special characters, embedded '#' and numbers
    sample2 = ["we", "say", ":", "yes", "!@#$%^&*()"]
    assert codec.decode(codec.encode(sample2)) == sample2
    sample3 = ["4#code", "10#tencharacters", "###", ""]
    assert codec.decode(codec.encode(sample3)) == sample3
    sample4 = [""]
    assert codec.decode(codec.encode(sample4)) == sample4
    sample5 = []
    assert codec.decode(codec.encode(sample5)) == sample5
    print("PASS: 6. Encode and Decode Strings")


def test_product_except_self():
    sol = SolutionProductExceptSelf()
    # Standard cases
    assert sol.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
    # Arrays containing single zero and multiple zeroes
    assert sol.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    assert sol.productExceptSelf([0, 0]) == [0, 0]
    assert sol.productExceptSelf([5, 2]) == [2, 5]
    print("PASS: 7. Product of Array Except Self")


def test_valid_sudoku():
    sol = SolutionValidSudoku()
    valid_board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    assert sol.isValidSudoku(valid_board) is True

    # Invalid board: duplicate '8' in the top-left 3x3 box
    invalid_board = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    assert sol.isValidSudoku(invalid_board) is False
    print("PASS: 8. Valid Sudoku")


def test_longest_consecutive_sequence():
    sol = SolutionLongestConsecutive()
    # Standard cases
    assert sol.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4  # [1, 2, 3, 4]
    assert sol.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9  # [0..8]
    # Edge cases
    assert sol.longestConsecutive([]) == 0
    assert sol.longestConsecutive([10]) == 1
    assert sol.longestConsecutive([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]) == 7  # [-1..5]
    print("PASS: 9. Longest Consecutive Sequence")


if __name__ == "__main__":
    print("\n================ RUNNING VERIFICATION SUITE ================\n")
    test_contains_duplicate()
    test_valid_anagram()
    test_two_sum()
    test_group_anagrams()
    test_top_k_frequent()
    test_encode_and_decode_strings()
    test_product_except_self()
    test_valid_sudoku()
    test_longest_consecutive_sequence()
    print("\n================ ALL 9 TESTS PASSED! (100% VERIFIED) ================\n")
