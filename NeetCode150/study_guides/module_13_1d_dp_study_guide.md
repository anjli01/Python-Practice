# Module 5.1: 1-D Dynamic Programming – Study Guide & Pattern Deep-Dive

Dynamic Programming (DP) solves complex problems by breaking them down into **overlapping subproblems** that exhibit **optimal substructure**. In 1-D DP, each state is defined along a single progression axis (time, index, or capacity).

---

## 1. Climbing Stairs (LeetCode 70) - Easy
* **Quick Links**: [LeetCode](https://leetcode.com/problems/climbing-stairs/) • [NeetCode Problem](https://neetcode.io/problems/climbing-stairs) • [NeetCode Solution](https://neetcode.io/solutions/climbing-stairs) • [YouTube Video](https://www.youtube.com/watch?v=Y0lT9Fck7qI)
* **Pattern**: Fibonacci Recurrence
* **Core Concept**:
  $\text{dp}[i] = \text{dp}[i-1] + \text{dp}[i-2]$. The number of ways to reach step $i$ is the sum of ways to reach the two preceding steps, because you can arrive from either one. Only retain the previous two scalar values for $O(1)$ space.
* **Mental Model**:
  A staircase where each step has a counter showing how many unique paths lead to it. Each counter is the sum of the two counters below it — exactly like Pascal's triangle flattened into a line.
* **Tips & Interview Tricks**:
  * **Recognize the Fibonacci**: This IS the Fibonacci sequence. Saying *"This reduces to Fibonacci"* immediately signals pattern recognition to the interviewer.
  * **Space Optimization**: Don't allocate a full DP array. Two variables (`one, two`) updated in a rolling fashion achieve $O(1)$ space.
* **Complexity**:
  * Time: $O(n)$
  * Space: $O(1)$

---

## 2. Min Cost Climbing Stairs (LeetCode 746) - Easy
* **Quick Links**: [LeetCode](https://leetcode.com/problems/min-cost-climbing-stairs/) • [NeetCode Problem](https://neetcode.io/problems/min-cost-climbing-stairs) • [NeetCode Solution](https://neetcode.io/solutions/min-cost-climbing-stairs) • [YouTube Video](https://www.youtube.com/watch?v=ktmzAZWkEZ0)
* **Pattern**: Backward In-Place Cost Accumulation
* **Core Concept**:
  $\text{cost}[i] += \min(\text{cost}[i+1], \text{cost}[i+2])$. Working backwards, each step accumulates the cheapest future cost. The answer is $\min(\text{cost}[0], \text{cost}[1])$ since you can start from either step 0 or step 1.
* **Mental Model**:
  Standing at the bottom of a staircase with toll booths. Each step charges a fee. Look ahead to the next two steps and always choose the cheaper path forward. Working backwards "pre-computes" the optimal route.
* **Tips & Interview Tricks**:
  * **Forward vs. Backward**: Both directions work. Backward iteration modifies `cost` in-place without extra space. Forward requires a separate DP array (or two variables).
  * **Starting Condition**: You can start from step 0 OR step 1 (both are free to stand on). The answer is `min(cost[0], cost[1])` after accumulation.
* **Complexity**:
  * Time: $O(n)$
  * Space: $O(1)$

---

## 3. House Robber (LeetCode 198) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/house-robber/) • [NeetCode Problem](https://neetcode.io/problems/house-robber) • [NeetCode Solution](https://neetcode.io/solutions/house-robber) • [YouTube Video](https://www.youtube.com/watch?v=73r3KWiEvyk)
* **Pattern**: Non-Adjacent Maximum Accumulator
* **Core Concept**:
  At house $i$: choose $\max(\text{rob}1 + nums[i], \text{rob}2)$ where $\text{rob}1$ is the max loot excluding the adjacent house, and $\text{rob}2$ is the max loot including it. Two variables slide forward, avoiding the need for a full DP array.
* **Mental Model**:
  Walking down a street of houses. At each house, you decide: *"Is it worth robbing this house plus what I had two houses ago, or am I better off with what I already have from the previous house?"*
* **Tips & Interview Tricks**:
  * **Variable Naming**: Use `rob1` (max up to `i-2`) and `rob2` (max up to `i-1`). After processing house $i$: `rob1, rob2 = rob2, max(rob1 + nums[i], rob2)`.
  * **Foundation Problem**: This recurrence is the basis for House Robber II, Delete and Earn (LC 740), and many other DP problems. Master it thoroughly.
* **Complexity**:
  * Time: $O(n)$
  * Space: $O(1)$

---

## 4. House Robber II (LeetCode 213) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/house-robber-ii/) • [NeetCode Problem](https://neetcode.io/problems/house-robber-ii) • [NeetCode Solution](https://neetcode.io/solutions/house-robber-ii) • [YouTube Video](https://www.youtube.com/watch?v=rWAJCfYYOvM)
* **Pattern**: Circular Reduction
* **Core Concept**:
  The first and last houses are neighbors (circular street). Run House Robber I twice: once ignoring the first house (`nums[1:]`), once ignoring the last house (`nums[:-1]`). Return the maximum of both runs.
* **Mental Model**:
  A circular street where the first and last houses share a fence. You can't rob both. So consider two scenarios: pretend the first house doesn't exist, or pretend the last house doesn't exist. The better scenario wins.
* **Tips & Interview Tricks**:
  * **Reduction to Known Problem**: The elegance is reducing a harder problem to two runs of an easier one. Tell the interviewer: *"The circular constraint means we can never take both house 0 and house n-1. Splitting into two linear subproblems eliminates this conflict."*
  * **Edge Case**: If `len(nums) == 1`, return `nums[0]` directly — the two-run approach would produce empty subarrays.
* **Complexity**:
  * Time: $O(n)$
  * Space: $O(1)$

---

## 5. Longest Palindromic Substring (LeetCode 5) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/longest-palindromic-substring/) • [NeetCode Problem](https://neetcode.io/problems/longest-palindromic-substring) • [NeetCode Solution](https://neetcode.io/solutions/longest-palindromic-substring) • [YouTube Video](https://www.youtube.com/watch?v=XYQecbcd6_c)
* **Pattern**: Expand Around Center
* **Core Concept**:
  Expand outward from $2n - 1$ centers: odd-length palindromes centered at $(i, i)$ and even-length palindromes centered at $(i, i+1)$. For each center, expand while characters match and track the longest palindrome found.
* **Mental Model**:
  Dropping a pebble at each character and watching ripples expand symmetrically. If the characters on both sides match, the ripple grows. The widest ripple from any drop point is the longest palindrome.
* **Tips & Interview Tricks**:
  * **$2n - 1$ Centers, Not $n$**: Every character is a center (odd-length), and every gap between characters is a center (even-length). Forgetting even-length centers is a common bug.
  * **$O(n^2)$ is Expected**: Manacher's algorithm achieves $O(n)$ but is rarely expected in interviews. The expand-around-center approach is clean and sufficient.
* **Complexity**:
  * Time: $O(n^2)$
  * Space: $O(1)$

---

## 6. Palindromic Substrings (LeetCode 647) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/palindromic-substrings/) • [NeetCode Problem](https://neetcode.io/problems/palindromic-substrings) • [NeetCode Solution](https://neetcode.io/solutions/palindromic-substrings) • [YouTube Video](https://www.youtube.com/watch?v=4RACzI5-du8)
* **Pattern**: Center Expansion Counter
* **Core Concept**:
  Expand outward from each center, incrementing the count for every symmetric expansion step. Each successful expansion discovers one new palindromic substring.
* **Mental Model**:
  Identical to Longest Palindromic Substring, but instead of tracking the longest ripple, you count every ripple at every expansion step. Each step = one new palindrome.
* **Tips & Interview Tricks**:
  * **Relationship to LC 5**: This is Longest Palindromic Substring but counting ALL instead of finding the longest. If you can solve LC 5, you can solve this by changing one line: increment a counter instead of tracking max length.
  * **Single Characters Count**: Every individual character is a palindrome of length 1. The minimum answer for a string of length $n$ is $n$.
* **Complexity**:
  * Time: $O(n^2)$
  * Space: $O(1)$

---

## 7. Decode Ways (LeetCode 91) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/decode-ways/) • [NeetCode Problem](https://neetcode.io/problems/decode-ways) • [NeetCode Solution](https://neetcode.io/solutions/decode-ways) • [YouTube Video](https://www.youtube.com/watch?v=6aEyTjOwlJU)
* **Pattern**: Single/Double Digit Branching DP
* **Core Concept**:
  * Single digit ($1-9$): contributes $\text{dp}[i+1]$ ways (decode one character).
  * Valid two digits ($10-26$): contributes $\text{dp}[i+2]$ ways (decode two characters).
  * `'0'` cannot be decoded alone — it must be part of `10` or `20`.
* **Mental Model**:
  Reading a coded message where each number maps to a letter (1=A, 2=B, ..., 26=Z). At each position, decide: *"Should I read one digit or two?"* The total ways to decode is the sum of valid single-digit and two-digit readings.
* **Tips & Interview Tricks**:
  * **Leading Zeros Are Invalid**: `'06'` is not a valid encoding of `'F'`. If `s[i] == '0'`, the single-digit branch contributes 0 ways. This is the #1 edge case candidates miss.
  * **Two Variables Suffice**: Like Fibonacci, only `dp[i+1]` and `dp[i+2]` are needed. Use two variables instead of a full array.
* **Complexity**:
  * Time: $O(n)$
  * Space: $O(1)$

---

## 8. Coin Change (LeetCode 322) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/coin-change/) • [NeetCode Problem](https://neetcode.io/problems/coin-change) • [NeetCode Solution](https://neetcode.io/solutions/coin-change) • [YouTube Video](https://www.youtube.com/watch?v=H9bfqozjoqs)
* **Pattern**: Unbounded Knapsack (Minimization)
* **Core Concept**:
  $\text{dp}[a] = \min_{c \in \text{coins}} (1 + \text{dp}[a - c])$. Initialize $\text{dp}[0] = 0$ (base case: 0 coins for amount 0) and all others to $\infty$ (impossible until proven otherwise). Build up from amount 1 to the target.
* **Mental Model**:
  A vending machine's coin-return mechanism. For each target amount, try every coin denomination and ask: *"If I use this coin, what's the fewest coins needed for the remaining amount?"* Take the minimum across all denominations.
* **Tips & Interview Tricks**:
  * **Bottom-Up vs. Top-Down**: Bottom-up (tabulation) is more natural here and avoids recursion stack overhead. Initialize `dp = [float('inf')] * (amount + 1); dp[0] = 0`.
  * **Return -1 for Impossible**: If `dp[amount]` remains `float('inf')`, no combination of coins can make the amount. Return $-1$.
* **Complexity**:
  * Time: $O(A \cdot C)$ where $A$ is amount, $C$ is number of coin types
  * Space: $O(A)$

---

## 9. Maximum Product Subarray (LeetCode 152) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/maximum-product-subarray/) • [NeetCode Problem](https://neetcode.io/problems/maximum-product-subarray) • [NeetCode Solution](https://neetcode.io/solutions/maximum-product-subarray) • [YouTube Video](https://www.youtube.com/watch?v=lXVy6YWFcRM)
* **Pattern**: Dual-Extrema Tracking (Min & Max)
* **Core Concept**:
  Multiplying by a negative number flips minimum to maximum and vice versa. Maintain both `cur_max` and `cur_min` at each step. Update both with `max(n, cur_max * n, cur_min * n)` and `min(n, cur_max * n, cur_min * n)`.
* **Mental Model**:
  A roller coaster of positive and negative numbers. A large negative product can become the largest positive product with one more negative number. Track both the highest peak and the deepest valley at every position.
* **Tips & Interview Tricks**:
  * **Why Track Min?**: A very negative `cur_min` multiplied by a negative `nums[i]` can produce the new `cur_max`. This is the key insight that distinguishes this from Maximum Subarray Sum (Kadane's).
  * **Zero Resets**: Multiplying by zero collapses both `cur_max` and `cur_min` to 0, effectively restarting the subarray. The `max(n, ...)` and `min(n, ...)` handle this automatically.
* **Complexity**:
  * Time: $O(n)$
  * Space: $O(1)$

---

## 10. Word Break (LeetCode 139) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/word-break/) • [NeetCode Problem](https://neetcode.io/problems/word-break) • [NeetCode Solution](https://neetcode.io/solutions/word-break) • [YouTube Video](https://www.youtube.com/watch?v=Sx9NNgInc3A)
* **Pattern**: Suffix Segmentation Matching
* **Core Concept**:
  Working backwards from end of string: $\text{dp}[i] = \text{True}$ if any dictionary word matches the prefix $s[i:i+L]$ and $\text{dp}[i + L] == \text{True}$. The base case is $\text{dp}[n] = \text{True}$ (empty suffix is always valid).
* **Mental Model**:
  Cutting a long rope into segments where each segment must match a word in the dictionary. Starting from the end, check if any dictionary word fits the current position. If it does AND the remaining rope can also be segmented, this position is valid.
* **Tips & Interview Tricks**:
  * **Iterate Words, Not Substrings**: For each position $i$, try each word $w$ in the dictionary: `if s[i:i+len(w)] == w and dp[i+len(w)]: dp[i] = True`. This is $O(n \cdot m \cdot k)$ but avoids generating all substrings.
  * **Trie Optimization**: For large dictionaries, insert words into a Trie for $O(L)$ prefix matching instead of $O(L)$ string comparison per word.
* **Complexity**:
  * Time: $O(N \cdot M \cdot K)$ where $N$ is string length, $M$ is dictionary size, $K$ is max word length
  * Space: $O(N)$

---

## 11. Longest Increasing Subsequence (LeetCode 300) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/longest-increasing-subsequence/) • [NeetCode Problem](https://neetcode.io/problems/longest-increasing-subsequence) • [NeetCode Solution](https://neetcode.io/solutions/longest-increasing-subsequence) • [YouTube Video](https://www.youtube.com/watch?v=cjWnW0hdF1Y)
* **Pattern**: Patience Sorting with Binary Search
* **Core Concept**:
  Maintain an array `tails` where `tails[i]` stores the smallest tail of all increasing subsequences of length $i + 1$. For each new element, binary search (`bisect_left`) to find its position: either extend the longest subsequence or replace an existing tail with a smaller value.
* **Mental Model**:
  A card game (Patience Sorting). Lay cards in piles: a card goes on the leftmost pile whose top is $\ge$ the card, or starts a new pile if no such pile exists. The number of piles equals the LIS length.
* **Tips & Interview Tricks**:
  * **$O(n^2)$ vs. $O(n \log n)$**: The naive DP (`dp[i] = max(dp[j] + 1 for j < i if nums[j] < nums[i])`) is $O(n^2)$. The `tails` + binary search approach is $O(n \log n)$. Know both — start with $O(n^2)$ and optimize.
  * **`tails` is NOT the LIS**: The `tails` array gives the correct LENGTH but may not contain the actual subsequence. If asked to reconstruct the LIS, maintain parent pointers.
* **Complexity**:
  * Time: $O(n \log n)$
  * Space: $O(n)$

---

## 12. Partition Equal Subset Sum (LeetCode 416) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/partition-equal-subset-sum/) • [NeetCode Problem](https://neetcode.io/problems/partition-equal-subset-sum) • [NeetCode Solution](https://neetcode.io/solutions/partition-equal-subset-sum) • [YouTube Video](https://www.youtube.com/watch?v=IsvocB5BJhw)
* **Pattern**: 0/1 Knapsack Target Sum
* **Core Concept**:
  If $\sum nums$ is odd, return False immediately. Otherwise, find a subset summing to $\text{target} = \text{total} // 2$. Maintain a set of reachable sums, iterating through each number and adding it to all existing sums.
* **Mental Model**:
  Packing a suitcase to exactly half the total weight. For each item, ask: *"Can I reach any new weight by adding this item to combinations I've already found?"* If you hit exactly half, the remaining items automatically form the other half.
* **Tips & Interview Tricks**:
  * **Odd Sum Early Exit**: If `total % 2 != 0`, return `False` immediately. This is an $O(1)$ check that avoids all DP computation.
  * **Set-Based DP**: Use `dp = {0}` and for each `num`: `dp = dp | {s + num for s in dp}`. This is concise and Pythonic. For efficiency, iterate in reverse when using a boolean array to avoid using the same item twice.
  * **Bounded Target**: The target is at most `total // 2`, which bounds the DP table size and prevents unnecessary computation.
* **Complexity**:
  * Time: $O(n \cdot \text{target})$
  * Space: $O(\text{target})$
