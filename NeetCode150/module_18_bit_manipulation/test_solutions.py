"""
NeetCode 150 - Module 6.3: Verification & Test Suite
Unit tests with comprehensive edge cases for all 7 Bit Manipulation solutions.
"""

from solutions import (
    SolutionSingleNumber,
    SolutionNumberOf1Bits,
    SolutionCountingBits,
    SolutionReverseBits,
    SolutionMissingNumber,
    SolutionSumOfTwoIntegers,
    SolutionReverseInteger,
)


def test_single_number():
    sol = SolutionSingleNumber()
    assert sol.singleNumber([2, 2, 1]) == 1
    assert sol.singleNumber([4, 1, 2, 1, 2]) == 4
    assert sol.singleNumber([1]) == 1
    assert sol.singleNumber([-3, 5, -3]) == 5
    print("PASS: 1. Single Number")


def test_number_of_1_bits():
    sol = SolutionNumberOf1Bits()
    assert sol.hammingWeight(11) == 3  # 1011
    assert sol.hammingWeight(128) == 1
    assert sol.hammingWeight(2147483645) == 30
    assert sol.hammingWeight(0) == 0
    print("PASS: 2. Number of 1 Bits")


def test_counting_bits():
    sol = SolutionCountingBits()
    assert sol.countBits(2) == [0, 1, 1]
    assert sol.countBits(5) == [0, 1, 1, 2, 1, 2]
    assert sol.countBits(0) == [0]
    print("PASS: 3. Counting Bits")


def test_reverse_bits():
    sol = SolutionReverseBits()
    # 43261596 has binary 00000010100101000001111010011100
    # Reversed: 00111001011110000010100101000000 (964176192)
    assert sol.reverseBits(43261596) == 964176192
    assert sol.reverseBits(0) == 0
    print("PASS: 4. Reverse Bits")


def test_missing_number():
    sol = SolutionMissingNumber()
    assert sol.missingNumber([3, 0, 1]) == 2
    assert sol.missingNumber([0, 1]) == 2
    assert sol.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
    assert sol.missingNumber([0]) == 1
    print("PASS: 5. Missing Number")


def test_sum_of_two_integers():
    sol = SolutionSumOfTwoIntegers()
    assert sol.getSum(1, 2) == 3
    assert sol.getSum(2, 3) == 5
    assert sol.getSum(-1, 1) == 0
    assert sol.getSum(-2, 3) == 1
    assert sol.getSum(-5, -7) == -12
    assert sol.getSum(0, 0) == 0
    print("PASS: 6. Sum of Two Integers")


def test_reverse_integer():
    sol = SolutionReverseInteger()
    assert sol.reverse(123) == 321
    assert sol.reverse(-123) == -321
    assert sol.reverse(120) == 21
    assert sol.reverse(0) == 0
    # 32-bit overflow check: 1534236469 reversed exceeds 2^31 - 1
    assert sol.reverse(1534236469) == 0
    assert sol.reverse(-2147483648) == 0
    print("PASS: 7. Reverse Integer")


if __name__ == "__main__":
    print("\n================ RUNNING BIT MANIPULATION VERIFICATION ================\n")
    test_single_number()
    test_number_of_1_bits()
    test_counting_bits()
    test_reverse_bits()
    test_missing_number()
    test_sum_of_two_integers()
    test_reverse_integer()
    print("\n================ ALL 7 TESTS PASSED! (100% VERIFIED) ================\n")
