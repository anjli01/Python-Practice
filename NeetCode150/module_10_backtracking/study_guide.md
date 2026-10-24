# Module 4.1: Backtracking – Study Guide & Pattern Deep-Dive

Backtracking is **exhaustive state-space exploration with systematic pruning**. At every node in the recursion tree, you make a choice, recurse down to explore consequences, and undo the choice (**backtrack**) to restore the state before exploring alternative paths.

---

## 1. Subsets (LeetCode 78) - Medium
* **Pattern**: Pick / Don't-Pick Binary Decision Tree
* **Core Concept**:
  For each element, branch into two decisions: include `nums[i]` or exclude `nums[i]`. Total leaves = $2^n$.
* **Complexity**: Time: $O(n \cdot 2^n)$, Space: $O(n)$ recursion depth.

---

## 2. Combination Sum (LeetCode 39) - Medium
* **Pattern**: Unbounded Choice Backtracking
* **Core Concept**:
  At index $i$, branch 1 includes `candidates[i]` and recurses on $i$ again (allowing reuse). Branch 2 skips `candidates[i]` and moves to $i + 1$.
* **Complexity**: Time: $O(2^{\text{target}/\min})$, Space: $O(\text{target}/\min)$.

---

## 3. Permutations (LeetCode 46) - Medium
* **Pattern**: Remaining Element Permutation Tree
* **Core Concept**:
  Choose an unused number for the current position, recurse on the remaining $n - 1$ elements, and backtrack.
* **Complexity**: Time: $O(n \cdot n!)$, Space: $O(n)$.

---

## 4. Subsets II (LeetCode 90) - Medium
* **Pattern**: Sort + Duplicate-Skipping Branch
* **Core Concept**:
  Sort the array first. When skipping an element, skip ALL identical consecutive duplicates:
  `while i + 1 < len(nums) and nums[i] == nums[i+1]: i += 1`.
* **Complexity**: Time: $O(n \cdot 2^n)$, Space: $O(n)$.

---

## 5. Combination Sum II (LeetCode 40) - Medium
* **Pattern**: Loop-Level Deduplication
* **Core Concept**:
  Sort the array. Inside the candidate loop:
  `if i > start_idx and candidates[i] == candidates[i-1]: continue`
  This ensures the same value is never chosen as a sibling branch at the same tree depth.
* **Complexity**: Time: $O(2^n)$, Space: $O(n)$.

---

## 6. Word Search (LeetCode 79) - Medium
* **Pattern**: 2D Grid DFS with In-Place Visited Masking
* **Core Concept**:
  Explore all 4 directions. Mark `board[r][c] = '#'` before recursing, and restore `board[r][c] = original_char` immediately after.
* **Complexity**: Time: $O(M \cdot N \cdot 3^L)$ where $L$ is word length, Space: $O(L)$.

---

## 7. Palindrome Partitioning (LeetCode 131) - Medium
* **Pattern**: Prefix Palindrome Split
* **Core Concept**:
  Iterate partition cut index from `start` to `end`. If substring `s[start:end+1]` is a palindrome, recurse on remaining substring `end + 1`.
* **Complexity**: Time: $O(n \cdot 2^n)$, Space: $O(n)$.

---

## 8. Letter Combinations of a Phone Number (LeetCode 17) - Medium
* **Pattern**: Cartesian Product Tree
* **Core Concept**:
  Map digit to letter choices. At index `idx`, loop over all letters assigned to `digits[idx]` and recurse on `idx + 1`.
* **Complexity**: Time: $O(4^n)$, Space: $O(n)$.

---

## 9. N-Queens (LeetCode 51) - Hard
* **Pattern**: Diagonal Hash Sets
* **Core Concept**:
  Place one queen per row. To detect conflicts in $O(1)$:
  * Column collision: `c in cols`
  * Positive diagonal ($/$): `(r + c) in pos_diags`
  * Negative diagonal ($\backslash$): `(r - c) in neg_diags`
* **Complexity**: Time: $O(N!)$, Space: $O(N)$.
