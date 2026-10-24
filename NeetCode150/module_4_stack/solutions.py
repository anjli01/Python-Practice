"""
NeetCode 150 - Module 1.4: Stack
Detailed, fully-commented Python 3 solutions for all 7 problems.
"""

from typing import List


# ============================================================================
# Problem 1: Valid Parentheses (LeetCode 20) - Easy
# Pattern: LIFO Stack with Closing-to-Opening Map
# ============================================================================
class SolutionValidParentheses:
    def isValid(self, s: str) -> bool:
        """
        Determines if the input string has valid matching and ordering of brackets.
        
        Concept / Pattern:
        - LIFO (Last-In-First-Out): The most recently opened bracket must be the
          first one closed.
        - Map each closing bracket to its corresponding opening bracket.
        
        Complexity:
        - Time: O(n) - Single pass through the string.
        - Space: O(n) - Stack can grow up to len(s) in worst case (e.g. "(((((").
        """
        stack = []
        close_to_open = {')': '(', ']': '[', '}': '{'}
        
        for char in s:
            if char in close_to_open:
                # If closing bracket, top of stack must match
                if stack and stack[-1] == close_to_open[char]:
                    stack.pop()
                else:
                    return False
            else:
                # Opening bracket, push to stack
                stack.append(char)
                
        # Valid only if all opened brackets were successfully matched
        return len(stack) == 0


# ============================================================================
# Problem 2: Min Stack (LeetCode 155) - Medium
# Pattern: Stack of Pairs / Parallel Min-Tracking
# ============================================================================
class MinStack:
    """
    Stack that supports push, pop, top, and retrieving the minimum element in O(1) time.
    
    Concept / Pattern:
    - Alongside each pushed value, store the running minimum of the stack up to that element.
    - Storing `(val, current_min)` guarantees that when elements are popped, the previous
      minimum is immediately restored with zero extra lookups.
    """
    def __init__(self):
        # Stores tuples of (val, min_at_this_level)
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            current_min = min(val, self.stack[-1][1])
            self.stack.append((val, current_min))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0] if self.stack else -1

    def getMin(self) -> int:
        return self.stack[-1][1] if self.stack else -1


# ============================================================================
# Problem 3: Evaluate Reverse Polish Notation (LeetCode 150) - Medium
# Pattern: Postfix Operand Stack Evaluation
# ============================================================================
class SolutionEvaluateReversePolishNotation:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Evaluates the value of an arithmetic expression in Reverse Polish Notation.
        
        Concept / Pattern:
        - Numbers are pushed onto the stack.
        - When an operator is encountered, pop the top two operands:
          Caution: Second popped is left operand, first popped is right operand!
          Compute: `left op right`, then push the result back onto the stack.
        - Division must truncate toward zero: in Python, `int(a / b)` truncates toward zero,
          whereas `a // b` floors toward negative infinity.
        
        Complexity:
        - Time: O(n) - Each token is processed once.
        - Space: O(n) - Stack stores operands.
        """
        stack = []
        
        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    # int(a / b) truncates toward zero (e.g. int(-6 / 132) = 0)
                    stack.append(int(a / b))
            else:
                stack.append(int(token))
                
        return stack[0]


# ============================================================================
# Problem 4: Generate Parentheses (LeetCode 22) - Medium
# Pattern: State-Space Exploration with Stack-Constrained Invariants
# ============================================================================
class SolutionGenerateParentheses:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Generates all combinations of well-formed parentheses for n pairs.
        
        Concept / Pattern:
        - Invariants for valid parentheses:
          1. Can add '(' only if `open_count < n`.
          2. Can add ')' only if `close_count < open_count`.
          3. Base case: `open_count == close_count == n`.
        
        Complexity:
        - Time: O(4^n / sqrt(n)) - n-th Catalan number bounds the number of combinations.
        - Space: O(n) - Stack recursion depth.
        """
        result = []
        stack = []
        
        def backtrack(open_c: int, close_c: int):
            if open_c == close_c == n:
                result.append("".join(stack))
                return
                
            if open_c < n:
                stack.append("(")
                backtrack(open_c + 1, close_c)
                stack.pop()
                
            if close_c < open_c:
                stack.append(")")
                backtrack(open_c, close_c + 1)
                stack.pop()
                
        backtrack(0, 0)
        return result


# ============================================================================
# Problem 5: Daily Temperatures (LeetCode 739) - Medium
# Pattern: Monotonic Decreasing Stack (Next Greater Element)
# ============================================================================
class SolutionDailyTemperatures:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Calculates the number of days you have to wait after the i-th day to get a warmer temperature.
        
        Concept / Pattern:
        - Monotonic Decreasing Stack: Stores pairs `(temperature, index)`.
        - When temperature at day i is GREATER than the top of the stack, we found the
          "next warmer day" for that top day!
        - Pop it, calculate wait time `i - prev_index`, and repeat.
        
        Complexity:
        - Time: O(n) - Each day index is pushed and popped at most once.
        - Space: O(n) - Stack stores unresolved days.
        """
        n = len(temperatures)
        answer = [0] * n
        stack = []  # stores pairs of (temp, index)
        
        for current_day, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                prev_temp, prev_day = stack.pop()
                answer[prev_day] = current_day - prev_day
                
            stack.append((temp, current_day))
            
        return answer


# ============================================================================
# Problem 6: Car Fleet (LeetCode 853) - Medium
# Pattern: Position-Sorted Time-to-Destination Stack
# ============================================================================
class SolutionCarFleet:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        Calculates the number of car fleets that will arrive at the destination.
        
        Concept / Pattern:
        - Sort cars by starting position in DESCENDING order (closest to target first).
        - Time to destination for each car: `(target - position) / speed`.
        - Stack of fleet arrival times:
          - If a trailing car takes LESS than or EQUAL time to reach the target than
            the fleet ahead of it, it will catch up and merge into that fleet.
          - Thus, its arrival time is bounded by the slower car ahead, and we don't
            create a new fleet.
        
        Complexity:
        - Time: O(n log n) - Dominated by sorting positions.
        - Space: O(n) - Stores cars and fleet arrival stack.
        """
        # Pair positions with speeds, sorted by position descending
        cars = sorted(zip(position, speed), reverse=True)
        stack = []  # stores arrival times of fleet leaders
        
        for pos, spd in cars:
            time_to_target = (target - pos) / spd
            stack.append(time_to_target)
            
            # If the current car arrives earlier or at the same time as the fleet ahead,
            # it joins that fleet! Pop the current car since it cannot pass the leader.
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
                
        return len(stack)


# ============================================================================
# Problem 7: Largest Rectangle in Histogram (LeetCode 84) - Hard
# Pattern: Monotonic Increasing Stack with Back-Extended Indices
# ============================================================================
class SolutionLargestRectangleInHistogram:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Finds the area of the largest rectangle in the histogram in O(n) time.
        
        Concept / Pattern:
        - Monotonic Increasing Stack: Stores pairs of `(start_index, height)`.
        - When the current bar is SHORTER than the bar on top of the stack:
          - The rectangle with height `stack[-1][1]` CANNOT extend any further right!
          - Pop it and calculate area: `height * (current_index - start_index)`.
          - Key Insight: The shorter current bar CAN extend to the left as far as the
            popped bar's start index! Update the current bar's start index backwards.
        
        Complexity:
        - Time: O(n) - Each bar is pushed and popped at most once.
        - Space: O(n) - Stack holds at most n elements.
        """
        max_area = 0
        stack = []  # (start_index, height)
        
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                prev_start, prev_h = stack.pop()
                # Area bounded by the popped taller bar
                max_area = max(max_area, prev_h * (i - prev_start))
                # Current shorter bar can extend back to where prev taller bar started
                start = prev_start
                
            stack.append((start, h))
            
        # Clear remaining bars that extend all the way to the end of the histogram
        total_len = len(heights)
        for start, h in stack:
            max_area = max(max_area, h * (total_len - start))
            
        return max_area
