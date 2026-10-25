# Module 5.3: Greedy Algorithms – Study Guide & Pattern Deep-Dive

A **Greedy algorithm** makes the locally optimal choice at each stage with the intent of finding a global optimum. Unlike Dynamic Programming, greedy algorithms never reconsider previous choices.

---

## 1. Maximum Subarray (LeetCode 53) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/maximum-subarray/) • [NeetCode Problem](https://neetcode.io/problems/maximum-subarray) • [NeetCode Solution](https://neetcode.io/solutions/maximum-subarray) • [YouTube Video](https://www.youtube.com/watch?v=5WZl3MMT0Eg)
* **Pattern**: Kadane's Algorithm
* **Core Concept**:
  $\text{cur\_sum} = \max(n, \text{cur\_sum} + n)$. If a running sum dips below zero, it can never contribute positively to future subarrays, so reset by starting fresh from the current element. Track the global maximum across all positions.
* **Mental Model**:
  A hitchhiker deciding whether to stay on the current bus or start walking. If the bus (running sum) has gone into negative territory, it's dragging you backward — get off and start a new journey from here.
* **Tips & Interview Tricks**:
  * **Initialize Correctly**: Set `max_sum = nums[0]`, not `0` or `-inf`, to handle all-negative arrays cleanly. Alternatively, `max_sum = float('-inf')` works too.
  * **Divide-and-Conquer Follow-Up**: Interviewers may ask for an $O(n \log n)$ solution. Split the array in half; the max subarray is in the left half, the right half, or crosses the midpoint. Mention it, but Kadane's $O(n)$ is strictly better.
* **Complexity**:
  * Time: $O(n)$
  * Space: $O(1)$

---

## 2. Jump Game (LeetCode 55) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/jump-game/) • [NeetCode Problem](https://neetcode.io/problems/jump-game) • [NeetCode Solution](https://neetcode.io/solutions/jump-game) • [YouTube Video](https://www.youtube.com/watch?v=Yan0cv2cLy8)
* **Pattern**: Backward Goalpost Shift
* **Core Concept**:
  Start with `goal = len(nums) - 1`. Scan backwards: if index $i$ can reach `goal` ($i + nums[i] \ge goal$), move `goal = i`. Return `True` if `goal == 0` at the end.
* **Mental Model**:
  Working backwards from the finish line. At each position, ask: *"Can I reach the current goalpost from here?"* If yes, the goalpost moves to your position. If the goalpost reaches the starting line, the course is completable.
* **Tips & Interview Tricks**:
  * **Forward Greedy Alternative**: Track `max_reach = 0`. For each index $i \le \text{max\_reach}$: `max_reach = max(max_reach, i + nums[i])`. If `max_reach >= n - 1`, return `True`. Both approaches are $O(n)$.
  * **Why Greedy Works**: If any index along the path can reach the goal, the goal can be pulled closer. The greedy choice is provably optimal because reachability is transitive.
* **Complexity**:
  * Time: $O(n)$
  * Space: $O(1)$

---

## 3. Jump Game II (LeetCode 45) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/jump-game-ii/) • [NeetCode Problem](https://neetcode.io/problems/jump-game-ii) • [NeetCode Solution](https://neetcode.io/solutions/jump-game-ii) • [YouTube Video](https://www.youtube.com/watch?v=dJ7sWiOoK7g)
* **Pattern**: BFS Range Window Slicing
* **Core Concept**:
  Maintain the current jump range $[left, right]$. Calculate the farthest index reachable from any index within the range. Advance $left = right + 1$ and $right = farthest$, incrementing the jump count. This is effectively BFS where each "level" is a jump.
* **Mental Model**:
  A frog hopping across lily pads. Each jump lands on a range of pads. From that range, calculate the farthest pad reachable by the next jump. Count the jumps until the frog reaches the shore.
* **Tips & Interview Tricks**:
  * **BFS Analogy**: Each jump is a BFS level. The "frontier" is the range $[\text{left}, \text{right}]$. The next frontier extends to `farthest`. This perspective makes the algorithm intuitive.
  * **Don't Process the Last Index**: The loop runs `for i in range(len(nums) - 1)` — you don't need to jump FROM the last index. Including it can cause an off-by-one error.
* **Complexity**:
  * Time: $O(n)$
  * Space: $O(1)$

---

## 4. Gas Station (LeetCode 134) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/gas-station/) • [NeetCode Problem](https://neetcode.io/problems/gas-station) • [NeetCode Solution](https://neetcode.io/solutions/gas-station) • [YouTube Video](https://www.youtube.com/watch?v=lJwbPZGo05A)
* **Pattern**: Greedy Net-Gas Reset
* **Core Concept**:
  If $\sum gas < \sum cost$, completion is impossible (return $-1$). Otherwise, maintain a running `total += gas[i] - cost[i]`. Whenever `total < 0`, the starting station cannot be anywhere from the current `start` to $i$. Reset `total = 0` and set `start = i + 1`.
* **Mental Model**:
  A road trip around a circular highway. Track your fuel tank as you go. If you run out at any point, everything you've tried so far is a dead end — restart from the next station. The guarantee that a solution exists (total gas ≥ total cost) means the last restart position must work.
* **Tips & Interview Tricks**:
  * **Single-Pass Proof**: If total gas ≥ total cost, a valid starting station is guaranteed. The greedy reset finds it in one pass because: if starting from $s$ fails at $i$, then starting from any station between $s$ and $i$ also fails (they'd have even less accumulated gas).
  * **Two Checks**: (1) Global check: `sum(gas) >= sum(cost)`, (2) Local greedy: reset when tank goes negative. Both are needed.
* **Complexity**:
  * Time: $O(n)$
  * Space: $O(1)$

---

## 5. Hand of Straights (LeetCode 846) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/hand-of-straights/) • [NeetCode Problem](https://neetcode.io/problems/hand-of-straights) • [NeetCode Solution](https://neetcode.io/solutions/hand-of-straights) • [YouTube Video](https://www.youtube.com/watch?v=amnrMCVd2YI)
* **Pattern**: Min-Heap Consecutive Slicing
* **Core Concept**:
  Sort unique card values in a min-heap (or sort the array). Pop the smallest available card $c$; cards $c, c+1, \dots, c + \text{groupSize} - 1$ must all exist with sufficient frequency. Decrement their counts and repeat until all cards are grouped.
* **Mental Model**:
  Sorting a hand of playing cards and trying to form consecutive runs (like straights in poker). Always start a new run from the smallest ungrouped card. If you can't complete a run, the hand is invalid.
* **Tips & Interview Tricks**:
  * **Early Exit**: If `len(hand) % groupSize != 0`, return `False` immediately — you can't evenly divide the cards into groups.
  * **Counter + Sort**: Use `Counter(hand)` for frequency tracking and iterate through `sorted(count.keys())`. For each key, if its count > 0, try to form a group starting from that key.
  * **Equivalent Problem**: This is identical to LC 1296 "Divide Array in Sets of K Consecutive Numbers."
* **Complexity**:
  * Time: $O(N \log N)$
  * Space: $O(N)$

---

## 6. Merge Triplets to Form Target Triplet (LeetCode 1899) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/merge-triplets-to-form-target-triplet/) • [NeetCode Problem](https://neetcode.io/problems/merge-triplets-to-form-target) • [NeetCode Solution](https://neetcode.io/solutions/merge-triplets-to-form-target-triplet) • [YouTube Video](https://www.youtube.com/watch?v=kShkQLQZ9K4)
* **Pattern**: Invalid Candidate Filtering
* **Core Concept**:
  Discard any triplet having any component strictly greater than the target (it would "pollute" the max operation). For the remaining valid triplets, record which target components are achievable. If all 3 components are matched, return `True`.
* **Mental Model**:
  A hiring committee with three criteria. Each candidate (triplet) has three scores. Disqualify anyone who exceeds any target score (they'd push the max too high). Among the remaining qualified candidates, check if collectively they cover all three criteria.
* **Tips & Interview Tricks**:
  * **Why Discard Oversize?**: The `max` operation can only increase values. If any component of a triplet exceeds the target, using that triplet would make the merged result exceed the target in that dimension — permanently.
  * **Set-Based Tracking**: Use a set `good = set()`. For each valid triplet, add the indices (0, 1, 2) where it matches the target. Return `len(good) == 3`.
* **Complexity**:
  * Time: $O(N)$
  * Space: $O(1)$

---

## 7. Partition Labels (LeetCode 763) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/partition-labels/) • [NeetCode Problem](https://neetcode.io/problems/partition-labels) • [NeetCode Solution](https://neetcode.io/solutions/partition-labels) • [YouTube Video](https://www.youtube.com/watch?v=B7m8UmZE-vw)
* **Pattern**: Furthest Occurrence Slicing
* **Core Concept**:
  Store the last index where each character appears. As you iterate, expand `end = max(end, last[char])`. When $i == end$, no character in the current partition appears later in the string — cut an independent partition here.
* **Mental Model**:
  A shepherd grouping animals. Each animal type must be in exactly one pen. As you scan left to right, keep extending the current pen's boundary to include the last occurrence of every animal type you've seen. When you reach the boundary, close the pen and start a new one.
* **Tips & Interview Tricks**:
  * **Two-Pass**: Pass 1 builds `last = {char: idx}` in $O(n)$. Pass 2 scans with two pointers `start` and `end` to identify partition boundaries.
  * **Partition Size**: Record `end - start + 1` as the partition size, then set `start = end + 1` for the next partition.
* **Complexity**:
  * Time: $O(n)$
  * Space: $O(1)$ (26 characters)

---

## 8. Valid Parenthesis String (LeetCode 678) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/valid-parenthesis-string/) • [NeetCode Problem](https://neetcode.io/problems/valid-parenthesis-string) • [NeetCode Solution](https://neetcode.io/solutions/valid-parenthesis-string) • [YouTube Video](https://www.youtube.com/watch?v=QhPdNS143Qg)
* **Pattern**: Wildcard Range Interval Tracking
* **Core Concept**:
  Maintain the minimum and maximum possible number of open brackets $[c_{\min}, c_{\max}]$. `'('` increments both. `')'` decrements both. `'*'` decrements $c_{\min}$ and increments $c_{\max}$ (it could be `')'`, `'('`, or empty). If $c_{\max} < 0$, too many closing brackets appeared. Floor $c_{\min}$ at 0. Return `True` if $c_{\min} == 0$ at the end.
* **Mental Model**:
  A balance scale that can wobble within a range. `'('` tips it right, `')'` tips it left, and `'*'` is a wild card that could tip it either way. Track the full range of possible positions. If the range ever goes entirely negative, it's invalid. If zero is within the final range, it's valid.
* **Tips & Interview Tricks**:
  * **Floor $c_{\min}$ at 0**: The minimum open count can't go below 0 (you can't have negative open brackets). Clamping at 0 accounts for `'*'` being treated as empty instead of `')'`.
  * **Why Not Stack?**: A stack-based approach works but requires tracking positions of both `'('` and `'*'` in separate stacks. The range approach is $O(1)$ space and more elegant.
* **Complexity**:
  * Time: $O(n)$
  * Space: $O(1)$
