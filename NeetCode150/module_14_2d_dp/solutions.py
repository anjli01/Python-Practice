"""
NeetCode 150 - Module 5.2: 2-D Dynamic Programming
Detailed, fully-commented Python 3 solutions for all 11 problems.
"""

from typing import List


# ============================================================================
# Problem 1: Unique Paths (LeetCode 62) - Medium
# Pattern: Grid Path DP with 1D Space Optimization
# ============================================================================
class SolutionUniquePaths:
    def uniquePaths(self, m: int, n: int) -> int:
        """Finds total unique paths from top-left to bottom-right of an m x n grid."""
        row = [1] * n
        for _ in range(m - 1):
            new_row = [1] * n
            for j in range(n - 2, -1, -1):
                new_row[j] = new_row[j + 1] + row[j]
            row = new_row
        return row[0]


# ============================================================================
# Problem 2: Longest Common Subsequence (LeetCode 1143) - Medium
# Pattern: 2D String Alignment DP
# ============================================================================
class SolutionLongestCommonSubsequence:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """Finds length of longest common subsequence between two strings."""
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        return dp[0][0]


# ============================================================================
# Problem 3: Best Time to Buy and Sell Stock with Cooldown (LeetCode 309) - Medium
# Pattern: State-Machine DP (Buy, Sell, Cooldown)
# ============================================================================
class SolutionStockWithCooldown:
    def maxProfit(self, prices: List[int]) -> int:
        """Finds max profit with an enforced 1-day cooldown after selling."""
        memo = {}

        def dfs(i: int, buying: bool) -> int:
            if i >= len(prices):
                return 0
            if (i, buying) in memo:
                return memo[(i, buying)]

            cooldown = dfs(i + 1, buying)
            if buying:
                buy = dfs(i + 1, False) - prices[i]
                memo[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, True) + prices[i]  # i + 2 due to 1-day cooldown
                memo[(i, buying)] = max(sell, cooldown)

            return memo[(i, buying)]

        return dfs(0, True)


# ============================================================================
# Problem 4: Coin Change II (LeetCode 518) - Medium
# Pattern: Unbounded Knapsack (Combinations Count)
# ============================================================================
class SolutionCoinChangeII:
    def change(self, amount: int, coins: List[int]) -> int:
        """Calculates total combinations of coins that make up amount."""
        dp = [0] * (amount + 1)
        dp[0] = 1  # 1 way to make 0 amount

        # Outer loop over coins ensures ordered combinations (no permutation duplicates)
        for c in coins:
            for a in range(c, amount + 1):
                dp[a] += dp[a - c]

        return dp[amount]


# ============================================================================
# Problem 5: Target Sum (LeetCode 494) - Medium
# Pattern: Math Reduction to Subset Sum
# ============================================================================
class SolutionTargetSum:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        Calculates distinct symbol assignments (+/-) yielding target.
        P - N = target, P + N = total -> 2P = target + total -> P = (target + total) // 2
        """
        total = sum(nums)
        if (total + target) % 2 != 0 or total < abs(target):
            return 0

        subset_target = (total + target) // 2
        dp = [0] * (subset_target + 1)
        dp[0] = 1

        for n in nums:
            for s in range(subset_target, n - 1, -1):
                dp[s] += dp[s - n]

        return dp[subset_target]


# ============================================================================
# Problem 6: Interleaving String (LeetCode 97) - Medium
# Pattern: 2D Matrix Grid DP
# ============================================================================
class SolutionInterleavingString:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """Determines if s3 is formed by an interleaving of s1 and s2."""
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        dp[len(s1)][len(s2)] = True

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True

        return dp[0][0]


# ============================================================================
# Problem 7: Longest Increasing Path in a Matrix (LeetCode 329) - Hard
# Pattern: Memoized DFS on Implicit DAG
# ============================================================================
class SolutionLongestIncreasingPath:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """Finds length of longest increasing path in matrix."""
        ROWS, COLS = len(matrix), len(matrix[0])
        memo = {}

        def dfs(r: int, c: int) -> int:
            if (r, c) in memo:
                return memo[(r, c)]
            res = 1
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and matrix[nr][nc] > matrix[r][c]:
                    res = max(res, 1 + dfs(nr, nc))
            memo[(r, c)] = res
            return res

        return max(dfs(r, c) for r in range(ROWS) for c in range(COLS))


# ============================================================================
# Problem 8: Distinct Subsequences (LeetCode 115) - Hard
# Pattern: 2D Subsequence Frequency DP
# ============================================================================
class SolutionDistinctSubsequences:
    def numDistinct(self, s: str, t: str) -> int:
        """Finds number of distinct subsequences of s which equal t."""
        m, n = len(s), len(t)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = 1  # Empty string is a subsequence of any prefix

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[m][n]


# ============================================================================
# Problem 9: Edit Distance (LeetCode 72) - Medium
# Pattern: Classical Levenshtein Distance DP
# ============================================================================
class SolutionEditDistance:
    def minDistance(self, word1: str, word2: str) -> int:
        """Finds minimum operations (insert, delete, replace) to convert word1 to word2."""
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j],      # Delete
                                       dp[i][j - 1],      # Insert
                                       dp[i - 1][j - 1])  # Replace

        return dp[m][n]


# ============================================================================
# Problem 10: Burst Balloons (LeetCode 312) - Hard
# Pattern: Interval DP (Choice of Last Balloon to Burst)
# ============================================================================
class SolutionBurstBalloons:
    def maxCoins(self, nums: List[int]) -> int:
        """Finds maximum coins collected by bursting balloons."""
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        # Window length from 1 to n - 2
        for length in range(1, n - 1):
            for left in range(1, n - length):
                right = left + length - 1
                for i in range(left, right + 1):
                    coins = nums[left - 1] * nums[i] * nums[right + 1]
                    coins += dp[left][i - 1] + dp[i + 1][right]
                    dp[left][right] = max(dp[left][right], coins)

        return dp[1][n - 2]


# ============================================================================
# Problem 11: Regular Expression Matching (LeetCode 10) - Hard
# Pattern: Top-Down Memoized State Machine with Wildcard Lookahead
# ============================================================================
class SolutionRegularExpressionMatching:
    def isMatch(self, s: str, p: str) -> bool:
        """Evaluates regex matching with '.' and '*' support."""
        memo = {}

        def dfs(i: int, j: int) -> bool:
            if (i, j) in memo:
                return memo[(i, j)]
            if j == len(p):
                return i == len(s)

            match = i < len(s) and (s[i] == p[j] or p[j] == '.')

            if (j + 1) < len(p) and p[j + 1] == '*':
                # Branch 1: Skip '*' and previous char (0 occurrences)
                # Branch 2: Use '*' if char matches
                res = dfs(i, j + 2) or (match and dfs(i + 1, j))
            else:
                res = match and dfs(i + 1, j + 1)

            memo[(i, j)] = res
            return res

        return dfs(0, 0)
