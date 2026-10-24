"""
NeetCode 150 - Module 5.1: Verification & Test Suite
Unit tests with comprehensive edge cases for all 12 1-D Dynamic Programming solutions.
"""

from solutions import (
    SolutionClimbingStairs,
    SolutionMinCostClimbingStairs,
    SolutionHouseRobber,
    SolutionHouseRobberII,
    SolutionLongestPalindrome,
    SolutionPalindromicSubstrings,
    SolutionDecodeWays,
    SolutionCoinChange,
    SolutionMaxProductSubarray,
    SolutionWordBreak,
    SolutionLongestIncreasingSubsequence,
    SolutionPartitionEqualSubsetSum,
)


def test_climbing_stairs():
    sol = SolutionClimbingStairs()
    assert sol.climbStairs(2) == 2
    assert sol.climbStairs(3) == 3
    assert sol.climbStairs(1) == 1
    assert sol.climbStairs(5) == 8
    print("PASS: 1. Climbing Stairs")


def test_min_cost_climbing_stairs():
    sol = SolutionMinCostClimbingStairs()
    assert sol.minCostClimbingStairs([10, 15, 20]) == 15
    assert sol.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
    assert sol.minCostClimbingStairs([0, 0]) == 0
    print("PASS: 2. Min Cost Climbing Stairs")


def test_house_robber():
    sol = SolutionHouseRobber()
    assert sol.rob([1, 2, 3, 1]) == 4
    assert sol.rob([2, 7, 9, 3, 1]) == 12
    assert sol.rob([5]) == 5
    assert sol.rob([2, 1]) == 2
    print("PASS: 3. House Robber")


def test_house_robber_ii():
    sol = SolutionHouseRobberII()
    assert sol.rob([2, 3, 2]) == 3
    assert sol.rob([1, 2, 3, 1]) == 4
    assert sol.rob([1, 2, 3]) == 3
    assert sol.rob([1]) == 1
    print("PASS: 4. House Robber II")


def test_longest_palindrome():
    sol = SolutionLongestPalindrome()
    assert sol.longestPalindrome("babad") in ("bab", "aba")
    assert sol.longestPalindrome("cbbd") == "bb"
    assert sol.longestPalindrome("a") == "a"
    assert sol.longestPalindrome("ac") in ("a", "c")
    print("PASS: 5. Longest Palindromic Substring")


def test_palindromic_substrings():
    sol = SolutionPalindromicSubstrings()
    assert sol.countSubstrings("abc") == 3
    assert sol.countSubstrings("aaa") == 6
    assert sol.countSubstrings("a") == 1
    print("PASS: 6. Palindromic Substrings")


def test_decode_ways():
    sol = SolutionDecodeWays()
    assert sol.numDecodings("12") == 2
    assert sol.numDecodings("226") == 3
    assert sol.numDecodings("06") == 0
    assert sol.numDecodings("10") == 1
    assert sol.numDecodings("27") == 1
    print("PASS: 7. Decode Ways")


def test_coin_change():
    sol = SolutionCoinChange()
    assert sol.coinChange([1, 2, 5], 11) == 3
    assert sol.coinChange([2], 3) == -1
    assert sol.coinChange([1], 0) == 0
    assert sol.coinChange([2, 5, 10, 1], 27) == 4
    print("PASS: 8. Coin Change")


def test_max_product_subarray():
    sol = SolutionMaxProductSubarray()
    assert sol.maxProduct([2, 3, -2, 4]) == 6
    assert sol.maxProduct([-2, 0, -1]) == 0
    assert sol.maxProduct([-2, 3, -4]) == 24
    assert sol.maxProduct([-2]) == -2
    print("PASS: 9. Maximum Product Subarray")


def test_word_break():
    sol = SolutionWordBreak()
    assert sol.wordBreak("leetcode", ["leet", "code"]) is True
    assert sol.wordBreak("applepenapple", ["apple", "pen"]) is True
    assert sol.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) is False
    print("PASS: 10. Word Break")


def test_longest_increasing_subsequence():
    sol = SolutionLongestIncreasingSubsequence()
    assert sol.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert sol.lengthOfLIS([0, 1, 0, 3, 2, 3]) == 4
    assert sol.lengthOfLIS([7, 7, 7, 7, 7]) == 1
    assert sol.lengthOfLIS([5]) == 1
    print("PASS: 11. Longest Increasing Subsequence")


def test_partition_equal_subset_sum():
    sol = SolutionPartitionEqualSubsetSum()
    assert sol.canPartition([1, 5, 11, 5]) is True
    assert sol.canPartition([1, 2, 3, 5]) is False
    assert sol.canPartition([1, 2, 5]) is False
    print("PASS: 12. Partition Equal Subset Sum")


if __name__ == "__main__":
    print("\n================ RUNNING 1-D DP VERIFICATION ================\n")
    test_climbing_stairs()
    test_min_cost_climbing_stairs()
    test_house_robber()
    test_house_robber_ii()
    test_longest_palindrome()
    test_palindromic_substrings()
    test_decode_ways()
    test_coin_change()
    test_max_product_subarray()
    test_word_break()
    test_longest_increasing_subsequence()
    test_partition_equal_subset_sum()
    print("\n================ ALL 12 TESTS PASSED! (100% VERIFIED) ================\n")
