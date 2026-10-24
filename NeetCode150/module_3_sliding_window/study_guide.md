# Module 1.3: Sliding Window – Study Guide & Pattern Deep-Dive

Sliding Window is the premier technique for analyzing contiguous sub-arrays or substrings. By dynamically resizing or shifting a window $[L, R]$, we avoid recomputing subproblem states, turning $O(n^2)$ brute-force checks into linear $O(n)$ traversals.

---

## 1. Best Time to Buy and Sell Stock (LeetCode 121) - Easy
* **Pattern**: One-Pass Running Minimum (2-Pointer Window)
* **Core Concept**:
  You must buy before you sell. Maintain the lowest historical price encountered so far; the maximum profit obtainable on any day is $\text{price} - \text{min\_price}$.
* **Mental Model**:
  Slide forward through time. If today's price dips below your historical valley, update your buy price. Otherwise, evaluate the profit if you liquidated today.
* **Tips & Interview Tricks**:
  * **Kadane's Connection**: This problem can be mapped to Maximum Subarray (Kadane's Algorithm) over the daily price differences `prices[i] - prices[i-1]`.
* **Complexity**:
  * Time: $O(n)$
  * Space: $O(1)$

---

## 2. Longest Substring Without Repeating Characters (LeetCode 3) - Medium
* **Pattern**: Dynamic Window with Last-Seen Index Map
* **Core Concept**:
  Maintain a window $[L, R]$ of unique characters. When $s[R]$ duplicates a character already in the window, fast-forward $L$ directly to $\text{last\_seen}[s[R]] + 1$.
* **Mental Model**:
  An expanding rubber band. When the right edge hits a duplicate, the left edge snaps forward past the previous occurrence.
* **Tips & Interview Tricks**:
  * **The "ABBA" Trap**: When updating $L$, always verify that the previous occurrence index is $\ge L$:
    ```python
    if char in last_seen and last_seen[char] >= left:
        left = last_seen[char] + 1
    ```
    If you omit `last_seen[char] >= left`, on string `"abba"`, when you hit the second `'a'` at index 3, `last_seen['a'] = 0` would mistakenly move `left` *backwards* from 2 to 1!
* **Complexity**:
  * Time: $O(n)$
  * Space: $O(\min(n, m))$ where $m$ is alphabet size

---

## 3. Longest Repeating Character Replacement (LeetCode 424) - Medium
* **Pattern**: Frequency Budget Window
* **Core Concept**:
  In any window of size $(R - L + 1)$, the number of replacements needed to make all characters identical is:
  $$\text{replacements} = (R - L + 1) - \text{max\_frequency}$$
  A window is valid if and only if $\text{replacements} \le k$.
* **Mental Model**:
  You are allowed to "paint over" at most $k$ non-majority characters. If the minority characters outnumber your $k$ paint buckets, shrink the window from the left.
* **Tips & Interview Tricks**:
  * **Do We Need to Decrement `max_f` When Shrinking?** NO! This is a legendary interview subtlety. Even though shrinking the window may lower the actual max frequency inside it, our goal is to find a *strictly larger* valid window. A smaller `max_f` can never produce a larger window than what we've already discovered.
* **Complexity**:
  * Time: $O(n)$
  * Space: $O(1)$ (26 uppercase letters)

---

## 4. Permutation in String (LeetCode 567) - Medium
* **Pattern**: Fixed-Size Window with Match Count Tracking
* **Core Concept**:
  A permutation of $s_1$ inside $s_2$ must have length exactly equal to $|s_1|$. Slide a window of fixed length $|s_1|$ across $s_2$.
* **Mental Model**:
  A fixed-length sliding frame. As the frame moves right, one character enters on the right and one leaves on the left.
* **Tips & Interview Tricks**:
  * **$O(1)$ Window Comparison**: Don't compare the two 26-element arrays on every step ($26 \times n$ operations). Maintain a `matches` counter tracking how many of the 26 character slots currently have identical counts. Check if `matches == 26` in $O(1)$ time!
* **Complexity**:
  * Time: $O(n)$
  * Space: $O(1)$

---

## 5. Minimum Window Substring (LeetCode 76) - Hard
* **Pattern**: Variable Window (Expand to Satisfy, Contract to Minimize)
* **Core Concept**:
  1. Expand $R$ until all character frequency requirements of $t$ are satisfied (`have == need`).
  2. While valid, contract $L$ to discard excess characters and record the minimal window length.
* **Mental Model**:
  A scavenger hunt. Keep walking forward collecting items until your shopping list is complete. Once complete, drop items from your backpack from the beginning until you are just about to lose a necessary item.
* **Tips & Interview Tricks**:
  * **`have` and `need` Counters**: Count unique characters in $t$ rather than total characters. For instance, if $t = \text{"AABC"}$, `need = 3` (for keys 'A', 'B', 'C'). Only increment `have` when `window[char] == count_t[char]`.
* **Complexity**:
  * Time: $O(|s| + |t|)$
  * Space: $O(|s| + |t|)$

---

## 6. Sliding Window Maximum (LeetCode 239) - Hard
* **Pattern**: Monotonic Decreasing Deque
* **Core Concept**:
  Maintain a double-ended queue (`deque`) storing **indices** such that the values corresponding to these indices are in strictly decreasing order.
* **Mental Model**:
  *"If a younger candidate is smarter and faster than an older candidate, the older candidate will never get promoted."*
  When a new element $nums[R]$ arrives, any previous elements in the deque that are $\le nums[R]$ are obsolete because they are older AND smaller. Pop them from the back!
* **Tips & Interview Tricks**:
  * **Store Indices, Not Values**: Storing indices allows you to easily check if the maximum at the front has expired from the window (`q[0] < R - k + 1`).
  * **Front is Always Maximum**: Because monotonicity is strictly preserved, `nums[q[0]]` is guaranteed to be the maximum of the current window.
* **Complexity**:
  * Time: $O(n)$ (each index is pushed once and popped at most once)
  * Space: $O(k)$
