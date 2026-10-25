# Module 2.2: Linked List – Study Guide & Pattern Deep-Dive

Linked Lists test your ability to manage **explicit pointer manipulation and memory references** without introducing null-dereferences or circular leaks.

---

## 1. Reverse Linked List (LeetCode 206) - Easy
* **Quick Links**: [LeetCode](https://leetcode.com/problems/reverse-linked-list/) • [NeetCode Problem](https://neetcode.io/problems/reverse-a-linked-list) • [NeetCode Solution](https://neetcode.io/solutions/reverse-linked-list) • [YouTube Video](https://www.youtube.com/watch?v=G0_I-ZF0S38)
* **Pattern**: In-Place Three Pointers (`prev`, `curr`, `nxt`)
* **Core Concept**:
  Iterate through the list, caching `nxt = curr.next` before redirecting `curr.next = prev`. Advance `prev = curr` and `curr = nxt`. When `curr` becomes `None`, `prev` is the new head.
* **Mental Model**:
  Reversing a chain of paper clips. Detach each clip from the front of the original chain and reattach it to a growing reversed chain held in your other hand (`prev`).
* **Tips & Interview Tricks**:
  * **The Three-Variable Dance**: `prev`, `curr`, `nxt` is the #1 most tested linked list primitive. Draw the pointer diagram on the whiteboard — interviewers expect it.
  * **Recursive Alternative**: The recursive version returns the new head from the base case, and each stack frame rewires `curr.next.next = curr; curr.next = None`. Mention it to show depth, but the iterative version is preferred for $O(1)$ space.
* **Complexity**:
  * Time: $O(n)$
  * Space: $O(1)$

---

## 2. Merge Two Sorted Lists (LeetCode 21) - Easy
* **Quick Links**: [LeetCode](https://leetcode.com/problems/merge-two-sorted-lists/) • [NeetCode Problem](https://neetcode.io/problems/merge-two-sorted-linked-lists) • [NeetCode Solution](https://neetcode.io/solutions/merge-two-sorted-lists) • [YouTube Video](https://www.youtube.com/watch?v=XIdigk956u0)
* **Pattern**: Sentinel Dummy Head Splice
* **Core Concept**:
  A dummy node eliminates special handling for initializing the head of the merged list. Compare `l1.val` and `l2.val`, appending the smaller node to `tail`. After one list is exhausted, directly link the remaining non-empty list to `tail.next` in $O(1)$ time.
* **Mental Model**:
  Zipping two sorted card decks into one pile. Always take the smaller card from the top of either deck. When one deck runs out, slap the remaining deck on top.
* **Tips & Interview Tricks**:
  * **Dummy Node Pattern**: `dummy = ListNode(0); tail = dummy` eliminates `if head is None` checks. Return `dummy.next` at the end. This pattern appears in nearly every list-construction problem.
  * **In-Place**: No new nodes are created — you are re-wiring existing `.next` pointers, so auxiliary space is $O(1)$.
* **Complexity**:
  * Time: $O(n + m)$
  * Space: $O(1)$

---

## 3. Reorder List (LeetCode 143) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/reorder-list/) • [NeetCode Problem](https://neetcode.io/problems/reorder-linked-list) • [NeetCode Solution](https://neetcode.io/solutions/reorder-list) • [YouTube Video](https://www.youtube.com/watch?v=S5bfdUTrKLM)
* **Pattern**: Three-Stage Pipeline (Midpoint -> Inversion -> Interleave)
* **Core Concept**:
  1. Split list in half using Fast & Slow pointers (`slow.next = None`).
  2. Reverse the second half in-place.
  3. Interleave nodes from the first and reversed second half.
* **Mental Model**:
  Folding a piece of paper in half. The second half flips over and interleaves with the first half, creating the alternating pattern $L_0 \to L_n \to L_1 \to L_{n-1} \to \ldots$
* **Tips & Interview Tricks**:
  * **Composite Problem**: This problem is three sub-problems glued together — *find middle* (Fast/Slow), *reverse list*, and *merge two lists*. Each is a standalone interview question. Practice each in isolation.
  * **Even-Length Midpoint**: For even-length lists, `slow` should land on the last node of the first half. Use `while fast.next and fast.next.next` to achieve this cleanly.
* **Complexity**:
  * Time: $O(n)$
  * Space: $O(1)$

---

## 4. Remove Nth Node From End of List (LeetCode 19) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) • [NeetCode Problem](https://neetcode.io/problems/remove-node-from-end-of-linked-list) • [NeetCode Solution](https://neetcode.io/solutions/remove-nth-node-from-end-of-list) • [YouTube Video](https://www.youtube.com/watch?v=XVuQxVej6y8)
* **Pattern**: Offset Fast & Slow Pointers (Dummy Node)
* **Core Concept**:
  Advance `right` by $n$ steps from a dummy head. Then move `left` and `right` simultaneously until `right` reaches the last node. `left.next` is guaranteed to be the node to remove. Splice it out with `left.next = left.next.next`.
* **Mental Model**:
  A ruler of fixed length $n$ sliding along the list. When the far end of the ruler hits the wall (end of list), the near end marks the node just before the target.
* **Tips & Interview Tricks**:
  * **Dummy Node for Head Removal**: If you need to remove the actual head node (e.g., single-element list, $n$ = length), a dummy node before head prevents a special case: `dummy.next = head; left = dummy`.
  * **One-Pass Guarantee**: This is a classic *"Can you do it in one pass?"* follow-up. The offset pointer technique traverses the list exactly once.
* **Complexity**:
  * Time: $O(n)$
  * Space: $O(1)$

---

## 5. Copy List with Random Pointer (LeetCode 138) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/copy-list-with-random-pointer/) • [NeetCode Problem](https://neetcode.io/problems/copy-linked-list-with-random-pointer) • [NeetCode Solution](https://neetcode.io/solutions/copy-list-with-random-pointer) • [YouTube Video](https://www.youtube.com/watch?v=5Y2EiZST97Y)
* **Pattern**: Two-Pass Hash Map Association
* **Core Concept**:
  * Pass 1: Clone every node into a hash map `old_to_copy[curr] = Node(curr.val)`.
  * Pass 2: Re-link `copy.next = old_to_copy[curr.next]` and `copy.random = old_to_copy[curr.random]`.
  The hash map bridges old nodes to new nodes, enabling $O(1)$ random pointer resolution.
* **Mental Model**:
  Photocopying a social network. First, photocopy every person (node). Then, use an address book (hash map) to wire up their friendships (next and random pointers) between the copies.
* **Tips & Interview Tricks**:
  * **Handle `None` Gracefully**: Map `None` to `None` in your hash map (`old_to_copy[None] = None`) so you never need special-case checks when `curr.next` or `curr.random` is `None`.
  * **$O(1)$ Space Follow-Up**: The interleaving approach (weave clones between originals: `A -> A' -> B -> B'`) avoids a hash map but is harder to code correctly. Mention it to show awareness but default to the hash map approach.
* **Complexity**:
  * Time: $O(n)$
  * Space: $O(n)$

---

## 6. Add Two Numbers (LeetCode 2) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/add-two-numbers/) • [NeetCode Problem](https://neetcode.io/problems/add-two-numbers) • [NeetCode Solution](https://neetcode.io/solutions/add-two-numbers) • [YouTube Video](https://www.youtube.com/watch?v=wgFPrzTjm7s)
* **Pattern**: Digit Addition with Carry Propagation
* **Core Concept**:
  Traverse while `l1 or l2 or carry`. Compute the digit sum `total = v1 + v2 + carry`, extract the ones digit `total % 10` as the new node value, and propagate `carry = total // 10`. The least-significant-digit-first ordering means no reversal is needed.
* **Mental Model**:
  Grade-school column addition, but the digits arrive in reverse order (ones place first), which actually makes it easier — you naturally process carries left to right.
* **Tips & Interview Tricks**:
  * **The Triple `or` Condition**: `while l1 or l2 or carry` handles all edge cases in a single loop: unequal list lengths and the final carry (e.g., $999 + 1 = 1000$ produces an extra node).
  * **Don't Forget the Final Carry**: If carry is 1 after the loop ends, you need one more node. The triple `or` condition handles this automatically.
* **Complexity**:
  * Time: $O(\max(n, m))$
  * Space: $O(\max(n, m))$

---

## 7. Linked List Cycle (LeetCode 141) - Easy
* **Quick Links**: [LeetCode](https://leetcode.com/problems/linked-list-cycle/) • [NeetCode Problem](https://neetcode.io/problems/linked-list-cycle-detection) • [NeetCode Solution](https://neetcode.io/solutions/linked-list-cycle) • [YouTube Video](https://www.youtube.com/watch?v=gBTe7lFR3vc)
* **Pattern**: Floyd's Cycle Detection (Tortoise & Hare)
* **Core Concept**:
  Slow pointer advances 1 step; fast pointer advances 2 steps. In a cycle of length $C$, the distance between fast and slow decreases by 1 each step, guaranteeing they meet in at most $C$ iterations. If fast reaches `None`, no cycle exists.
* **Mental Model**:
  Two runners on a circular track. The fast runner laps the slow runner if the track is a loop. If the track is a straight line, the fast runner simply reaches the finish line first.
* **Tips & Interview Tricks**:
  * **Why $O(1)$ Space Matters**: A hash set approach (`if node in seen`) also detects cycles in $O(n)$ time, but uses $O(n)$ space. Floyd's achieves the same with $O(1)$ space — always mention this trade-off.
  * **Null Check**: Always check `while fast and fast.next` (not just `while fast`) because `fast.next.next` would dereference `None` if `fast.next` is `None`.
* **Complexity**:
  * Time: $O(n)$
  * Space: $O(1)$

---

## 8. Find the Duplicate Number (LeetCode 287) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/find-the-duplicate-number/) • [NeetCode Problem](https://neetcode.io/problems/find-duplicate-integer) • [NeetCode Solution](https://neetcode.io/solutions/find-the-duplicate-number) • [YouTube Video](https://www.youtube.com/watch?v=wjYnzkAhcNk)
* **Pattern**: Array as Functional Graph (Cycle Entrance)
* **Core Concept**:
  Since array values are in $[1, n]$ with length $n + 1$, treat index $i$ as pointing to node `nums[i]`. A duplicate number means multiple indices point to the same node, forming a cycle entrance.
  * Phase 1: Fast/Slow pointers meet inside the cycle.
  * Phase 2: Reset `slow2 = 0`. Move both `slow` and `slow2` at 1 step per turn. Their meeting point is the duplicate value.
* **Mental Model**:
  The array IS a linked list in disguise. Each cell says *"go to this index next"*. A duplicate means two different cells point to the same destination — exactly like two edges entering the same node, which creates a cycle entrance.
* **Tips & Interview Tricks**:
  * **The "Aha" Insight**: The hardest part is recognizing that this is Floyd's algorithm on an implicit graph. Once you see it, the code is identical to Linked List Cycle II (LC 142).
  * **Phase 2 Proof**: The mathematical guarantee is: distance from index 0 to the cycle entrance equals the distance from the meeting point to the cycle entrance. This is why the two slow pointers converge at the duplicate.
* **Complexity**:
  * Time: $O(n)$
  * Space: $O(1)$

---

## 9. LRU Cache (LeetCode 146) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/lru-cache/) • [NeetCode Problem](https://neetcode.io/problems/lru-cache) • [NeetCode Solution](https://neetcode.io/solutions/lru-cache) • [YouTube Video](https://www.youtube.com/watch?v=7ABFKPK2hD4)
* **Pattern**: Hash Map + Doubly Linked List
* **Core Concept**:
  * Hash Map: Key $\to$ Doubly Linked List Node for $O(1)$ lookup.
  * Doubly Linked List: Dummy `head` (LRU end) and `tail` (MRU end) allow $O(1)$ removal and insertion of any node.
  On every `get` or `put`, move the accessed node to the MRU end. On capacity overflow, evict the node at the LRU end.
* **Mental Model**:
  A VIP line at a nightclub. When someone is accessed, they jump to the front of the line (most recently used). When the club is full, the person who has been idle the longest (back of the line) gets kicked out.
* **Tips & Interview Tricks**:
  * **Sentinel Nodes**: Dummy `head` and `tail` nodes that never hold real data eliminate all null-pointer edge cases for insertion and removal. `head.next` is always the LRU node; `tail.prev` is always the MRU node.
  * **Two Helper Methods**: Write `_remove(node)` and `_insert(node)` as private methods. Every operation becomes: remove from current position, then insert at MRU end. This keeps the code clean and bug-free.
  * **Hash Map Update on Eviction**: When evicting the LRU node, don't forget to also delete its key from the hash map.
* **Complexity**:
  * Time: $O(1)$ for `get` and `put`
  * Space: $O(\text{capacity})$

---

## 10. Merge k Sorted Lists (LeetCode 23) - Hard
* **Quick Links**: [LeetCode](https://leetcode.com/problems/merge-k-sorted-lists/) • [NeetCode Problem](https://neetcode.io/problems/merge-k-sorted-linked-lists) • [NeetCode Solution](https://neetcode.io/solutions/merge-k-sorted-lists) • [YouTube Video](https://www.youtube.com/watch?v=q5a5OiGbT6Q)
* **Pattern**: Divide-and-Conquer Pairwise Merge
* **Core Concept**:
  Pairwise merge lists iteratively: merge $k$ lists into $k/2$, then $k/4$, down to 1. Each round touches all $N$ total nodes exactly once, and there are $\log k$ rounds, yielding $O(N \log k)$ total work. This avoids the $O(k \cdot N)$ overhead of merging sequentially.
* **Mental Model**:
  A tournament bracket. In each round, pair up adjacent lists and merge them. After $\log k$ rounds, one champion list remains.
* **Tips & Interview Tricks**:
  * **D&C vs. Min-Heap**: Both achieve $O(N \log k)$. The divide-and-conquer approach reuses your `mergeTwoLists` function and is simpler to code. The heap approach requires handling comparator tie-breaking (wrap nodes in tuples with unique IDs to avoid `TypeError` in Python).
  * **Odd-Count Handling**: When the number of lists is odd, carry the unpaired list forward to the next round unchanged.
* **Complexity**:
  * Time: $O(N \log k)$ where $N$ is total nodes across all lists
  * Space: $O(1)$ auxiliary

---

## 11. Reverse Nodes in k-Group (LeetCode 25) - Hard
* **Quick Links**: [LeetCode](https://leetcode.com/problems/reverse-nodes-in-k-group/) • [NeetCode Problem](https://neetcode.io/problems/reverse-nodes-in-k-group) • [NeetCode Solution](https://neetcode.io/solutions/reverse-nodes-in-k-group) • [YouTube Video](https://www.youtube.com/watch?v=1UOPsfP85V4)
* **Pattern**: Block Window Reversal with Boundary Stitches
* **Core Concept**:
  Check if at least $k$ nodes remain ahead. If so, reverse the $k$-length segment in-place and splice the previous group's tail to the new group head. Repeat until fewer than $k$ nodes remain (those are left as-is).
* **Mental Model**:
  Reversing $k$-length segments of a train, then coupling the reversed cars back together. Before detaching each segment, note where it connects to the previous and next segments so you can re-couple after reversal.
* **Tips & Interview Tricks**:
  * **Boundary Bookkeeping**: Before reversing a group, save `group_prev` (the node before the group) and `group_next` (the node after the group). After reversal, stitch: `group_prev.next = new_group_head` and `old_group_head.next = group_next`.
  * **Dummy Node**: Use a dummy node before `head` so the first group's stitching doesn't require special-case handling.
  * **Count-Ahead Check**: Walk $k$ steps forward first to verify enough nodes exist. If not, leave the remaining nodes untouched and return.
* **Complexity**:
  * Time: $O(n)$
  * Space: $O(1)$
