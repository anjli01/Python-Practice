# Module 2.2: Linked List – Study Guide & Pattern Deep-Dive

Linked Lists test your ability to manage **explicit pointer manipulation and memory references** without introducing null-dereferences or circular leaks.

---

## 1. Reverse Linked List (LeetCode 206) - Easy
* **Pattern**: In-Place Three Pointers (`prev`, `curr`, `nxt`)
* **Core Concept**:
  Iterate through the list, caching `nxt = curr.next` before redirecting `curr.next = prev`. Advance `prev = curr` and `curr = nxt`.
* **Complexity**: Time: $O(n)$, Space: $O(1)$.

---

## 2. Merge Two Sorted Lists (LeetCode 21) - Easy
* **Pattern**: Sentinel Dummy Head Splice
* **Core Concept**:
  A dummy node eliminates special handling for initializing the head of the merged list. Always append the remaining non-empty list directly to `tail.next` in $O(1)$ time.
* **Complexity**: Time: $O(n + m)$, Space: $O(1)$.

---

## 3. Reorder List (LeetCode 143) - Medium
* **Pattern**: Three-Stage Pipeline (Midpoint -> Inversion -> Interleave)
* **Core Concept**:
  1. Split list in half using Fast & Slow pointers (`slow.next = None`).
  2. Reverse the second half in-place.
  3. Interleave nodes from the first and reversed second half.
* **Complexity**: Time: $O(n)$, Space: $O(1)$.

---

## 4. Remove Nth Node From End of List (LeetCode 19) - Medium
* **Pattern**: Offset Fast & Slow Pointers (Dummy Node)
* **Core Concept**:
  Advance `right` by $n$ steps from a dummy head. Then move `left` and `right` simultaneously until `right` reaches the last node. `left.next` is guaranteed to be the node to remove.
* **Complexity**: Time: $O(n)$, Space: $O(1)$.

---

## 5. Copy List with Random Pointer (LeetCode 138) - Medium
* **Pattern**: Two-Pass Hash Map Association
* **Core Concept**:
  * Pass 1: Clone every node into a hash map `old_to_copy[curr] = Node(curr.val)`.
  * Pass 2: Re-link `copy.next = old_to_copy[curr.next]` and `copy.random = old_to_copy[curr.random]`.
* **Complexity**: Time: $O(n)$, Space: $O(n)$.

---

## 6. Add Two Numbers (LeetCode 2) - Medium
* **Pattern**: Digit Addition with Carry Propagation
* **Core Concept**:
  Traverse while `l1 or l2 or carry`. Compute digit sum and propagate `carry = total // 10`.
* **Complexity**: Time: $O(\max(n, m))$, Space: $O(\max(n, m))$.

---

## 7. Linked List Cycle (LeetCode 141) - Easy
* **Pattern**: Floyd's Cycle Detection (Tortoise & Hare)
* **Core Concept**:
  Slow pointer advances 1 step; fast pointer advances 2 steps. In a cycle of length $C$, the distance between fast and slow decreases by 1 each step, guaranteeing they meet in at most $C$ iterations.
* **Complexity**: Time: $O(n)$, Space: $O(1)$.

---

## 8. Find the Duplicate Number (LeetCode 287) - Medium
* **Pattern**: Array as Functional Graph (Cycle Entrance)
* **Core Concept**:
  Since array values are in $[1, n]$ with length $n + 1$, treat index $i$ as pointing to node `nums[i]`. A duplicate number means multiple indices point to the same node, forming a cycle entrance.
  * Phase 1: Fast/Slow pointers meet inside the cycle.
  * Phase 2: Reset `slow2 = 0`. Move both `slow` and `slow2` at 1 step per turn. Their meeting point is the duplicate value.
* **Complexity**: Time: $O(n)$, Space: $O(1)$.

---

## 9. LRU Cache (LeetCode 146) - Medium
* **Pattern**: Hash Map + Doubly Linked List
* **Core Concept**:
  * Hash Map: Key $\to$ Doubly Linked List Node for $O(1)$ lookup.
  * Doubly Linked List: Dummy `head` (LRU) and `tail` (MRU) allow $O(1)$ removal and insertion of any node.
* **Complexity**: $O(1)$ for `get` and `put`.

---

## 10. Merge k Sorted Lists (LeetCode 23) - Hard
* **Pattern**: Divide-and-Conquer Pairwise Merge
* **Core Concept**:
  Pairwise merge lists iteratively: merge $k$ lists into $k/2$, then $k/4$, down to 1. Avoids the $O(k \cdot N)$ sequential merge overhead.
* **Complexity**: Time: $O(N \log k)$, Space: $O(1)$ auxiliary.

---

## 11. Reverse Nodes in k-Group (LeetCode 25) - Hard
* **Pattern**: Block Window Reversal with Boundary Stitches
* **Core Concept**:
  Check if at least $k$ nodes remain ahead. If so, reverse the $k$-length segment in-place and splice the previous group's tail to the new group head. Repeat until fewer than $k$ nodes remain.
* **Complexity**: Time: $O(n)$, Space: $O(1)$.
