"""
NeetCode 150 - Module 1.1: Arrays & Hashing
Detailed, fully-commented Python 3 solutions for all 9 problems.
"""

from typing import List, Dict, Tuple
from collections import defaultdict, Counter


# ============================================================================
# Problem 1: Contains Duplicate (LeetCode 217) - Easy
# Pattern: Hash Set / Membership Testing
# ============================================================================
class SolutionContainsDuplicate:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Determines whether any value appears at least twice in the array.
        
        Concept / Pattern:
        - Hash Set: Provides O(1) average lookup and insertion time.
        - Early Exit: We can terminate the scan as soon as a duplicate is found,
          avoiding processing the rest of the array.
        
        Complexity:
        - Time: O(n) - Single pass through the array.
        - Space: O(n) - Set stores at most n unique elements.
        """
        # A hash set stores unique elements we have already inspected.
        seen = set()
        
        for num in nums:
            # If the current number is already in the set, a duplicate exists.
            if num in seen:
                return True
            # Otherwise, remember this number for subsequent checks.
            seen.add(num)
            
        # No duplicates found after inspecting all numbers.
        return False


# ============================================================================
# Problem 2: Valid Anagram (LeetCode 242) - Easy
# Pattern: Frequency Map / Fixed Array Counting
# ============================================================================
class SolutionValidAnagram:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Checks if string t is an anagram of string s.
        
        Concept / Pattern:
        - Frequency Counting: Two strings are anagrams if and only if they have
          identical character frequencies.
        - Pre-check: If lengths differ, they can never be anagrams.
        
        Complexity:
        - Time: O(n) - Single pass to count and compare characters (where n = len(s)).
        - Space: O(1) - Fixed alphabet size (26 lowercase English letters).
        """
        # Fast exit: Anagrams must have the exact same length.
        if len(s) != len(t):
            return False

        # Fixed-size array for 26 lowercase English letters ('a' - 'z').
        # Using a fixed 26-element array is faster and uses O(1) space.
        counts = [0] * 26
        
        for char_s, char_t in zip(s, t):
            counts[ord(char_s) - ord('a')] += 1
            counts[ord(char_t) - ord('a')] -= 1
            
        # If all frequencies balanced out to 0, it's a valid anagram.
        return all(count == 0 for count in counts)


# ============================================================================
# Problem 3: Two Sum (LeetCode 1) - Easy
# Pattern: One-Pass Hash Map (Complement Lookup)
# ============================================================================
class SolutionTwoSum:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Returns indices of the two numbers such that they add up to target.
        
        Concept / Pattern:
        - Complement Hashing: Instead of checking every pair (O(n^2)), for each num,
          we ask: "Have we previously seen (target - num)?"
        - One-pass: We query the hash map first, then insert the current number,
          which naturally prevents using the same element twice.
        
        Complexity:
        - Time: O(n) - Inspect each number once with O(1) dictionary lookups.
        - Space: O(n) - Hash map stores up to n elements.
        """
        # Map: value -> index
        prev_map: Dict[int, int] = {}
        
        for current_idx, num in enumerate(nums):
            complement = target - num
            
            # Check if complement was already processed
            if complement in prev_map:
                return [prev_map[complement], current_idx]
                
            # Store the current number's index for future numbers
            prev_map[num] = current_idx
            
        return []


# ============================================================================
# Problem 4: Group Anagrams (LeetCode 49) - Medium
# Pattern: Canonical Key Categorization (Tuple / Frequency Signature)
# ============================================================================
class SolutionGroupAnagrams:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Groups anagrams together into sublists.
        
        Concept / Pattern:
        - Canonical Representation: All anagrams share the same character count.
        - We map a 26-element frequency tuple (hashable in Python) as the key:
          e.g., (1, 0, 0, ..., 1, 0) for "bat".
        
        Complexity:
        - Time: O(m * k) - where m = number of strings, k = max string length.
          (Faster than sorting which would be O(m * k log k)).
        - Space: O(m * k) - Stores all strings in the grouped dictionary.
        """
        # Defaultdict maps: count_tuple -> list of anagram strings
        anagram_groups: Dict[Tuple[int, ...], List[str]] = defaultdict(list)
        
        for word in strs:
            # Frequency counter for 26 lowercase English letters
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
                
            # Convert list to an immutable tuple so it can serve as a dict key
            anagram_groups[tuple(count)].append(word)
            
        return list(anagram_groups.values())


# ============================================================================
# Problem 5: Top K Frequent Elements (LeetCode 347) - Medium
# Pattern: Bucket Sort (Frequency as Index)
# ============================================================================
class SolutionTopKFrequent:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Returns the k most frequent elements in O(n) time.
        
        Concept / Pattern:
        - Bucket Sort: An element can appear at most len(nums) times.
        - We create buckets indexed by frequency (from 0 to len(nums)).
        - Bucket[f] holds all numbers that appeared exactly f times.
        - Iterating backwards from highest frequency yields top-k in O(n) time,
          beating Heap sort O(n log k).
        
        Complexity:
        - Time: O(n) - Single pass for counting, single pass for bucket placement,
          and at most n elements collected.
        - Space: O(n) - Frequency map and bucket array.
        """
        # Step 1: Count element frequencies
        count_map = Counter(nums)
        
        # Step 2: Buckets where index = frequency, value = list of numbers
        # Size is len(nums) + 1 because max possible frequency is len(nums).
        buckets: List[List[int]] = [[] for _ in range(len(nums) + 1)]
        
        for num, freq in count_map.items():
            buckets[freq].append(num)
            
        # Step 3: Collect top k elements from highest to lowest frequency
        result = []
        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result
                    
        return result


# ============================================================================
# Problem 6: Encode and Decode Strings (LeetCode 271) - Medium
# Pattern: Chunked Length-Prefixed Encoding
# ============================================================================
class Codec:
    def encode(self, strs: List[str]) -> str:
        """
        Encodes a list of strings to a single string.
        
        Concept / Pattern:
        - Length-Prefixing: Format each string as `<length>#<string>`.
        - Why this works: Any delimiter (like ',', ';', '|') could exist inside
          the strings themselves. By prepending the explicit byte length followed by
          a sentinel character '#', the decoder knows exactly how many characters
          to read ahead regardless of content.
        
        Complexity:
        - Time: O(n) - where n is the total length of all characters.
        - Space: O(1) auxiliary - excluding the returned encoded string.
        """
        encoded_chunks = []
        for s in strs:
            encoded_chunks.append(f"{len(s)}#{s}")
        return "".join(encoded_chunks)

    def decode(self, s: str) -> List[str]:
        """
        Decodes a single string to a list of strings.
        """
        result = []
        i = 0
        
        while i < len(s):
            # Locate the delimiter '#' that terminates the length prefix
            j = i
            while s[j] != '#':
                j += 1
                
            # Parse the length of the upcoming string
            length = int(s[i:j])
            
            # Extract the string payload using the parsed length
            start = j + 1
            end = start + length
            result.append(s[start:end])
            
            # Advance pointer past this chunk
            i = end
            
        return result


# ============================================================================
# Problem 7: Product of Array Except Self (LeetCode 238) - Medium
# Pattern: Prefix & Suffix Accumulator (Two-Pass In-Place)
# ============================================================================
class SolutionProductExceptSelf:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Calculates the product of all elements except nums[i] without division in O(n).
        
        Concept / Pattern:
        - For any index i: result[i] = (product of elements to the left) *
                                      (product of elements to the right).
        - Pass 1 (Left-to-Right): Populate result with prefix products.
        - Pass 2 (Right-to-Left): Maintain a running suffix product and multiply
          it directly into result in-place.
        
        Complexity:
        - Time: O(n) - Exactly two linear scans.
        - Space: O(1) auxiliary - Output array does not count toward extra space.
        """
        n = len(nums)
        result = [1] * n
        
        # Pass 1: result[i] contains the product of all elements to the left of i
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]
            
        # Pass 2: Multiply by the product of all elements to the right of i
        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
            
        return result


# ============================================================================
# Problem 8: Valid Sudoku (LeetCode 36) - Medium
# Pattern: Coordinate Hashing for Rows, Columns, and 3x3 Sub-grids
# ============================================================================
class SolutionValidSudoku:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Validates if a 9x9 Sudoku board configuration is valid so far.
        
        Concept / Pattern:
        - Coordinate Partitioning:
          - Row rule: (r, val) must be unique.
          - Column rule: (c, val) must be unique.
          - 3x3 Box rule: Cell (r, c) belongs to box index (r // 3, c // 3).
        
        Complexity:
        - Time: O(1) - Board size is strictly fixed at 9x9 = 81 cells.
        - Space: O(1) - At most 81 entries per hash set.
        """
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                # Skip empty cells denoted by '.'
                if val == '.':
                    continue
                    
                box_key = (r // 3, c // 3)
                
                # Check if the number was already encountered in current row, col, or box
                if (val in rows[r] or 
                    val in cols[c] or 
                    val in boxes[box_key]):
                    return False
                    
                # Record this value
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_key].add(val)
                
        return True


# ============================================================================
# Problem 9: Longest Consecutive Sequence (LeetCode 128) - Medium
# Pattern: Intelligent Sequence Start Detection (Hash Set Exploration)
# ============================================================================
class SolutionLongestConsecutive:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Finds the length of the longest consecutive elements sequence in O(n).
        
        Concept / Pattern:
        - Hash Set Lookups: Convert list to set for O(1) membership testing.
        - Starting Point Filter: A number `num` is the start of a consecutive sequence
          IF AND ONLY IF `num - 1` is NOT in the set!
        - Why this guarantees O(n): We only explore sequences forward from their root.
          Each number is visited at most twice (once in the outer loop, and once
          during sequence extension), avoiding O(n^2).
        
        Complexity:
        - Time: O(n) - Linear pass through set.
        - Space: O(n) - Stores numbers in hash set.
        """
        num_set = set(nums)
        longest_streak = 0
        
        for num in num_set:
            # Check if 'num' is the start of a sequence
            if (num - 1) not in num_set:
                current_num = num
                current_streak = 1
                
                # Count consecutive numbers forward
                while (current_num + 1) in num_set:
                    current_num += 1
                    current_streak += 1
                    
                longest_streak = max(longest_streak, current_streak)
                
        return longest_streak
