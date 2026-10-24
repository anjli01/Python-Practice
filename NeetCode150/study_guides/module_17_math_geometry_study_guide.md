# Module 6.2: Math & Geometry – Study Guide & Pattern Deep-Dive

Math and Geometry problems test **in-place spatial manipulation, number-theoretic cycles, binary divide-and-conquer, and Cartesian hash coordinate lookups**.

---

## 1. Rotate Image (LeetCode 48) - Medium
* **Pattern**: Transpose and Horizontal Reflection
* **Core Concept**:
  A $90^\circ$ clockwise rotation is algebraically equivalent to:
  1. Transpose the matrix across the primary diagonal (`matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]`).
  2. Reverse each row (`row.reverse()`).
* **Complexity**: Time: $O(N^2)$, Space: $O(1)$.

---

## 2. Spiral Matrix (LeetCode 54) - Medium
* **Pattern**: Four-Boundary Converging Squeeze
* **Core Concept**:
  Maintain `top, bottom, left, right` boundaries. Traverse top row left-to-right, right col top-to-bottom, bottom row right-to-left, left col bottom-to-top. Squeeze boundaries after each pass.
* **Complexity**: Time: $O(M \cdot N)$, Space: $O(1)$ auxiliary.

---

## 3. Set Matrix Zeroes (LeetCode 73) - Medium
* **Pattern**: In-Place Row/Column State Flags
* **Core Concept**:
  Use the first row and first column as the in-place zero-indicator flags. Maintain a single boolean `row_zero` for row 0 itself to prevent conflict with col 0.
* **Complexity**: Time: $O(M \cdot N)$, Space: $O(1)$ extra space.

---

## 4. Happy Number (LeetCode 202) - Easy
* **Pattern**: Cycle Detection in Sum of Squares
* **Core Concept**:
  Repeatedly sum squared digits. If the sequence does not reach 1, it enters a cycle (either Floyd's Tortoise and Hare or a Hash Set detects this in $O(1)$ time).
* **Complexity**: Time: $O(\log n)$, Space: $O(1)$.

---

## 5. Plus One (LeetCode 66) - Easy
* **Pattern**: Backward Carry Propagation
* **Core Concept**:
  Traverse backwards. If `digit < 9`, increment and return immediately. If `digit == 9`, set to 0. If loop completes, prepend `[1]`.
* **Complexity**: Time: $O(n)$, Space: $O(1)$ in-place.

---

## 6. Pow(x, n) (LeetCode 50) - Medium
* **Pattern**: Fast Exponentiation by Squaring
* **Core Concept**:
  $x^n = (x^{n/2})^2$ for even $n$, and $x \cdot (x^{n/2})^2$ for odd $n$. Halves the exponent each step.
* **Complexity**: Time: $O(\log n)$, Space: $O(\log n)$ recursive stack or $O(1)$ iterative.

---

## 7. Multiply Strings (LeetCode 43) - Medium
* **Pattern**: Grade-School Column Multiplier
* **Core Concept**:
  Digits at index $i$ in `num1` and $j$ in `num2` contribute to positions $i + j$ and $i + j + 1$ in the output array of size $|num_1| + |num_2|$.
* **Complexity**: Time: $O(M \cdot N)$, Space: $O(M + N)$.

---

## 8. Detect Squares (LeetCode 2013) - Medium
* **Pattern**: Diagonal Anchor Multiplier
* **Core Concept**:
  To count squares formed with query point $(px, py)$, iterate through all stored points $(qx, qy)$. If $|px - qx| == |py - qy| > 0$, they form a square diagonal! The count of squares is $count[(px, qy)] \times count[(qx, py)]$.
* **Complexity**: `add`: $O(1)$, `count`: $O(N)$ where $N$ is number of stored points.
