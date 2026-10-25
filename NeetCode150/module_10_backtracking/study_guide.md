# Module 4.1: Backtracking – Study Guide & Pattern Deep-Dive

Backtracking is **exhaustive state-space exploration with systematic pruning**. At every node in the recursion tree, you make a choice, recurse down to explore consequences, and undo the choice (**backtrack**) to restore the state before exploring alternative paths.

---

## 1. Subsets (LeetCode 78) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/subsets/) • [NeetCode Problem](https://neetcode.io/problems/subsets) • [NeetCode Solution](https://neetcode.io/solutions/subsets) • [YouTube Video](https://www.youtube.com/watch?v=REOH22Xwdkk)
* **Pattern**: Pick / Don't-Pick Binary Decision Tree
* **Core Concept**:
  For each element, branch into two decisions: include `nums[i]` or exclude `nums[i]`. Total leaves = $2^n$. At each leaf, the current subset is one valid answer. Alternatively, use an iterative approach that builds subsets by appending to all existing subsets.
* **Mental Model**:
  A buffet line with $n$ dishes. At each dish, you decide: *take it* or *skip it*. Every possible combination of take/skip decisions produces a unique plate (subset).
* **Tips & Interview Tricks**:
  * **Two Equivalent Approaches**: (1) Binary decision tree: for index $i$, branch into "include" and "exclude". (2) Iterative loop: for each index $i$ from `start` to `n`, include `nums[i]`, recurse on `i+1`, then backtrack. Both generate the same subsets but the loop approach generalizes better to Combination Sum.
  * **Deep Copy**: Always append `subset[:]` (a copy) to the result, not the mutable `subset` list itself.
* **Complexity**:
  * Time: $O(n \cdot 2^n)$
  * Space: $O(n)$ recursion depth

---

## 2. Combination Sum (LeetCode 39) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/combination-sum/) • [NeetCode Problem](https://neetcode.io/problems/combination-target-sum) • [NeetCode Solution](https://neetcode.io/solutions/combination-sum) • [YouTube Video](https://www.youtube.com/watch?v=GBKI9VSKdGg)
* **Pattern**: Unbounded Choice Backtracking
* **Core Concept**:
  At index $i$, branch 1 includes `candidates[i]` and recurses on $i$ again (allowing reuse). Branch 2 skips `candidates[i]` and moves to $i + 1$. The "stay at $i$" branch is what makes this unbounded (a candidate can be chosen unlimited times).
* **Mental Model**:
  A coin machine dispensing exact change. You can use the same coin denomination multiple times. Try stuffing in as many of the current coin as possible, then move to the next denomination.
* **Tips & Interview Tricks**:
  * **Why Not Start From 0 Each Time?**: Starting the loop from `i` (not `0`) avoids generating duplicate combinations like `[2, 3]` and `[3, 2]`. The "only move forward" constraint enforces combination ordering.
  * **Pruning**: Sort candidates first. If `candidates[i] > remaining_target`, break the loop early — no larger candidate can help either.
* **Complexity**:
  * Time: $O(2^{\text{target}/\min})$
  * Space: $O(\text{target}/\min)$

---

## 3. Permutations (LeetCode 46) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/permutations/) • [NeetCode Problem](https://neetcode.io/problems/permutations) • [NeetCode Solution](https://neetcode.io/solutions/permutations) • [YouTube Video](https://www.youtube.com/watch?v=FZe0UqISmUw)
* **Pattern**: Remaining Element Permutation Tree
* **Core Concept**:
  Choose an unused number for the current position, recurse on the remaining $n - 1$ elements, and backtrack. Unlike subsets/combinations, every element must appear exactly once, and order matters.
* **Mental Model**:
  Arranging books on a shelf. For the first slot, choose any of $n$ books. For the second slot, choose from the remaining $n - 1$. Continue until all slots are filled. Undo each placement to try alternative arrangements.
* **Tips & Interview Tricks**:
  * **Subsets vs. Permutations**: Subsets explore "include/exclude" — order doesn't matter. Permutations explore "which element goes in position $k$" — order matters. This distinction drives the recursion structure.
  * **Visited Set vs. Swap**: Two implementation styles: (1) maintain a `used` boolean array or set, (2) swap elements in-place (`nums[i], nums[start] = nums[start], nums[i]`). The swap approach uses $O(1)$ extra space but is harder to reason about.
* **Complexity**:
  * Time: $O(n \cdot n!)$
  * Space: $O(n)$

---

## 4. Subsets II (LeetCode 90) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/subsets-ii/) • [NeetCode Problem](https://neetcode.io/problems/subsets-ii) • [NeetCode Solution](https://neetcode.io/solutions/subsets-ii) • [YouTube Video](https://www.youtube.com/watch?v=Vn2v6ajA7U0)
* **Pattern**: Sort + Duplicate-Skipping Branch
* **Core Concept**:
  Sort the array first. When the "exclude" branch is taken at index $i$, skip ALL identical consecutive elements:
  `while i + 1 < len(nums) and nums[i] == nums[i+1]: i += 1`.
  This ensures that duplicate values are never independently chosen at the same recursion level.
* **Mental Model**:
  Ordering from a menu with duplicate items. If you decide not to order a particular dish, you skip past all identical copies of that dish to avoid redundant orders.
* **Tips & Interview Tricks**:
  * **Sorting is Mandatory**: Without sorting, duplicates aren't adjacent, making skip logic impossible. Always `nums.sort()` first.
  * **Alternative Skip**: In the loop-based approach (vs. binary decision tree), the skip condition is `if i > start and nums[i] == nums[i-1]: continue`. Both approaches are correct; use whichever you're more comfortable with.
* **Complexity**:
  * Time: $O(n \cdot 2^n)$
  * Space: $O(n)$

---

## 5. Combination Sum II (LeetCode 40) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/combination-sum-ii/) • [NeetCode Problem](https://neetcode.io/problems/combination-target-sum-ii) • [NeetCode Solution](https://neetcode.io/solutions/combination-sum-ii) • [YouTube Video](https://www.youtube.com/watch?v=FOyRpNUSFeA)
* **Pattern**: Loop-Level Deduplication
* **Core Concept**:
  Sort the array. Inside the candidate loop:
  `if i > start_idx and candidates[i] == candidates[i-1]: continue`
  This ensures the same value is never chosen as a sibling branch at the same tree depth. Each element can be used at most once (recurse on `i + 1`, not `i`).
* **Mental Model**:
  A casting director choosing actors. Two identical twins audition, but only one can be cast in each role. If twin A was already rejected at this casting round, skip twin B too — they'd produce the same movie.
* **Tips & Interview Tricks**:
  * **Key Difference from Combination Sum I**: Here each element is used at most once (`i + 1`), and duplicates exist in the input. In Combination Sum I, elements can be reused (recurse on `i`), and all candidates are unique.
  * **`i > start_idx` Guard**: The condition `i > start_idx` (not `i > 0`) is critical. It allows the first occurrence at each depth to proceed while skipping subsequent identical siblings.
* **Complexity**:
  * Time: $O(2^n)$
  * Space: $O(n)$

---

## 6. Word Search (LeetCode 79) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/word-search/) • [NeetCode Problem](https://neetcode.io/problems/search-for-word) • [NeetCode Solution](https://neetcode.io/solutions/word-search) • [YouTube Video](https://www.youtube.com/watch?v=pfiQ_PS1g8E)
* **Pattern**: 2D Grid DFS with In-Place Visited Masking
* **Core Concept**:
  Explore all 4 directions from each matching cell. Mark `board[r][c] = '#'` before recursing to prevent revisiting, and restore `board[r][c] = original_char` immediately after backtracking.
* **Mental Model**:
  Tracing a word on a Boggle board with your finger. You can move up/down/left/right, but you can't lift your finger and place it on a cell you've already touched in this word.
* **Tips & Interview Tricks**:
  * **In-Place vs. Visited Set**: Mutating the board (`'#'`) is $O(1)$ space vs. a `visited` set which is $O(L)$. Always use in-place marking in interviews — it's more efficient and demonstrates awareness.
  * **Early Termination**: Check `if board[r][c] != word[idx]: return False` immediately. Don't explore further if the current cell doesn't match.
  * **Optimization**: Count character frequencies in the word and the board. If any character in the word has a higher frequency than in the board, return `False` immediately.
* **Complexity**:
  * Time: $O(M \cdot N \cdot 3^L)$ where $L$ is word length (3 directions after the first step since you can't go back)
  * Space: $O(L)$

---

## 7. Palindrome Partitioning (LeetCode 131) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/palindrome-partitioning/) • [NeetCode Problem](https://neetcode.io/problems/palindrome-partitioning) • [NeetCode Solution](https://neetcode.io/solutions/palindrome-partitioning) • [YouTube Video](https://www.youtube.com/watch?v=3jvWodd7ht0)
* **Pattern**: Prefix Palindrome Split
* **Core Concept**:
  Iterate partition cut index from `start` to `end`. If substring `s[start:end+1]` is a palindrome, add it to the current partition and recurse on the remaining substring starting at `end + 1`. When `start` reaches the end of the string, the current partition is valid.
* **Mental Model**:
  Cutting a ribbon into segments where each segment reads the same forwards and backwards. Try every possible first cut. If the first segment is a palindrome, recursively cut the remainder.
* **Tips & Interview Tricks**:
  * **Palindrome Check Optimization**: Cache palindrome checks using a 2D DP table or `@lru_cache`. The naive `s[i:j] == s[i:j][::-1]` check at every split is $O(n)$ and may cause TLE on large inputs.
  * **Backtracking Template**: `partition.append(s[start:end+1])`, recurse, `partition.pop()`. This is the classic append-recurse-pop backtracking pattern.
* **Complexity**:
  * Time: $O(n \cdot 2^n)$
  * Space: $O(n)$

---

## 8. Letter Combinations of a Phone Number (LeetCode 17) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) • [NeetCode Problem](https://neetcode.io/problems/combinations-of-a-phone-number) • [NeetCode Solution](https://neetcode.io/solutions/letter-combinations-of-a-phone-number) • [YouTube Video](https://www.youtube.com/watch?v=0snEunUacZY)
* **Pattern**: Cartesian Product Tree
* **Core Concept**:
  Map each digit to its letter choices (e.g., `'2' -> 'abc'`). At index `idx`, loop over all letters assigned to `digits[idx]` and recurse on `idx + 1`. When `idx == len(digits)`, the accumulated string is one complete combination.
* **Mental Model**:
  Old-school T9 phone texting. Each key press presents 3–4 letter options. The total combinations are the Cartesian product of all key presses — like a combination lock with variable-width dials.
* **Tips & Interview Tricks**:
  * **Empty Input**: If `digits == ""`, return `[]` (not `[""]`). This is an easy edge case to miss.
  * **String Building**: Use a list and `"".join()` at the leaf, rather than string concatenation at each level, to avoid $O(n^2)$ string copying.
* **Complexity**:
  * Time: $O(4^n)$ where $n$ is the number of digits (4 for digits 7 and 9)
  * Space: $O(n)$

---

## 9. N-Queens (LeetCode 51) - Hard
* **Quick Links**: [LeetCode](https://leetcode.com/problems/n-queens/) • [NeetCode Problem](https://neetcode.io/problems/n-queens) • [NeetCode Solution](https://neetcode.io/solutions/n-queens) • [YouTube Video](https://www.youtube.com/watch?v=Ph95IHmRp5M)
* **Pattern**: Diagonal Hash Sets
* **Core Concept**:
  Place one queen per row. To detect conflicts in $O(1)$:
  * Column collision: `c in cols`
  * Positive diagonal ($/$): `(r + c) in pos_diags`
  * Negative diagonal ($\backslash$): `(r - c) in neg_diags`
  All cells on the same positive diagonal share the same $r + c$ value; all cells on the same negative diagonal share the same $r - c$ value.
* **Mental Model**:
  A chessboard negotiation. Each queen claims a row, a column, and two diagonals. Track the claimed columns and diagonals in sets. If a cell's column or either diagonal is already claimed, that cell is under attack.
* **Tips & Interview Tricks**:
  * **Diagonal Formula**: The key insight is $r + c = \text{const}$ for positive diagonals and $r - c = \text{const}$ for negative diagonals. Deriving this on the whiteboard impresses interviewers.
  * **Board Construction**: Build the board at the end from the column positions array, rather than maintaining a 2D grid throughout recursion. Store `col_positions = []` and append the column chosen for each row.
  * **Symmetry Pruning**: For a further optimization, only explore the first half of columns for row 0 and mirror solutions. This halves the search space but isn't required in interviews.
* **Complexity**:
  * Time: $O(N!)$
  * Space: $O(N)$
