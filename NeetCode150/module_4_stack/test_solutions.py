"""
NeetCode 150 - Module 1.4: Verification & Test Suite
Unit tests with comprehensive edge cases for all 7 Stack solutions.
"""

from solutions import (
    SolutionValidParentheses,
    MinStack,
    SolutionEvaluateReversePolishNotation,
    SolutionGenerateParentheses,
    SolutionDailyTemperatures,
    SolutionCarFleet,
    SolutionLargestRectangleInHistogram,
)


def test_valid_parentheses():
    sol = SolutionValidParentheses()
    # Standard cases
    assert sol.isValid("()") is True
    assert sol.isValid("()[]{}") is True
    assert sol.isValid("(]") is False
    assert sol.isValid("([)]") is False
    assert sol.isValid("{[]}") is True
    # Edge cases
    assert sol.isValid("") is True
    assert sol.isValid("(") is False
    assert sol.isValid("]") is False
    print("PASS: 1. Valid Parentheses")


def test_min_stack():
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    assert min_stack.getMin() == -3
    min_stack.pop()
    assert min_stack.top() == 0
    assert min_stack.getMin() == -2
    # Edge cases with duplicate mins
    min_stack.push(-2)
    assert min_stack.getMin() == -2
    min_stack.pop()
    assert min_stack.getMin() == -2
    print("PASS: 2. Min Stack")


def test_evaluate_reverse_polish_notation():
    sol = SolutionEvaluateReversePolishNotation()
    # Standard cases
    assert sol.evalRPN(["2", "1", "+", "3", "*"]) == 9
    assert sol.evalRPN(["4", "13", "5", "/", "+"]) == 6
    # Negative division truncation toward zero: 6 / -132 = 0
    assert sol.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22
    # Single element
    assert sol.evalRPN(["42"]) == 42
    print("PASS: 3. Evaluate Reverse Polish Notation")


def test_generate_parentheses():
    sol = SolutionGenerateParentheses()
    # Standard cases
    res3 = sol.generateParenthesis(3)
    expected3 = ["((()))", "(()())", "(())()", "()(())", "()()()"]
    assert sorted(res3) == sorted(expected3)
    assert sol.generateParenthesis(1) == ["()"]
    # n = 2
    assert sorted(sol.generateParenthesis(2)) == sorted(["(())", "()()"])
    print("PASS: 4. Generate Parentheses")


def test_daily_temperatures():
    sol = SolutionDailyTemperatures()
    # Standard cases
    assert sol.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
    assert sol.dailyTemperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
    # Edge cases: strictly descending, flat, single day
    assert sol.dailyTemperatures([30, 60, 90]) == [1, 1, 0]
    assert sol.dailyTemperatures([80, 70, 60, 50]) == [0, 0, 0, 0]
    assert sol.dailyTemperatures([50, 50, 50]) == [0, 0, 0]
    assert sol.dailyTemperatures([70]) == [0]
    print("PASS: 5. Daily Temperatures")


def test_car_fleet():
    sol = SolutionCarFleet()
    # Standard cases
    assert sol.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]) == 3
    assert sol.carFleet(10, [3], [3]) == 1
    assert sol.carFleet(100, [0, 2, 4], [4, 2, 1]) == 1
    # Edge cases: cars already at same speed, separated fleets
    assert sol.carFleet(10, [6, 8], [3, 2]) == 2
    assert sol.carFleet(10, [0, 4, 2], [2, 1, 3]) == 1
    print("PASS: 6. Car Fleet")


def test_largest_rectangle_in_histogram():
    sol = SolutionLargestRectangleInHistogram()
    # Standard cases
    assert sol.largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10
    assert sol.largestRectangleArea([2, 4]) == 4
    # Edge cases: single bar, flat bars, strictly increasing, strictly decreasing
    assert sol.largestRectangleArea([1]) == 1
    assert sol.largestRectangleArea([2, 2, 2, 2]) == 8
    assert sol.largestRectangleArea([1, 2, 3, 4, 5]) == 9
    assert sol.largestRectangleArea([5, 4, 3, 2, 1]) == 9
    print("PASS: 7. Largest Rectangle in Histogram")


if __name__ == "__main__":
    print("\n================ RUNNING STACK VERIFICATION ================\n")
    test_valid_parentheses()
    test_min_stack()
    test_evaluate_reverse_polish_notation()
    test_generate_parentheses()
    test_daily_temperatures()
    test_car_fleet()
    test_largest_rectangle_in_histogram()
    print("\n================ ALL 7 TESTS PASSED! (100% VERIFIED) ================\n")
