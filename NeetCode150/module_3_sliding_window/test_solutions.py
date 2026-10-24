"""
NeetCode 150 - Module 1.3: Verification & Test Suite
Unit tests with comprehensive edge cases for all 6 Sliding Window solutions.
"""

from solutions import (
    SolutionBestTimeToBuyAndSellStock,
    SolutionLongestSubstringWithoutRepeatingCharacters,
    SolutionLongestRepeatingCharacterReplacement,
    SolutionPermutationInString,
    SolutionMinimumWindowSubstring,
    SolutionSlidingWindowMaximum,
)


def test_best_time_to_buy_and_sell_stock():
    sol = SolutionBestTimeToBuyAndSellStock()
    # Standard cases
    assert sol.maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert sol.maxProfit([7, 6, 4, 3, 1]) == 0
    # Edge cases: single day, flat prices, ascending
    assert sol.maxProfit([5]) == 0
    assert sol.maxProfit([3, 3, 3, 3]) == 0
    assert sol.maxProfit([1, 2, 3, 4, 5]) == 4
    print("PASS: 1. Best Time to Buy and Sell Stock")


def test_longest_substring_without_repeating_characters():
    sol = SolutionLongestSubstringWithoutRepeatingCharacters()
    # Standard cases
    assert sol.lengthOfLongestSubstring("abcabcbb") == 3
    assert sol.lengthOfLongestSubstring("bbbbb") == 1
    assert sol.lengthOfLongestSubstring("pwwkew") == 3
    # Edge cases
    assert sol.lengthOfLongestSubstring("") == 0
    assert sol.lengthOfLongestSubstring(" ") == 1
    assert sol.lengthOfLongestSubstring("au") == 2
    assert sol.lengthOfLongestSubstring("abba") == 2  # tricky left-pointer jump check
    print("PASS: 2. Longest Substring Without Repeating Characters")


def test_longest_repeating_character_replacement():
    sol = SolutionLongestRepeatingCharacterReplacement()
    # Standard cases
    assert sol.characterReplacement("ABAB", 2) == 4
    assert sol.characterReplacement("AABABBA", 1) == 4
    # Edge cases: k = 0, k >= len(s), single char
    assert sol.characterReplacement("ABBB", 0) == 3
    assert sol.characterReplacement("ABCDE", 5) == 5
    assert sol.characterReplacement("A", 0) == 1
    print("PASS: 3. Longest Repeating Character Replacement")


def test_permutation_in_string():
    sol = SolutionPermutationInString()
    # Standard cases
    assert sol.checkInclusion("ab", "eidbaooo") is True
    assert sol.checkInclusion("ab", "eidboaoo") is False
    # Edge cases: len(s1) > len(s2), identical strings, single letter
    assert sol.checkInclusion("hello", "ooolleoooleh") is False
    assert sol.checkInclusion("abc", "cba") is True
    assert sol.checkInclusion("a", "a") is True
    assert sol.checkInclusion("longer", "short") is False
    print("PASS: 4. Permutation in String")


def test_minimum_window_substring():
    sol = SolutionMinimumWindowSubstring()
    # Standard cases
    assert sol.minWindow("ADOBECODEBANC", "ABC") == "BANC"
    assert sol.minWindow("a", "a") == "a"
    assert sol.minWindow("a", "aa") == ""
    # Edge cases
    assert sol.minWindow("aa", "aa") == "aa"
    assert sol.minWindow("ab", "b") == "b"
    assert sol.minWindow("bba", "ab") == "ba"
    print("PASS: 5. Minimum Window Substring")


def test_sliding_window_maximum():
    sol = SolutionSlidingWindowMaximum()
    # Standard cases
    assert sol.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
    assert sol.maxSlidingWindow([1], 1) == [1]
    # Edge cases: k = 1, k = len(nums), negative values, strictly decreasing
    assert sol.maxSlidingWindow([1, -1], 1) == [1, -1]
    assert sol.maxSlidingWindow([9, 11], 2) == [11]
    assert sol.maxSlidingWindow([4, -2], 2) == [4]
    assert sol.maxSlidingWindow([7, 6, 5, 4, 3, 2, 1], 3) == [7, 6, 5, 4, 3]
    print("PASS: 6. Sliding Window Maximum")


if __name__ == "__main__":
    print("\n================ RUNNING SLIDING WINDOW VERIFICATION ================\n")
    test_best_time_to_buy_and_sell_stock()
    test_longest_substring_without_repeating_characters()
    test_longest_repeating_character_replacement()
    test_permutation_in_string()
    test_minimum_window_substring()
    test_sliding_window_maximum()
    print("\n================ ALL 6 TESTS PASSED! (100% VERIFIED) ================\n")
