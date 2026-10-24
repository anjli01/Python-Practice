"""
NeetCode 150 - Module 2.2: Linked List
Detailed, fully-commented Python 3 solutions for all 11 problems.
"""

from typing import Optional, List


class ListNode:
    """Standard singly-linked list node."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Node:
    """Node with an additional random pointer."""
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


# ============================================================================
# Problem 1: Reverse Linked List (LeetCode 206) - Easy
# Pattern: In-Place Pointer Inversion (Three Pointers)
# ============================================================================
class SolutionReverseList:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverses a singly linked list iteratively in O(n) time and O(1) space.
        
        Concept / Pattern:
        - Three Pointers: `prev`, `curr`, `nxt`.
        - Cache `curr.next` in `nxt` before overwriting `curr.next = prev`.
        
        Complexity:
        - Time: O(n) - Single pass through list.
        - Space: O(1) - In-place manipulation.
        """
        prev = None
        curr = head
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        return prev


# ============================================================================
# Problem 2: Merge Two Sorted Lists (LeetCode 21) - Easy
# Pattern: Sentinel Dummy Head Splice
# ============================================================================
class SolutionMergeTwoSortedLists:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merges two sorted linked lists into one sorted list in O(n + m).
        
        Concept / Pattern:
        - Sentinel Node: A dummy node eliminates special-casing for the head of the list.
        - Splice the smaller node to `tail.next`, then attach remaining list in O(1).
        
        Complexity:
        - Time: O(n + m) - Each node visited once.
        - Space: O(1) - Re-links existing nodes.
        """
        dummy = ListNode()
        tail = dummy
        
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
            
        # Attach the remaining portion of whichever list is not exhausted
        tail.next = list1 if list1 else list2
        return dummy.next


# ============================================================================
# Problem 3: Reorder List (LeetCode 143) - Medium
# Pattern: Three-Stage Pipeline (Find Middle -> Reverse Second Half -> Interleave)
# ============================================================================
class SolutionReorderList:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Reorders list to: L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 in-place.
        
        Concept / Pattern:
        - Step 1: Fast/Slow pointers to locate midpoint.
        - Step 2: Reverse the second half of the list.
        - Step 3: Interleave nodes from first half and reversed second half.
        
        Complexity:
        - Time: O(n) - Three linear passes.
        - Space: O(1) - Pure in-place pointer modifications.
        """
        if not head or not head.next:
            return
            
        # 1. Find midpoint (slow ends at middle)
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        second = slow.next
        slow.next = None  # Cut the first half from the second
        
        # 2. Reverse the second half
        prev = None
        curr = second
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        second = prev
        
        # 3. Interleave first half and reversed second half
        first = head
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2


# ============================================================================
# Problem 4: Remove Nth Node From End of List (LeetCode 19) - Medium
# Pattern: Two-Pointer Offset by n (Single Pass)
# ============================================================================
class SolutionRemoveNthFromEnd:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Removes the nth node from the end of the list in one pass.
        
        Concept / Pattern:
        - Dummy Sentinel: Handles removing the head node seamlessly.
        - Two Pointers: Advance `right` by n steps ahead. Then advance `left` and `right`
          together until `right` reaches the last node. `left.next` is the target node!
        
        Complexity:
        - Time: O(L) - Single pass through list.
        - Space: O(1) - Constant auxiliary space.
        """
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        # Advance right pointer n steps
        for _ in range(n):
            right = right.next
            
        # Slide both pointers until right reaches the end
        while right:
            left = left.next
            right = right.next
            
        # Delete the nth node from end
        left.next = left.next.next
        return dummy.next


# ============================================================================
# Problem 5: Copy List with Random Pointer (LeetCode 138) - Medium
# Pattern: Hash Map Clone Association
# ============================================================================
class SolutionCopyRandomList:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        Creates a deep copy of a list where nodes have next and random pointers.
        
        Concept / Pattern:
        - Pass 1: Clone all nodes and store mapping: `old_node -> new_node`.
        - Pass 2: Connect `new_node.next` and `new_node.random` using the map.
        
        Complexity:
        - Time: O(n) - Two passes.
        - Space: O(n) - Hash map storing n cloned nodes.
        """
        if not head:
            return None
            
        old_to_copy = {None: None}
        
        # Pass 1: Clone all nodes without pointers
        curr = head
        while curr:
            old_to_copy[curr] = Node(curr.val)
            curr = curr.next
            
        # Pass 2: Connect next and random pointers
        curr = head
        while curr:
            copy = old_to_copy[curr]
            copy.next = old_to_copy[curr.next]
            copy.random = old_to_copy[curr.random]
            curr = curr.next
            
        return old_to_copy[head]


# ============================================================================
# Problem 6: Add Two Numbers (LeetCode 2) - Medium
# Pattern: Digit-by-Digit Addition with Carry Propagation
# ============================================================================
class SolutionAddTwoNumbers:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Adds two numbers represented by linked lists in reverse order.
        
        Concept / Pattern:
        - Loop while `l1 or l2 or carry`.
        - Carry = `total // 10`, new digit = `total % 10`.
        
        Complexity:
        - Time: O(max(n, m)) - Process all digits.
        - Space: O(max(n, m)) - For the result list.
        """
        dummy = ListNode()
        tail = dummy
        carry = 0
        
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            total = val1 + val2 + carry
            carry = total // 10
            tail.next = ListNode(total % 10)
            tail = tail.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return dummy.next


# ============================================================================
# Problem 7: Linked List Cycle (LeetCode 141) - Easy
# Pattern: Floyd's Cycle Detection (Tortoise and Hare)
# ============================================================================
class SolutionLinkedListCycle:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Determines if a linked list has a cycle in O(1) space.
        
        Concept / Pattern:
        - Slow moves 1 step, Fast moves 2 steps.
        - If a cycle exists, Fast will lap Slow and they will meet.
        - If Fast reaches None, no cycle exists.
        
        Complexity:
        - Time: O(n) - Linear traversal.
        - Space: O(1) - Constant auxiliary space.
        """
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
                
        return False


# ============================================================================
# Problem 8: Find the Duplicate Number (LeetCode 287) - Medium
# Pattern: Array as Implicit Linked List (Floyd's Cycle Entry)
# ============================================================================
class SolutionFindDuplicate:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Finds the duplicate number in nums without modifying the array and in O(1) space.
        
        Concept / Pattern:
        - Values are in range [1, n] and length is n + 1.
        - Interpret the array as a functional graph: node i points to node nums[i].
        - A duplicate value means two different indices point to the same node (cycle entrance).
        - Phase 1: Fast (2 steps) and slow (1 step) find the intersection inside the cycle.
        - Phase 2: Start slow2 at 0; advance both slow and slow2 by 1 step. They meet at the entrance.
        
        Complexity:
        - Time: O(n) - Linear traversal.
        - Space: O(1) - Constant auxiliary space.
        """
        # Phase 1: Detect intersection inside the cycle
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
                
        # Phase 2: Find cycle entrance (the duplicate number)
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow


# ============================================================================
# Problem 9: LRU Cache (LeetCode 146) - Medium
# Pattern: Hash Map + Doubly Linked List
# ============================================================================
class DListNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    """
    Least Recently Used (LRU) Cache supporting get and put in O(1) time.
    
    Concept / Pattern:
    - Hash Map: key -> DListNode for O(1) lookup.
    - Doubly Linked List with dummy head and tail:
      - `head.next` is the Least Recently Used (LRU).
      - `tail.prev` is the Most Recently Used (MRU).
    """
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # key -> node
        
        # Dummy sentinel boundaries
        self.head = DListNode()
        self.tail = DListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: DListNode):
        """Unlinks a node from the doubly linked list."""
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def _insert_at_tail(self, node: DListNode):
        """Inserts a node right before the dummy tail (marks it as Most Recently Used)."""
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # Move accessed node to MRU (tail)
            self._remove(node)
            self._insert_at_tail(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
            
        new_node = DListNode(key, value)
        self.cache[key] = new_node
        self._insert_at_tail(new_node)
        
        # Evict LRU if capacity exceeded
        if len(self.cache) > self.cap:
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key]


# ============================================================================
# Problem 10: Merge k Sorted Lists (LeetCode 23) - Hard
# Pattern: Divide and Conquer Pairwise Merging
# ============================================================================
class SolutionMergeKSortedLists:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Merges k sorted linked lists in O(N log k) time and O(1) auxiliary space.
        
        Concept / Pattern:
        - Divide and Conquer: Pairwise merge lists iteratively:
          Merge lists in pairs until only 1 list remains.
        - Reduces k lists to k/2, then k/4, ..., down to 1.
        
        Complexity:
        - Time: O(N log k) - N total nodes, log k levels of merging.
        - Space: O(1) auxiliary - in-place pointer merging.
        """
        if not lists:
            return None
            
        def merge_two(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            dummy = ListNode()
            tail = dummy
            while l1 and l2:
                if l1.val <= l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next
            tail.next = l1 if l1 else l2
            return dummy.next

        while len(lists) > 1:
            merged_lists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                merged_lists.append(merge_two(l1, l2))
            lists = merged_lists
            
        return lists[0]


# ============================================================================
# Problem 11: Reverse Nodes in k-Group (LeetCode 25) - Hard
# Pattern: Block Reversal with Boundary Stitches
# ============================================================================
class SolutionReverseKGroup:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Reverses nodes of a linked list k at a time in O(n) time and O(1) space.
        
        Concept / Pattern:
        - Locate the k-th node ahead. If fewer than k nodes remain, leave them as-is.
        - Reverse the k-sized window.
        - Connect the previous group's tail to the new head, and recursively/iteratively proceed.
        
        Complexity:
        - Time: O(n) - Each node visited twice (once to verify k, once to reverse).
        - Space: O(1) - Constant auxiliary memory.
        """
        dummy = ListNode(0, head)
        group_prev = dummy
        
        def get_kth(curr: Optional[ListNode], k: int) -> Optional[ListNode]:
            while curr and k > 0:
                curr = curr.next
                k -= 1
            return curr

        while True:
            kth = get_kth(group_prev, k)
            if not kth:
                break
                
            group_next = kth.next
            
            # Reverse group: [curr ... kth]
            prev = kth.next
            curr = group_prev.next
            while curr != group_next:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
                
            # Stitch the newly reversed group
            tmp = group_prev.next
            group_prev.next = kth
            group_prev = tmp
            
        return dummy.next
