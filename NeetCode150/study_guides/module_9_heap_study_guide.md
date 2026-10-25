# Module 3.3: Heap / Priority Queue – Study Guide & Pattern Deep-Dive

A **Heap** provides $O(1)$ access to the extremal element (minimum or maximum) and $O(\log k)$ insertions/deletions. It is the premier tool for streaming top-$k$ problems, scheduling with cooldowns, and dynamic median maintenance.

---

## 1. Kth Largest Element in a Stream (LeetCode 703) - Easy
* **Quick Links**: [LeetCode](https://leetcode.com/problems/kth-largest-element-in-a-stream/) • [NeetCode Problem](https://neetcode.io/problems/kth-largest-integer-in-a-stream) • [NeetCode Solution](https://neetcode.io/solutions/kth-largest-element-in-a-stream) • [YouTube Video](https://www.youtube.com/watch?v=hOjcdrqMoQ8)
* **Pattern**: Min-Heap of Fixed Capacity $k$
* **Core Concept**:
  Maintain a min-heap with size bounded to $k$. Whenever size exceeds $k$, pop the smallest element. The root is always the $k$-th largest element seen so far, because exactly $k - 1$ elements larger than it remain in the heap.
* **Mental Model**:
  A velvet-rope VIP section that only holds $k$ guests. New arrivals must be taller than the shortest guest inside. If they are, the shortest guest is ejected and the newcomer enters. The shortest person inside is always the answer.
* **Tips & Interview Tricks**:
  * **Why Min-Heap, Not Max-Heap?**: A min-heap of size $k$ lets you access the $k$-th largest directly at the root. A max-heap would require popping $k - 1$ elements each query — $O(k \log n)$ per call instead of $O(\log k)$.
  * **Initialization**: Use `heapq.heapify(nums)` then pop until size $= k$ in `__init__` to efficiently warm up the heap.
* **Complexity**:
  * Time: $O(\log k)$ per `add`
  * Space: $O(k)$

---

## 2. Last Stone Weight (LeetCode 1046) - Easy
* **Quick Links**: [LeetCode](https://leetcode.com/problems/last-stone-weight/) • [NeetCode Problem](https://neetcode.io/problems/last-stone-weight) • [NeetCode Solution](https://neetcode.io/solutions/last-stone-weight) • [YouTube Video](https://www.youtube.com/watch?v=B-QCq79-Vfw)
* **Pattern**: Max-Heap Simulation
* **Core Concept**:
  Simulate by repeatedly popping the two heaviest stones. If they differ, push the remainder `|y - x|` back. In Python, multiply weights by $-1$ to utilize `heapq` (which is a min-heap) as a max-heap.
* **Mental Model**:
  A strongman competition. The two heaviest rocks smash together. If one survives as a fragment, it goes back into the pile. Keep smashing until at most one rock remains.
* **Tips & Interview Tricks**:
  * **Python Max-Heap Trick**: `heapq` only supports min-heaps. Negate all values on push (`heappush(h, -stone)`) and negate on pop (`-heappop(h)`) to simulate a max-heap. This is the standard Python interview pattern.
  * **Empty Heap Edge Case**: After the loop, the heap may be empty (all stones cancelled). Return `0` if empty, otherwise return `-heap[0]`.
* **Complexity**:
  * Time: $O(n \log n)$
  * Space: $O(n)$

---

## 3. K Closest Points to Origin (LeetCode 973) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/k-closest-points-to-origin/) • [NeetCode Problem](https://neetcode.io/problems/k-closest-points-to-origin) • [NeetCode Solution](https://neetcode.io/solutions/k-closest-points-to-origin) • [YouTube Video](https://www.youtube.com/watch?v=rI2EBUEMfTk)
* **Pattern**: Distance-Squared Min-Heap
* **Core Concept**:
  Push $(x^2 + y^2, [x, y])$ onto a min-heap. Pop $k$ times to retrieve the closest points. Since $\sqrt{d}$ is a monotonic function, comparing squared distances produces the same ordering as Euclidean distances — skip the square root.
* **Mental Model**:
  Throwing darts at a target. Sort all darts by how close they landed to the bullseye, then pick the $k$ closest.
* **Tips & Interview Tricks**:
  * **Skip the Square Root**: $\sqrt{a} < \sqrt{b} \iff a < b$. Computing square roots introduces floating-point imprecision and is slower. Always compare squared distances.
  * **Max-Heap Alternative**: Use a max-heap of size $k$ (negate distances). This processes in $O(n \log k)$ and uses $O(k)$ space, which is better when $k \ll n$. Mention both approaches.
* **Complexity**:
  * Time: $O(n + k \log n)$ with heapify, or $O(n \log k)$ with bounded max-heap
  * Space: $O(n)$ or $O(k)$

---

## 4. Kth Largest Element in an Array (LeetCode 215) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/kth-largest-element-in-an-array/) • [NeetCode Problem](https://neetcode.io/problems/kth-largest-element-in-an-array) • [NeetCode Solution](https://neetcode.io/solutions/kth-largest-element-in-an-array) • [YouTube Video](https://www.youtube.com/watch?v=XEmy13g1Qxc)
* **Pattern**: Bounded Min-Heap
* **Core Concept**:
  Push elements into a min-heap; whenever size exceeds $k$, pop the root. After processing all elements, the root is the $k$-th largest. The heap invariant ensures the $k$ largest elements always remain.
* **Mental Model**:
  A leaderboard with only $k$ slots. As contestants report scores, anyone who beats the current lowest-ranked player replaces them. After everyone has reported, the lowest-ranked player on the board is the $k$-th best.
* **Tips & Interview Tricks**:
  * **Quickselect Follow-Up**: Interviewers often ask for $O(n)$ average time. Quickselect (partition-based selection) achieves this but has $O(n^2)$ worst case. The heap approach guarantees $O(n \log k)$ worst case. Know both.
  * **Heap vs. Sort**: Sorting gives $O(n \log n)$. The heap approach is $O(n \log k)$, which is strictly better when $k \ll n$.
* **Complexity**:
  * Time: $O(n \log k)$
  * Space: $O(k)$

---

## 5. Task Scheduler (LeetCode 621) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/task-scheduler/) • [NeetCode Problem](https://neetcode.io/problems/task-scheduling) • [NeetCode Solution](https://neetcode.io/solutions/task-scheduler) • [YouTube Video](https://www.youtube.com/watch?v=s8p8ukTyA2I)
* **Pattern**: Greedy Task-Skeleton Formula
* **Core Concept**:
  The task with maximum frequency $M$ creates $M - 1$ chunks of size $(n + 1)$.
  $$\text{Intervals} = \max(\text{len}(tasks),\ (M - 1) \cdot (n + 1) + \text{count\_of\_max\_f\_tasks})$$
  If many distinct tasks exist, they fill idle slots and the answer is simply `len(tasks)`.
* **Mental Model**:
  Arranging seats at a banquet with spacing rules. The most frequent guest defines the table layout (number of rounds). Other guests fill in the empty seats. If there are enough diverse guests, no idle seats remain.
* **Tips & Interview Tricks**:
  * **Formula vs. Simulation**: The formula approach is $O(n)$ and elegant. The simulation approach (max-heap + cooldown queue) is more intuitive but $O(n \log 26)$. Interviewers appreciate seeing the formula derivation.
  * **Why `max(len(tasks), ...)`?**: When tasks are diverse enough, the cooldown constraint is never triggered and the answer is just the total number of tasks.
* **Complexity**:
  * Time: $O(\text{len}(tasks))$
  * Space: $O(1)$ (at most 26 task types)

---

## 6. Design Twitter (LeetCode 355) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/design-twitter/) • [NeetCode Problem](https://neetcode.io/problems/design-twitter-feed) • [NeetCode Solution](https://neetcode.io/solutions/design-twitter) • [YouTube Video](https://www.youtube.com/watch?v=pNichitDD2E)
* **Pattern**: K-Way Merge of Recent Posts using Max-Heap
* **Core Concept**:
  Store posts chronologically per user with a global timestamp counter. In `getNewsFeed`, push the latest post from each followed user (plus self) into a max-heap keyed by timestamp. Iteratively extract up to 10 most recent tweets, pushing each user's next-latest post after extraction.
* **Mental Model**:
  A personal newspaper editor compiling your morning digest. They check the latest headline from each journalist you follow, pick the most recent one, then check that journalist's second-most-recent, and so on until they have 10 stories.
* **Tips & Interview Tricks**:
  * **Global Timestamp**: Use a monotonically increasing counter (`self.count -= 1` for max-heap in Python) as the primary sort key. Do not use actual wall-clock time.
  * **Follow Self**: A user should always see their own tweets. Either explicitly add `self` to the follow set or handle it as a special case in `getNewsFeed`.
  * **Data Structure Choice**: Use `defaultdict(list)` for tweets and `defaultdict(set)` for follows to keep the implementation clean.
* **Complexity**:
  * Time: $O(k \log U)$ for `getNewsFeed` where $U$ is number of followees, $k \le 10$
  * Space: $O(N)$ total tweets stored

---

## 7. Find Median from Data Stream (LeetCode 295) - Hard
* **Quick Links**: [LeetCode](https://leetcode.com/problems/find-median-from-data-stream/) • [NeetCode Problem](https://neetcode.io/problems/find-median-in-a-data-stream) • [NeetCode Solution](https://neetcode.io/solutions/find-median-from-data-stream) • [YouTube Video](https://www.youtube.com/watch?v=itmhHWaHupI)
* **Pattern**: Dual-Heap Balancing
* **Core Concept**:
  * `small`: Max-heap holding the lower half of numbers.
  * `large`: Min-heap holding the upper half of numbers.
  * Maintain balance: $\text{len}(small) = \text{len}(large)$ or $\text{len}(small) = \text{len}(large) + 1$, and $\max(small) \le \min(large)$.
  The median is either the top of `small` or the average of both tops.
* **Mental Model**:
  Two buckets on a balance scale. The left bucket (max-heap) holds smaller numbers; the right bucket (min-heap) holds larger numbers. Keep the buckets roughly equal in size. The median is always visible at the top of each bucket.
* **Tips & Interview Tricks**:
  * **Rebalancing Protocol**: Always push to `small` first, then rebalance. If `small`'s max exceeds `large`'s min, move the max from `small` to `large`. If sizes differ by more than 1, move from the larger heap to the smaller.
  * **Python Negation**: Since `heapq` is a min-heap, negate values for the max-heap (`small`). The median from `small` is `-small[0]`.
  * **Follow-Up (Sorted Stream)**: If data arrives sorted, the heaps degenerate. Mention that a self-balancing BST (e.g., `SortedList` from `sortedcontainers`) handles this in $O(\log n)$ as well.
* **Complexity**:
  * Time: $O(\log n)$ for `addNum`, $O(1)$ for `findMedian`
  * Space: $O(n)$
