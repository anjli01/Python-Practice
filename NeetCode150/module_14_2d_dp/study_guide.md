# Module 5.2: 2-D Dynamic Programming – Study Guide & Pattern Deep-Dive

In 2-D Dynamic Programming, state transitions depend on **two independent variables** (e.g., indices in two strings, row and column in a grid, or left and right boundaries of an interval).

---

## 1. Unique Paths (LeetCode 62) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/unique-paths/) • [NeetCode Problem](https://neetcode.io/problems/count-paths) • [NeetCode Solution](https://neetcode.io/solutions/unique-paths) • [YouTube Video](https://www.youtube.com/watch?v=IlEsdxuD4lY)
* **Pattern**: Grid Path Summation
* **Core Concept**: $\text{dp}[r][c] = \text{dp}[r+1][c] + \text{dp}[r][c+1]$. Optimize to 1D array of size $N$.
* **Complexity**: Time: $O(M \cdot N)$, Space: $O(N)$.

---

## 2. Longest Common Subsequence (LeetCode 1143) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/longest-common-subsequence/) • [NeetCode Problem](https://neetcode.io/problems/longest-common-subsequence) • [NeetCode Solution](https://neetcode.io/solutions/longest-common-subsequence) • [YouTube Video](https://www.youtube.com/watch?v=Ua0GhsJSlWM)
* **Pattern**: 2D Grid String Alignment
* **Core Concept**: If $text_1[i] == text_2[j]$, $\text{dp}[i][j] = 1 + \text{dp}[i+1][j+1]$. Otherwise take $\max(\text{dp}[i+1][j], \text{dp}[i][j+1])$.
* **Complexity**: Time: $O(M \cdot N)$, Space: $O(M \cdot N)$ or $O(N)$ with rolling row.

---

## 3. Best Time to Buy and Sell Stock with Cooldown (LeetCode 309) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) • [NeetCode Problem](https://neetcode.io/problems/buy-and-sell-crypto-with-cooldown) • [NeetCode Solution](https://neetcode.io/solutions/best-time-to-buy-and-sell-stock-with-cooldown) • [YouTube Video](https://www.youtube.com/watch?v=I7j0F7AHpb8)
* **Pattern**: State-Machine Transition DP
* **Core Concept**:
  * If buying at day $i$: branch into $(i+1, \text{False}) - \text{price}[i]$ or cooldown $(i+1, \text{True})$.
  * If selling at day $i$: must cooldown next day, branching into $(i+2, \text{True}) + \text{price}[i]$ or cooldown $(i+1, \text{False})$.
* **Complexity**: Time: $O(N)$, Space: $O(N)$ memoization states.

---

## 4. Coin Change II (LeetCode 518) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/coin-change-ii/) • [NeetCode Problem](https://neetcode.io/problems/coin-change-ii) • [NeetCode Solution](https://neetcode.io/solutions/coin-change-ii) • [YouTube Video](https://www.youtube.com/watch?v=Mjy4hd2xgrs)
* **Pattern**: Unbounded Knapsack Combination Count
* **Core Concept**:
  Outer loop over coins, inner loop over amounts:
  `for c in coins: for a in range(c, amount + 1): dp[a] += dp[a - c]`
  Iterating over coins on the outer loop guarantees combination counting without duplicate permutations.
* **Complexity**: Time: $O(N \cdot A)$, Space: $O(A)$.

---

## 5. Target Sum (LeetCode 494) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/target-sum/) • [NeetCode Problem](https://neetcode.io/problems/target-sum) • [NeetCode Solution](https://neetcode.io/solutions/target-sum) • [YouTube Video](https://www.youtube.com/watch?v=dwMOrl85Xes)
* **Pattern**: Mathematical Reduction to 0/1 Subset Sum
* **Core Concept**:
  Let $P$ be positive choices and $N$ negative choices. $P - N = \text{target}$ and $P + N = \text{total}$.
  Adding gives $2P = \text{target} + \text{total} \implies P = \frac{\text{target} + \text{total}}{2}$. Solve standard 0/1 subset sum for target $P$.
* **Complexity**: Time: $O(N \cdot P)$, Space: $O(P)$.

---

## 6. Interleaving String (LeetCode 97) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/interleaving-string/) • [NeetCode Problem](https://neetcode.io/problems/interleaving-string) • [NeetCode Solution](https://neetcode.io/solutions/interleaving-string) • [YouTube Video](https://www.youtube.com/watch?v=3Rw3p9LrgvE)
* **Pattern**: 2D Grid Interleaving Matching
* **Core Concept**: $\text{dp}[i][j]$ indicates whether $s_3[i+j:]$ can be formed by interleaving $s_1[i:]$ and $s_2[j:]$.
* **Complexity**: Time: $O(|s_1| \cdot |s_2|)$, Space: $O(|s_1| \cdot |s_2|)$.

---

## 7. Longest Increasing Path in a Matrix (LeetCode 329) - Hard
* **Quick Links**: [LeetCode](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/) • [NeetCode Problem](https://neetcode.io/problems/longest-increasing-path-in-matrix) • [NeetCode Solution](https://neetcode.io/solutions/longest-increasing-path-in-a-matrix) • [YouTube Video](https://www.youtube.com/watch?v=wCc_nd-GiEc)
* **Pattern**: Memoized DFS on Implicit DAG
* **Core Concept**:
  A strictly increasing path cannot have cycles, forming a Directed Acyclic Graph (DAG). $\text{dfs}(r, c) = 1 + \max_{(nr, nc)} \text{dfs}(nr, nc)$. Memoize results to achieve linear time.
* **Complexity**: Time: $O(M \cdot N)$, Space: $O(M \cdot N)$.

---

## 8. Distinct Subsequences (LeetCode 115) - Hard
* **Quick Links**: [LeetCode](https://leetcode.com/problems/distinct-subsequences/) • [NeetCode Problem](https://neetcode.io/problems/count-subsequences) • [NeetCode Solution](https://neetcode.io/solutions/distinct-subsequences) • [YouTube Video](https://www.youtube.com/watch?v=-RDzMJ33nx8)
* **Pattern**: 2D Subsequence Frequency Matching
* **Core Concept**: If $s[i] == t[j]$, we can either use $s[i]$ to match $t[j]$ ($\text{dp}[i+1][j+1]$) or skip $s[i]$ ($\text{dp}[i+1][j]$). If they don't match, we must skip $s[i]$.
* **Complexity**: Time: $O(|s| \cdot |t|)$, Space: $O(|s| \cdot |t|)$.

---

## 9. Edit Distance (LeetCode 72) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/edit-distance/) • [NeetCode Problem](https://neetcode.io/problems/edit-distance) • [NeetCode Solution](https://neetcode.io/solutions/edit-distance) • [YouTube Video](https://www.youtube.com/watch?v=XYi2-LPrwm4)
* **Pattern**: Classical Levenshtein Distance
* **Core Concept**:
  If characters match, advance both ($\text{dp}[i+1][j+1]$). If mismatch, take $1 + \min(\text{delete}, \text{insert}, \text{replace})$.
* **Complexity**: Time: $O(M \cdot N)$, Space: $O(M \cdot N)$.

---

## 10. Burst Balloons (LeetCode 312) - Hard
* **Quick Links**: [LeetCode](https://leetcode.com/problems/burst-balloons/) • [NeetCode Problem](https://neetcode.io/problems/burst-balloons) • [NeetCode Solution](https://neetcode.io/solutions/burst-balloons) • [YouTube Video](https://www.youtube.com/watch?v=VFskby7lUbw)
* **Pattern**: Interval DP (Choice of Last Balloon)
* **Core Concept**:
  Instead of choosing which balloon to burst *first* (which changes adjacency for remaining balloons), choose which balloon $i$ bursts **last** in the sub-interval $(l, r)$.
  Coins gained: $nums[l-1] \cdot nums[i] \cdot nums[r+1] + \text{dp}[l][i-1] + \text{dp}[i+1][r]$.
* **Complexity**: Time: $O(N^3)$, Space: $O(N^2)$.

---

## 11. Regular Expression Matching (LeetCode 10) - Hard
* **Quick Links**: [LeetCode](https://leetcode.com/problems/regular-expression-matching/) • [NeetCode Problem](https://neetcode.io/problems/regular-expression-matching) • [NeetCode Solution](https://neetcode.io/solutions/regular-expression-matching) • [YouTube Video](https://www.youtube.com/watch?v=HAA8mgxlov8)
* **Pattern**: 2D Top-Down Memoized State Machine with Lookahead
* **Core Concept**:
  Check if $p[j+1] == '*'$. If so, branch into:
  1. Skip '*' and preceding character (0 matches): `dfs(i, j + 2)`.
  2. Consume character if $s[i]$ matches $p[j]$: `dfs(i + 1, j)`.
* **Complexity**: Time: $O(M \cdot N)$, Space: $O(M \cdot N)$.
