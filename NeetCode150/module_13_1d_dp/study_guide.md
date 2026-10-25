# Module 5.1: 1-D Dynamic Programming – Study Guide & Pattern Deep-Dive

Dynamic Programming (DP) solves complex problems by breaking them down into **overlapping subproblems** that exhibit **optimal substructure**. In 1-D DP, each state is defined along a single progression axis (time, index, or capacity).

---

## 1. Climbing Stairs (LeetCode 70) - Easy
* **Quick Links**: [LeetCode](https://leetcode.com/problems/climbing-stairs/) • [NeetCode Problem](https://neetcode.io/problems/climbing-stairs) • [NeetCode Solution](https://neetcode.io/solutions/climbing-stairs) • [YouTube Video](https://www.youtube.com/watch?v=Y0lT9Fck7qI)
* **Pattern**: Fibonacci Recurrence
* **Core Concept**: $\text{dp}[i] = \text{dp}[i-1] + \text{dp}[i-2]$. Only retain the previous two scalar values.
* **Complexity**: Time: $O(n)$, Space: $O(1)$.

---

## 2. Min Cost Climbing Stairs (LeetCode 746) - Easy
* **Quick Links**: [LeetCode](https://leetcode.com/problems/min-cost-climbing-stairs/) • [NeetCode Problem](https://neetcode.io/problems/min-cost-climbing-stairs) • [NeetCode Solution](https://neetcode.io/solutions/min-cost-climbing-stairs) • [YouTube Video](https://www.youtube.com/watch?v=ktmzAZWkEZ0)
* **Pattern**: Backward In-Place Cost Accumulation
* **Core Concept**: $\text{cost}[i] += \min(\text{cost}[i+1], \text{cost}[i+2])$.
* **Complexity**: Time: $O(n)$, Space: $O(1)$.

---

## 3. House Robber (LeetCode 198) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/house-robber/) • [NeetCode Problem](https://neetcode.io/problems/house-robber) • [NeetCode Solution](https://neetcode.io/solutions/house-robber) • [YouTube Video](https://www.youtube.com/watch?v=73r3KWiEvyk)
* **Pattern**: Non-Adjacent Maximum Accumulator
* **Core Concept**: At house $i$: choose $\max(\text{rob}1 + n, \text{rob}2)$ where $\text{rob}1$ skips adjacent house.
* **Complexity**: Time: $O(n)$, Space: $O(1)$.

---

## 4. House Robber II (LeetCode 213) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/house-robber-ii/) • [NeetCode Problem](https://neetcode.io/problems/house-robber-ii) • [NeetCode Solution](https://neetcode.io/solutions/house-robber-ii) • [YouTube Video](https://www.youtube.com/watch?v=rWAJCfYYOvM)
* **Pattern**: Circular Reduction
* **Core Concept**: The first and last houses are neighbors. Run House Robber I twice: once ignoring the first house (`nums[1:]`), once ignoring the last house (`nums[:-1]`).
* **Complexity**: Time: $O(n)$, Space: $O(1)$.

---

## 5. Longest Palindromic Substring (LeetCode 5) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/longest-palindromic-substring/) • [NeetCode Problem](https://neetcode.io/problems/longest-palindromic-substring) • [NeetCode Solution](https://neetcode.io/solutions/longest-palindromic-substring) • [YouTube Video](https://www.youtube.com/watch?v=XYQecbcd6_c)
* **Pattern**: Expand Around Center
* **Core Concept**: Expand outward from $2n - 1$ centers (odd centers $(i, i)$ and even centers $(i, i+1)$).
* **Complexity**: Time: $O(n^2)$, Space: $O(1)$.

---

## 6. Palindromic Substrings (LeetCode 647) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/palindromic-substrings/) • [NeetCode Problem](https://neetcode.io/problems/palindromic-substrings) • [NeetCode Solution](https://neetcode.io/solutions/palindromic-substrings) • [YouTube Video](https://www.youtube.com/watch?v=4RACzI5-du8)
* **Pattern**: Center Expansion Counter
* **Core Concept**: Expand outward from each center, incrementing the count for every symmetric expansion step.
* **Complexity**: Time: $O(n^2)$, Space: $O(1)$.

---

## 7. Decode Ways (LeetCode 91) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/decode-ways/) • [NeetCode Problem](https://neetcode.io/problems/decode-ways) • [NeetCode Solution](https://neetcode.io/solutions/decode-ways) • [YouTube Video](https://www.youtube.com/watch?v=6aEyTjOwlJU)
* **Pattern**: Single/Double Digit Branching DP
* **Core Concept**:
  * Single digit ($1-9$): contributes $\text{dp}[i+1]$.
  * Valid two digits ($10-26$): contributes $\text{dp}[i+2]$.
* **Complexity**: Time: $O(n)$, Space: $O(1)$.

---

## 8. Coin Change (LeetCode 322) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/coin-change/) • [NeetCode Problem](https://neetcode.io/problems/coin-change) • [NeetCode Solution](https://neetcode.io/solutions/coin-change) • [YouTube Video](https://www.youtube.com/watch?v=H9bfqozjoqs)
* **Pattern**: Unbounded Knapsack (Minimization)
* **Core Concept**: $\text{dp}[a] = \min_{c} (1 + \text{dp}[a - c])$. Initialize $\text{dp}[0] = 0$ and all others to $\infty$.
* **Complexity**: Time: $O(A \cdot C)$, Space: $O(A)$ where $A$ is amount.

---

## 9. Maximum Product Subarray (LeetCode 152) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/maximum-product-subarray/) • [NeetCode Problem](https://neetcode.io/problems/maximum-product-subarray) • [NeetCode Solution](https://neetcode.io/solutions/maximum-product-subarray) • [YouTube Video](https://www.youtube.com/watch?v=lXVy6YWFcRM)
* **Pattern**: Dual-Extrema Tracking (Min & Max)
* **Core Concept**: Multiplying by a negative number flips minimum to maximum. Maintain both `cur_max` and `cur_min` at each step.
* **Complexity**: Time: $O(n)$, Space: $O(1)$.

---

## 10. Word Break (LeetCode 139) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/word-break/) • [NeetCode Problem](https://neetcode.io/problems/word-break) • [NeetCode Solution](https://neetcode.io/solutions/word-break) • [YouTube Video](https://www.youtube.com/watch?v=Sx9NNgInc3A)
* **Pattern**: Suffix Segmentation Matching
* **Core Concept**: Working backwards from end of string: $\text{dp}[i] = \text{True}$ if any dictionary word matches prefix $s[i:i+L]$ and $\text{dp}[i + L] == \text{True}$.
* **Complexity**: Time: $O(N \cdot M \cdot K)$, Space: $O(N)$.

---

## 11. Longest Increasing Subsequence (LeetCode 300) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/longest-increasing-subsequence/) • [NeetCode Problem](https://neetcode.io/problems/longest-increasing-subsequence) • [NeetCode Solution](https://neetcode.io/solutions/longest-increasing-subsequence) • [YouTube Video](https://www.youtube.com/watch?v=cjWnW0hdF1Y)
* **Pattern**: Patience Sorting with Binary Search
* **Core Concept**: Maintain an array `tails` where `tails[i]` stores the smallest tail of all increasing subsequences of length $i + 1$. Binary search (`bisect_left`) updates or appends in $O(\log n)$.
* **Complexity**: Time: $O(n \log n)$, Space: $O(n)$.

---

## 12. Partition Equal Subset Sum (LeetCode 416) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/partition-equal-subset-sum/) • [NeetCode Problem](https://neetcode.io/problems/partition-equal-subset-sum) • [NeetCode Solution](https://neetcode.io/solutions/partition-equal-subset-sum) • [YouTube Video](https://www.youtube.com/watch?v=IsvocB5BJhw)
* **Pattern**: 0/1 Knapsack Target Sum
* **Core Concept**: If $\sum nums$ is odd, return False. Otherwise find a subset summing to $\text{total} // 2$. Maintain a set of reachable sums.
* **Complexity**: Time: $O(n \cdot \text{target})$, Space: $O(\text{target})$.
