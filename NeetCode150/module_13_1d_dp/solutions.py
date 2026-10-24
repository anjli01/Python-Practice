"""
NeetCode 150 - Module 5.1: 1-D Dynamic Programming
Detailed, fully-commented Python 3 solutions for all 12 problems.
"""

from typing import List
import bisect


# ============================================================================
# Problem 1: Climbing Stairs (LeetCode 70) - Easy
# Pattern: Fibonacci State Transition
# ============================================================================
class SolutionClimbingStairs:
    def climbStairs(self, n: int) -> int:
        """Calculates distinct ways to climb n steps taking 1 or 2 steps."""
        one, two = 1, 1
        for _ in range(n - 1):
            one, two = one + two, one
        return one


# ============================================================================
# Problem 2: Min Cost Climbing Stairs (LeetCode 746) - Easy
# Pattern: Bottom-Up Dynamic In-Place Accumulation
# ============================================================================
class SolutionMinCostClimbingStairs:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """Finds minimum cost to reach the top of the floor."""
        cost.append(0)
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])
        return min(cost[0], cost[1])


# ============================================================================
# Problem 3: House Robber (LeetCode 198) - Medium
# Pattern: Non-Adjacent Maximum Accumulator
# ============================================================================
class SolutionHouseRobber:
    def rob(self, nums: List[int]) -> int:
        """Finds max loot without robbing two adjacent houses."""
        rob1, rob2 = 0, 0
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2


# ============================================================================
# Problem 4: House Robber II (LeetCode 213) - Medium
# Pattern: Circular Array Subproblem Partitioning
# ============================================================================
class SolutionHouseRobberII:
    def rob(self, nums: List[int]) -> int:
        """Finds max loot in a circular street of houses."""
        def linear_rob(houses: List[int]) -> int:
            rob1, rob2 = 0, 0
            for h in houses:
                temp = max(h + rob1, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2

        return max(nums[0], linear_rob(nums[1:]), linear_rob(nums[:-1]))


# ============================================================================
# Problem 5: Longest Palindromic Substring (LeetCode 5) - Medium
# Pattern: Expand Around Center (Odd & Even Radii)
# ============================================================================
class SolutionLongestPalindrome:
    def longestPalindrome(self, s: str) -> str:
        """Finds the longest palindromic substring in s in O(n^2) time and O(1) space."""
        res = ""
        res_len = 0

        for i in range(len(s)):
            # Odd length palindromes: center at (i, i)
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > res_len:
                    res = s[l : r + 1]
                    res_len = r - l + 1
                l -= 1
                r += 1

            # Even length palindromes: center at (i, i + 1)
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > res_len:
                    res = s[l : r + 1]
                    res_len = r - l + 1
                l -= 1
                r += 1

        return res


# ============================================================================
# Problem 6: Palindromic Substrings (LeetCode 647) - Medium
# Pattern: Center Expansion Count
# ============================================================================
class SolutionPalindromicSubstrings:
    def countSubstrings(self, s: str) -> int:
        """Counts the total number of palindromic substrings in s."""
        count = 0

        for i in range(len(s)):
            # Odd radius
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            # Even radius
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

        return count


# ============================================================================
# Problem 7: Decode Ways (LeetCode 91) - Medium
# Pattern: Fibonacci-Style Valid Branch DP
# ============================================================================
class SolutionDecodeWays:
    def numDecodings(self, s: str) -> int:
        """Counts total ways to decode a message string encoded from '1'-'26'."""
        if not s or s[0] == '0':
            return 0

        dp1, dp2 = 1, 1  # dp[i+1], dp[i+2]
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                cur = 0
            else:
                cur = dp1

            # Two-digit check for 10-26
            if i + 1 < len(s) and (s[i] == '1' or (s[i] == '2' and s[i + 1] in "0123456")):
                cur += dp2

            dp2 = dp1
            dp1 = cur

        return dp1


# ============================================================================
# Problem 8: Coin Change (LeetCode 322) - Medium
# Pattern: Unbounded Knapsack (Bottom-Up Array)
# ============================================================================
class SolutionCoinChange:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """Finds fewest coins needed to make up amount."""
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])

        return int(dp[amount]) if dp[amount] != float('inf') else -1


# ============================================================================
# Problem 9: Maximum Product Subarray (LeetCode 152) - Medium
# Pattern: Dual-Extrema Tracking (Min & Max Multipliers)
# ============================================================================
class SolutionMaxProductSubarray:
    def maxProduct(self, nums: List[int]) -> int:
        """Finds contiguous subarray with the largest product."""
        res = max(nums)
        cur_min, cur_max = 1, 1

        for n in nums:
            if n == 0:
                cur_min, cur_max = 1, 1
                continue
            tmp = cur_max * n
            cur_max = max(n * cur_max, n * cur_min, n)
            cur_min = min(tmp, n * cur_min, n)
            res = max(res, cur_max)

        return res


# ============================================================================
# Problem 10: Word Break (LeetCode 139) - Medium
# Pattern: Suffix Segmentation DP
# ============================================================================
class SolutionWordBreak:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """Determines if s can be segmented into a space-separated sequence of dictionary words."""
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True  # Base case: empty string matches

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if i + len(w) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        return dp[0]


# ============================================================================
# Problem 11: Longest Increasing Subsequence (LeetCode 300) - Medium
# Pattern: Patience Sorting with Binary Search (O(n log n))
# ============================================================================
class SolutionLongestIncreasingSubsequence:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """Finds length of longest strictly increasing subsequence in O(n log n)."""
        tails = []
        for x in nums:
            idx = bisect.bisect_left(tails, x)
            if idx == len(tails):
                tails.append(x)
            else:
                tails[idx] = x
        return len(tails)


# ============================================================================
# Problem 12: Partition Equal Subset Sum (LeetCode 416) - Medium
# Pattern: 0/1 Knapsack Target Sum
# ============================================================================
class SolutionPartitionEqualSubsetSum:
    def canPartition(self, nums: List[int]) -> bool:
        """Determines if array can be partitioned into two subsets with equal sum."""
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        dp = {0}

        for num in nums:
            next_dp = set(dp)
            for t in dp:
                if t + num == target:
                    return True
                if t + num < target:
                    next_dp.add(t + num)
            dp = next_dp

        return target in dp
