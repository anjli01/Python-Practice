# Module 6.1: Intervals – Study Guide & Pattern Deep-Dive

Interval problems center on **merging overlapping segments, detecting temporal conflicts, and coordinate-line sweeping**.

---

## 1. Insert Interval (LeetCode 57) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/insert-interval/) • [NeetCode Problem](https://neetcode.io/problems/insert-new-interval) • [NeetCode Solution](https://neetcode.io/solutions/insert-interval) • [YouTube Video](https://www.youtube.com/watch?v=A8NUOmlwOlM)
* **Pattern**: Three-Phase Linear Splice
* **Core Concept**:
  1. Append all intervals ending before `newInterval` starts (`interval[1] < newInterval[0]`).
  2. Merge all overlapping intervals: $\text{newInterval} = [\min(\text{starts}), \max(\text{ends})]$.
  3. Append all intervals starting after `newInterval` ends.
  This three-phase approach handles all overlap cases cleanly in a single linear scan.
* **Mental Model**:
  Inserting a new appointment into a sorted calendar. First, copy all earlier non-conflicting appointments. Then, merge any overlapping ones into a single block. Finally, copy all later non-conflicting appointments.
* **Tips & Interview Tricks**:
  * **No Sort Needed**: The input is already sorted. Don't waste time re-sorting — it's $O(n \log n)$ when $O(n)$ is achievable.
  * **Overlap Condition**: Two intervals overlap when `interval[0] <= newInterval[1]` (the existing interval starts before the new one ends). This is the merge condition for phase 2.
* **Complexity**:
  * Time: $O(n)$
  * Space: $O(n)$ output

---

## 2. Merge Intervals (LeetCode 56) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/merge-intervals/) • [NeetCode Problem](https://neetcode.io/problems/merge-intervals) • [NeetCode Solution](https://neetcode.io/solutions/merge-intervals) • [YouTube Video](https://www.youtube.com/watch?v=44H3cEC2fFM)
* **Pattern**: Start-Sorted Sweep
* **Core Concept**:
  Sort intervals by start time. If `curr.start <= prev.end`, merge by updating `prev.end = max(prev.end, curr.end)`. Otherwise, the current interval is disjoint — append it as a distinct interval and it becomes the new `prev`.
* **Mental Model**:
  Stacking overlapping sticky notes on a timeline. Sort them by left edge. If the next note overlaps the current stack, extend the stack's right edge. If it doesn't overlap, start a new stack.
* **Tips & Interview Tricks**:
  * **Sort by Start is Sufficient**: Sorting by start time alone is enough. If two intervals have the same start, the merge logic handles them regardless of end-time order.
  * **In-Place vs. New Array**: Building a new `merged` list is cleaner than modifying the input. Append `intervals[0]` first, then iterate from index 1.
* **Complexity**:
  * Time: $O(n \log n)$
  * Space: $O(n)$

---

## 3. Non-overlapping Intervals (LeetCode 435) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/non-overlapping-intervals/) • [NeetCode Problem](https://neetcode.io/problems/non-overlapping-intervals) • [NeetCode Solution](https://neetcode.io/solutions/non-overlapping-intervals) • [YouTube Video](https://www.youtube.com/watch?v=nONCGxWoUfM)
* **Pattern**: Greedy Earliest-Finish Scheduling
* **Core Concept**:
  Sort by start time. When two intervals overlap, greedily keep the interval with the **smaller end time** (`prev_end = min(prev_end, end)`) to maximize space for future intervals. Increment removal count for the discarded interval.
* **Mental Model**:
  A conference room scheduler. When two meetings conflict, cancel the one that runs later — it blocks more future meetings. Always keep the meeting that ends earliest.
* **Tips & Interview Tricks**:
  * **Classic Activity Selection**: This is the textbook "Activity Selection Problem." Sort by end time and greedily select non-overlapping activities. The removal count is $n - \text{selected}$.
  * **Sort by End vs. Start**: Sorting by end time and greedily selecting is the classic approach. Sorting by start time and greedily removing the longer interval also works. Both are $O(n \log n)$.
* **Complexity**:
  * Time: $O(n \log n)$
  * Space: $O(1)$

---

## 4. Meeting Rooms (LeetCode 252) - Easy
* **Quick Links**: [LeetCode](https://leetcode.com/problems/meeting-rooms/) • [NeetCode Problem](https://neetcode.io/problems/meeting-schedule) • [NeetCode Solution](https://neetcode.io/solutions/meeting-rooms) • [YouTube Video](https://www.youtube.com/watch?v=PaJxqZVPhbg)
* **Pattern**: Sequential Overlap Check
* **Core Concept**:
  Sort by start time. Return `False` if any `intervals[i].start < intervals[i-1].end`. If no overlaps exist, a person can attend all meetings.
* **Mental Model**:
  Checking if your day planner has any double-bookings. Sort appointments by start time and verify each one begins after the previous one ends.
* **Tips & Interview Tricks**:
  * **Strict vs. Non-Strict**: The overlap condition is `start < prev_end` (strict less-than). If a meeting starts exactly when another ends (`start == prev_end`), there's no conflict — the person can walk between rooms.
  * **Building Block**: This is the prerequisite for Meeting Rooms II. If asked LC 252, expect LC 253 as a follow-up.
* **Complexity**:
  * Time: $O(n \log n)$
  * Space: $O(1)$

---

## 5. Meeting Rooms II (LeetCode 253) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/meeting-rooms-ii/) • [NeetCode Problem](https://neetcode.io/problems/meeting-schedule-ii) • [NeetCode Solution](https://neetcode.io/solutions/meeting-rooms-ii) • [YouTube Video](https://www.youtube.com/watch?v=FdzJmTCVyJU)
* **Pattern**: Chronological Event Sweep (Two Pointers)
* **Core Concept**:
  Extract and sort `starts` and `ends` arrays independently. Advance through start times: if `starts[s] < ends[e]`, a new room must open (increment count, advance `s`). Otherwise, a meeting ended and a room freed up (`e += 1`, advance `s`). Track the maximum concurrent rooms.
* **Mental Model**:
  A building manager watching people enter and leave. Sort all entry times and exit times separately. Walk through both timelines with two fingers. Each entry before the next exit means you need another room.
* **Tips & Interview Tricks**:
  * **Min-Heap Alternative**: Push end times onto a min-heap. For each meeting, if `heap[0] <= start`, pop (room freed). Always push the new end time. Heap size is the room count. Both approaches are $O(n \log n)$.
  * **Why Sort Independently?**: Sorting starts and ends separately works because we only care about *how many* meetings overlap, not *which* meetings overlap. The pairing between start and end doesn't matter.
* **Complexity**:
  * Time: $O(n \log n)$
  * Space: $O(n)$

---

## 6. Minimum Interval to Include Each Query (LeetCode 1851) - Hard
* **Quick Links**: [LeetCode](https://leetcode.com/problems/minimum-interval-to-include-each-query/) • [NeetCode Problem](https://neetcode.io/problems/minimum-interval-including-query) • [NeetCode Solution](https://neetcode.io/solutions/minimum-interval-to-include-each-query) • [YouTube Video](https://www.youtube.com/watch?v=5hQ5WWW5awQ)
* **Pattern**: Offline Sorted Queries + Min-Heap
* **Core Concept**:
  Sort queries while remembering original indices. Sort intervals by start.
  For each query (in sorted order):
  1. Add intervals with $\text{start} \le \text{query}$ into a min-heap ordered by $(\text{size}, \text{end})$.
  2. Pop expired intervals where $\text{end} < \text{query}$.
  3. The heap root is the minimum covering interval.
* **Mental Model**:
  A librarian answering questions about which shelf range covers each book's location. Process questions in order of book location. As you walk along the shelf, add all ranges that start before your position and remove ranges that have already ended. The smallest active range is the answer.
* **Tips & Interview Tricks**:
  * **Offline Processing**: "Offline" means you can reorder queries for efficiency. Sort queries by value, process them, then map answers back to original indices using a dictionary.
  * **Lazy Deletion**: Don't remove expired intervals proactively. Instead, when peeking at the heap root, pop entries where `end < query` — they're stale.
  * **Interval Size**: Size = $\text{end} - \text{start} + 1$. Use this as the heap key to find the minimum-size covering interval.
* **Complexity**:
  * Time: $O((N + Q) \log N)$
  * Space: $O(N + Q)$
