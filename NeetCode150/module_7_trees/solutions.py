"""
NeetCode 150 - Module 3.1: Trees
Detailed, fully-commented Python 3 solutions for all 15 problems.
"""

from typing import Optional, List
from collections import deque


class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ============================================================================
# Problem 1: Invert Binary Tree (LeetCode 226) - Easy
# Pattern: Recursive Child Swap (Post-Order / Pre-Order DFS)
# ============================================================================
class SolutionInvertTree:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """Inverts a binary tree by recursively swapping left and right subtrees."""
        if not root:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root


# ============================================================================
# Problem 2: Maximum Depth of Binary Tree (LeetCode 104) - Easy
# Pattern: Bottom-Up Depth DFS
# ============================================================================
class SolutionMaxDepth:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """Finds the maximum depth from root down to the farthest leaf node."""
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# ============================================================================
# Problem 3: Diameter of Binary Tree (LeetCode 543) - Easy
# Pattern: Dual-Return DFS (Height to Parent, Diameter to Global)
# ============================================================================
class SolutionDiameterOfBinaryTree:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """Calculates the length of the longest path between any two nodes."""
        max_diameter = 0

        def get_height(node: Optional[TreeNode]) -> int:
            nonlocal max_diameter
            if not node:
                return 0
            left_h = get_height(node.left)
            right_h = get_height(node.right)
            # Path through current node connects left and right subtrees
            max_diameter = max(max_diameter, left_h + right_h)
            return 1 + max(left_h, right_h)

        get_height(root)
        return max_diameter


# ============================================================================
# Problem 4: Balanced Binary Tree (LeetCode 110) - Easy
# Pattern: Fast-Failing Height DFS (-1 Sentinel)
# ============================================================================
class SolutionBalancedBinaryTree:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """Determines if a tree's subtree heights never differ by more than 1."""
        def check_height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            lh = check_height(node.left)
            if lh == -1:
                return -1
            rh = check_height(node.right)
            if rh == -1 or abs(lh - rh) > 1:
                return -1
            return 1 + max(lh, rh)

        return check_height(root) != -1


# ============================================================================
# Problem 5: Same Tree (LeetCode 100) - Easy
# Pattern: Simultaneous Structural & Value Traversal
# ============================================================================
class SolutionSameTree:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """Checks if two binary trees are structurally identical with equal values."""
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# ============================================================================
# Problem 6: Subtree of Another Tree (LeetCode 572) - Easy
# Pattern: Tree Traversal with Subtree Equivalence Matching
# ============================================================================
class SolutionSubtreeOfAnotherTree:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """Determines if subRoot matches any subtree rooted at any node of root."""
        def is_same(p, q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False
            return is_same(p.left, q.left) and is_same(p.right, q.right)

        if not subRoot:
            return True
        if not root:
            return False
        if is_same(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


# ============================================================================
# Problem 7: Lowest Common Ancestor of a BST (LeetCode 235) - Medium
# Pattern: BST Value-Split Navigation
# ============================================================================
class SolutionLowestCommonAncestorBST:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """Finds the lowest common ancestor in a Binary Search Tree in O(h)."""
        curr = root
        while curr:
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                # Split occurs or curr matches p or q
                return curr
        return root


# ============================================================================
# Problem 8: Binary Tree Level Order Traversal (LeetCode 102) - Medium
# Pattern: BFS with Fixed-Level Queue Snapshots
# ============================================================================
class SolutionLevelOrder:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """Returns the level order traversal of node values."""
        if not root:
            return []
        result = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            current_level = []
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(current_level)
            
        return result


# ============================================================================
# Problem 9: Binary Tree Right Side View (LeetCode 199) - Medium
# Pattern: BFS Level-End Capture
# ============================================================================
class SolutionRightSideView:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """Returns the values of nodes visible from the right side."""
        if not root:
            return []
        result = []
        queue = deque([root])
        
        while queue:
            level_len = len(queue)
            for i in range(level_len):
                node = queue.popleft()
                if i == level_len - 1:
                    result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
        return result


# ============================================================================
# Problem 10: Count Good Nodes in Binary Tree (LeetCode 1448) - Medium
# Pattern: DFS with Path Maximum Accumulator
# ============================================================================
class SolutionCountGoodNodes:
    def goodNodes(self, root: TreeNode) -> int:
        """Counts nodes with no ancestor having a greater value."""
        def dfs(node: Optional[TreeNode], max_so_far: int) -> int:
            if not node:
                return 0
            good = 1 if node.val >= max_so_far else 0
            new_max = max(max_so_far, node.val)
            return good + dfs(node.left, new_max) + dfs(node.right, new_max)

        return dfs(root, root.val)


# ============================================================================
# Problem 11: Validate Binary Search Tree (LeetCode 98) - Medium
# Pattern: DFS with Open Interval Bounding (low < val < high)
# ============================================================================
class SolutionValidateBST:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """Validates if a binary tree satisfies strict BST properties."""
        def validate(node: Optional[TreeNode], low: float, high: float) -> bool:
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)

        return validate(root, float('-inf'), float('inf'))


# ============================================================================
# Problem 12: Kth Smallest Element in a BST (LeetCode 230) - Medium
# Pattern: Iterative In-Order Traversal with Early Exit
# ============================================================================
class SolutionKthSmallestBST:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """Finds the kth smallest element in a BST in sorted order."""
        stack = []
        curr = root
        
        while curr or stack:
            # Go as far left as possible
            while curr:
                stack.append(curr)
                curr = curr.left
                
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
                
            curr = curr.right
            
        return -1


# ============================================================================
# Problem 13: Construct Binary Tree from Preorder & Inorder Traversal (LeetCode 105) - Medium
# Pattern: Divide and Conquer Subtree Partitioning
# ============================================================================
class SolutionBuildTree:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """Constructs a binary tree from preorder and inorder traversals."""
        in_map = {val: idx for idx, val in enumerate(inorder)}
        pre_idx = 0

        def helper(left_in: int, right_in: int) -> Optional[TreeNode]:
            nonlocal pre_idx
            if left_in > right_in:
                return None

            root_val = preorder[pre_idx]
            pre_idx += 1
            root = TreeNode(root_val)
            
            mid = in_map[root_val]
            root.left = helper(left_in, mid - 1)
            root.right = helper(mid + 1, right_in)
            return root

        return helper(0, len(inorder) - 1)


# ============================================================================
# Problem 14: Binary Tree Maximum Path Sum (LeetCode 124) - Hard
# Pattern: Post-Order Path Combination with Global Max
# ============================================================================
class SolutionMaxPathSum:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """Finds the maximum path sum of any non-empty path in the tree."""
        global_max = float('-inf')

        def max_gain(node: Optional[TreeNode]) -> int:
            nonlocal global_max
            if not node:
                return 0

            # Ignore negative paths by taking max with 0
            left_gain = max(0, max_gain(node.left))
            right_gain = max(0, max_gain(node.right))

            # Price of the new path where `node` is the highest turn point
            current_path = node.val + left_gain + right_gain
            global_max = max(global_max, current_path)

            # Return max single-branch contribution to parent
            return node.val + max(left_gain, right_gain)

        max_gain(root)
        return int(global_max)


# ============================================================================
# Problem 15: Serialize and Deserialize Binary Tree (LeetCode 297) - Hard
# Pattern: Pre-Order DFS with Sentinel Delimiters
# ============================================================================
class CodecTree:
    """Encodes a tree to a single string and decodes it back."""
    def serialize(self, root: Optional[TreeNode]) -> str:
        vals = []
        def dfs(node):
            if not node:
                vals.append("#")
                return
            vals.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(vals)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        idx = 0
        def dfs():
            nonlocal idx
            if vals[idx] == "#":
                idx += 1
                return None
            node = TreeNode(int(vals[idx]))
            idx += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
