"""
NeetCode 150 - Module 3.1: Verification & Test Suite
Unit tests with comprehensive edge cases for all 15 Tree solutions.
"""

from solutions import (
    TreeNode,
    SolutionInvertTree,
    SolutionMaxDepth,
    SolutionDiameterOfBinaryTree,
    SolutionBalancedBinaryTree,
    SolutionSameTree,
    SolutionSubtreeOfAnotherTree,
    SolutionLowestCommonAncestorBST,
    SolutionLevelOrder,
    SolutionRightSideView,
    SolutionCountGoodNodes,
    SolutionValidateBST,
    SolutionKthSmallestBST,
    SolutionBuildTree,
    SolutionMaxPathSum,
    CodecTree,
)


def build_tree_from_level_order(vals):
    if not vals:
        return None
    root = TreeNode(vals[0])
    queue = [root]
    i = 1
    while queue and i < len(vals):
        node = queue.pop(0)
        if vals[i] is not None:
            node.left = TreeNode(vals[i])
            queue.append(node.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            node.right = TreeNode(vals[i])
            queue.append(node.right)
        i += 1
    return root


def test_invert_tree():
    sol = SolutionInvertTree()
    root = build_tree_from_level_order([4, 2, 7, 1, 3, 6, 9])
    inv = sol.invertTree(root)
    assert inv.left.val == 7 and inv.right.val == 2
    assert inv.left.left.val == 9 and inv.left.right.val == 6
    assert sol.invertTree(None) is None
    print("PASS: 1. Invert Binary Tree")


def test_max_depth():
    sol = SolutionMaxDepth()
    assert sol.maxDepth(build_tree_from_level_order([3, 9, 20, None, None, 15, 7])) == 3
    assert sol.maxDepth(build_tree_from_level_order([1, None, 2])) == 2
    assert sol.maxDepth(None) == 0
    print("PASS: 2. Maximum Depth of Binary Tree")


def test_diameter():
    sol = SolutionDiameterOfBinaryTree()
    assert sol.diameterOfBinaryTree(build_tree_from_level_order([1, 2, 3, 4, 5])) == 3
    assert sol.diameterOfBinaryTree(build_tree_from_level_order([1, 2])) == 1
    assert sol.diameterOfBinaryTree(None) == 0
    print("PASS: 3. Diameter of Binary Tree")


def test_balanced_binary_tree():
    sol = SolutionBalancedBinaryTree()
    assert sol.isBalanced(build_tree_from_level_order([3, 9, 20, None, None, 15, 7])) is True
    assert sol.isBalanced(build_tree_from_level_order([1, 2, 2, 3, 3, None, None, 4, 4])) is False
    assert sol.isBalanced(None) is True
    print("PASS: 4. Balanced Binary Tree")


def test_same_tree():
    sol = SolutionSameTree()
    t1 = build_tree_from_level_order([1, 2, 3])
    t2 = build_tree_from_level_order([1, 2, 3])
    t3 = build_tree_from_level_order([1, 2])
    assert sol.isSameTree(t1, t2) is True
    assert sol.isSameTree(t1, t3) is False
    print("PASS: 5. Same Tree")


def test_subtree_of_another_tree():
    sol = SolutionSubtreeOfAnotherTree()
    root = build_tree_from_level_order([3, 4, 5, 1, 2])
    sub = build_tree_from_level_order([4, 1, 2])
    not_sub = build_tree_from_level_order([4, 1, 3])
    assert sol.isSubtree(root, sub) is True
    assert sol.isSubtree(root, not_sub) is False
    print("PASS: 6. Subtree of Another Tree")


def test_lowest_common_ancestor():
    sol = SolutionLowestCommonAncestorBST()
    root = build_tree_from_level_order([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    p = root.left  # 2
    q = root.right  # 8
    assert sol.lowestCommonAncestor(root, p, q).val == 6
    p2 = root.left  # 2
    q2 = root.left.right  # 4
    assert sol.lowestCommonAncestor(root, p2, q2).val == 2
    print("PASS: 7. Lowest Common Ancestor of a BST")


def test_level_order():
    sol = SolutionLevelOrder()
    tree = build_tree_from_level_order([3, 9, 20, None, None, 15, 7])
    assert sol.levelOrder(tree) == [[3], [9, 20], [15, 7]]
    assert sol.levelOrder(None) == []
    print("PASS: 8. Binary Tree Level Order Traversal")


def test_right_side_view():
    sol = SolutionRightSideView()
    tree = build_tree_from_level_order([1, 2, 3, None, 5, None, 4])
    assert sol.rightSideView(tree) == [1, 3, 4]
    assert sol.rightSideView(None) == []
    print("PASS: 9. Binary Tree Right Side View")


def test_count_good_nodes():
    sol = SolutionCountGoodNodes()
    tree = build_tree_from_level_order([3, 1, 4, 3, None, 1, 5])
    assert sol.goodNodes(tree) == 4
    tree2 = build_tree_from_level_order([3, 3, None, 4, 2])
    assert sol.goodNodes(tree2) == 3
    print("PASS: 10. Count Good Nodes in Binary Tree")


def test_validate_bst():
    sol = SolutionValidateBST()
    assert sol.isValidBST(build_tree_from_level_order([2, 1, 3])) is True
    assert sol.isValidBST(build_tree_from_level_order([5, 1, 4, None, None, 3, 6])) is False
    assert sol.isValidBST(build_tree_from_level_order([2, 2, 2])) is False
    print("PASS: 11. Validate Binary Search Tree")


def test_kth_smallest_bst():
    sol = SolutionKthSmallestBST()
    tree = build_tree_from_level_order([3, 1, 4, None, 2])
    assert sol.kthSmallest(tree, 1) == 1
    tree2 = build_tree_from_level_order([5, 3, 6, 2, 4, None, None, 1])
    assert sol.kthSmallest(tree2, 3) == 3
    print("PASS: 12. Kth Smallest Element in a BST")


def test_build_tree():
    sol = SolutionBuildTree()
    root = sol.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    assert root.val == 3
    assert root.left.val == 9
    assert root.right.val == 20
    assert root.right.left.val == 15
    print("PASS: 13. Construct Binary Tree from Preorder and Inorder Traversal")


def test_max_path_sum():
    sol = SolutionMaxPathSum()
    assert sol.maxPathSum(build_tree_from_level_order([1, 2, 3])) == 6
    assert sol.maxPathSum(build_tree_from_level_order([-10, 9, 20, None, None, 15, 7])) == 42
    assert sol.maxPathSum(build_tree_from_level_order([-3])) == -3
    print("PASS: 14. Binary Tree Maximum Path Sum")


def test_serialize_deserialize():
    codec = CodecTree()
    tree = build_tree_from_level_order([1, 2, 3, None, None, 4, 5])
    serialized = codec.serialize(tree)
    deserialized = codec.deserialize(serialized)
    assert deserialized.val == 1
    assert deserialized.left.val == 2
    assert deserialized.right.val == 3
    assert deserialized.right.left.val == 4
    assert deserialized.right.right.val == 5
    assert codec.deserialize(codec.serialize(None)) is None
    print("PASS: 15. Serialize and Deserialize Binary Tree")


if __name__ == "__main__":
    print("\n================ RUNNING TREES VERIFICATION ================\n")
    test_invert_tree()
    test_max_depth()
    test_diameter()
    test_balanced_binary_tree()
    test_same_tree()
    test_subtree_of_another_tree()
    test_lowest_common_ancestor()
    test_level_order()
    test_right_side_view()
    test_count_good_nodes()
    test_validate_bst()
    test_kth_smallest_bst()
    test_build_tree()
    test_max_path_sum()
    test_serialize_deserialize()
    print("\n================ ALL 15 TESTS PASSED! (100% VERIFIED) ================\n")
