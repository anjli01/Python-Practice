"""
NeetCode 150 - Module 6.1: Verification & Test Suite
Unit tests with comprehensive edge cases for all 6 Intervals solutions.
"""

from solutions import (
    SolutionInsertInterval,
    SolutionMergeIntervals,
    SolutionNonOverlappingIntervals,
    SolutionMeetingRooms,
    SolutionMeetingRoomsII,
    SolutionMinInterval,
)


def test_insert_interval():
    sol = SolutionInsertInterval()
    assert sol.insert([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]
    assert sol.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]) == [[1, 2], [3, 10], [12, 16]]
    assert sol.insert([], [5, 7]) == [[5, 7]]
    assert sol.insert([[1, 5]], [6, 8]) == [[1, 5], [6, 8]]
    print("PASS: 1. Insert Interval")


def test_merge_intervals():
    sol = SolutionMergeIntervals()
    assert sol.merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert sol.merge([[1, 4], [4, 5]]) == [[1, 5]]
    assert sol.merge([[1, 4]]) == [[1, 4]]
    print("PASS: 2. Merge Intervals")


def test_non_overlapping_intervals():
    sol = SolutionNonOverlappingIntervals()
    assert sol.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1
    assert sol.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]) == 2
    assert sol.eraseOverlapIntervals([[1, 2], [2, 3]]) == 0
    print("PASS: 3. Non-overlapping Intervals")


def test_meeting_rooms():
    sol = SolutionMeetingRooms()
    assert sol.canAttendMeetings([[0, 30], [5, 10], [15, 20]]) is False
    assert sol.canAttendMeetings([[7, 10], [2, 4]]) is True
    assert sol.canAttendMeetings([]) is True
    print("PASS: 4. Meeting Rooms")


def test_meeting_rooms_ii():
    sol = SolutionMeetingRoomsII()
    assert sol.minMeetingRooms([[0, 30], [5, 10], [15, 20]]) == 2
    assert sol.minMeetingRooms([[7, 10], [2, 4]]) == 1
    assert sol.minMeetingRooms([[1, 5], [5, 10]]) == 1  # end at 5, start at 5 doesn't overlap
    print("PASS: 5. Meeting Rooms II")


def test_min_interval():
    sol = SolutionMinInterval()
    assert sol.minInterval([[1, 4], [2, 4], [3, 6], [4, 4]], [2, 3, 4, 5]) == [3, 3, 1, 4]
    assert sol.minInterval([[2, 3], [2, 5], [1, 8], [20, 25]], [2, 19, 5, 22]) == [2, -1, 4, 6]
    print("PASS: 6. Minimum Interval to Include Each Query")


if __name__ == "__main__":
    print("\n================ RUNNING INTERVALS VERIFICATION ================\n")
    test_insert_interval()
    test_merge_intervals()
    test_non_overlapping_intervals()
    test_meeting_rooms()
    test_meeting_rooms_ii()
    test_min_interval()
    print("\n================ ALL 6 TESTS PASSED! (100% VERIFIED) ================\n")
