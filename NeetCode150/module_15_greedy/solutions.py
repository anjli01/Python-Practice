"""
NeetCode 150 - Module 5.3: Greedy
Detailed, fully-commented Python 3 solutions for all 8 problems.
"""

from typing import List
from collections import Counter
import heapq


# ============================================================================
# Problem 1: Maximum Subarray (LeetCode 53) - Medium
# Pattern: Kadane's Algorithm
# ============================================================================
class SolutionMaximumSubarray:
    def maxSubArray(self, nums: List[int]) -> int:
        """Finds contiguous subarray with the largest sum in O(n) time and O(1) space."""
        max_sum = nums[0]
        cur_sum = 0
        for n in nums:
            cur_sum = max(n, cur_sum + n)
            max_sum = max(max_sum, cur_sum)
        return max_sum


# ============================================================================
# Problem 2: Jump Game (LeetCode 55) - Medium
# Pattern: Backward Goalpost Shift
# ============================================================================
class SolutionJumpGame:
    def canJump(self, nums: List[int]) -> bool:
        """Determines if you can reach the last index."""
        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0


# ============================================================================
# Problem 3: Jump Game II (LeetCode 45) - Medium
# Pattern: Implicit BFS Window Levels
# ============================================================================
class SolutionJumpGameII:
    def jump(self, nums: List[int]) -> int:
        """Finds minimum number of jumps to reach the last index."""
        jumps = 0
        left, right = 0, 0

        while right < len(nums) - 1:
            farthest = 0
            for i in range(left, right + 1):
                farthest = max(farthest, i + nums[i])
            left = right + 1
            right = farthest
            jumps += 1

        return jumps


# ============================================================================
# Problem 4: Gas Station (LeetCode 134) - Medium
# Pattern: Greedy Net-Gas Reset
# ============================================================================
class SolutionGasStation:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """Finds starting gas station index to complete circular circuit."""
        if sum(gas) < sum(cost):
            return -1

        total = 0
        start = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0:
                total = 0
                start = i + 1

        return start


# ============================================================================
# Problem 5: Hand of Straights (LeetCode 846) - Medium
# Pattern: Min-Heap / Counter Consecutive Slicing
# ============================================================================
class SolutionHandOfStraights:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """Determines if hand can be rearranged into groups of consecutive cards."""
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)
        min_heap = list(count.keys())
        heapq.heapify(min_heap)

        while min_heap:
            first = min_heap[0]
            if count[first] == 0:
                heapq.heappop(min_heap)
                continue

            for card in range(first, first + groupSize):
                if count[card] < count[first]:
                    return False
                count[card] -= count[first]

        return True


# ============================================================================
# Problem 6: Merge Triplets to Form Target Triplet (LeetCode 1899) - Medium
# Pattern: Greedy Validity Filtering
# ============================================================================
class SolutionMergeTriplets:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        """Determines if target triplet can be obtained by merging valid triplets."""
        good_indices = set()

        for t in triplets:
            # Skip any triplet containing any component strictly greater than target
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            for i in range(3):
                if t[i] == target[i]:
                    good_indices.add(i)

        return len(good_indices) == 3


# ============================================================================
# Problem 7: Partition Labels (LeetCode 763) - Medium
# Pattern: Furthest Occurrence Window Slicing
# ============================================================================
class SolutionPartitionLabels:
    def partitionLabels(self, s: str) -> List[int]:
        """Partitions s so that each letter appears in at most one part."""
        last_index = {char: idx for idx, char in enumerate(s)}
        result = []
        start, end = 0, 0

        for idx, char in enumerate(s):
            end = max(end, last_index[char])
            if idx == end:
                result.append(end - start + 1)
                start = idx + 1

        return result


# ============================================================================
# Problem 8: Valid Parenthesis String (LeetCode 678) - Medium
# Pattern: Wildcard Range Invariant Tracking ([cmin, cmax])
# ============================================================================
class SolutionValidParenthesisString:
    def checkValidString(self, s: str) -> bool:
        """Determines if parenthesis string with '*' wildcards is valid."""
        cmin, cmax = 0, 0

        for char in s:
            if char == '(':
                cmin += 1
                cmax += 1
            elif char == ')':
                cmin -= 1
                cmax -= 1
            else:  # '*' can be '(', ')', or ''
                cmin -= 1
                cmax += 1

            if cmax < 0:
                return False
            cmin = max(cmin, 0)  # Open brackets count cannot be negative

        return cmin == 0
