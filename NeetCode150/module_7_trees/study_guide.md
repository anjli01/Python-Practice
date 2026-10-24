# Module 3.1: Trees – Study Guide & Pattern Deep-Dive

Tree problems are dominated by **recursive decomposition (DFS)** and **level-by-level queue traversal (BFS)**. The key to solving tree problems is determining whether a node requires information from its children (bottom-up post-order) or passes constraints down to its children (top-down pre-order).

---

## 1. Invert Binary Tree (LeetCode 226) - Easy
* **Pattern**: Post-Order / Pre-Order Recursive Swap
* **Core Concept**: Recursively swap the left and right child pointers at every node.
* **Complexity**: Time: $O(n)$, Space: $O(h)$ where $h$ is tree height.

---

## 2. Maximum Depth of Binary Tree (LeetCode 104) - Easy
* **Pattern**: Bottom-Up Depth DFS
* **Core Concept**: $\text{Depth}(node) = 1 + \max(\text{Depth}(left), \text{Depth}(right))$.
* **Complexity**: Time: $O(n)$, Space: $O(h)$.

---

## 3. Diameter of Binary Tree (LeetCode 543) - Easy
* **Pattern**: Dual-Return Bottom-Up DFS
* **Core Concept**:
  The longest path passing through any node is $\text{height}(left) + \text{height}(right)$. Return height up to the parent while updating a global diameter maximum.
* **Complexity**: Time: $O(n)$, Space: $O(h)$.

---

## 4. Balanced Binary Tree (LeetCode 110) - Easy
* **Pattern**: Early-Failing Height DFS (-1 Sentinel)
* **Core Concept**:
  If any subtree has $|left\_h - right\_h| > 1$, immediately return $-1$ up the call stack to abort further recursive evaluation.
* **Complexity**: Time: $O(n)$, Space: $O(h)$.

---

## 5. Same Tree (LeetCode 100) - Easy
* **Pattern**: Simultaneous Structural & Value Traversal
* **Core Concept**: Two trees are identical if and only if $p.val == q.val$ and both their left and right subtrees are recursively identical.
* **Complexity**: Time: $O(n)$, Space: $O(h)$.

---

## 6. Subtree of Another Tree (LeetCode 572) - Easy
* **Pattern**: Traversal with Subtree Equivalence
* **Core Concept**: A tree $T$ contains $S$ if $T$ is identical to $S$, or $S$ is a subtree of $T.left$, or $S$ is a subtree of $T.right$.
* **Complexity**: Time: $O(n \cdot m)$ in worst case, Space: $O(h)$.

---

## 7. Lowest Common Ancestor of a BST (LeetCode 235) - Medium
* **Pattern**: BST Value-Split Navigation
* **Core Concept**:
  In a BST, if both $p$ and $q$ are greater than $root.val$, search right. If both are smaller, search left. The first node where $p$ and $q$ diverge (or match $root$) is the LCA.
* **Complexity**: Time: $O(h)$, Space: $O(1)$ iterative.

---

## 8. Binary Tree Level Order Traversal (LeetCode 102) - Medium
* **Pattern**: BFS with Fixed-Level Queue Snapshots
* **Core Concept**: Use `level_len = len(queue)` at the start of each while loop iteration to process all nodes of the current level together.
* **Complexity**: Time: $O(n)$, Space: $O(n)$ queue width.

---

## 9. Binary Tree Right Side View (LeetCode 199) - Medium
* **Pattern**: BFS Level-End Capture
* **Core Concept**: In level-order BFS, the last element popped from each level is the rightmost visible node.
* **Complexity**: Time: $O(n)$, Space: $O(n)$.

---

## 10. Count Good Nodes in Binary Tree (LeetCode 1448) - Medium
* **Pattern**: DFS with Path Maximum Accumulator
* **Core Concept**: Pass down the maximum value encountered on the path from root. A node is "good" if $node.val \ge max\_so\_far$.
* **Complexity**: Time: $O(n)$, Space: $O(h)$.

---

## 11. Validate Binary Search Tree (LeetCode 98) - Medium
* **Pattern**: DFS with Open Interval Bounding
* **Core Concept**:
  Every node must satisfy $low < node.val < high$. When going left, update $high = node.val$. When going right, update $low = node.val$.
* **Complexity**: Time: $O(n)$, Space: $O(h)$.

---

## 12. Kth Smallest Element in a BST (LeetCode 230) - Medium
* **Pattern**: In-Order Traversal (Iterative Stack)
* **Core Concept**: In-order traversal (Left, Root, Right) traverses a BST in strictly ascending order. Pop $k$ nodes from the stack to find the $k$-th smallest in $O(h + k)$ time.
* **Complexity**: Time: $O(h + k)$, Space: $O(h)$.

---

## 13. Construct Binary Tree from Preorder & Inorder Traversal (LeetCode 105) - Medium
* **Pattern**: Subtree Partitioning via Inorder Hash Map
* **Core Concept**: Preorder root is always at `preorder[pre_idx]`. Find this root's index in `inorder` to split elements into left and right subtrees.
* **Complexity**: Time: $O(n)$ with hash map lookup, Space: $O(n)$.

---

## 14. Binary Tree Maximum Path Sum (LeetCode 124) - Hard
* **Pattern**: Post-Order Path Combination with Global Max
* **Core Concept**:
  At each node, compute the max gain from left and right children (floored at 0 to reject negative paths). A complete path turns at $node$: $node.val + left\_gain + right\_gain$. Return $node.val + \max(left\_gain, right\_gain)$ to the parent.
* **Complexity**: Time: $O(n)$, Space: $O(h)$.

---

## 15. Serialize and Deserialize Binary Tree (LeetCode 297) - Hard
* **Pattern**: Pre-Order DFS with Sentinel Tokens
* **Core Concept**: Serialize using preorder traversal with commas and `'#'` for null nodes. Deserialize recursively by consuming tokens from left to right.
* **Complexity**: Time: $O(n)$, Space: $O(n)$.
