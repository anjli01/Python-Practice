# Module 2.1: Binary Search – Study Guide & Pattern Deep-Dive

Binary Search is the ultimate tool for achieving **logarithmic $O(\log n)$ runtime**. It is not limited to searching sorted arrays; it applies to any monotonic predicate function where a search space can be divided into viable and non-viable partitions.

---

## 1. Binary Search (LeetCode 704) - Easy
* **Pattern**: Standard Interval Halving
* **Core Concept**:
  If the target is smaller than the midpoint, search left (`right = mid - 1`). If larger, search right (`left = mid + 1`).
* **Mental Model**:
  Opening a dictionary at the midpoint and discarding the half that cannot contain your word.
* **Tips & Interview Tricks**:
  * **Midpoint Overflow**: In languages like C++/Java, `(left + right) // 2` can trigger 32-bit signed integer overflow. Always write `mid = left + (right - left) // 2` to demonstrate senior-level engineering hygiene.
* **Complexity**:
  * Time: $O(\log n)$
  * Space: $O(1)$

---

## 2. Search a 2D Matrix (LeetCode 74) - Medium
* **Pattern**: Virtual 1D Array Coordinate Mapping
* **Core Concept**:
  Since each row is sorted and the first integer of each row is greater than the last integer of the previous row, the entire $m \times n$ matrix is equivalent to a single continuous 1D sorted array of length $m \cdot n$.
* **Mental Model**:
  Flatten the matrix conceptually. Binary search an imaginary array of indices from $0$ to $m \cdot n - 1$, mapping back to 2D on demand.
* **Tips & Interview Tricks**:
  * **Coordinate Transformation**:
    $$\text{row} = \text{mid} // n, \quad \text{col} = \text{mid} \% n$$
  * **Two-Step Binary Search vs. Flattened**: You can also binary search the rows first ($O(\log m)$) then binary search the column ($O(\log n)$). Both yield identical $O(\log(m \cdot n))$ runtime, but the virtual 1D approach is cleaner and requires one loop.
* **Complexity**:
  * Time: $O(\log(m \cdot n))$
  * Space: $O(1)$

---

## 3. Koko Eating Bananas (LeetCode 875) - Medium
* **Pattern**: Binary Search on the Answer Space (Monotonic Predicate)
* **Core Concept**:
  When asked to find the *minimum* or *maximum* value satisfying a condition, and checking a candidate value takes polynomial time, binary search over the range of answers.
* **Mental Model**:
  * Range of speeds: $[1, \max(\text{piles})]$.
  * If Koko can finish at speed $k$, she can certainly finish at any speed $> k$. Search left for a slower speed.
  * If she runs out of time at speed $k$, she must speed up. Search right.
* **Tips & Interview Tricks**:
  * **Integer Ceiling**: $\lceil \frac{\text{pile}}{k} \rceil = \frac{\text{pile} + k - 1}{k}$ or `math.ceil(pile / k)`.
* **Complexity**:
  * Time: $O(n \cdot \log(\max(\text{piles})))$
  * Space: $O(1)$

---

## 4. Find Minimum in Rotated Sorted Array (LeetCode 153) - Medium
* **Pattern**: Inflection / Pivot Detection
* **Core Concept**:
  Compare `nums[mid]` against `nums[right]`:
  * If `nums[mid] > nums[right]`: The array wrapped around; the minimum lies strictly to the right of `mid` (`left = mid + 1`).
  * If `nums[mid] <= nums[right]`: The right half is in sorted order; the minimum is at `mid` or to the left (`right = mid`).
* **Mental Model**:
  Two rising slopes separated by a cliff. You want to locate the base of the cliff.
* **Tips & Interview Tricks**:
  * **Loop Condition**: Use `while left < right` (not `<=`). When `left == right`, the search has converged to the exact minimum.
* **Complexity**:
  * Time: $O(\log n)$
  * Space: $O(1)$

---

## 5. Search in Rotated Sorted Array (LeetCode 33) - Medium
* **Pattern**: Halved Sorted-Subarray Invariant
* **Core Concept**:
  In any rotated sorted array, splitting at `mid` always leaves **at least one half strictly sorted**.
* **Mental Model**:
  Determine which half is sorted. Then ask: *"Does the target fall within the clean sorted range?"* If yes, search that half. If no, search the other half.
* **Tips & Interview Tricks**:
  * **Left Half Sorted Check**: `nums[left] <= nums[mid]`.
    * If `nums[left] <= target < nums[mid]`: `right = mid - 1`
    * Else: `left = mid + 1`
  * **Right Half Sorted Check**:
    * If `nums[mid] < target <= nums[right]`: `left = mid + 1`
    * Else: `right = mid - 1`
* **Complexity**:
  * Time: $O(\log n)$
  * Space: $O(1)$

---

## 6. Time Based Key-Value Store (LeetCode 981) - Medium
* **Pattern**: Hash Map of Sorted Arrays with Timestamp Search
* **Core Concept**:
  Since timestamps are inserted in strictly increasing order, the list of `(timestamp, value)` tuples for any key is already sorted.
* **Mental Model**:
  A filing cabinet where each folder contains timestamped snapshots in chronological order. Binary search finds the snapshot closest to, but not exceeding, the target timestamp.
* **Tips & Interview Tricks**:
  * **Rightmost Condition**: When `values[mid][0] <= timestamp`, record `res = values[mid][1]` and push `left = mid + 1` to check if an even closer snapshot exists later in time.
* **Complexity**:
  * `set`: $O(1)$
  * `get`: $O(\log n)$
  * Space: $O(n)$

---

## 7. Median of Two Sorted Arrays (LeetCode 4) - Hard
* **Pattern**: Binary Search on Partition of Smaller Array
* **Core Concept**:
  Find a partition of array $A$ and array $B$ such that:
  1. The left half has $(|A| + |B| + 1) // 2$ elements.
  2. $\max(A_{\text{left}}, B_{\text{left}}) \le \min(A_{\text{right}}, B_{\text{right}})$.
* **Mental Model**:
  Two conveyor belts feeding into one. Adjust the divider on the smaller belt; the position of the divider on the larger belt is automatically determined.
* **Tips & Interview Tricks**:
  * **Always Binary Search on the Smaller Array**: Swap $A$ and $B$ so that $|A| \le |B|$. This ensures $O(\log(\min(m, n)))$ runtime and guarantees that the corresponding cut index in $B$ is always valid ($0 \le j \le |B|$).
  * **Infinity Guards**: Use `float('-inf')` when a partition takes zero elements from an array, and `float('inf')` when it takes all elements.
* **Complexity**:
  * Time: $O(\log(\min(m, n)))$
  * Space: $O(1)$
