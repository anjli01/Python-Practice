"""
NeetCode 150 - Module 6.1: Intervals
Detailed, fully-commented Python 3 solutions for all 6 problems.
"""

from typing import List
import heapq


# ============================================================================
# Problem 1: Insert Interval (LeetCode 57) - Medium
# Pattern: Three-Phase Linear Splice
# ============================================================================
class SolutionInsertInterval:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """Inserts newInterval into sorted non-overlapping intervals, merging if necessary."""
        result = []
        i = 0
        n = len(intervals)

        # Phase 1: Add all intervals ending before newInterval starts
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # Phase 2: Merge overlapping intervals with newInterval
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        result.append(newInterval)

        # Phase 3: Add remaining intervals
        while i < n:
            result.append(intervals[i])
            i += 1

        return result


# ============================================================================
# Problem 2: Merge Intervals (LeetCode 56) - Medium
# Pattern: Start-Sorted Overlap Merge
# ============================================================================
class SolutionMergeIntervals:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """Merges all overlapping intervals."""
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]

        for start, end in intervals[1:]:
            last_end = merged[-1][1]
            if start <= last_end:
                merged[-1][1] = max(last_end, end)
            else:
                merged.append([start, end])

        return merged


# ============================================================================
# Problem 3: Non-overlapping Intervals (LeetCode 435) - Medium
# Pattern: Greedy Earliest-Deadline Scheduling
# ============================================================================
class SolutionNonOverlappingIntervals:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """Finds minimum intervals to remove to make the rest non-overlapping."""
        intervals.sort(key=lambda x: x[0])
        removals = 0
        prev_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start < prev_end:
                # Overlap! Keep the one that finishes earliest to leave room
                removals += 1
                prev_end = min(prev_end, end)
            else:
                prev_end = end

        return removals


# ============================================================================
# Problem 4: Meeting Rooms (LeetCode 252) - Easy
# Pattern: Sort and Adjacent Overlap Check
# ============================================================================
class SolutionMeetingRooms:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        """Determines if a person could attend all meetings."""
        intervals.sort(key=lambda x: x[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:
                return False
        return True


# ============================================================================
# Problem 5: Meeting Rooms II (LeetCode 253) - Medium
# Pattern: Chronological Start/End Sweep (Two Pointers)
# ============================================================================
class SolutionMeetingRoomsII:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """Finds minimum number of conference rooms required."""
        starts = sorted([i[0] for i in intervals])
        ends = sorted([i[1] for i in intervals])

        rooms = 0
        max_rooms = 0
        s_ptr, e_ptr = 0, 0

        while s_ptr < len(intervals):
            if starts[s_ptr] < ends[e_ptr]:
                rooms += 1
                s_ptr += 1
            else:
                rooms -= 1
                e_ptr += 1
            max_rooms = max(max_rooms, rooms)

        return max_rooms


# ============================================================================
# Problem 6: Minimum Interval to Include Each Query (LeetCode 1851) - Hard
# Pattern: Offline Sorted Queries with Active Min-Heap
# ============================================================================
class SolutionMinInterval:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        """Finds the size of the smallest interval containing each query in O((n+q) log n)."""
        intervals.sort(key=lambda x: x[0])
        sorted_queries = sorted((q, idx) for idx, q in enumerate(queries))
        result = [-1] * len(queries)
        min_heap = []  # (size, end)
        i = 0
        n = len(intervals)

        for q, orig_idx in sorted_queries:
            # 1. Add all intervals starting <= q
            while i < n and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(min_heap, (r - l + 1, r))
                i += 1

            # 2. Pop expired intervals ending < q
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)

            # 3. Smallest valid interval is at top of heap
            if min_heap:
                result[orig_idx] = min_heap[0][0]

        return result
