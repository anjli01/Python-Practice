"""
NeetCode 150 - Module 5.2: Verification & Test Suite
Unit tests with comprehensive edge cases for all 11 2-D Dynamic Programming solutions.
"""

from solutions import (
    SolutionUniquePaths,
    SolutionLongestCommonSubsequence,
    SolutionStockWithCooldown,
    SolutionCoinChangeII,
    SolutionTargetSum,
    SolutionInterleavingString,
    SolutionLongestIncreasingPath,
    SolutionDistinctSubsequences,
    SolutionEditDistance,
    SolutionBurstBalloons,
    SolutionRegularExpressionMatching,
)


def test_unique_paths():
    sol = SolutionUniquePaths()
    assert sol.uniquePaths(3, 7) == 28
    assert sol.uniquePaths(3, 2) == 3
    assert sol.uniquePaths(1, 1) == 1
    print("PASS: 1. Unique Paths")


def test_longest_common_subsequence():
    sol = SolutionLongestCommonSubsequence()
    assert sol.longestCommonSubsequence("abcde", "ace") == 3
    assert sol.longestCommonSubsequence("abc", "abc") == 3
    assert sol.longestCommonSubsequence("abc", "def") == 0
    print("PASS: 2. Longest Common Subsequence")


def test_stock_with_cooldown():
    sol = SolutionStockWithCooldown()
    assert sol.maxProfit([1, 2, 3, 0, 2]) == 3
    assert sol.maxProfit([1]) == 0
    assert sol.maxProfit([1, 2]) == 1
    print("PASS: 3. Best Time to Buy and Sell Stock with Cooldown")


def test_coin_change_ii():
    sol = SolutionCoinChangeII()
    assert sol.change(5, [1, 2, 5]) == 4
    assert sol.change(3, [2]) == 0
    assert sol.change(10, [10]) == 1
    assert sol.change(0, [7]) == 1
    print("PASS: 4. Coin Change II")


def test_target_sum():
    sol = SolutionTargetSum()
    assert sol.findTargetSumWays([1, 1, 1, 1, 1], 3) == 5
    assert sol.findTargetSumWays([1], 1) == 1
    assert sol.findTargetSumWays([1], 2) == 0
    print("PASS: 5. Target Sum")


def test_interleaving_string():
    sol = SolutionInterleavingString()
    assert sol.isInterleave("aabcc", "dbbca", "aadbbcbcac") is True
    assert sol.isInterleave("aabcc", "dbbca", "aadbbbaccc") is False
    assert sol.isInterleave("", "", "") is True
    print("PASS: 6. Interleaving String")


def test_longest_increasing_path():
    sol = SolutionLongestIncreasingPath()
    matrix = [
        [9, 9, 4],
        [6, 6, 8],
        [2, 1, 1]
    ]
    assert sol.longestIncreasingPath(matrix) == 4
    assert sol.longestIncreasingPath([[1]]) == 1
    print("PASS: 7. Longest Increasing Path in a Matrix")


def test_distinct_subsequences():
    sol = SolutionDistinctSubsequences()
    assert sol.numDistinct("rabbbit", "rabbit") == 3
    assert sol.numDistinct("babgbag", "bag") == 5
    assert sol.numDistinct("a", "b") == 0
    print("PASS: 8. Distinct Subsequences")


def test_edit_distance():
    sol = SolutionEditDistance()
    assert sol.minDistance("horse", "ros") == 3
    assert sol.minDistance("intention", "execution") == 5
    assert sol.minDistance("", "") == 0
    assert sol.minDistance("", "a") == 1
    print("PASS: 9. Edit Distance")


def test_burst_balloons():
    sol = SolutionBurstBalloons()
    assert sol.maxCoins([3, 1, 5, 8]) == 167
    assert sol.maxCoins([1, 5]) == 10
    assert sol.maxCoins([7]) == 7
    print("PASS: 10. Burst Balloons")


def test_regular_expression_matching():
    sol = SolutionRegularExpressionMatching()
    assert sol.isMatch("aa", "a") is False
    assert sol.isMatch("aa", "a*") is True
    assert sol.isMatch("ab", ".*") is True
    assert sol.isMatch("aab", "c*a*b") is True
    assert sol.isMatch("", ".*") is True
    assert sol.isMatch("mississippi", "mis*is*p*.") is False
    print("PASS: 11. Regular Expression Matching")


if __name__ == "__main__":
    print("\n================ RUNNING 2-D DP VERIFICATION ================\n")
    test_unique_paths()
    test_longest_common_subsequence()
    test_stock_with_cooldown()
    test_coin_change_ii()
    test_target_sum()
    test_interleaving_string()
    test_longest_increasing_path()
    test_distinct_subsequences()
    test_edit_distance()
    test_burst_balloons()
    test_regular_expression_matching()
    print("\n================ ALL 11 TESTS PASSED! (100% VERIFIED) ================\n")
