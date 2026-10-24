"""
NeetCode 150 - Module 2.2: Verification & Test Suite
Unit tests with comprehensive edge cases for all 11 Linked List solutions.
"""

from solutions import (
    ListNode,
    Node,
    SolutionReverseList,
    SolutionMergeTwoSortedLists,
    SolutionReorderList,
    SolutionRemoveNthFromEnd,
    SolutionCopyRandomList,
    SolutionAddTwoNumbers,
    SolutionLinkedListCycle,
    SolutionFindDuplicate,
    LRUCache,
    SolutionMergeKSortedLists,
    SolutionReverseKGroup,
)


def to_list(head):
    res = []
    curr = head
    while curr:
        res.append(curr.val)
        curr = curr.next
    return res


def from_list(vals):
    dummy = ListNode()
    curr = dummy
    for v in vals:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def test_reverse_list():
    sol = SolutionReverseList()
    assert to_list(sol.reverseList(from_list([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]
    assert to_list(sol.reverseList(from_list([1, 2]))) == [2, 1]
    assert to_list(sol.reverseList(from_list([]))) == []
    print("PASS: 1. Reverse Linked List")


def test_merge_two_sorted_lists():
    sol = SolutionMergeTwoSortedLists()
    assert to_list(sol.mergeTwoLists(from_list([1, 2, 4]), from_list([1, 3, 4]))) == [1, 1, 2, 3, 4, 4]
    assert to_list(sol.mergeTwoLists(from_list([]), from_list([]))) == []
    assert to_list(sol.mergeTwoLists(from_list([]), from_list([0]))) == [0]
    print("PASS: 2. Merge Two Sorted Lists")


def test_reorder_list():
    sol = SolutionReorderList()
    head1 = from_list([1, 2, 3, 4])
    sol.reorderList(head1)
    assert to_list(head1) == [1, 4, 2, 3]

    head2 = from_list([1, 2, 3, 4, 5])
    sol.reorderList(head2)
    assert to_list(head2) == [1, 5, 2, 4, 3]

    head3 = from_list([1])
    sol.reorderList(head3)
    assert to_list(head3) == [1]
    print("PASS: 3. Reorder List")


def test_remove_nth_from_end():
    sol = SolutionRemoveNthFromEnd()
    assert to_list(sol.removeNthFromEnd(from_list([1, 2, 3, 4, 5]), 2)) == [1, 2, 3, 5]
    assert to_list(sol.removeNthFromEnd(from_list([1]), 1)) == []
    assert to_list(sol.removeNthFromEnd(from_list([1, 2]), 1)) == [1]
    assert to_list(sol.removeNthFromEnd(from_list([1, 2]), 2)) == [2]  # remove head
    print("PASS: 4. Remove Nth Node From End of List")


def test_copy_random_list():
    sol = SolutionCopyRandomList()
    n1 = Node(7)
    n2 = Node(13)
    n3 = Node(11)
    n1.next = n2
    n2.next = n3
    n2.random = n1
    n3.random = n2

    copied = sol.copyRandomList(n1)
    assert copied is not n1
    assert copied.val == 7
    assert copied.next.val == 13
    assert copied.next.random.val == 7
    assert sol.copyRandomList(None) is None
    print("PASS: 5. Copy List with Random Pointer")


def test_add_two_numbers():
    sol = SolutionAddTwoNumbers()
    l1 = from_list([2, 4, 3])  # 342
    l2 = from_list([5, 6, 4])  # 465
    assert to_list(sol.addTwoNumbers(l1, l2)) == [7, 0, 8]  # 807
    # Edge case: carry extends beyond input lengths
    assert to_list(sol.addTwoNumbers(from_list([9, 9, 9]), from_list([1]))) == [0, 0, 0, 1]
    print("PASS: 6. Add Two Numbers")


def test_linked_list_cycle():
    sol = SolutionLinkedListCycle()
    n1 = ListNode(3)
    n2 = ListNode(2)
    n3 = ListNode(0)
    n4 = ListNode(-4)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n2  # cycle back to 2
    assert sol.hasCycle(n1) is True

    n_linear = from_list([1, 2, 3])
    assert sol.hasCycle(n_linear) is False
    assert sol.hasCycle(None) is False
    print("PASS: 7. Linked List Cycle")


def test_find_duplicate():
    sol = SolutionFindDuplicate()
    assert sol.findDuplicate([1, 3, 4, 2, 2]) == 2
    assert sol.findDuplicate([3, 1, 3, 4, 2]) == 3
    assert sol.findDuplicate([3, 3, 3, 3, 3]) == 3
    print("PASS: 8. Find the Duplicate Number")


def test_lru_cache():
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    assert lru.get(1) == 1
    lru.put(3, 3)  # evicts key 2
    assert lru.get(2) == -1
    lru.put(4, 4)  # evicts key 1
    assert lru.get(1) == -1
    assert lru.get(3) == 3
    assert lru.get(4) == 4
    print("PASS: 9. LRU Cache")


def test_merge_k_sorted_lists():
    sol = SolutionMergeKSortedLists()
    lists = [
        from_list([1, 4, 5]),
        from_list([1, 3, 4]),
        from_list([2, 6])
    ]
    assert to_list(sol.mergeKLists(lists)) == [1, 1, 2, 3, 4, 4, 5, 6]
    assert sol.mergeKLists([]) is None
    assert to_list(sol.mergeKLists([from_list([])])) == []
    print("PASS: 10. Merge k Sorted Lists")


def test_reverse_k_group():
    sol = SolutionReverseKGroup()
    assert to_list(sol.reverseKGroup(from_list([1, 2, 3, 4, 5]), 2)) == [2, 1, 4, 3, 5]
    assert to_list(sol.reverseKGroup(from_list([1, 2, 3, 4, 5]), 3)) == [3, 2, 1, 4, 5]
    assert to_list(sol.reverseKGroup(from_list([1, 2]), 2)) == [2, 1]
    assert to_list(sol.reverseKGroup(from_list([1, 2, 3]), 1)) == [1, 2, 3]
    print("PASS: 11. Reverse Nodes in k-Group")


if __name__ == "__main__":
    print("\n================ RUNNING LINKED LIST VERIFICATION ================\n")
    test_reverse_list()
    test_merge_two_sorted_lists()
    test_reorder_list()
    test_remove_nth_from_end()
    test_copy_random_list()
    test_add_two_numbers()
    test_linked_list_cycle()
    test_find_duplicate()
    test_lru_cache()
    test_merge_k_sorted_lists()
    test_reverse_k_group()
    print("\n================ ALL 11 TESTS PASSED! (100% VERIFIED) ================\n")
