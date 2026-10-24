"""
NeetCode 150 - Module 4.1: Verification & Test Suite
Unit tests with comprehensive edge cases for all 9 Backtracking solutions.
"""

from solutions import (
    SolutionSubsets,
    SolutionCombinationSum,
    SolutionPermutations,
    SolutionSubsetsII,
    SolutionCombinationSumII,
    SolutionWordSearch,
    SolutionPalindromePartitioning,
    SolutionLetterCombinations,
    SolutionNQueens,
)


def test_subsets():
    sol = SolutionSubsets()
    res = sol.subsets([1, 2, 3])
    assert len(res) == 8
    assert [] in res and [1] in res and [1, 2, 3] in res
    assert sol.subsets([0]) == [[0], []]
    print("PASS: 1. Subsets")


def test_combination_sum():
    sol = SolutionCombinationSum()
    res = sol.combinationSum([2, 3, 6, 7], 7)
    assert sorted([sorted(c) for c in res]) == sorted([[2, 2, 3], [7]])
    assert sol.combinationSum([2], 1) == []
    print("PASS: 2. Combination Sum")


def test_permutations():
    sol = SolutionPermutations()
    res = sol.permute([1, 2, 3])
    assert len(res) == 6
    assert [1, 2, 3] in res and [3, 2, 1] in res
    assert sol.permute([1]) == [[1]]
    print("PASS: 3. Permutations")


def test_subsets_ii():
    sol = SolutionSubsetsII()
    res = sol.subsetsWithDup([1, 2, 2])
    sorted_res = sorted([sorted(s) for s in res])
    expected = sorted([[], [1], [1, 2], [1, 2, 2], [2], [2, 2]])
    assert sorted_res == expected
    assert sorted([sorted(s) for s in sol.subsetsWithDup([0])]) == sorted([[], [0]])
    print("PASS: 4. Subsets II")


def test_combination_sum_ii():
    sol = SolutionCombinationSumII()
    res = sol.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
    sorted_res = sorted([sorted(c) for c in res])
    expected = sorted([[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]])
    assert sorted_res == expected
    assert sol.combinationSum2([2, 5, 2, 1, 2], 5) == [[1, 2, 2], [5]]
    print("PASS: 5. Combination Sum II")


def test_word_search():
    sol = SolutionWordSearch()
    board = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"]
    ]
    assert sol.exist(board, "ABCCED") is True
    assert sol.exist(board, "SEE") is True
    assert sol.exist(board, "ABCB") is False
    print("PASS: 6. Word Search")


def test_palindrome_partitioning():
    sol = SolutionPalindromePartitioning()
    res = sol.partition("aab")
    assert sorted(res) == sorted([["a", "a", "b"], ["aa", "b"]])
    assert sol.partition("a") == [["a"]]
    print("PASS: 7. Palindrome Partitioning")


def test_letter_combinations():
    sol = SolutionLetterCombinations()
    res = sol.letterCombinations("23")
    expected = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    assert sorted(res) == sorted(expected)
    assert sol.letterCombinations("") == []
    assert sol.letterCombinations("2") == ["a", "b", "c"]
    print("PASS: 8. Letter Combinations of a Phone Number")


def test_n_queens():
    sol = SolutionNQueens()
    res4 = sol.solveNQueens(4)
    assert len(res4) == 2
    res1 = sol.solveNQueens(1)
    assert res1 == [["Q"]]
    print("PASS: 9. N-Queens")


if __name__ == "__main__":
    print("\n================ RUNNING BACKTRACKING VERIFICATION ================\n")
    test_subsets()
    test_combination_sum()
    test_permutations()
    test_subsets_ii()
    test_combination_sum_ii()
    test_word_search()
    test_palindrome_partitioning()
    test_letter_combinations()
    test_n_queens()
    print("\n================ ALL 9 TESTS PASSED! (100% VERIFIED) ================\n")
