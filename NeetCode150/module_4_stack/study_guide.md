# Module 1.4: Stack – Study Guide & Pattern Deep-Dive

The Stack data structure enforces a **Last-In, First-Out (LIFO)** invariant. It is the premier tool for parsing hierarchical/nested structures (parentheses, syntax trees) and managing **Monotonic Sequences** (next greater/smaller element queries).

---

## 1. Valid Parentheses (LeetCode 20) - Easy
* **Pattern**: LIFO Matching with Closing-to-Opening Map
* **Core Concept**:
  Every opening bracket must be closed by the same type in reverse order of appearance.
* **Mental Model**:
  A stack of plates. Put an opening bracket on the stack. When a closing bracket comes along, check if the plate on top of the stack matches. If not, the stack is corrupted.
* **Tips & Interview Tricks**:
  * **Map Closing to Opening**: Map keys should be the *closing* brackets (`close_to_open = {')': '(', ']': '[', '}': '{'}`). This makes checks `if char in close_to_open` direct and clean.
* **Complexity**:
  * Time: $O(n)$
  * Space: $O(n)$

---

## 2. Min Stack (LeetCode 155) - Medium
* **Pattern**: Stack of Pairs / Parallel Min-Tracking
* **Core Concept**:
  Achieve $O(1)$ time for `push`, `pop`, `top`, and `getMin`.
* **Mental Model**:
  Attach a "tag" to each element pushed onto the stack that records the minimum value of the entire stack up to that level: `(val, min_so_far)`.
* **Tips & Interview Tricks**:
  * **Why not a simple variable `min_val`?** If the minimum element is popped, a single variable cannot tell you what the previous minimum was without an $O(n)$ scan. The pair approach stores the historical minimum at every altitude of the stack!
* **Complexity**:
  * Time: $O(1)$ for all operations
  * Space: $O(n)$

---

## 3. Evaluate Reverse Polish Notation (LeetCode 150) - Medium
* **Pattern**: Postfix Stack Evaluation
* **Core Concept**:
  In postfix notation, operators follow their operands. Push numbers onto the stack. When an operator arrives, pop the two most recent numbers, apply the operator, and push the result back.
* **Mental Model**:
  A calculator stack.
* **Tips & Interview Tricks**:
  * **Operand Order**: `b = stack.pop()`, `a = stack.pop()`. Note that `a` was pushed first, so the expression is `a - b` or `a / b` (NOT `b - a` or `b / a`).
  * **Python Integer Division Trap**: In Python, `-6 // 132 = -1` (flooring toward $-\infty$), but LeetCode demands truncation toward zero (`0`). Always use `int(a / b)`.
* **Complexity**:
  * Time: $O(n)$
  * Space: $O(n)$

---

## 4. Generate Parentheses (LeetCode 22) - Medium
* **Pattern**: Backtracking with Catalan Invariants
* **Core Concept**:
  Generate all valid combinations of $n$ pairs of parentheses.
  * Invariant 1: Can add `'('` if `open_count < n`.
  * Invariant 2: Can add `')'` if `close_count < open_count`.
* **Mental Model**:
  A decision tree. At each node, decide whether to open a bracket or close a bracket based strictly on whether doing so violates balance.
* **Tips & Interview Tricks**:
  * **Catalan Number**: The total number of valid strings is given by the $n$-th Catalan number $C_n = \frac{1}{n+1} \binom{2n}{n} \approx O(\frac{4^n}{n\sqrt{n}})$.
* **Complexity**:
  * Time: $O(\frac{4^n}{\sqrt{n}})$
  * Space: $O(n)$ recursion stack

---

## 5. Daily Temperatures (LeetCode 739) - Medium
* **Pattern**: Monotonic Decreasing Stack (Next Greater Element)
* **Core Concept**:
  Find how many days you must wait for a warmer temperature.
* **Mental Model**:
  Maintain a stack of days waiting for a warmer temperature. As long as temperatures keep dropping, stack them up. The moment a warm day arrives, it resolves the wait time for all colder days below it!
* **Tips & Interview Tricks**:
  * **Store `(temp, index)`**: You need the index to compute the distance `current_day - prev_day`.
* **Complexity**:
  * Time: $O(n)$ (each day pushed and popped at most once)
  * Space: $O(n)$

---

## 6. Car Fleet (LeetCode 853) - Medium
* **Pattern**: Position-Sorted Time-to-Target Stack
* **Core Concept**:
  Cars that catch up to a slower car ahead cannot pass and merge into that fleet.
* **Mental Model**:
  Sort cars by starting position descending (the car closest to the finish line first). Compute each car's unobstructed time to the finish: $\frac{\text{target} - \text{position}}{\text{speed}}$.
  If a car behind arrives in $\le$ time than the car ahead, it merges into the fleet ahead.
* **Tips & Interview Tricks**:
  * **Sort Direction**: Always sort by position DESCENDING. The leader dictates the maximum speed for everyone behind them.
* **Complexity**:
  * Time: $O(n \log n)$ (sorting)
  * Space: $O(n)$

---

## 7. Largest Rectangle in Histogram (LeetCode 84) - Hard
* **Pattern**: Monotonic Increasing Stack with Back-Extended Indices
* **Core Concept**:
  For each bar of height $h$, find the largest rectangle where $h$ is the bottleneck height.
* **Mental Model**:
  Maintain a stack of bars increasing in height: `(start_index, height)`.
  When a shorter bar arrives, the taller bars on the stack cannot extend any further to the right. Pop them, compute their maximum area, and extend the current shorter bar backwards to the popped bar's starting position!
* **Tips & Interview Tricks**:
  * **The "Back-Extension" Trick**: When popping taller bar $(start_t, h_t)$, the current shorter bar $h_{curr}$ can stretch all the way back to $start_t$. So set `start = start_t` before pushing $h_{curr}$.
  * **End of Array Flush**: After the loop finishes, bars remaining on the stack can stretch all the way to the end of the histogram (`len(heights)`).
* **Complexity**:
  * Time: $O(n)$ (each bar is pushed once, popped once)
  * Space: $O(n)$
