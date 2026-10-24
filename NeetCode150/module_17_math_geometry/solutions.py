"""
NeetCode 150 - Module 6.2: Math & Geometry
Detailed, fully-commented Python 3 solutions for all 8 problems.
"""

from typing import List
from collections import defaultdict


# ============================================================================
# Problem 1: Rotate Image (LeetCode 48) - Medium
# Pattern: Transpose & Reverse
# ============================================================================
class SolutionRotateImage:
    def rotate(self, matrix: List[List[int]]) -> None:
        """Rotates an n x n 2D matrix by 90 degrees clockwise in-place."""
        n = len(matrix)
        # Step 1: Transpose matrix
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row
        for i in range(n):
            matrix[i].reverse()


# ============================================================================
# Problem 2: Spiral Matrix (LeetCode 54) - Medium
# Pattern: Four-Boundary Squeeze
# ============================================================================
class SolutionSpiralMatrix:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """Returns all elements of the matrix in spiral order."""
        result = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # Move Right along top row
            for c in range(left, right + 1):
                result.append(matrix[top][c])
            top += 1

            # Move Down along right column
            for r in range(top, bottom + 1):
                result.append(matrix[r][right])
            right -= 1

            if not (top <= bottom and left <= right):
                break

            # Move Left along bottom row
            for c in range(right, left - 1, -1):
                result.append(matrix[bottom][c])
            bottom -= 1

            # Move Up along left column
            for r in range(bottom, top - 1, -1):
                result.append(matrix[r][left])
            left += 1

        return result


# ============================================================================
# Problem 3: Set Matrix Zeroes (LeetCode 73) - Medium
# Pattern: In-Place Boundary Markers (O(1) Space)
# ============================================================================
class SolutionSetMatrixZeroes:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """Sets entire row and column to 0 if an element is 0 in-place."""
        ROWS, COLS = len(matrix), len(matrix[0])
        row_zero = False

        # Determine which rows and columns need to be zeroed
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        row_zero = True

        # Zero out inner cells based on markers
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # Handle first column
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0

        # Handle first row
        if row_zero:
            for c in range(COLS):
                matrix[0][c] = 0


# ============================================================================
# Problem 4: Happy Number (LeetCode 202) - Easy
# Pattern: Cycle Detection in Sum of Squares
# ============================================================================
class SolutionHappyNumber:
    def isHappy(self, n: int) -> bool:
        """Determines if a number is happy (reaches 1 via sum of squared digits)."""
        seen = set()

        def get_next(num: int) -> int:
            total = 0
            while num > 0:
                digit = num % 10
                total += digit * digit
                num //= 10
            return total

        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)

        return n == 1


# ============================================================================
# Problem 5: Plus One (LeetCode 66) - Easy
# Pattern: Backward Carry Ripple
# ============================================================================
class SolutionPlusOne:
    def plusOne(self, digits: List[int]) -> List[int]:
        """Increments large integer by one."""
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits


# ============================================================================
# Problem 6: Pow(x, n) (LeetCode 50) - Medium
# Pattern: Fast Exponentiation by Squaring (Binary Exponentiation)
# ============================================================================
class SolutionPow:
    def myPow(self, x: float, n: int) -> float:
        """Calculates x raised to the power n in O(log n)."""
        def helper(base: float, exp: int) -> float:
            if exp == 0:
                return 1.0
            half = helper(base, exp // 2)
            if exp % 2 == 0:
                return half * half
            return half * half * base

        res = helper(x, abs(n))
        return res if n >= 0 else 1.0 / res


# ============================================================================
# Problem 7: Multiply Strings (LeetCode 43) - Medium
# Pattern: Elementary Column Multiplication
# ============================================================================
class SolutionMultiplyStrings:
    def multiply(self, num1: str, num2: str) -> str:
        """Multiplies two non-negative integers represented as strings without BigInteger."""
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        res = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                p1, p2 = i + j, i + j + 1
                total = mul + res[p2]

                res[p2] = total % 10
                res[p1] += total // 10

        # Trim leading zeroes
        start_idx = 0
        while start_idx < len(res) and res[start_idx] == 0:
            start_idx += 1

        return "".join(map(str, res[start_idx:]))


# ============================================================================
# Problem 8: Detect Squares (LeetCode 2013) - Medium
# Pattern: Diagonal Anchor Counting via Hash Map
# ============================================================================
class DetectSquares:
    """Maintains a stream of 2D points and counts axis-aligned squares."""
    def __init__(self):
        self.pts_count = defaultdict(int)
        self.pts = []

    def add(self, point: List[int]) -> None:
        self.pts_count[tuple(point)] += 1
        self.pts.append(point)

    def count(self, point: List[int]) -> int:
        px, py = point
        total_squares = 0

        for qx, qy in self.pts:
            # (qx, qy) must form a non-degenerate square diagonal with (px, py)
            if abs(px - qx) == abs(py - qy) and px != qx and py != qy:
                # The other two required corners are (px, qy) and (qx, py)
                total_squares += self.pts_count[(px, qy)] * self.pts_count[(qx, py)]

        return total_squares
