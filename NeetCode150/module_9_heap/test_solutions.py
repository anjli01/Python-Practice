"""
NeetCode 150 - Module 3.3: Verification & Test Suite
Unit tests with comprehensive edge cases for all 7 Heap solutions.
"""

from solutions import (
    KthLargest,
    SolutionLastStoneWeight,
    SolutionKClosest,
    SolutionKthLargestElement,
    SolutionTaskScheduler,
    Twitter,
    MedianFinder,
)


def test_kth_largest_stream():
    kth = KthLargest(3, [4, 5, 8, 2])
    assert kth.add(3) == 4
    assert kth.add(5) == 5
    assert kth.add(10) == 5
    assert kth.add(9) == 8
    assert kth.add(4) == 8
    print("PASS: 1. Kth Largest Element in a Stream")


def test_last_stone_weight():
    sol = SolutionLastStoneWeight()
    assert sol.lastStoneWeight([2, 7, 4, 1, 8, 1]) == 1
    assert sol.lastStoneWeight([1]) == 1
    assert sol.lastStoneWeight([2, 2]) == 0
    print("PASS: 2. Last Stone Weight")


def test_k_closest():
    sol = SolutionKClosest()
    res = sol.kClosest([[1, 3], [-2, 2]], 1)
    assert res == [[-2, 2]]
    res2 = sol.kClosest([[3, 3], [5, -1], [-2, 4]], 2)
    assert sorted(res2) == sorted([[3, 3], [-2, 4]])
    print("PASS: 3. K Closest Points to Origin")


def test_kth_largest_array():
    sol = SolutionKthLargestElement()
    assert sol.findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
    assert sol.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
    assert sol.findKthLargest([1], 1) == 1
    print("PASS: 4. Kth Largest Element in an Array")


def test_task_scheduler():
    sol = SolutionTaskScheduler()
    assert sol.leastInterval(["A", "A", "A", "B", "B", "B"], 2) == 8
    assert sol.leastInterval(["A", "A", "A", "B", "B", "B"], 0) == 6
    assert sol.leastInterval(["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2) == 16
    print("PASS: 5. Task Scheduler")


def test_twitter():
    tw = Twitter()
    tw.postTweet(1, 5)
    assert tw.getNewsFeed(1) == [5]
    tw.follow(1, 2)
    tw.postTweet(2, 6)
    assert tw.getNewsFeed(1) == [6, 5]
    tw.unfollow(1, 2)
    assert tw.getNewsFeed(1) == [5]
    print("PASS: 6. Design Twitter")


def test_median_finder():
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    assert mf.findMedian() == 1.5
    mf.addNum(3)
    assert mf.findMedian() == 2.0
    mf.addNum(0)
    assert mf.findMedian() == 1.5
    mf.addNum(-1)
    assert mf.findMedian() == 1.0
    print("PASS: 7. Find Median from Data Stream")


if __name__ == "__main__":
    print("\n================ RUNNING HEAP VERIFICATION ================\n")
    test_kth_largest_stream()
    test_last_stone_weight()
    test_k_closest()
    test_kth_largest_array()
    test_task_scheduler()
    test_twitter()
    test_median_finder()
    print("\n================ ALL 7 TESTS PASSED! (100% VERIFIED) ================\n")
