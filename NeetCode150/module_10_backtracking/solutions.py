"""
NeetCode 150 - Module 4.1: Backtracking
Detailed, fully-commented Python 3 solutions for all 9 problems.
"""

from typing import List


# ============================================================================
# Problem 1: Subsets (LeetCode 78) - Medium
# Pattern: Pick / Don't-Pick Binary Decision Tree
# ============================================================================
class SolutionSubsets:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """Generates all 2^n unique subsets (power set) of distinct integers."""
        result = []
        subset = []

        def dfs(i: int):
            if i >= len(nums):
                result.append(subset.copy())
                return
            # Decision 1: Include nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            # Decision 2: Do NOT include nums[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return result


# ============================================================================
# Problem 2: Combination Sum (LeetCode 39) - Medium
# Pattern: Unbounded Choice Backtracking
# ============================================================================
class SolutionCombinationSum:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """Finds all unique combinations where candidate numbers sum to target (reusable)."""
        result = []

        def dfs(i: int, cur_comb: List[int], total: int):
            if total == target:
                result.append(cur_comb.copy())
                return
            if i >= len(candidates) or total > target:
                return

            # Branch 1: Pick candidates[i] (can be picked repeatedly)
            cur_comb.append(candidates[i])
            dfs(i, cur_comb, total + candidates[i])
            cur_comb.pop()

            # Branch 2: Skip candidates[i] completely
            dfs(i + 1, cur_comb, total)

        dfs(0, [], 0)
        return result


# ============================================================================
# Problem 3: Permutations (LeetCode 46) - Medium
# Pattern: Unused-Element State Tracking
# ============================================================================
class SolutionPermutations:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """Generates all n! permutations of distinct integers."""
        result = []

        def backtrack(curr: List[int], remaining: List[int]):
            if not remaining:
                result.append(curr.copy())
                return
            for i in range(len(remaining)):
                curr.append(remaining[i])
                backtrack(curr, remaining[:i] + remaining[i + 1:])
                curr.pop()

        backtrack([], nums)
        return result


# ============================================================================
# Problem 4: Subsets II (LeetCode 90) - Medium
# Pattern: Sort + Duplicate-Skipping Branch
# ============================================================================
class SolutionSubsetsII:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """Generates all unique subsets from a collection that may contain duplicates."""
        nums.sort()
        result = []
        subset = []

        def dfs(i: int):
            if i >= len(nums):
                result.append(subset.copy())
                return

            # Include nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()

            # Skip nums[i] and all consecutive duplicates of nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1)

        dfs(0)
        return result


# ============================================================================
# Problem 5: Combination Sum II (LeetCode 40) - Medium
# Pattern: Loop-Based Deduplication (Each element used at most once)
# ============================================================================
class SolutionCombinationSumII:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """Finds unique combinations summing to target with each candidate used at most once."""
        candidates.sort()
        result = []

        def dfs(start_idx: int, cur_comb: List[int], remaining: int):
            if remaining == 0:
                result.append(cur_comb.copy())
                return
            if remaining < 0:
                return

            for i in range(start_idx, len(candidates)):
                # Skip duplicate elements at the same decision level
                if i > start_idx and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > remaining:
                    break  # Prune search since candidates is sorted

                cur_comb.append(candidates[i])
                dfs(i + 1, cur_comb, remaining - candidates[i])
                cur_comb.pop()

        dfs(0, [], target)
        return result


# ============================================================================
# Problem 6: Word Search (LeetCode 79) - Medium
# Pattern: 2D Grid DFS with Visited Masking
# ============================================================================
class SolutionWordSearch:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """Determines if word exists in grid through horizontally or vertically adjacent cells."""
        ROWS, COLS = len(board), len(board[0])

        def dfs(r: int, c: int, idx: int) -> bool:
            if idx == len(word):
                return True
            if not (0 <= r < ROWS and 0 <= c < COLS) or board[r][c] != word[idx]:
                return False

            # Mark visited
            temp = board[r][c]
            board[r][c] = '#'

            found = (dfs(r + 1, c, idx + 1) or
                     dfs(r - 1, c, idx + 1) or
                     dfs(r, c + 1, idx + 1) or
                     dfs(r, c - 1, idx + 1))

            # Backtrack
            board[r][c] = temp
            return found

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False


# ============================================================================
# Problem 7: Palindrome Partitioning (LeetCode 131) - Medium
# Pattern: Prefix Palindrome Split
# ============================================================================
class SolutionPalindromePartitioning:
    def partition(self, s: str) -> List[List[str]]:
        """Partitions s such that every substring of the partition is a palindrome."""
        result = []
        part = []

        def is_palindrome(sub: str) -> bool:
            return sub == sub[::-1]

        def dfs(start: int):
            if start >= len(s):
                result.append(part.copy())
                return

            for end in range(start, len(s)):
                candidate = s[start : end + 1]
                if is_palindrome(candidate):
                    part.append(candidate)
                    dfs(end + 1)
                    part.pop()

        dfs(0)
        return result


# ============================================================================
# Problem 8: Letter Combinations of a Phone Number (LeetCode 17) - Medium
# Pattern: Combinatorial Product Tree
# ============================================================================
class SolutionLetterCombinations:
    def letterCombinations(self, digits: str) -> List[str]:
        """Returns all possible letter combinations representing the phone number digits."""
        if not digits:
            return []

        digit_to_letters = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        result = []

        def backtrack(idx: int, cur_str: List[str]):
            if idx == len(digits):
                result.append("".join(cur_str))
                return

            for letter in digit_to_letters[digits[idx]]:
                cur_str.append(letter)
                backtrack(idx + 1, cur_str)
                cur_str.pop()

        backtrack(0, [])
        return result


# ============================================================================
# Problem 9: N-Queens (LeetCode 51) - Hard
# Pattern: Row-by-Row Placement with Diagonal Collision Hash Sets
# ============================================================================
class SolutionNQueens:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """Places n non-attacking queens on an n x n chessboard."""
        cols = set()
        pos_diags = set()  # (r + c) constant along / diagonals
        neg_diags = set()  # (r - c) constant along \ diagonals
        board = [["."] * n for _ in range(n)]
        result = []

        def backtrack(r: int):
            if r == n:
                result.append(["".join(row) for row in board])
                return

            for c in range(n):
                if c in cols or (r + c) in pos_diags or (r - c) in neg_diags:
                    continue

                # Place queen
                cols.add(c)
                pos_diags.add(r + c)
                neg_diags.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                # Backtrack
                cols.remove(c)
                pos_diags.remove(r + c)
                neg_diags.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return result
