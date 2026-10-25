# Module 1.1: Arrays & Hashing – Study Guide & Pattern Deep-Dive

Arrays & Hashing forms the bedrock of technical interviews. The central theme of this module is **trading auxiliary memory for constant-time $O(1)$ lookups**.

---

## 1. Contains Duplicate (LeetCode 217) - Easy
* **Quick Links**: [LeetCode](https://leetcode.com/problems/contains-duplicate/) • [NeetCode Problem](https://neetcode.io/problems/duplicate-integer) • [NeetCode Solution](https://neetcode.io/solutions/contains-duplicate) • [YouTube Video](https://www.youtube.com/watch?v=3OamzN90kPg)
* **Pattern**: Hash Set / Direct Membership Testing
* **Core Concept**:
  A Hash Set uses a hashing function to map elements to memory buckets, providing expected $O(1)$ lookup and insertion.
* **Mental Model**:
  As you iterate through the list, keep a mental registry of numbers already observed. If an incoming number matches any registered number, immediately return `True`.
* **Tips & Interview Tricks**:
  * **Early Exit**: Do not use `len(nums) != len(set(nums))` in a real interview without explaining the trade-off. While concise, `len(set(nums))` forces processing of the entire array even if the duplicate is at index 0 and 1. Iterating with a set allows immediate $O(1)$ termination on the first duplicate.
  * **Space-Time Trade-off**: If the interviewer asks for $O(1)$ extra space, sort the array first ($O(n \log n)$ time) and check adjacent elements (`nums[i] == nums[i-1]`).
* **Complexity**:
  * Time: $O(n)$
  * Space: $O(n)$

---

## 2. Valid Anagram (LeetCode 242) - Easy
* **Quick Links**: [LeetCode](https://leetcode.com/problems/valid-anagram/) • [NeetCode Problem](https://neetcode.io/problems/is-anagram) • [NeetCode Solution](https://neetcode.io/solutions/valid-anagram) • [YouTube Video](https://www.youtube.com/watch?v=9UtInBqnCgA)
* **Pattern**: Fixed-Size Frequency Counting
* **Core Concept**:
  Two strings are anagrams if and only if they possess identical character distributions.
* **Mental Model**:
  Think of a 26-pan balance scale. Increment the pan corresponding to each character in string `s`, and decrement for each character in string `t`. If all pans balance to zero at the end, the strings are anagrams.
* **Tips & Interview Tricks**:
  * **Length Mismatch Pre-Check**: Always check `if len(s) != len(t): return False` at the very top. It avoids unnecessary allocation and loops.
  * **Array vs. Hash Map**: For ASCII/lowercase English letters (`'a'` - `'z'`), an integer array of size 26 (`counts[ord(c) - ord('a')]`) is strictly faster and uses $O(1)$ auxiliary space compared to a general hash map or `collections.Counter`.
  * **Follow-up (Unicode)**: If the interviewer asks *"What if inputs contain Unicode characters?"*, state that you should switch to a Python `dict` / `Counter` to handle arbitrary code points dynamically.
* **Complexity**:
  * Time: $O(n)$
  * Space: $O(1)$ (bounded by alphabet size 26)

---

## 3. Two Sum (LeetCode 1) - Easy
* **Quick Links**: [LeetCode](https://leetcode.com/problems/two-sum/) • [NeetCode Problem](https://neetcode.io/problems/two-integer-sum) • [NeetCode Solution](https://neetcode.io/solutions/two-sum) • [YouTube Video](https://www.youtube.com/watch?v=KLlXCFG5TnA)
* **Pattern**: One-Pass Hash Map (Complement Lookup)
* **Core Concept**:
  For an equation $x + y = \text{target}$, if you are currently at $x$, you only need to know whether $y = \text{target} - x$ has already appeared in the array.
* **Mental Model**:
  Walk through the array with a notebook mapping `value -> index`. At each step, ask: *"Is my complement in the notebook?"* If yes, you have your pair. If not, record your own value and index, then move forward.
* **Tips & Interview Tricks**:
  * **One-Pass vs. Two-Pass**: Never do a two-pass hash map where you insert everything first, because duplicate values (e.g., `[3, 3]`, target = 6) can overwrite indices. The one-pass approach guarantees that an element cannot pair with itself.
  * **Follow-up (Sorted Array)**: If the array is already sorted, remember that Two Pointers ($O(1)$ space) is preferred over a Hash Map.
* **Complexity**:
  * Time: $O(n)$
  * Space: $O(n)$

---

## 4. Group Anagrams (LeetCode 49) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/group-anagrams/) • [NeetCode Problem](https://neetcode.io/problems/anagram-groups) • [NeetCode Solution](https://neetcode.io/solutions/group-anagrams) • [YouTube Video](https://www.youtube.com/watch?v=vzdNOK2oB2E)
* **Pattern**: Canonical Key Categorization
* **Core Concept**:
  To group items together, transform each item into a standardized canonical signature that is identical for all members of the group.
* **Mental Model**:
  Imagine sorting mail into bins. Every anagram must have the exact same barcode. The barcode can be either:
  1. The sorted string: `"eat" -> "aet"`, `"tea" -> "aet"`.
  2. The character count tuple: `(1, 0, 0, ..., 1, 0)` for 26 letters.
* **Tips & Interview Tricks**:
  * **Tuple as Dict Key**: In Python, lists are mutable and cannot be dictionary keys. Always convert the 26-count list to an immutable `tuple(count)` to use it as a key in `defaultdict(list)`.
  * **Sorting vs. Counting**:
    * Sorting string: $O(m \cdot k \log k)$, where $m$ is number of strings, $k$ is max length.
    * 26-character count: $O(m \cdot k)$. This is asymptotically optimal.
* **Complexity**:
  * Time: $O(m \cdot k)$
  * Space: $O(m \cdot k)$

---

## 5. Top K Frequent Elements (LeetCode 347) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/top-k-frequent-elements/) • [NeetCode Problem](https://neetcode.io/problems/top-k-elements-in-list) • [NeetCode Solution](https://neetcode.io/solutions/top-k-frequent-elements) • [YouTube Video](https://www.youtube.com/watch?v=YPTqKIgVk-k)
* **Pattern**: Bucket Sort (Frequency as Index)
* **Core Concept**:
  Instead of sorting all frequencies ($O(n \log n)$) or maintaining a Min-Heap of size $k$ ($O(n \log k)$), use the property that an element's frequency cannot exceed $n$.
* **Mental Model**:
  Create an array of $n + 1$ buckets, where `bucket[f]` holds a list of all numbers that appear with frequency `f`. Iterate from the highest frequency bucket down to 1 until you gather $k$ numbers.
* **Tips & Interview Tricks**:
  * **Linear Time Guarantee**: Many candidates default to a heap (`heapq.nlargest`). Mention the heap approach first to demonstrate knowledge, then pivot: *"We can do better than $O(n \log k)$ using Bucket Sort in $O(n)$ time because the maximum frequency is strictly bounded by $n$."*
  * **Array Sizing**: Don't forget that the bucket array size must be `len(nums) + 1` (to account for an element appearing $n$ times at index $n$).
* **Complexity**:
  * Time: $O(n)$
  * Space: $O(n)$

---

## 6. Encode and Decode Strings (LeetCode 271) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/encode-and-decode-strings/) • [NeetCode Problem](https://neetcode.io/problems/string-encode-and-decode) • [NeetCode Solution](https://neetcode.io/solutions/encode-and-decode-strings) • [YouTube Video](https://www.youtube.com/watch?v=B1k_sxOSgv8)
* **Pattern**: Chunked Length-Prefixed Framing
* **Core Concept**:
  Any static delimiter character (such as `,`, `;`, or `|`) could naturally appear inside the input strings. To eliminate ambiguity, encode each string with its length and a sentinel: `<length>#<string>`.
* **Mental Model**:
  This is the exact framing protocol used in low-level networking (e.g., HTTP Content-Length, WebSocket framing). The reader parses the integer before `#`, then reads ahead exactly that many characters.
* **Tips & Interview Tricks**:
  * **Edge Cases Handled Automatically**:
    * Empty string `""` becomes `"0#"`.
    * Strings containing `#` like `"4#code"` become `"6#4#code"`. The decoder reads `6`, so the inner `#` is treated as raw data.
    * Strings containing numbers or commas.
* **Complexity**:
  * Time: $O(n)$ (where $n$ is total character count)
  * Space: $O(1)$ auxiliary memory (excluding output)

---

## 7. Product of Array Except Self (LeetCode 238) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/product-of-array-except-self/) • [NeetCode Problem](https://neetcode.io/problems/products-of-array-discluding-self) • [NeetCode Solution](https://neetcode.io/solutions/product-of-array-except-self) • [YouTube Video](https://www.youtube.com/watch?v=bNvIQI2wAjk)
* **Pattern**: Prefix & Suffix Accumulator (Two-Pass In-Place)
* **Core Concept**:
  The product of all numbers except `nums[i]` is equivalent to:
  $$\text{result}[i] = (\text{product of all numbers to the left of } i) \times (\text{product of all numbers to the right of } i)$$
* **Mental Model**:
  Make two passes over the array:
  1. Left-to-Right: Fill `result[i]` with the cumulative prefix product up to $i-1$.
  2. Right-to-Left: Maintain a running `suffix` product variable, multiplying it directly into `result[i]`.
* **Tips & Interview Tricks**:
  * **Division Trap**: The problem explicitly forbids division. Even with division, arrays with zeroes (`[0, 0]` or `[1, 0]`) break standard arithmetic with `ZeroDivisionError`.
  * **$O(1)$ Space Optimization**: Instead of allocating separate `prefix` and `suffix` arrays, use the output array to store prefixes, and a single scalar float/int variable for the rolling suffix.
* **Complexity**:
  * Time: $O(n)$ (exactly two passes)
  * Space: $O(1)$ auxiliary (output array does not count as extra memory)

---

## 8. Valid Sudoku (LeetCode 36) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/valid-sudoku/) • [NeetCode Problem](https://neetcode.io/problems/valid-sudoku) • [NeetCode Solution](https://neetcode.io/solutions/valid-sudoku) • [YouTube Video](https://www.youtube.com/watch?v=TjFXEUCMqI8)
* **Pattern**: Coordinate Hashing / Grid Partitioning
* **Core Concept**:
  Check uniqueness constraints independently across three dimensions:
  1. 9 Rows
  2. 9 Columns
  3. 9 3x3 Sub-boxes
* **Mental Model**:
  Every cell `(r, c)` belongs to:
  * Row `r`
  * Column `c`
  * Box coordinate `(r // 3, c // 3)`
* **Tips & Interview Tricks**:
  * **Box Coordinate Formula**: Integer division `r // 3` and `c // 3` automatically groups rows (0,1,2), (3,4,5), and (6,7,8) into box indices `0, 1, 2`.
  * **Single Pass**: You do not need three separate passes. A single nested loop traversing each cell can check and update row, col, and box sets simultaneously.
* **Complexity**:
  * Time: $O(1)$ (strictly bounded by 81 cells)
  * Space: $O(1)$ (at most 81 entries in hash sets)

---

## 9. Longest Consecutive Sequence (LeetCode 128) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/longest-consecutive-sequence/) • [NeetCode Problem](https://neetcode.io/problems/longest-consecutive-sequence) • [NeetCode Solution](https://neetcode.io/solutions/longest-consecutive-sequence) • [YouTube Video](https://www.youtube.com/watch?v=P6RZZMu_maU)
* **Pattern**: Intelligent Sequence Start Detection
* **Core Concept**:
  To achieve $O(n)$ without sorting ($O(n \log n)$), store all numbers in a Hash Set. Only explore consecutive sequences starting from numbers that are the **head** of a streak.
* **Mental Model**:
  How do you know if `num` is the start of a streak? If `num - 1` is NOT in the set! If `num - 1` is in the set, skip `num` because it will be counted as part of an earlier number's sequence.
* **Tips & Interview Tricks**:
  * **Why is this strictly $O(n)$?** Interviewers frequently push back, thinking the nested `while` loop makes it $O(n^2)$. You must explain: *"Each element is visited in the inner loop only if it is part of a streak explored from its head. Across the entire run, each number is extended at most once, resulting in strictly $2n = O(n)$ total operations."*
  * **Iterate over Set, not List**: Iterate over `for num in num_set:` instead of `for num in nums:` to automatically bypass redundant duplicate elements.
* **Complexity**:
  * Time: $O(n)$
  * Space: $O(n)$
