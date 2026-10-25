# Module 6.1: Intervals – Study Guide & Pattern Deep-Dive

Interval problems center on **merging overlapping segments, detecting temporal conflicts, and coordinate-line sweeping**.

---

## 1. Insert Interval (LeetCode 57) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/insert-interval/) • [NeetCode Problem](https://neetcode.io/problems/insert-new-interval) • [NeetCode Solution](https://neetcode.io/solutions/insert-interval) • [YouTube Video](https://www.youtube.com/watch?v=A8NUOmlwOlM)
* **Pattern**: Three-Phase Linear Splice
* **Core Concept**:
  1. Append all intervals ending before `newInterval` starts.
  2. Merge all overlapping intervals: $\text{newInterval} = [\min(start_i), \max(end_i)]$.
  3. Append all intervals starting after `newInterval` ends.
* **Complexity**: Time: $O(n)$, Space: $O(n)$ output.

---

## 2. Merge Intervals (LeetCode 56) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/merge-intervals/) • [NeetCode Problem](https://neetcode.io/problems/merge-intervals) • [NeetCode Solution](https://neetcode.io/solutions/merge-intervals) • [YouTube Video](https://www.youtube.com/watch?v=44H3cEC2fFM)
* **Pattern**: Start-Sorted Sweep
* **Core Concept**:
  Sort intervals by start time. If `curr.start <= prev.end`, merge by updating `prev.end = max(prev.end, curr.end)`. Otherwise, append as a distinct interval.
* **Complexity**: Time: $O(n \log n)$, Space: $O(n)$.

---

## 3. Non-overlapping Intervals (LeetCode 435) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/non-overlapping-intervals/) • [NeetCode Problem](https://neetcode.io/problems/non-overlapping-intervals) • [NeetCode Solution](https://neetcode.io/solutions/non-overlapping-intervals) • [YouTube Video](https://www.youtube.com/watch?v=nONCGxWoUfM)
* **Pattern**: Greedy Earliest-Finish Scheduling
* **Core Concept**:
  When two intervals overlap, greedily keep the interval with the **smaller end time** (`prev_end = min(prev_end, end)`) to maximize space for future intervals. Increment removal count.
* **Complexity**: Time: $O(n \log n)$, Space: $O(1)$.

---

## 4. Meeting Rooms (LeetCode 252) - Easy
* **Quick Links**: [LeetCode](https://leetcode.com/problems/meeting-rooms/) • [NeetCode Problem](https://neetcode.io/problems/meeting-schedule) • [NeetCode Solution](https://neetcode.io/solutions/meeting-rooms) • [YouTube Video](https://www.youtube.com/watch?v=PaJxqZVPhbg)
* **Pattern**: Sequential Overlap Check
* **Core Concept**: Sort by start time. Return False if any `intervals[i].start < intervals[i-1].end`.
* **Complexity**: Time: $O(n \log n)$, Space: $O(1)$.

---

## 5. Meeting Rooms II (LeetCode 253) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/meeting-rooms-ii/) • [NeetCode Problem](https://neetcode.io/problems/meeting-schedule-ii) • [NeetCode Solution](https://neetcode.io/solutions/meeting-rooms-ii) • [YouTube Video](https://www.youtube.com/watch?v=FdzJmTCVyJU)
* **Pattern**: Chronological Event Sweep (Two Pointers)
* **Core Concept**:
  Extract and sort `starts` and `ends` arrays independently. Advance through start times: if `starts[s] < ends[e]`, a new room must open. Otherwise, a meeting ended and a room freed up (`e += 1`).
* **Complexity**: Time: $O(n \log n)$, Space: $O(n)$.

---

## 6. Minimum Interval to Include Each Query (LeetCode 1851) - Hard
* **Quick Links**: [LeetCode](https://leetcode.com/problems/minimum-interval-to-include-each-query/) • [NeetCode Problem](https://neetcode.io/problems/minimum-interval-including-query) • [NeetCode Solution](https://neetcode.io/solutions/minimum-interval-to-include-each-query) • [YouTube Video](https://www.youtube.com/watch?v=5hQ5WWW5awQ)
* **Pattern**: Offline Sorted Queries + Min-Heap
* **Core Concept**:
  Sort queries while remembering original indices. Sort intervals by start.
  For each query:
  1. Add intervals with $start \le query$ into a min-heap ordered by $(size, end)$.
  2. Pop expired intervals where $end < query$.
  3. The heap root is the minimum covering interval.
* **Complexity**: Time: $O((N + Q) \log N)$, Space: $O(N + Q)$.
