"""
NeetCode 150 - Module 1.2: Two Pointers
Detailed, fully-commented Python 3 solutions for all 5 problems.
"""

from typing import List


# ============================================================================
# Problem 1: Valid Palindrome (LeetCode 125) - Easy
# Pattern: Inward-Converging Pointers / In-Place Filtering
# ============================================================================
class SolutionValidPalindrome:
    def isPalindrome(self, s: str) -> bool:
        """
        Determines if a string is a palindrome considering only alphanumeric characters
        and ignoring case, using O(1) auxiliary space.
        
        Concept / Pattern:
        - Two Pointers: Left pointer at index 0, right pointer at index len(s) - 1.
        - In-place skip: Move pointers inward past non-alphanumeric characters without
          allocating a new filtered copy of the string.
        
        Complexity:
        - Time: O(n) - Each character is examined at most twice.
        - Space: O(1) - Modifies no memory, allocates no new strings.
        """
        left, right = 0, len(s) - 1
        
        while left < right:
            # Skip non-alphanumeric characters on the left
            while left < right and not s[left].isalnum():
                left += 1
                
            # Skip non-alphanumeric characters on the right
            while left < right and not s[right].isalnum():
                right -= 1
                
            # Compare characters case-insensitively
            if s[left].lower() != s[right].lower():
                return False
                
            left += 1
            right -= 1
            
        return True


# ============================================================================
# Problem 2: Two Sum II - Input Array Is Sorted (LeetCode 167) - Medium
# Pattern: Inward Squeeze via Sorted Monotonicity
# ============================================================================
class SolutionTwoSumII:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Finds two numbers such that they add up to target in a 1-indexed sorted array.
        
        Concept / Pattern:
        - Monotonic Squeeze:
          - If numbers[left] + numbers[right] > target, the sum is too large.
            Because numbers is sorted, the only way to reduce the sum is to decrement right.
          - If numbers[left] + numbers[right] < target, increment left.
          - If equal, we found our unique solution.
        
        Complexity:
        - Time: O(n) - Pointers meet after at most n steps.
        - Space: O(1) - Constant auxiliary memory (unlike Hash Map which takes O(n)).
        """
        left, right = 0, len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                # Problem requires 1-based indexing
                return [left + 1, right + 1]
            elif current_sum > target:
                right -= 1
            else:
                left += 1
                
        return []


# ============================================================================
# Problem 3: 3Sum (LeetCode 15) - Medium
# Pattern: Sort + Fixed Anchor + Two-Pointer Squeeze (with Duplicate Pruning)
# ============================================================================
class Solution3Sum:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Finds all unique triplets [nums[i], nums[j], nums[k]] that sum to 0.
        
        Concept / Pattern:
        - Sort the array first: Sorting takes O(n log n) and enables:
          1. Two-pointer search for the remaining two elements in O(n).
          2. Easy skipping of duplicate values adjacent to each other.
        - Fixed anchor nums[i]: For each unique i, find pairs (l, r) where
          nums[l] + nums[r] == -nums[i].
        - Early Termination: If nums[i] > 0, break early because all subsequent
          numbers are >= nums[i] > 0, making a sum of 0 impossible.
        
        Complexity:
        - Time: O(n^2) - O(n log n) sort + n iterations of an O(n) two-pointer pass.
        - Space: O(1) auxiliary (or O(n) depending on language sorting implementation).
        """
        nums.sort()
        result = []
        n = len(nums)
        
        for i in range(n - 2):
            # Early exit: remaining numbers are strictly positive
            if nums[i] > 0:
                break
                
            # Skip duplicate anchor values to prevent duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            left = i + 1
            right = n - 1
            target = -nums[i]
            
            while left < right:
                current_sum = nums[left] + nums[right]
                
                if current_sum == target:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    # Skip duplicate values for the left pointer
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                        
                    # Skip duplicate values for the right pointer
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                        
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
                    
        return result


# ============================================================================
# Problem 4: Container With Most Water (LeetCode 11) - Medium
# Pattern: Greedy Two Pointers (Bottleneck Elimination)
# ============================================================================
class SolutionContainerWithMostWater:
    def maxArea(self, height: List[int]) -> int:
        """
        Finds two lines that together with the x-axis form a container containing the most water.
        
        Concept / Pattern:
        - Area formula: (right - left) * min(height[left], height[right]).
        - Start at maximum width: left = 0, right = len(height) - 1.
        - Greedy Bottleneck Choice: The height of the water is strictly limited by the
          SHORTER line. Moving the taller line inward will only decrease width without
          any chance of increasing the height boundary. Therefore, we must advance the
          pointer with the smaller height to search for a taller wall.
        
        Complexity:
        - Time: O(n) - Single pass as left and right converge.
        - Space: O(1) - Only scalar variables tracked.
        """
        left, right = 0, len(height) - 1
        max_water = 0
        
        while left < right:
            width = right - left
            current_height = min(height[left], height[right])
            current_area = width * current_height
            
            max_water = max(max_water, current_area)
            
            # Move the bottleneck pointer inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_water


# ============================================================================
# Problem 5: Trapping Rain Water (LeetCode 42) - Hard
# Pattern: Two Pointers with Running Prefix/Suffix Max
# ============================================================================
class SolutionTrappingRainWater:
    def trap(self, height: List[int]) -> int:
        """
        Computes how much water it can trap after raining in O(n) time and O(1) space.
        
        Concept / Pattern:
        - Water trapped above bar i = max(0, min(max_left, max_right) - height[i]).
        - Two-Pointer Optimization:
          - We maintain `left_max` and `right_max`.
          - If `left_max < right_max`, we KNOW that whatever exists between left and right
            is at least as tall as left_max (bounded by right_max). Thus, the water level
            at `left` is solely determined by `left_max`, regardless of higher peaks in between!
          - Conversely, if `right_max <= left_max`, water at `right` is strictly determined
            by `right_max`.
        
        Complexity:
        - Time: O(n) - Single linear pass.
        - Space: O(1) - Eliminates the need for O(n) prefix/suffix max arrays.
        """
        if not height:
            return 0
            
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        total_water = 0
        
        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                # Water trapped is the difference between boundary and current bar
                total_water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                total_water += right_max - height[right]
                
        return total_water
