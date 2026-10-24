"""
NeetCode 150 - Module 3.3: Heap / Priority Queue
Detailed, fully-commented Python 3 solutions for all 7 problems.
"""

from typing import List
import heapq
from collections import Counter, defaultdict, deque


# ============================================================================
# Problem 1: Kth Largest Element in a Stream (LeetCode 703) - Easy
# Pattern: Min-Heap of Fixed Capacity k
# ============================================================================
class KthLargest:
    """Maintains the kth largest element in a dynamic stream in O(log k) per add."""
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = nums
        heapq.heapify(self.min_heap)
        # Prune until size is at most k
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]


# ============================================================================
# Problem 2: Last Stone Weight (LeetCode 1046) - Easy
# Pattern: Max-Heap Simulation
# ============================================================================
class SolutionLastStoneWeight:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """Simulates stone smashing by repeatedly extracting the two heaviest stones."""
        # Python heapq is a min-heap; negate weights to simulate max-heap
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            first = -heapq.heappop(max_heap)
            second = -heapq.heappop(max_heap)
            if first != second:
                heapq.heappush(max_heap, -(first - second))

        return -max_heap[0] if max_heap else 0


# ============================================================================
# Problem 3: K Closest Points to Origin (LeetCode 973) - Medium
# Pattern: Heapified Distance Tuples
# ============================================================================
class SolutionKClosest:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """Returns the k closest points to (0, 0) in O(n + k log n) time."""
        # Min-heap of tuples: (dist_squared, point)
        min_heap = [(x * x + y * y, [x, y]) for x, y in points]
        heapq.heapify(min_heap)

        result = []
        for _ in range(k):
            dist, pt = heapq.heappop(min_heap)
            result.append(pt)

        return result


# ============================================================================
# Problem 4: Kth Largest Element in an Array (LeetCode 215) - Medium
# Pattern: Min-Heap of Size k or QuickSelect
# ============================================================================
class SolutionKthLargestElement:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """Finds the kth largest element in nums in O(n log k) time and O(k) space."""
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return min_heap[0]


# ============================================================================
# Problem 5: Task Scheduler (LeetCode 621) - Medium
# Pattern: Greedy Formula / Max-Frequency Frame
# ============================================================================
class SolutionTaskScheduler:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        Calculates the least number of CPU intervals to finish all tasks with cooldown n.
        
        Concept / Pattern:
        - The most frequent task determines the minimum schedule skeleton:
          `idle_slots = (max_f - 1) * (n + 1) + count_of_max_f_tasks`.
        - If tasks outnumber the frame, total time is simply len(tasks).
        
        Complexity:
        - Time: O(len(tasks)) - Single pass counting.
        - Space: O(1) - At most 26 task frequencies.
        """
        counts = Counter(tasks)
        max_f = max(counts.values())
        max_f_count = sum(1 for f in counts.values() if f == max_f)

        return max(len(tasks), (max_f - 1) * (n + 1) + max_f_count)


# ============================================================================
# Problem 6: Design Twitter (LeetCode 355) - Medium
# Pattern: K-Way Merge of Recent Posts using Max-Heap
# ============================================================================
class Twitter:
    """Simplified Twitter service supporting tweet posting and 10-most-recent feed."""
    def __init__(self):
        self.time = 0
        self.tweet_map = defaultdict(list)    # userId -> list of (time, tweetId)
        self.follow_map = defaultdict(set)   # userId -> set of followees

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweet_map[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        min_heap = []

        # User sees their own tweets and their followees' tweets
        users = set(self.follow_map[userId])
        users.add(userId)

        # Push the most recent tweet from each followed user
        for u in users:
            if u in self.tweet_map and self.tweet_map[u]:
                idx = len(self.tweet_map[u]) - 1
                t, tweet_id = self.tweet_map[u][idx]
                heapq.heappush(min_heap, (-t, tweet_id, u, idx - 1))

        # Extract top 10 most recent tweets
        while min_heap and len(res) < 10:
            neg_time, tweet_id, u, next_idx = heapq.heappop(min_heap)
            res.append(tweet_id)
            if next_idx >= 0:
                prev_t, prev_id = self.tweet_map[u][next_idx]
                heapq.heappush(min_heap, (-prev_t, prev_id, u, next_idx - 1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].discard(followeeId)


# ============================================================================
# Problem 7: Find Median from Data Stream (LeetCode 295) - Hard
# Pattern: Dual-Heap Balancing (Max-Heap Small, Min-Heap Large)
# ============================================================================
class MedianFinder:
    """Finds the median from a continuous stream in O(log n) add and O(1) find."""
    def __init__(self):
        # small: max-heap (negated) stores lower half
        # large: min-heap stores upper half
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        # Step 1: Add to small (max-heap)
        heapq.heappush(self.small, -num)

        # Invariant 1: Every element in small <= every element in large
        if self.small and self.large and (-self.small[0]) > self.large[0]:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Invariant 2: Balance sizes (small size can exceed large by at most 1)
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0
