# Module 1.2: Two Pointers – Study Guide & Pattern Deep-Dive

Two Pointers is one of the most fundamental algorithmic paradigms. It leverages **array ordering and geometric properties** to systematically eliminate entire regions of the search space, achieving $O(n)$ time while maintaining $O(1)$ auxiliary space.

---

## 1. Valid Palindrome (LeetCode 125) - Easy
* **Pattern**: Inward-Converging Pointers / In-Place Filtering
* **Core Concept**:
  A palindrome reads identically forwards and backwards. Two pointers placed at opposing ends converge toward the center, verifying symmetry.
* **Mental Model**:
  Two fingers sliding inward towards the center. Ignore non-letters/non-digits on the fly, comparing letters case-insensitively.
* **Tips & Interview Tricks**:
  * **$O(1)$ Space Invariant**: Do not do `s = "".join([c.lower() for c in s if c.isalnum()]); return s == s[::-1]`. While a 1-liner, it allocates extra memory ($O(n)$ space). In interviews, writing the two-pointer loop with `isalnum()` in-place demonstrates true memory consciousness.
  * **Nested While Pointer Guard**: When skipping invalid characters inside the main loop, always include the boundary check `while left < right and not s[left].isalnum(): left += 1` to prevent index out of bounds.
* **Complexity**:
  * Time: $O(n)$
  * Space: $O(1)$

---

## 2. Two Sum II - Input Array Is Sorted (LeetCode 167) - Medium
* **Pattern**: Monotonic Squeeze via Sorted Property
* **Core Concept**:
  In a sorted array, the sum of values at opposite ends exhibits a strictly monotonic behavior:
  * Decreasing the right pointer decreases the sum.
  * Increasing the left pointer increases the sum.
* **Mental Model**:
  Think of a thermostat. If the current temperature (`nums[l] + nums[r]`) is too high, turn the dial down by moving `r` left. If it is too cold, turn it up by moving `l` right.
* **Tips & Interview Tricks**:
  * **1-Based Indexing**: The problem explicitly requires returning 1-based indices (`[left + 1, right + 1]`).
  * **Compare with LC 1**: Emphasize to the interviewer: *"Because the array is sorted, we can avoid the $O(n)$ hash map from Two Sum I and solve this in optimal $O(1)$ extra space."*
* **Complexity**:
  * Time: $O(n)$
  * Space: $O(1)$

---

## 3. 3Sum (LeetCode 15) - Medium
* **Pattern**: Sort + Fixed Anchor + Two-Pointer Squeeze (with Deduplication)
* **Core Concept**:
  Transform a 3-variable problem ($a + b + c = 0$) into the 2-variable Two Sum II problem: for each fixed $a$, find $b + c = -a$.
* **Mental Model**:
  Pin down the first element `nums[i]` as the anchor. Use two pointers on the remaining subarray `nums[i+1:]` to find pairs that sum to `-nums[i]`.
* **Tips & Interview Tricks**:
  * **Deduplication Strategy**:
    * **Anchor Deduplication**: `if i > 0 and nums[i] == nums[i-1]: continue`
    * **Inner Pointer Deduplication**: When a match is found, after recording the triplet, advance pointers and skip adjacent duplicates:
      `while left < right and nums[left] == nums[left-1]: left += 1`
  * **Early Termination**: Since the array is sorted, if `nums[i] > 0`, break immediately because no three positive numbers can sum to zero.
* **Complexity**:
  * Time: $O(n^2)$ ($O(n \log n)$ sort $+ n \times O(n)$ two-pointer scans)
  * Space: $O(1)$ auxiliary (ignoring sort implementation stack)

---

## 4. Container With Most Water (LeetCode 11) - Medium
* **Pattern**: Greedy Two Pointers (Bottleneck Elimination)
* **Core Concept**:
  $\text{Area} = (\text{right} - \text{left}) \times \min(\text{height}[\text{left}], \text{height}[\text{right}])$.
  The water height is strictly constrained by the **shorter line**.
* **Mental Model**:
  Start at maximum possible width (`left = 0`, `right = n - 1`). To find a larger area with a smaller width, the only hope is finding a significantly taller line. Moving the taller line inward is guaranteed to be useless because the width shrinks and the bottleneck (the shorter line) remains. Therefore, always advance the shorter line.
* **Tips & Interview Tricks**:
  * **Mathematical Proof**: Interviewers often ask *"Why can we safely discard the shorter line?"* Answer: Any container using that shorter line paired with any other inner line will have both smaller width AND a height $\le$ the shorter line, so its area will strictly be smaller.
* **Complexity**:
  * Time: $O(n)$
  * Space: $O(1)$

---

## 5. Trapping Rain Water (LeetCode 42) - Hard
* **Pattern**: Two Pointers with Independent Bounding Maxima
* **Core Concept**:
  Water trapped directly above bar $i$ is:
  $$\text{water}[i] = \max(0, \min(\text{left\_max}, \text{right\_max}) - \text{height}[i])$$
* **Mental Model**:
  Instead of precomputing prefix and suffix max arrays (which takes $O(n)$ space), track `left_max` and `right_max` dynamically with two pointers converging inward.
  * If `left_max < right_max`: We know the water above `left` is strictly capped by `left_max`, regardless of any taller mountains between `left` and `right`. Process `left` and move rightward.
  * If `right_max <= left_max`: Water above `right` is strictly capped by `right_max`. Process `right` and move leftward.
* **Tips & Interview Tricks**:
  * **Space Optimization**: Explain both the 3-pass $O(n)$ space approach (prefix max array + suffix max array) and the 1-pass $O(1)$ space Two Pointer approach to showcase your progression of thought.
* **Complexity**:
  * Time: $O(n)$
  * Space: $O(1)$
