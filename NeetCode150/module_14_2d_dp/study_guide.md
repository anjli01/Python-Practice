# Module 5.2: 2-D Dynamic Programming – Study Guide & Pattern Deep-Dive

In 2-D Dynamic Programming, state transitions depend on **two independent variables** (e.g., indices in two strings, row and column in a grid, or left and right boundaries of an interval).

---

## 1. Unique Paths (LeetCode 62) - Medium
* **Pattern**: Grid Path Summation
* **Core Concept**: $\text{dp}[r][c] = \text{dp}[r+1][c] + \text{dp}[r][c+1]$. Optimize to 1D array of size $N$.
* **Complexity**: Time: $O(M \cdot N)$, Space: $O(N)$.

---

## 2. Longest Common Subsequence (LeetCode 1143) - Medium
* **Pattern**: 2D Grid String Alignment
* **Core Concept**: If $text_1[i] == text_2[j]$, $\text{dp}[i][j] = 1 + \text{dp}[i+1][j+1]$. Otherwise take $\max(\text{dp}[i+1][j], \text{dp}[i][j+1])$.
* **Complexity**: Time: $O(M \cdot N)$, Space: $O(M \cdot N)$ or $O(N)$ with rolling row.

---

## 3. Best Time to Buy and Sell Stock with Cooldown (LeetCode 309) - Medium
* **Pattern**: State-Machine Transition DP
* **Core Concept**:
  * If buying at day $i$: branch into $(i+1, \text{False}) - \text{price}[i]$ or cooldown $(i+1, \text{True})$.
  * If selling at day $i$: must cooldown next day, branching into $(i+2, \text{True}) + \text{price}[i]$ or cooldown $(i+1, \text{False})$.
* **Complexity**: Time: $O(N)$, Space: $O(N)$ memoization states.

---

## 4. Coin Change II (LeetCode 518) - Medium
* **Pattern**: Unbounded Knapsack Combination Count
* **Core Concept**:
  Outer loop over coins, inner loop over amounts:
  `for c in coins: for a in range(c, amount + 1): dp[a] += dp[a - c]`
  Iterating over coins on the outer loop guarantees combination counting without duplicate permutations.
* **Complexity**: Time: $O(N \cdot A)$, Space: $O(A)$.

---

## 5. Target Sum (LeetCode 494) - Medium
* **Pattern**: Mathematical Reduction to 0/1 Subset Sum
* **Core Concept**:
  Let $P$ be positive choices and $N$ negative choices. $P - N = \text{target}$ and $P + N = \text{total}$.
  Adding gives $2P = \text{target} + \text{total} \implies P = \frac{\text{target} + \text{total}}{2}$. Solve standard 0/1 subset sum for target $P$.
* **Complexity**: Time: $O(N \cdot P)$, Space: $O(P)$.

---

## 6. Interleaving String (LeetCode 97) - Medium
* **Pattern**: 2D Grid Interleaving Matching
* **Core Concept**: $\text{dp}[i][j]$ indicates whether $s_3[i+j:]$ can be formed by interleaving $s_1[i:]$ and $s_2[j:]$.
* **Complexity**: Time: $O(|s_1| \cdot |s_2|)$, Space: $O(|s_1| \cdot |s_2|)$.

---

## 7. Longest Increasing Path in a Matrix (LeetCode 329) - Hard
* **Pattern**: Memoized DFS on Implicit DAG
* **Core Concept**:
  A strictly increasing path cannot have cycles, forming a Directed Acyclic Graph (DAG). $\text{dfs}(r, c) = 1 + \max_{(nr, nc)} \text{dfs}(nr, nc)$. Memoize results to achieve linear time.
* **Complexity**: Time: $O(M \cdot N)$, Space: $O(M \cdot N)$.

---

## 8. Distinct Subsequences (LeetCode 115) - Hard
* **Pattern**: 2D Subsequence Frequency Matching
* **Core Concept**: If $s[i] == t[j]$, we can either use $s[i]$ to match $t[j]$ ($\text{dp}[i+1][j+1]$) or skip $s[i]$ ($\text{dp}[i+1][j]$). If they don't match, we must skip $s[i]$.
* **Complexity**: Time: $O(|s| \cdot |t|)$, Space: $O(|s| \cdot |t|)$.

---

## 9. Edit Distance (LeetCode 72) - Medium
* **Pattern**: Classical Levenshtein Distance
* **Core Concept**:
  If characters match, advance both ($\text{dp}[i+1][j+1]$). If mismatch, take $1 + \min(\text{delete}, \text{insert}, \text{replace})$.
* **Complexity**: Time: $O(M \cdot N)$, Space: $O(M \cdot N)$.

---

## 10. Burst Balloons (LeetCode 312) - Hard
* **Pattern**: Interval DP (Choice of Last Balloon)
* **Core Concept**:
  Instead of choosing which balloon to burst *first* (which changes adjacency for remaining balloons), choose which balloon $i$ bursts **last** in the sub-interval $(l, r)$.
  Coins gained: $nums[l-1] \cdot nums[i] \cdot nums[r+1] + \text{dp}[l][i-1] + \text{dp}[i+1][r]$.
* **Complexity**: Time: $O(N^3)$, Space: $O(N^2)$.

---

## 11. Regular Expression Matching (LeetCode 10) - Hard
* **Pattern**: 2D Top-Down Memoized State Machine with Lookahead
* **Core Concept**:
  Check if $p[j+1] == '*'$. If so, branch into:
  1. Skip '*' and preceding character (0 matches): `dfs(i, j + 2)`.
  2. Consume character if $s[i]$ matches $p[j]$: `dfs(i + 1, j)`.
* **Complexity**: Time: $O(M \cdot N)$, Space: $O(M \cdot N)$.
