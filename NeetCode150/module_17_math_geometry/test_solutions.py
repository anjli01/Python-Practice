"""
NeetCode 150 - Module 6.2: Verification & Test Suite
Unit tests with comprehensive edge cases for all 8 Math & Geometry solutions.
"""

from solutions import (
    SolutionRotateImage,
    SolutionSpiralMatrix,
    SolutionSetMatrixZeroes,
    SolutionHappyNumber,
    SolutionPlusOne,
    SolutionPow,
    SolutionMultiplyStrings,
    DetectSquares,
)


def test_rotate_image():
    sol = SolutionRotateImage()
    mat = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    sol.rotate(mat)
    assert mat == [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3]
    ]
    print("PASS: 1. Rotate Image")


def test_spiral_matrix():
    sol = SolutionSpiralMatrix()
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    assert sol.spiralOrder(matrix) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert sol.spiralOrder([[1]]) == [1]
    assert sol.spiralOrder([[1, 2, 3, 4]]) == [1, 2, 3, 4]
    print("PASS: 2. Spiral Matrix")


def test_set_matrix_zeroes():
    sol = SolutionSetMatrixZeroes()
    mat = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    sol.setZeroes(mat)
    assert mat == [
        [1, 0, 1],
        [0, 0, 0],
        [1, 0, 1]
    ]
    mat2 = [[0, 1]]
    sol.setZeroes(mat2)
    assert mat2 == [[0, 0]]
    print("PASS: 3. Set Matrix Zeroes")


def test_happy_number():
    sol = SolutionHappyNumber()
    assert sol.isHappy(19) is True
    assert sol.isHappy(2) is False
    assert sol.isHappy(1) is True
    assert sol.isHappy(7) is True
    print("PASS: 4. Happy Number")


def test_plus_one():
    sol = SolutionPlusOne()
    assert sol.plusOne([1, 2, 3]) == [1, 2, 4]
    assert sol.plusOne([4, 3, 2, 1]) == [4, 3, 2, 2]
    assert sol.plusOne([9]) == [1, 0]
    assert sol.plusOne([9, 9, 9]) == [1, 0, 0, 0]
    print("PASS: 5. Plus One")


def test_pow():
    sol = SolutionPow()
    assert abs(sol.myPow(2.0, 10) - 1024.0) < 1e-5
    assert abs(sol.myPow(2.1, 3) - 9.261) < 1e-5
    assert abs(sol.myPow(2.0, -2) - 0.25) < 1e-5
    assert abs(sol.myPow(2.0, 0) - 1.0) < 1e-5
    print("PASS: 6. Pow(x, n)")


def test_multiply_strings():
    sol = SolutionMultiplyStrings()
    assert sol.multiply("2", "3") == "6"
    assert sol.multiply("123", "456") == "56088"
    assert sol.multiply("0", "52") == "0"
    assert sol.multiply("999", "999") == "998001"
    print("PASS: 7. Multiply Strings")


def test_detect_squares():
    ds = DetectSquares()
    ds.add([3, 10])
    ds.add([11, 2])
    ds.add([3, 2])
    assert ds.count([11, 10]) == 1
    assert ds.count([14, 8]) == 0
    ds.add([11, 2])  # Duplicate point
    assert ds.count([11, 10]) == 2
    print("PASS: 8. Detect Squares")


if __name__ == "__main__":
    print("\n================ RUNNING MATH & GEOMETRY VERIFICATION ================\n")
    test_rotate_image()
    test_spiral_matrix()
    test_set_matrix_zeroes()
    test_happy_number()
    test_plus_one()
    test_pow()
    test_multiply_strings()
    test_detect_squares()
    print("\n================ ALL 8 TESTS PASSED! (100% VERIFIED) ================\n")
