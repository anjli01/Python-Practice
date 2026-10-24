"""
NeetCode 150 - Module 2.1: Binary Search
Detailed, fully-commented Python 3 solutions for all 7 problems.
"""

from typing import List
from collections import defaultdict
import math


# ============================================================================
# Problem 1: Binary Search (LeetCode 704) - Easy
# Pattern: Standard Logarithmic Divide-and-Conquer
# ============================================================================
class SolutionBinarySearch:
    def search(self, nums: List[int], target: int) -> int:
        """
        Searches for target in a sorted array in O(log n) time.
        
        Concept / Pattern:
        - Divide and Conquer: Halve the search space each step.
        - Midpoint Calculation: `mid = left + (right - left) // 2` prevents integer overflow.
        
        Complexity:
        - Time: O(log n) - Search space is halved every iteration.
        - Space: O(1) - Iterative pointers.
        """
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return -1


# ============================================================================
# Problem 2: Search a 2D Matrix (LeetCode 74) - Medium
# Pattern: Virtual 1D Array Mapping
# ============================================================================
class SolutionSearch2DMatrix:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Searches for target in an m x n matrix where rows and columns are sorted.
        
        Concept / Pattern:
        - Virtual 1D Array: An m x n matrix can be viewed as a 1D sorted array of length m * n.
        - Coordinate Mapping: For any virtual 1D index `mid`:
          - `row = mid // n`
          - `col = mid % n`
        
        Complexity:
        - Time: O(log(m * n)) - Single binary search across all cells.
        - Space: O(1) - Constant auxiliary memory.
        """
        if not matrix or not matrix[0]:
            return False
            
        m, n = len(matrix), len(matrix[0])
        left, right = 0, (m * n) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            mid_val = matrix[mid // n][mid % n]
            
            if mid_val == target:
                return True
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return False


# ============================================================================
# Problem 3: Koko Eating Bananas (LeetCode 875) - Medium
# Pattern: Binary Search on the Answer Space (Monotonic Predicate)
# ============================================================================
class SolutionKokoEatingBananas:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Finds the minimum integer eating speed k to eat all bananas within h hours.
        
        Concept / Pattern:
        - Monotonic Feasibility:
          If speed k is fast enough, any speed > k is also fast enough.
          If speed k is too slow, any speed < k is also too slow.
        - Search Space: k ranges from 1 to max(piles).
        - Predicate function: hours_needed(k) = sum(ceil(pile / k)) <= h.
        
        Complexity:
        - Time: O(n * log(max(piles))) - O(n) feasibility check per binary search step.
        - Space: O(1) - Constant auxiliary memory.
        """
        left, right = 1, max(piles)
        best_speed = right
        
        while left <= right:
            mid_speed = left + (right - left) // 2
            
            # Calculate total hours needed at speed mid_speed
            hours_spent = sum(math.ceil(pile / mid_speed) for pile in piles)
            
            if hours_spent <= h:
                # Speed is feasible! Record and try finding a slower valid speed
                best_speed = mid_speed
                right = mid_speed - 1
            else:
                # Too slow, must speed up
                left = mid_speed + 1
                
        return best_speed


# ============================================================================
# Problem 4: Find Minimum in Rotated Sorted Array (LeetCode 153) - Medium
# Pattern: Rotated Pivot Detection
# ============================================================================
class SolutionFindMinRotatedSortedArray:
    def findMin(self, nums: List[int]) -> int:
        """
        Finds the minimum element in a rotated sorted array in O(log n).
        
        Concept / Pattern:
        - Compare mid with the right boundary:
          - If `nums[mid] > nums[right]`: The inflection point (minimum) MUST lie strictly
            to the right of mid (`left = mid + 1`).
          - If `nums[mid] <= nums[right]`: The right half is properly sorted, so the minimum
            is at mid or to the left (`right = mid`).
        - Terminate when left == right.
        
        Complexity:
        - Time: O(log n) - Halves the search space each step.
        - Space: O(1) - Constant auxiliary memory.
        """
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
                
        return nums[left]


# ============================================================================
# Problem 5: Search in Rotated Sorted Array (LeetCode 33) - Medium
# Pattern: Halved Sorted-Subarray Invariant
# ============================================================================
class SolutionSearchRotatedSortedArray:
    def search(self, nums: List[int], target: int) -> int:
        """
        Searches for target in a rotated sorted array in O(log n) time.
        
        Concept / Pattern:
        - Fundamental Invariant: In any rotated sorted array, splitting at `mid`
          guarantees that AT LEAST ONE half is strictly sorted!
          1. If `nums[left] <= nums[mid]`: The LEFT half is sorted.
             - Check if target lies within `[nums[left], nums[mid]]`.
          2. Otherwise: The RIGHT half is sorted.
             - Check if target lies within `[nums[mid], nums[right]]`.
        
        Complexity:
        - Time: O(log n) - Logarithmic search.
        - Space: O(1) - Constant auxiliary space.
        """
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
                
            # Case 1: Left half is strictly sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Case 2: Right half is strictly sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
                    
        return -1


# ============================================================================
# Problem 6: Time Based Key-Value Store (LeetCode 981) - Medium
# Pattern: Hash Map of Sorted Arrays with Timestamp Binary Search
# ============================================================================
class TimeMap:
    """
    Key-value store that stores multiple values for the same key at different timestamps
    and retrieves the key's value at a certain timestamp in O(log n).
    
    Concept / Pattern:
    - `set` appends strictly increasing timestamps, so values for any key are naturally sorted.
    - `get` performs binary search on the timestamp array to find the largest timestamp <= query.
    """
    def __init__(self):
        # key -> list of (timestamp, value)
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.store.get(key, [])
        left, right = 0, len(values) - 1
        res = ""
        
        # Binary search for rightmost timestamp <= query timestamp
        while left <= right:
            mid = left + (right - left) // 2
            if values[mid][0] <= timestamp:
                res = values[mid][1]
                left = mid + 1
            else:
                right = mid - 1
                
        return res


# ============================================================================
# Problem 7: Median of Two Sorted Arrays (LeetCode 4) - Hard
# Pattern: Binary Search on Partition of Smaller Array
# ============================================================================
class SolutionMedianOfTwoSortedArrays:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Finds the median of two sorted arrays in O(log(min(m, n))) time.
        
        Concept / Pattern:
        - Ensure nums1 is the smaller array (if not, swap).
        - Partition nums1 and nums2 such that:
          1. Left partition has (total_len + 1) // 2 elements.
          2. All elements in left partition are <= all elements in right partition:
             - A_left <= B_right
             - B_left <= A_right
        - Binary search on the cut index of the smaller array.
        
        Complexity:
        - Time: O(log(min(m, n))) - Binary search on smaller array.
        - Space: O(1) - Constant auxiliary memory.
        """
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A
            
        total = len(A) + len(B)
        half = (total + 1) // 2
        
        left, right = 0, len(A)
        
        while left <= right:
            i = (left + right) // 2  # Partition cut in A
            j = half - i             # Partition cut in B
            
            # Boundary values with infinity guards
            A_left = A[i - 1] if i > 0 else float('-inf')
            A_right = A[i] if i < len(A) else float('inf')
            B_left = B[j - 1] if j > 0 else float('-inf')
            B_right = B[j] if j < len(B) else float('inf')
            
            # Valid partition found!
            if A_left <= B_right and B_left <= A_right:
                # Odd total length: max of left side
                if total % 2 != 0:
                    return float(max(A_left, B_left))
                # Even total length: average of middle two
                return (max(A_left, B_left) + min(A_right, B_right)) / 2.0
            elif A_left > B_right:
                # Too many elements from A, move cut left
                right = i - 1
            else:
                # Too few elements from A, move cut right
                left = i + 1
                
        return 0.0
