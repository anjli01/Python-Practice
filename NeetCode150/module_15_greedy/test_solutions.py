"""
NeetCode 150 - Module 5.3: Verification & Test Suite
Unit tests with comprehensive edge cases for all 8 Greedy solutions.
"""

from solutions import (
    SolutionMaximumSubarray,
    SolutionJumpGame,
    SolutionJumpGameII,
    SolutionGasStation,
    SolutionHandOfStraights,
    SolutionMergeTriplets,
    SolutionPartitionLabels,
    SolutionValidParenthesisString,
)


def test_maximum_subarray():
    sol = SolutionMaximumSubarray()
    assert sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert sol.maxSubArray([1]) == 1
    assert sol.maxSubArray([5, 4, -1, 7, 8]) == 23
    assert sol.maxSubArray([-5, -2, -1, -4]) == -1
    print("PASS: 1. Maximum Subarray")


def test_jump_game():
    sol = SolutionJumpGame()
    assert sol.canJump([2, 3, 1, 1, 4]) is True
    assert sol.canJump([3, 2, 1, 0, 4]) is False
    assert sol.canJump([0]) is True
    print("PASS: 2. Jump Game")


def test_jump_game_ii():
    sol = SolutionJumpGameII()
    assert sol.jump([2, 3, 1, 1, 4]) == 2
    assert sol.jump([2, 3, 0, 1, 4]) == 2
    assert sol.jump([0]) == 0
    print("PASS: 3. Jump Game II")


def test_gas_station():
    sol = SolutionGasStation()
    assert sol.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) == 3
    assert sol.canCompleteCircuit([2, 3, 4], [3, 4, 3]) == -1
    print("PASS: 4. Gas Station")


def test_hand_of_straights():
    sol = SolutionHandOfStraights()
    assert sol.isNStraightHand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3) is True
    assert sol.isNStraightHand([1, 2, 3, 4, 5], 4) is False
    assert sol.isNStraightHand([8, 10, 10, 2, 8], 2) is False
    print("PASS: 5. Hand of Straights")


def test_merge_triplets():
    sol = SolutionMergeTriplets()
    triplets1 = [[2, 5, 3], [1, 8, 4], [1, 7, 5]]
    assert sol.mergeTriplets(triplets1, [2, 7, 5]) is True
    triplets2 = [[3, 4, 5], [4, 5, 6]]
    assert sol.mergeTriplets(triplets2, [3, 2, 5]) is False
    print("PASS: 6. Merge Triplets to Form Target Triplet")


def test_partition_labels():
    sol = SolutionPartitionLabels()
    assert sol.partitionLabels("ababcbacadefegdehijhklij") == [9, 7, 8]
    assert sol.partitionLabels("eccbbbbdec") == [10]
    print("PASS: 7. Partition Labels")


def test_valid_parenthesis_string():
    sol = SolutionValidParenthesisString()
    assert sol.checkValidString("()") is True
    assert sol.checkValidString("(*)") is True
    assert sol.checkValidString("(*))") is True
    assert sol.checkValidString(")(") is False
    assert sol.checkValidString("(((((*)))**") is True
    print("PASS: 8. Valid Parenthesis String")


if __name__ == "__main__":
    print("\n================ RUNNING GREEDY VERIFICATION ================\n")
    test_maximum_subarray()
    test_jump_game()
    test_jump_game_ii()
    test_gas_station()
    test_hand_of_straights()
    test_merge_triplets()
    test_partition_labels()
    test_valid_parenthesis_string()
    print("\n================ ALL 8 TESTS PASSED! (100% VERIFIED) ================\n")
