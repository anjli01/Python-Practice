"""
NeetCode 150 - Module 1.3: Sliding Window
Detailed, fully-commented Python 3 solutions for all 6 problems.
"""

from typing import List
from collections import defaultdict, deque


# ============================================================================
# Problem 1: Best Time to Buy and Sell Stock (LeetCode 121) - Easy
# Pattern: One-Pass Running Minimum (Sliding Window of 2 Points)
# ============================================================================
class SolutionBestTimeToBuyAndSellStock:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Finds the maximum profit possible by buying on one day and selling on a future day.
        
        Concept / Pattern:
        - Running Minimum: You must buy BEFORE you sell.
        - As we iterate, we maintain the lowest purchase price seen so far.
        - At each day, calculate profit if sold today: price - min_price.
        
        Complexity:
        - Time: O(n) - Single pass through the prices list.
        - Space: O(1) - Only scalar variables tracked.
        """
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                # Found a cheaper day to buy
                min_price = price
            else:
                # Potential profit if bought at min_price and sold today
                max_profit = max(max_profit, price - min_price)
                
        return max_profit


# ============================================================================
# Problem 2: Longest Substring Without Repeating Characters (LeetCode 3) - Medium
# Pattern: Dynamic Sliding Window with Last-Seen Index Map
# ============================================================================
class SolutionLongestSubstringWithoutRepeatingCharacters:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Finds the length of the longest substring without repeating characters.
        
        Concept / Pattern:
        - Sliding Window: Window [left, right] expands to the right.
        - Hash Map (Last Seen): Stores the most recent index where each character appeared.
        - Jumping Left Pointer: When a duplicate char s[right] is encountered, we can
          instantly jump `left` to `last_seen[s[right]] + 1` (provided that index is
          within the current window), avoiding step-by-step contraction.
        
        Complexity:
        - Time: O(n) - Right pointer scans once from 0 to n - 1.
        - Space: O(min(n, m)) - Map stores unique characters (m is alphabet size).
        """
        last_seen = {}
        left = 0
        max_length = 0
        
        for right, char in enumerate(s):
            # If char was seen and is within the active window, move left past it
            if char in last_seen and last_seen[char] >= left:
                left = last_seen[char] + 1
                
            last_seen[char] = right
            max_length = max(max_length, right - left + 1)
            
        return max_length


# ============================================================================
# Problem 3: Longest Repeating Character Replacement (LeetCode 424) - Medium
# Pattern: Frequency Budget Window (Window Size - Max Frequency <= k)
# ============================================================================
class SolutionLongestRepeatingCharacterReplacement:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Returns the length of the longest substring containing the same letter
        after performing at most k character replacements.
        
        Concept / Pattern:
        - Window Validity Condition:
          In any window [left, right], the number of characters that need to be
          replaced to make all characters identical is:
          `replacements = (right - left + 1) - max_frequency`
        - If `replacements <= k`, the window is valid.
        - If `replacements > k`, shrink the window by advancing `left`.
        
        Complexity:
        - Time: O(n) - Each pointer moves from 0 to n.
        - Space: O(1) - Frequency map holds at most 26 uppercase English letters.
        """
        count = defaultdict(int)
        left = 0
        max_f = 0
        max_length = 0
        
        for right in range(len(s)):
            count[s[right]] += 1
            max_f = max(max_f, count[s[right]])
            
            # If current window requires more than k replacements, shrink from left
            while (right - left + 1) - max_f > k:
                count[s[left]] -= 1
                left += 1
                
            max_length = max(max_length, right - left + 1)
            
        return max_length


# ============================================================================
# Problem 4: Permutation in String (LeetCode 567) - Medium
# Pattern: Fixed-Size Sliding Window with Match Count Tracking
# ============================================================================
class SolutionPermutationInString:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Determines whether s2 contains a permutation of s1 as a substring.
        
        Concept / Pattern:
        - Fixed-size window: A permutation of s1 must have length equal to len(s1).
        - Rolling Match Count: Maintain an array of frequencies for 26 letters.
          Instead of comparing the entire 26-element array on every step (O(26)),
          track a `matches` counter (number of characters with identical frequencies).
          When matches == 26, an exact permutation is found in O(1).
        
        Complexity:
        - Time: O(n) - where n = len(s2).
        - Space: O(1) - Fixed 26-element frequency arrays.
        """
        if len(s1) > len(s2):
            return False
            
        s1_count = [0] * 26
        s2_count = [0] * 26
        
        # Populate initial window of size len(s1)
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1
            
        matches = 0
        for i in range(26):
            if s1_count[i] == s2_count[i]:
                matches += 1
                
        # Slide the window across s2
        left = 0
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True
                
            # Add new character at index right
            idx_in = ord(s2[right]) - ord('a')
            s2_count[idx_in] += 1
            if s1_count[idx_in] == s2_count[idx_in]:
                matches += 1
            elif s1_count[idx_in] + 1 == s2_count[idx_in]:
                matches -= 1
                
            # Remove old character at index left
            idx_out = ord(s2[left]) - ord('a')
            s2_count[idx_out] -= 1
            if s1_count[idx_out] == s2_count[idx_out]:
                matches += 1
            elif s1_count[idx_out] - 1 == s2_count[idx_out]:
                matches -= 1
                
            left += 1
            
        return matches == 26


# ============================================================================
# Problem 5: Minimum Window Substring (LeetCode 76) - Hard
# Pattern: Variable Sliding Window (Expand to Satisfy, Shrink to Minimize)
# ============================================================================
class SolutionMinimumWindowSubstring:
    def minWindow(self, s: str, t: str) -> str:
        """
        Finds the minimum window substring of s that contains every character in t.
        
        Concept / Pattern:
        - Expand right until the window contains all characters of t with sufficient frequency.
        - Once valid, shrink left as much as possible while maintaining validity to find the minimum.
        - State Tracking:
          - `need`: target character frequencies from t.
          - `have`: number of unique characters that meet or exceed the required frequency.
        
        Complexity:
        - Time: O(m + n) - Each character in s is visited at most twice (by left and right).
        - Space: O(m + n) - Hash maps for character frequencies.
        """
        if not t or not s:
            return ""
            
        count_t = defaultdict(int)
        for char in t:
            count_t[char] += 1
            
        window = defaultdict(int)
        have, need = 0, len(count_t)
        min_len = float('inf')
        res_indices = [-1, -1]
        
        left = 0
        for right in range(len(s)):
            char = s[right]
            window[char] += 1
            
            # Check if this character now meets the required frequency in t
            if char in count_t and window[char] == count_t[char]:
                have += 1
                
            # When the window satisfies all requirements, try shrinking from the left
            while have == need:
                # Update our minimum window result
                window_size = right - left + 1
                if window_size < min_len:
                    min_len = window_size
                    res_indices = [left, right]
                    
                # Remove left character and advance
                left_char = s[left]
                window[left_char] -= 1
                if left_char in count_t and window[left_char] < count_t[left_char]:
                    have -= 1
                left += 1
                
        l, r = res_indices
        return s[l : r + 1] if min_len != float('inf') else ""


# ============================================================================
# Problem 6: Sliding Window Maximum (LeetCode 239) - Hard
# Pattern: Monotonic Decreasing Deque
# ============================================================================
class SolutionSlidingWindowMaximum:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Returns the maximum elements in a sliding window of size k moving across nums.
        
        Concept / Pattern:
        - Monotonic Deque: A double-ended queue storing INDICES in strictly decreasing order of values.
        - For each incoming element nums[right]:
          1. Expire Left: Pop indices from the front if they fall outside [right - k + 1, right].
          2. Maintain Monotonicity: Pop indices from the back whose values are <= nums[right]
             (they can never be the maximum of this or future windows).
          3. Append current index: `q.append(right)`.
          4. Window Max: Once the window reaches size k (right >= k - 1), `nums[q[0]]`
             is the maximum of the current window.
        
        Complexity:
        - Time: O(n) - Each index is pushed and popped from the deque at most once.
        - Space: O(k) - Deque holds at most k indices.
        """
        output = []
        q = deque()  # stores indices
        
        for right, num in enumerate(nums):
            # 1. Discard smaller values from the back of deque
            while q and nums[q[-1]] <= num:
                q.pop()
                
            q.append(right)
            
            # 2. Discard front index if it has fallen outside the window
            if q[0] < right - k + 1:
                q.popleft()
                
            # 3. If window size is at least k, record maximum (front of deque)
            if right >= k - 1:
                output.append(nums[q[0]])
                
        return output
