# Module 5.2: 2-D Dynamic Programming – Study Guide & Pattern Deep-Dive

In 2-D Dynamic Programming, state transitions depend on **two independent variables** (e.g., indices in two strings, row and column in a grid, or left and right boundaries of an interval).

---

## 1. Unique Paths (LeetCode 62) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/unique-paths/) • [NeetCode Problem](https://neetcode.io/problems/count-paths) • [NeetCode Solution](https://neetcode.io/solutions/unique-paths) • [YouTube Video](https://www.youtube.com/watch?v=IlEsdxuD4lY)
* **Pattern**: Grid Path Summation
* **Core Concept**:
  $\text{dp}[r][c] = \text{dp}[r+1][c] + \text{dp}[r][c+1]$. Each cell's path count is the sum of paths from the cell below and the cell to the right. Optimize to a 1D array of size $N$ by processing row by row.
* **Mental Model**:
  A city grid where you can only move right or down. At each intersection, the number of routes to the destination is the sum of routes from the intersection below and the intersection to the right.
* **Tips & Interview Tricks**:
  * **Combinatorial Solution**: The answer is $\binom{m+n-2}{m-1}$. You need exactly $m-1$ down moves and $n-1$ right moves in any order. Mention this to demonstrate mathematical insight.
  * **1D Space Optimization**: Process one row at a time: `for c in range(n-2, -1, -1): row[c] += row[c+1]`. This reduces space from $O(m \cdot n)$ to $O(n)$.
* **Complexity**:
  * Time: $O(M \cdot N)$
  * Space: $O(N)$

---

## 2. Longest Common Subsequence (LeetCode 1143) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/longest-common-subsequence/) • [NeetCode Problem](https://neetcode.io/problems/longest-common-subsequence) • [NeetCode Solution](https://neetcode.io/solutions/longest-common-subsequence) • [YouTube Video](https://www.youtube.com/watch?v=Ua0GhsJSlWM)
* **Pattern**: 2D Grid String Alignment
* **Core Concept**:
  If $text_1[i] == text_2[j]$, $\text{dp}[i][j] = 1 + \text{dp}[i+1][j+1]$. Otherwise take $\max(\text{dp}[i+1][j], \text{dp}[i][j+1])$ — skip a character from either string. Build the table bottom-up from the last characters.
* **Mental Model**:
  Two people reading different books, trying to find the longest sequence of words they share in order. At each step, if their current words match, they both advance. If not, one of them skips ahead, and you try both options.
* **Tips & Interview Tricks**:
  * **Rolling Row Optimization**: Only two rows of the DP table are active at any time. Use `prev` and `curr` arrays to reduce space from $O(M \cdot N)$ to $O(N)$.
  * **Foundation Problem**: LCS is the basis for Edit Distance (LC 72), Shortest Common Supersequence (LC 1092), and diff algorithms. Mastering it unlocks multiple related problems.
* **Complexity**:
  * Time: $O(M \cdot N)$
  * Space: $O(M \cdot N)$ or $O(N)$ with rolling row

---

## 3. Best Time to Buy and Sell Stock with Cooldown (LeetCode 309) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) • [NeetCode Problem](https://neetcode.io/problems/buy-and-sell-crypto-with-cooldown) • [NeetCode Solution](https://neetcode.io/solutions/best-time-to-buy-and-sell-stock-with-cooldown) • [YouTube Video](https://www.youtube.com/watch?v=I7j0F7AHpb8)
* **Pattern**: State-Machine Transition DP
* **Core Concept**:
  * If buying at day $i$: branch into $(i+1, \text{selling}) - \text{price}[i]$ or cooldown $(i+1, \text{buying})$.
  * If selling at day $i$: must cooldown next day, branching into $(i+2, \text{buying}) + \text{price}[i]$ or cooldown $(i+1, \text{selling})$.
  Memoize on `(day, is_buying)` to avoid recomputation.
* **Mental Model**:
  A state machine with three states: *Buying*, *Selling*, *Cooldown*. From each state, certain transitions are allowed. The cooldown state forces you to skip one day after selling before you can buy again.
* **Tips & Interview Tricks**:
  * **State Machine Visualization**: Draw three circles (Buy, Sell, Cooldown) with arrows showing valid transitions. This clarifies the recurrence and impresses interviewers.
  * **Variable Approach**: Instead of a 2D DP table, use three variables: `buy`, `sell`, `cooldown` updated each day. This achieves $O(1)$ space.
* **Complexity**:
  * Time: $O(N)$
  * Space: $O(N)$ memoization states or $O(1)$ with variables

---

## 4. Coin Change II (LeetCode 518) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/coin-change-ii/) • [NeetCode Problem](https://neetcode.io/problems/coin-change-ii) • [NeetCode Solution](https://neetcode.io/solutions/coin-change-ii) • [YouTube Video](https://www.youtube.com/watch?v=Mjy4hd2xgrs)
* **Pattern**: Unbounded Knapsack Combination Count
* **Core Concept**:
  Outer loop over coins, inner loop over amounts:
  `for c in coins: for a in range(c, amount + 1): dp[a] += dp[a - c]`
  Iterating coins on the outer loop guarantees combination counting (not permutation counting), because each coin type is considered in a fixed order.
* **Mental Model**:
  A cashier making change. Consider one denomination at a time. For each denomination, determine how many ways it can contribute to every possible amount. Because denominations are processed in order, you never count "1 nickel + 1 dime" and "1 dime + 1 nickel" as different.
* **Tips & Interview Tricks**:
  * **Loop Order Matters**: Coins-outer counts **combinations** (order doesn't matter). Amounts-outer counts **permutations** (order matters). Swapping the loop order changes the problem entirely.
  * **Coin Change I vs. II**: CC-I asks for minimum coins (use `min`). CC-II asks for number of combinations (use `+=`). Don't confuse them.
* **Complexity**:
  * Time: $O(N \cdot A)$
  * Space: $O(A)$

---

## 5. Target Sum (LeetCode 494) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/target-sum/) • [NeetCode Problem](https://neetcode.io/problems/target-sum) • [NeetCode Solution](https://neetcode.io/solutions/target-sum) • [YouTube Video](https://www.youtube.com/watch?v=dwMOrl85Xes)
* **Pattern**: Mathematical Reduction to 0/1 Subset Sum
* **Core Concept**:
  Let $P$ be the sum of positive choices and $N$ the sum of negative choices. $P - N = \text{target}$ and $P + N = \text{total}$.
  Adding gives $2P = \text{target} + \text{total} \implies P = \frac{\text{target} + \text{total}}{2}$. This reduces to: find the number of subsets summing to $P$.
* **Mental Model**:
  Assigning $+$ or $-$ signs to each number is equivalent to splitting numbers into two groups. The positive group minus the negative group must equal the target. The math reveals you just need to find subsets summing to a specific value.
* **Tips & Interview Tricks**:
  * **Early Exit Conditions**: If $(\text{target} + \text{total})$ is odd, return 0 (no integer solution). If $|\text{target}| > \text{total}$, return 0.
  * **Alternative: Hash Map DP**: Use `dp = {0: 1}` (sum → count). For each `num`, create a new dict: for each existing `(s, cnt)`, add to `s + num` and `s - num`. This avoids the mathematical reduction but is less efficient.
* **Complexity**:
  * Time: $O(N \cdot P)$
  * Space: $O(P)$

---

## 6. Interleaving String (LeetCode 97) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/interleaving-string/) • [NeetCode Problem](https://neetcode.io/problems/interleaving-string) • [NeetCode Solution](https://neetcode.io/solutions/interleaving-string) • [YouTube Video](https://www.youtube.com/watch?v=3Rw3p9LrgvE)
* **Pattern**: 2D Grid Interleaving Matching
* **Core Concept**:
  $\text{dp}[i][j]$ indicates whether $s_3[i+j:]$ can be formed by interleaving $s_1[i:]$ and $s_2[j:]$. At each cell, either $s_3[i+j]$ matches $s_1[i]$ (move down in the grid) or $s_3[i+j]$ matches $s_2[j]$ (move right).
* **Mental Model**:
  Shuffling two decks of cards into one combined deck. The relative order within each deck must be preserved, but cards from the two decks can alternate freely. Check if the target deck is a valid shuffle.
* **Tips & Interview Tricks**:
  * **Length Check First**: If `len(s1) + len(s2) != len(s3)`, return `False` immediately.
  * **1D Space Optimization**: Since each row only depends on the row below, use a single 1D array of size `len(s2) + 1`.
  * **Memoization Alternative**: Top-down with `@lru_cache(None)` on `(i, j)` is often cleaner to code in interviews.
* **Complexity**:
  * Time: $O(|s_1| \cdot |s_2|)$
  * Space: $O(|s_1| \cdot |s_2|)$ or $O(|s_2|)$ optimized

---

## 7. Longest Increasing Path in a Matrix (LeetCode 329) - Hard
* **Quick Links**: [LeetCode](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/) • [NeetCode Problem](https://neetcode.io/problems/longest-increasing-path-in-matrix) • [NeetCode Solution](https://neetcode.io/solutions/longest-increasing-path-in-a-matrix) • [YouTube Video](https://www.youtube.com/watch?v=wCc_nd-GiEc)
* **Pattern**: Memoized DFS on Implicit DAG
* **Core Concept**:
  A strictly increasing path cannot have cycles, forming a Directed Acyclic Graph (DAG). $\text{dfs}(r, c) = 1 + \max_{(nr, nc)} \text{dfs}(nr, nc)$ for all neighbors where $grid[nr][nc] > grid[r][c]$. Memoize results to achieve linear time.
* **Mental Model**:
  A ball rolling downhill on a terrain map. It can only roll to adjacent cells that are strictly higher (we're finding the longest *increasing* path, so think of it as climbing *up*). Each cell's result is "how far can I climb from here?" — once computed, reuse it.
* **Tips & Interview Tricks**:
  * **No Visited Set Needed**: Because paths are strictly increasing, you can never revisit a cell in the same path. The memoization cache replaces the visited set.
  * **Every Cell is a Starting Point**: Launch DFS from every cell and take the global maximum. The memoization ensures total work is $O(M \cdot N)$ despite starting from every cell.
* **Complexity**:
  * Time: $O(M \cdot N)$
  * Space: $O(M \cdot N)$

---

## 8. Distinct Subsequences (LeetCode 115) - Hard
* **Quick Links**: [LeetCode](https://leetcode.com/problems/distinct-subsequences/) • [NeetCode Problem](https://neetcode.io/problems/count-subsequences) • [NeetCode Solution](https://neetcode.io/solutions/distinct-subsequences) • [YouTube Video](https://www.youtube.com/watch?v=-RDzMJ33nx8)
* **Pattern**: 2D Subsequence Frequency Matching
* **Core Concept**:
  If $s[i] == t[j]$, we can either use $s[i]$ to match $t[j]$ ($\text{dp}[i+1][j+1]$) or skip $s[i]$ ($\text{dp}[i+1][j]$). If they don't match, we must skip $s[i]$. Sum the two choices when they match.
* **Mental Model**:
  Highlighting letters in source string $s$ to spell out target $t$. When $s[i]$ matches $t[j]$, you have two choices: use this match (advance both pointers) or skip it (maybe a better match exists later in $s$). Count all valid highlighting patterns.
* **Tips & Interview Tricks**:
  * **Direction Matters**: Process bottom-up (from the ends of both strings toward the beginnings). The base case is `dp[i][len(t)] = 1` for all $i$ (empty target can always be matched).
  * **Space Optimization**: Use a 1D array since each row only depends on the next row.
* **Complexity**:
  * Time: $O(|s| \cdot |t|)$
  * Space: $O(|s| \cdot |t|)$

---

## 9. Edit Distance (LeetCode 72) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/edit-distance/) • [NeetCode Problem](https://neetcode.io/problems/edit-distance) • [NeetCode Solution](https://neetcode.io/solutions/edit-distance) • [YouTube Video](https://www.youtube.com/watch?v=XYi2-LPrwm4)
* **Pattern**: Classical Levenshtein Distance
* **Core Concept**:
  If characters match ($word_1[i] == word_2[j]$), advance both pointers: $\text{dp}[i+1][j+1]$. If they mismatch, take $1 + \min(\text{delete:}\ \text{dp}[i+1][j],\ \text{insert:}\ \text{dp}[i][j+1],\ \text{replace:}\ \text{dp}[i+1][j+1])$.
* **Mental Model**:
  An autocorrect engine transforming one word into another with the fewest keystrokes. At each position, you can delete a character, insert one, or replace one. The DP table maps out the cheapest edit path through all possible alignments.
* **Tips & Interview Tricks**:
  * **Three Operations = Three Neighbors**: Delete corresponds to moving down in the grid (skip a character in $word_1$). Insert corresponds to moving right (add a character from $word_2$). Replace corresponds to moving diagonally.
  * **Base Cases**: `dp[i][n] = m - i` and `dp[m][j] = n - j`. Transforming the remaining suffix of one word into an empty string requires one deletion/insertion per character.
  * **Real-World Application**: Mention that this is used in spell-checkers, DNA sequence alignment (bioinformatics), and diff utilities.
* **Complexity**:
  * Time: $O(M \cdot N)$
  * Space: $O(M \cdot N)$

---

## 10. Burst Balloons (LeetCode 312) - Hard
* **Quick Links**: [LeetCode](https://leetcode.com/problems/burst-balloons/) • [NeetCode Problem](https://neetcode.io/problems/burst-balloons) • [NeetCode Solution](https://neetcode.io/solutions/burst-balloons) • [YouTube Video](https://www.youtube.com/watch?v=VFskby7lUbw)
* **Pattern**: Interval DP (Choice of Last Balloon)
* **Core Concept**:
  Instead of choosing which balloon to burst *first* (which changes adjacency for remaining balloons), choose which balloon $i$ bursts **last** in the sub-interval $(l, r)$.
  Coins gained: $nums[l-1] \cdot nums[i] \cdot nums[r+1] + \text{dp}[l][i-1] + \text{dp}[i+1][r]$.
* **Mental Model**:
  A demolition planner. Instead of deciding which building to demolish first (which changes the neighborhood for remaining buildings), ask: *"Which building will be the LAST one standing in this block?"* The last building's payout depends only on the fixed boundaries of the block, not on the internal demolition order.
* **Tips & Interview Tricks**:
  * **Padding with 1s**: Add `1` at the beginning and end of the array: `nums = [1] + nums + [1]`. This handles boundary conditions cleanly — the "virtual" balloons at the edges always have value 1.
  * **Reverse Thinking is Key**: The crucial insight is thinking about the LAST balloon in each interval, not the first. This makes adjacent elements deterministic (the interval boundaries), enabling clean subproblem decomposition.
* **Complexity**:
  * Time: $O(N^3)$
  * Space: $O(N^2)$

---

## 11. Regular Expression Matching (LeetCode 10) - Hard
* **Quick Links**: [LeetCode](https://leetcode.com/problems/regular-expression-matching/) • [NeetCode Problem](https://neetcode.io/problems/regular-expression-matching) • [NeetCode Solution](https://neetcode.io/solutions/regular-expression-matching) • [YouTube Video](https://www.youtube.com/watch?v=HAA8mgxlov8)
* **Pattern**: 2D Top-Down Memoized State Machine with Lookahead
* **Core Concept**:
  Check if $p[j+1] == '*'$. If so, branch into:
  1. Skip '*' and preceding character (0 matches): `dfs(i, j + 2)`.
  2. Consume one character if $s[i]$ matches $p[j]$: `dfs(i + 1, j)`.
  If no '*' follows, simply check character match and advance both pointers.
* **Mental Model**:
  A regex engine with a program counter. The `'*'` operator creates a fork in the road: either skip the pattern entirely (0 matches) or consume one matching character and stay at the same pattern position (to potentially match more). Try both paths.
* **Tips & Interview Tricks**:
  * **Lookahead for '*'**: Always check `j + 1 < len(p) and p[j+1] == '*'` FIRST, before checking character match. The '*' fundamentally changes the branching logic.
  * **Dot Matches Any**: `'.'` matches any single character. Handle it uniformly: `match = i < len(s) and (s[i] == p[j] or p[j] == '.')`.
  * **Memoize on `(i, j)`**: Without memoization, the branching creates exponential time complexity. Cache results for each `(string_index, pattern_index)` pair.
* **Complexity**:
  * Time: $O(M \cdot N)$
  * Space: $O(M \cdot N)$
