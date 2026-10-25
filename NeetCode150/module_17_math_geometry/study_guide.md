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
  This decomposition avoids complex index math and operates entirely in-place.
* **Mental Model**:
  Flip the matrix diagonally (like folding along the top-left to bottom-right crease), then flip it horizontally (like looking at it in a mirror). Two simple flips = one rotation.
* **Tips & Interview Tricks**:
  * **Rotation Cheat Sheet**: $90^\circ$ CW = Transpose + Reverse rows. $90^\circ$ CCW = Transpose + Reverse columns. $180^\circ$ = Reverse rows + Reverse columns. Knowing this family impresses interviewers.
  * **Transpose Loop Bounds**: Only iterate over the upper triangle (`for i in range(n): for j in range(i+1, n)`) to avoid double-swapping.
* **Complexity**:
  * Time: $O(N^2)$
  * Space: $O(1)$

---

## 2. Spiral Matrix (LeetCode 54) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/spiral-matrix/) • [NeetCode Problem](https://neetcode.io/problems/spiral-matrix) • [NeetCode Solution](https://neetcode.io/solutions/spiral-matrix) • [YouTube Video](https://www.youtube.com/watch?v=BJnMZNwUk1M)
* **Pattern**: Four-Boundary Converging Squeeze
* **Core Concept**:
  Maintain `top, bottom, left, right` boundaries. Traverse: top row left-to-right, right column top-to-bottom, bottom row right-to-left, left column bottom-to-top. After each traversal, squeeze the corresponding boundary inward. Stop when boundaries cross.
* **Mental Model**:
  Peeling an onion layer by layer. Each layer is a rectangular ring. Traverse the ring in four directional sweeps, then peel inward to the next ring.
* **Tips & Interview Tricks**:
  * **Boundary Crossing Check**: After traversing the top row and right column, check `if top > bottom or left > right: break` before traversing the bottom row and left column. Without this, non-square matrices produce duplicate entries.
  * **Non-Square Matrices**: Rectangular matrices ($m \ne n$) are the primary source of bugs. Test with $1 \times 4$, $4 \times 1$, and $2 \times 3$ matrices.
* **Complexity**:
  * Time: $O(M \cdot N)$
  * Space: $O(1)$ auxiliary

---

## 3. Set Matrix Zeroes (LeetCode 73) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/set-matrix-zeroes/) • [NeetCode Problem](https://neetcode.io/problems/set-zeroes-in-matrix) • [NeetCode Solution](https://neetcode.io/solutions/set-matrix-zeroes) • [YouTube Video](https://www.youtube.com/watch?v=T41rL0L3Pnw)
* **Pattern**: In-Place Row/Column State Flags
* **Core Concept**:
  Use the first row and first column as the in-place zero-indicator flags. When `matrix[i][j] == 0`, set `matrix[i][0] = 0` and `matrix[0][j] = 0`. Maintain a single boolean `row_zero` for row 0 itself to prevent conflict with column 0's flag.
* **Mental Model**:
  A spreadsheet where you need to highlight entire rows and columns. Instead of using sticky notes (extra memory), use the header row and header column as the highlight markers. Process the interior cells first, then apply the headers.
* **Tips & Interview Tricks**:
  * **Processing Order**: Mark flags first (scan all cells). Then zero out interior cells based on flags. Finally, zero out the first row and first column themselves. Reversing this order corrupts the flags.
  * **Why `row_zero`?**: Cell `matrix[0][0]` serves as the flag for both row 0 and column 0. A separate boolean `row_zero` disambiguates row 0's status.
  * **Three Space Approaches**: $O(m + n)$ with row/col arrays, $O(1)$ with in-place flags (described above), and $O(mn)$ brute force. Know all three and present the optimal one.
* **Complexity**:
  * Time: $O(M \cdot N)$
  * Space: $O(1)$ extra space

---

## 4. Happy Number (LeetCode 202) - Easy
* **Quick Links**: [LeetCode](https://leetcode.com/problems/happy-number/) • [NeetCode Problem](https://neetcode.io/problems/non-cyclical-number) • [NeetCode Solution](https://neetcode.io/solutions/happy-number) • [YouTube Video](https://www.youtube.com/watch?v=ljz85bxOYJ0)
* **Pattern**: Cycle Detection in Sum of Squares
* **Core Concept**:
  Repeatedly sum the squares of digits. If the sequence reaches 1, the number is happy. If it enters a cycle (revisiting a previous sum), it's not happy. Detect cycles using either Floyd's Tortoise and Hare or a Hash Set.
* **Mental Model**:
  A number on a journey through digit-squaring transformations. It either arrives at the "happy destination" (1) or gets trapped running in circles. Floyd's algorithm detects the circular trap in $O(1)$ space.
* **Tips & Interview Tricks**:
  * **Floyd's vs. Hash Set**: Hash Set is $O(n)$ space but simpler to code. Floyd's (slow computes one step, fast computes two steps) is $O(1)$ space. Mention both; use Floyd's if asked for optimal space.
  * **Digit Extraction**: `digit = n % 10; n = n // 10` in a while loop. Or use `sum(int(d)**2 for d in str(n))` for conciseness (but mention the string conversion overhead).
* **Complexity**:
  * Time: $O(\log n)$
  * Space: $O(1)$ with Floyd's

---

## 5. Plus One (LeetCode 66) - Easy
* **Quick Links**: [LeetCode](https://leetcode.com/problems/plus-one/) • [NeetCode Problem](https://neetcode.io/problems/plus-one) • [NeetCode Solution](https://neetcode.io/solutions/plus-one) • [YouTube Video](https://www.youtube.com/watch?v=jIaA8boiG1s)
* **Pattern**: Backward Carry Propagation
* **Core Concept**:
  Traverse the digits array from right to left. If `digit < 9`, increment it and return immediately (no carry). If `digit == 9`, set it to 0 and continue propagating the carry leftward. If the loop completes (all 9s), prepend `[1]` to the array.
* **Mental Model**:
  An odometer rolling over. Each `9` flips to `0` and passes the carry to the next digit. If every digit is `9`, a new digit `1` appears at the front (like 999 → 1000).
* **Tips & Interview Tricks**:
  * **Early Return Optimization**: The moment you find a digit $< 9$, increment it and return. No need to process the remaining digits. This makes the common case (no carry propagation) $O(1)$.
  * **Edge Case**: `[9, 9, 9]` → `[1, 0, 0, 0]`. This is the only case where the array length changes.
* **Complexity**:
  * Time: $O(n)$
  * Space: $O(1)$ in-place (except the all-9s case)

---

## 6. Pow(x, n) (LeetCode 50) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/powx-n/) • [NeetCode Problem](https://neetcode.io/problems/pow-x-n) • [NeetCode Solution](https://neetcode.io/solutions/powx-n) • [YouTube Video](https://www.youtube.com/watch?v=g9YQyYi4IQQ)
* **Pattern**: Fast Exponentiation by Squaring
* **Core Concept**:
  $x^n = (x^{n/2})^2$ for even $n$, and $x \cdot (x^{n/2})^2$ for odd $n$. Halves the exponent each step, achieving $O(\log n)$ multiplications instead of $O(n)$.
* **Mental Model**:
  Instead of multiplying $x$ by itself $n$ times, keep squaring your result. $x^{16} = ((((x^2)^2)^2)^2)$ takes only 4 squarings instead of 15 multiplications.
* **Tips & Interview Tricks**:
  * **Negative Exponent**: If $n < 0$, compute $x^{-n}$ and return $1 / \text{result}$. Handle this upfront: `if n < 0: x = 1/x; n = -n`.
  * **Integer Overflow (Java/C++)**: $n = -2^{31}$ causes overflow when negated. Convert to `long` first. In Python, this isn't an issue due to arbitrary precision integers.
  * **Iterative Version**: Use a loop: while $n > 0$, if $n$ is odd multiply result by $x$, then square $x$ and halve $n$. This avoids recursion stack overhead.
* **Complexity**:
  * Time: $O(\log n)$
  * Space: $O(\log n)$ recursive stack or $O(1)$ iterative

---

## 7. Multiply Strings (LeetCode 43) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/multiply-strings/) • [NeetCode Problem](https://neetcode.io/problems/multiply-strings) • [NeetCode Solution](https://neetcode.io/solutions/multiply-strings) • [YouTube Video](https://www.youtube.com/watch?v=1vZswirL8Y8)
* **Pattern**: Grade-School Column Multiplier
* **Core Concept**:
  Digits at index $i$ in `num1` and $j$ in `num2` contribute to positions $i + j$ and $i + j + 1$ in the output array of size $|num_1| + |num_2|$. Multiply each pair of digits, accumulate products into the result array, then propagate carries.
* **Mental Model**:
  Long multiplication as taught in elementary school. Multiply each digit of the bottom number by each digit of the top number, placing partial products in the correct column positions, then sum the columns with carry propagation.
* **Tips & Interview Tricks**:
  * **Position Formula**: `result[i + j + 1] += digit1 * digit2`. The `+1` offset accounts for the result array being indexed from the most significant digit. After accumulation, propagate carries from right to left.
  * **Leading Zeros**: Strip leading zeros from the result: `result_str.lstrip('0') or '0'`. The `or '0'` handles the edge case where the product is zero.
  * **No Built-In Conversion**: The problem prohibits converting the entire string to an integer. You may convert individual characters via `ord(c) - ord('0')`.
* **Complexity**:
  * Time: $O(M \cdot N)$
  * Space: $O(M + N)$

---

## 8. Detect Squares (LeetCode 2013) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/detect-squares/) • [NeetCode Problem](https://neetcode.io/problems/count-squares) • [NeetCode Solution](https://neetcode.io/solutions/detect-squares) • [YouTube Video](https://www.youtube.com/watch?v=bahebearrDc)
* **Pattern**: Diagonal Anchor Multiplier
* **Core Concept**:
  To count squares formed with query point $(px, py)$, iterate through all stored points $(qx, qy)$ that form a valid diagonal. If $|px - qx| == |py - qy| > 0$, they could be diagonal corners of a square. The count of valid squares is $count[(px, qy)] \times count[(qx, py)]$ — checking if the other two corners exist and multiplying their frequencies.
* **Mental Model**:
  You're given one corner of a potential square. For each candidate diagonal corner, the other two corners are uniquely determined. Check if those corners exist in your point database and multiply their counts.
* **Tips & Interview Tricks**:
  * **Diagonal, Not Adjacent**: Iterate over diagonal candidates, not adjacent corners. The diagonal approach requires checking only one point to determine the remaining two corners, while an adjacent-corner approach requires more complex case analysis.
  * **Counter Storage**: Use `defaultdict(int)` with tuple keys `(x, y)` for $O(1)$ point counting. Also maintain a list of all points for iteration in `count`.
  * **Axis-Aligned Only**: The problem specifies axis-aligned squares. Don't consider rotated squares.
* **Complexity**:
  * `add`: $O(1)$
  * `count`: $O(N)$ where $N$ is number of stored points
  * Space: $O(N)$
