# Module 5.3: Greedy Algorithms – Study Guide & Pattern Deep-Dive

A **Greedy algorithm** makes the locally optimal choice at each stage with the intent of finding a global optimum. Unlike Dynamic Programming, greedy algorithms never reconsider previous choices.

---

## 1. Maximum Subarray (LeetCode 53) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/maximum-subarray/) • [NeetCode Problem](https://neetcode.io/problems/maximum-subarray) • [NeetCode Solution](https://neetcode.io/solutions/maximum-subarray) • [YouTube Video](https://www.youtube.com/watch?v=5WZl3MMT0Eg)
* **Pattern**: Kadane's Algorithm
* **Core Concept**: $\text{cur\_sum} = \max(n, \text{cur\_sum} + n)$. If a running sum dips below zero, it can never contribute positively to future subarrays.
* **Complexity**: Time: $O(n)$, Space: $O(1)$.

---

## 2. Jump Game (LeetCode 55) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/jump-game/) • [NeetCode Problem](https://neetcode.io/problems/jump-game) • [NeetCode Solution](https://neetcode.io/solutions/jump-game) • [YouTube Video](https://www.youtube.com/watch?v=Yan0cv2cLy8)
* **Pattern**: Backward Goalpost Shift
* **Core Concept**:
  Start with `goal = len(nums) - 1`. Scan backwards: if index $i$ can reach `goal` ($i + nums[i] \ge goal$), move `goal = i`. Return True if `goal == 0`.
* **Complexity**: Time: $O(n)$, Space: $O(1)$.

---

## 3. Jump Game II (LeetCode 45) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/jump-game-ii/) • [NeetCode Problem](https://neetcode.io/problems/jump-game-ii) • [NeetCode Solution](https://neetcode.io/solutions/jump-game-ii) • [YouTube Video](https://www.youtube.com/watch?v=dJ7sWiOoK7g)
* **Pattern**: BFS Range Window Slicing
* **Core Concept**:
  Maintain the current jump range $[left, right]$. Calculate the farthest index reachable from any index within the range. Advance $left = right + 1$ and $right = farthest$, incrementing the jump count.
* **Complexity**: Time: $O(n)$, Space: $O(1)$.

---

## 4. Gas Station (LeetCode 134) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/gas-station/) • [NeetCode Problem](https://neetcode.io/problems/gas-station) • [NeetCode Solution](https://neetcode.io/solutions/gas-station) • [YouTube Video](https://www.youtube.com/watch?v=lJwbPZGo05A)
* **Pattern**: Greedy Net-Gas Reset
* **Core Concept**:
  If $\sum gas < \sum cost$, completion is impossible (return -1). Otherwise, maintain running `total += gas[i] - cost[i]`. Whenever `total < 0`, the starting station cannot be anywhere from index 0 to $i$. Reset `total = 0` and set `start = i + 1`.
* **Complexity**: Time: $O(n)$, Space: $O(1)$.

---

## 5. Hand of Straights (LeetCode 846) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/hand-of-straights/) • [NeetCode Problem](https://neetcode.io/problems/hand-of-straights) • [NeetCode Solution](https://neetcode.io/solutions/hand-of-straights) • [YouTube Video](https://www.youtube.com/watch?v=amnrMCVd2YI)
* **Pattern**: Min-Heap Consecutive Slicing
* **Core Concept**:
  Sort unique card values in a min-heap. Pop the smallest available card $c$; cards $c, c+1, \dots, c + groupSize - 1$ must exist with frequency at least $count[c]$.
* **Complexity**: Time: $O(N \log N)$, Space: $O(N)$.

---

## 6. Merge Triplets to Form Target Triplet (LeetCode 1899) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/merge-triplets-to-form-target-triplet/) • [NeetCode Problem](https://neetcode.io/problems/merge-triplets-to-form-target) • [NeetCode Solution](https://neetcode.io/solutions/merge-triplets-to-form-target-triplet) • [YouTube Video](https://www.youtube.com/watch?v=kShkQLQZ9K4)
* **Pattern**: Invalid Candidate Filtering
* **Core Concept**:
  Discard any triplet having any component strictly greater than target. For the remaining valid triplets, record which target components are matched. If all 3 components are matched, return True.
* **Complexity**: Time: $O(N)$, Space: $O(1)$.

---

## 7. Partition Labels (LeetCode 763) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/partition-labels/) • [NeetCode Problem](https://neetcode.io/problems/partition-labels) • [NeetCode Solution](https://neetcode.io/solutions/partition-labels) • [YouTube Video](https://www.youtube.com/watch?v=B7m8UmZE-vw)
* **Pattern**: Furthest Occurrence Slicing
* **Core Concept**:
  Store the last index where each character appears. As you iterate, expand `end = max(end, last[char])`. When $i == end$, an independent partition is cut.
* **Complexity**: Time: $O(n)$, Space: $O(1)$ (26 characters).

---

## 8. Valid Parenthesis String (LeetCode 678) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/valid-parenthesis-string/) • [NeetCode Problem](https://neetcode.io/problems/valid-parenthesis-string) • [NeetCode Solution](https://neetcode.io/solutions/valid-parenthesis-string) • [YouTube Video](https://www.youtube.com/watch?v=QhPdNS143Qg)
* **Pattern**: Wildcard Range Interval Tracking
* **Core Concept**:
  Maintain the minimum and maximum possible number of open brackets $[c_{min}, c_{max}]$. If $c_{max} < 0$, too many closing brackets appeared. Floor $c_{min}$ at 0. Return True if $c_{min} == 0$ at the end.
* **Complexity**: Time: $O(n)$, Space: $O(1)$.
