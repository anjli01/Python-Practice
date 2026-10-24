"""
NeetCode 150 - Module 6.3: Bit Manipulation
Detailed, fully-commented Python 3 solutions for all 7 problems.
"""

from typing import List


# ============================================================================
# Problem 1: Single Number (LeetCode 136) - Easy
# Pattern: XOR Self-Cancellation
# ============================================================================
class SolutionSingleNumber:
    def singleNumber(self, nums: List[int]) -> int:
        """Finds element that appears once where all others appear twice in O(n) and O(1) space."""
        res = 0
        for n in nums:
            res ^= n
        return res


# ============================================================================
# Problem 2: Number of 1 Bits (LeetCode 191) - Easy
# Pattern: Brian Kernighan's Bit-Clearing Algorithm
# ============================================================================
class SolutionNumberOf1Bits:
    def hammingWeight(self, n: int) -> int:
        """Counts set bits (Hamming weight) of an unsigned integer in O(set bits)."""
        count = 0
        while n > 0:
            n &= (n - 1)  # Clears the least significant set bit
            count += 1
        return count


# ============================================================================
# Problem 3: Counting Bits (LeetCode 338) - Easy
# Pattern: Bit-Shift DP Subproblem
# ============================================================================
class SolutionCountingBits:
    def countBits(self, n: int) -> List[int]:
        """Calculates number of 1 bits for every number from 0 to n in O(n)."""
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            # dp[i] = dp[i // 2] + (1 if i is odd else 0)
            dp[i] = dp[i >> 1] + (i & 1)
        return dp


# ============================================================================
# Problem 4: Reverse Bits (LeetCode 190) - Easy
# Pattern: 32-Bit Shift and Accumulate
# ============================================================================
class SolutionReverseBits:
    def reverseBits(self, n: int) -> int:
        """Reverses the 32 bits of a given unsigned integer."""
        res = 0
        for _ in range(32):
            res = (res << 1) | (n & 1)
            n >>= 1
        return res


# ============================================================================
# Problem 5: Missing Number (LeetCode 268) - Easy
# Pattern: XOR or Gauss Summation
# ============================================================================
class SolutionMissingNumber:
    def missingNumber(self, nums: List[int]) -> int:
        """Finds the only number in range [0, n] missing from the array in O(n) and O(1) space."""
        n = len(nums)
        res = n
        for i in range(n):
            res ^= i ^ nums[i]
        return res


# ============================================================================
# Problem 6: Sum of Two Integers (LeetCode 371) - Medium
# Pattern: Bitwise Half-Adder with 32-Bit Masking
# ============================================================================
class SolutionSumOfTwoIntegers:
    def getSum(self, a: int, b: int) -> int:
        """Calculates sum of two integers without using operators + and -."""
        mask = 0xFFFFFFFF  # 32-bit mask to handle Python's arbitrary-precision integers

        while (b & mask) != 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry

        # Convert back from 32-bit two's complement if negative
        return (a & mask) if (a & mask) <= 0x7FFFFFFF else ~( (a & mask) ^ mask )


# ============================================================================
# Problem 7: Reverse Integer (LeetCode 7) - Medium
# Pattern: Digit-by-Digit Reversal with 32-bit Overflow Guard
# ============================================================================
class SolutionReverseInteger:
    def reverse(self, x: int) -> int:
        """Reverses digits of a 32-bit signed integer, returning 0 if overflowing."""
        sign = -1 if x < 0 else 1
        x = abs(x)
        res = 0

        while x > 0:
            digit = x % 10
            x //= 10
            res = res * 10 + digit

        res *= sign

        # Check 32-bit signed integer boundaries: [-2^31, 2^31 - 1]
        if res < -2**31 or res > 2**31 - 1:
            return 0
        return res
