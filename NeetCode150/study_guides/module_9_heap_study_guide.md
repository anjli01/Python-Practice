# Module 3.3: Heap / Priority Queue – Study Guide & Pattern Deep-Dive

A **Heap** provides $O(1)$ access to the extremal element (minimum or maximum) and $O(\log k)$ insertions/deletions. It is the premier tool for streaming top-$k$ problems, scheduling with cooldowns, and dynamic median maintenance.

---

## 1. Kth Largest Element in a Stream (LeetCode 703) - Easy
* **Pattern**: Min-Heap of Fixed Capacity $k$
* **Core Concept**:
  Maintain a min-heap with size bounded to $k$. The root is always the $k$-th largest element seen so far.
* **Complexity**: Time: $O(\log k)$ per `add`, Space: $O(k)$.

---

## 2. Last Stone Weight (LeetCode 1046) - Easy
* **Pattern**: Max-Heap Simulation
* **Core Concept**:
  Simulate by repeatedly popping the two heaviest stones. In Python, multiply weights by $-1$ to utilize `heapq` as a max-heap.
* **Complexity**: Time: $O(n \log n)$, Space: $O(n)$.

---

## 3. K Closest Points to Origin (LeetCode 973) - Medium
* **Pattern**: Distance-Squared Min-Heap
* **Core Concept**:
  Push $(x^2 + y^2, [x, y])$ onto a min-heap. Pop $k$ times to retrieve the closest points in $O(n + k \log n)$ time.
* **Complexity**: Time: $O(n + k \log n)$, Space: $O(n)$.

---

## 4. Kth Largest Element in an Array (LeetCode 215) - Medium
* **Pattern**: Bounded Min-Heap
* **Core Concept**: Push elements into a min-heap; whenever size exceeds $k$, pop the root. At the end, the root is the $k$-th largest.
* **Complexity**: Time: $O(n \log k)$, Space: $O(k)$.

---

## 5. Task Scheduler (LeetCode 621) - Medium
* **Pattern**: Greedy Task-Skeleton Formula
* **Core Concept**:
  The task with maximum frequency $M$ creates $M - 1$ chunks of size $(n + 1)$.
  $$\text{Intervals} = \max(\text{len}(tasks), (M - 1) \cdot (n + 1) + \text{count\_of\_max\_f\_tasks})$$
* **Complexity**: Time: $O(\text{len}(tasks))$, Space: $O(1)$.

---

## 6. Design Twitter (LeetCode 355) - Medium
* **Pattern**: K-Way Merge of Recent Posts using Max-Heap
* **Core Concept**:
  Store posts chronologically per user. In `getNewsFeed`, push the latest post from each followed user into a max-heap, and iteratively extract up to 10 most recent tweets.
* **Complexity**: Time: $O(k \log U)$ where $U$ is number of followees, Space: $O(N)$ total tweets.

---

## 7. Find Median from Data Stream (LeetCode 295) - Hard
* **Pattern**: Dual-Heap Balancing
* **Core Concept**:
  * `small`: Max-heap holding lower half of numbers.
  * `large`: Min-heap holding upper half of numbers.
  * Maintain balance: $\text{len}(small) = \text{len}(large)$ or $\text{len}(small) = \text{len}(large) + 1$, and $\max(small) \le \min(large)$.
* **Complexity**: Time: $O(\log n)$ for `addNum`, $O(1)$ for `findMedian`. Space: $O(n)$.
