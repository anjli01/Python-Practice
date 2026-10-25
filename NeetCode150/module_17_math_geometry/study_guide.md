# Module 6.2: Math & Geometry – Study Guide & Pattern Deep-Dive

Math and Geometry problems test **in-place spatial manipulation, number-theoretic cycles, binary divide-and-conquer, and Cartesian hash coordinate lookups**.

---

## 1. Rotate Image (LeetCode 48) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/rotate-image/) • [NeetCode Problem](https://neetcode.io/problems/rotate-matrix) • [NeetCode Solution](https://neetcode.io/solutions/rotate-image) • [YouTube Video](https://www.youtube.com/watch?v=fMSJSS7eO1w)
* **Pattern**: Transpose and Horizontal Reflection
* **Core Concept**:
  A $90^\circ$ clockwise rotation is algebraically equivalent to:
  1. Transpose the matrix across the primary diagonal (`matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]`).
  2. Reverse each row (`row.reverse()`).
* **Complexity**: Time: $O(N^2)$, Space: $O(1)$.

---

## 2. Spiral Matrix (LeetCode 54) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/spiral-matrix/) • [NeetCode Problem](https://neetcode.io/problems/spiral-matrix) • [NeetCode Solution](https://neetcode.io/solutions/spiral-matrix) • [YouTube Video](https://www.youtube.com/watch?v=BJnMZNwUk1M)
* **Pattern**: Four-Boundary Converging Squeeze
* **Core Concept**:
  Maintain `top, bottom, left, right` boundaries. Traverse top row left-to-right, right col top-to-bottom, bottom row right-to-left, left col bottom-to-top. Squeeze boundaries after each pass.
* **Complexity**: Time: $O(M \cdot N)$, Space: $O(1)$ auxiliary.

---

## 3. Set Matrix Zeroes (LeetCode 73) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/set-matrix-zeroes/) • [NeetCode Problem](https://neetcode.io/problems/set-zeroes-in-matrix) • [NeetCode Solution](https://neetcode.io/solutions/set-matrix-zeroes) • [YouTube Video](https://www.youtube.com/watch?v=T41rL0L3Pnw)
* **Pattern**: In-Place Row/Column State Flags
* **Core Concept**:
  Use the first row and first column as the in-place zero-indicator flags. Maintain a single boolean `row_zero` for row 0 itself to prevent conflict with col 0.
* **Complexity**: Time: $O(M \cdot N)$, Space: $O(1)$ extra space.

---

## 4. Happy Number (LeetCode 202) - Easy
* **Quick Links**: [LeetCode](https://leetcode.com/problems/happy-number/) • [NeetCode Problem](https://neetcode.io/problems/non-cyclical-number) • [NeetCode Solution](https://neetcode.io/solutions/happy-number) • [YouTube Video](https://www.youtube.com/watch?v=ljz85bxOYJ0)
* **Pattern**: Cycle Detection in Sum of Squares
* **Core Concept**:
  Repeatedly sum squared digits. If the sequence does not reach 1, it enters a cycle (either Floyd's Tortoise and Hare or a Hash Set detects this in $O(1)$ time).
* **Complexity**: Time: $O(\log n)$, Space: $O(1)$.

---

## 5. Plus One (LeetCode 66) - Easy
* **Quick Links**: [LeetCode](https://leetcode.com/problems/plus-one/) • [NeetCode Problem](https://neetcode.io/problems/plus-one) • [NeetCode Solution](https://neetcode.io/solutions/plus-one) • [YouTube Video](https://www.youtube.com/watch?v=jIaA8boiG1s)
* **Pattern**: Backward Carry Propagation
* **Core Concept**:
  Traverse backwards. If `digit < 9`, increment and return immediately. If `digit == 9`, set to 0. If loop completes, prepend `[1]`.
* **Complexity**: Time: $O(n)$, Space: $O(1)$ in-place.

---

## 6. Pow(x, n) (LeetCode 50) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/powx-n/) • [NeetCode Problem](https://neetcode.io/problems/pow-x-n) • [NeetCode Solution](https://neetcode.io/solutions/powx-n) • [YouTube Video](https://www.youtube.com/watch?v=g9YQyYi4IQQ)
* **Pattern**: Fast Exponentiation by Squaring
* **Core Concept**:
  $x^n = (x^{n/2})^2$ for even $n$, and $x \cdot (x^{n/2})^2$ for odd $n$. Halves the exponent each step.
* **Complexity**: Time: $O(\log n)$, Space: $O(\log n)$ recursive stack or $O(1)$ iterative.

---

## 7. Multiply Strings (LeetCode 43) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/multiply-strings/) • [NeetCode Problem](https://neetcode.io/problems/multiply-strings) • [NeetCode Solution](https://neetcode.io/solutions/multiply-strings) • [YouTube Video](https://www.youtube.com/watch?v=1vZswirL8Y8)
* **Pattern**: Grade-School Column Multiplier
* **Core Concept**:
  Digits at index $i$ in `num1` and $j$ in `num2` contribute to positions $i + j$ and $i + j + 1$ in the output array of size $|num_1| + |num_2|$.
* **Complexity**: Time: $O(M \cdot N)$, Space: $O(M + N)$.

---

## 8. Detect Squares (LeetCode 2013) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/detect-squares/) • [NeetCode Problem](https://neetcode.io/problems/count-squares) • [NeetCode Solution](https://neetcode.io/solutions/detect-squares) • [YouTube Video](https://www.youtube.com/watch?v=bahebearrDc)
* **Pattern**: Diagonal Anchor Multiplier
* **Core Concept**:
  To count squares formed with query point $(px, py)$, iterate through all stored points $(qx, qy)$. If $|px - qx| == |py - qy| > 0$, they form a square diagonal! The count of squares is $count[(px, qy)] \times count[(qx, py)]$.
* **Complexity**: `add`: $O(1)$, `count`: $O(N)$ where $N$ is number of stored points.
