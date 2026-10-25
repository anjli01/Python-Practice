# Module 3.1: Trees – Study Guide & Pattern Deep-Dive

Tree problems are dominated by **recursive decomposition (DFS)** and **level-by-level queue traversal (BFS)**. The key to solving tree problems is determining whether a node requires information from its children (bottom-up post-order) or passes constraints down to its children (top-down pre-order).

---

## 1. Invert Binary Tree (LeetCode 226) - Easy
* **Quick Links**: [LeetCode](https://leetcode.com/problems/invert-binary-tree/) • [NeetCode Problem](https://neetcode.io/problems/invert-a-binary-tree) • [NeetCode Solution](https://neetcode.io/solutions/invert-binary-tree) • [YouTube Video](https://www.youtube.com/watch?v=OnSn2XEQ4MY)
* **Pattern**: Post-Order / Pre-Order Recursive Swap
* **Core Concept**:
  Recursively swap the left and right child pointers at every node. The order of traversal (pre-order or post-order) doesn't matter because each swap is independent — swapping children at any node does not affect the correctness of swaps at other nodes.
* **Mental Model**:
  Holding a tree up to a mirror. Every left child becomes the right child and vice versa, recursively applied all the way down.
* **Tips & Interview Tricks**:
  * **Base Case**: `if not root: return None`. This is the simplest tree recursion — use it to warm up your whiteboard coding and establish confidence early.
  * **Iterative Alternative**: A BFS queue or DFS stack works identically — at each node, swap its children. Mention this to show versatility.
* **Complexity**:
  * Time: $O(n)$
  * Space: $O(h)$ where $h$ is tree height

---

## 2. Maximum Depth of Binary Tree (LeetCode 104) - Easy
* **Quick Links**: [LeetCode](https://leetcode.com/problems/maximum-depth-of-binary-tree/) • [NeetCode Problem](https://neetcode.io/problems/depth-of-binary-tree) • [NeetCode Solution](https://neetcode.io/solutions/maximum-depth-of-binary-tree) • [YouTube Video](https://www.youtube.com/watch?v=hTM3phVI6YQ)
* **Pattern**: Bottom-Up Depth DFS
* **Core Concept**:
  $\text{Depth}(node) = 1 + \max(\text{Depth}(left), \text{Depth}(right))$. The base case is `if not node: return 0`. Each node asks its children how deep they are, takes the bigger answer, and adds 1 for itself.
* **Mental Model**:
  Dropping a plumb line from every leaf to the root. The longest plumb line is the maximum depth. Each node reports *"I'm one level deeper than whichever of my children is deeper."*
* **Tips & Interview Tricks**:
  * **Three Approaches**: Recursive DFS (most concise), iterative BFS (count levels), and iterative DFS with a stack of `(node, depth)` pairs. Know all three — interviewers may ask for alternatives.
  * **BFS Level Count**: `depth = 0; while queue: for _ in range(len(queue)): ...` — each iteration of the outer `while` is one level.
* **Complexity**:
  * Time: $O(n)$
  * Space: $O(h)$

---

## 3. Diameter of Binary Tree (LeetCode 543) - Easy
* **Quick Links**: [LeetCode](https://leetcode.com/problems/diameter-of-binary-tree/) • [NeetCode Problem](https://neetcode.io/problems/binary-tree-diameter) • [NeetCode Solution](https://neetcode.io/solutions/diameter-of-binary-tree) • [YouTube Video](https://www.youtube.com/watch?v=K81C31ytOZE)
* **Pattern**: Dual-Return Bottom-Up DFS
* **Core Concept**:
  The longest path passing through any node is $\text{height}(left) + \text{height}(right)$. Return height up to the parent while updating a global diameter maximum. The diameter does not necessarily pass through the root.
* **Mental Model**:
  Stretching a rope through the tree. At each node, the longest rope you can stretch passes through that node by extending as far as possible into both the left and right subtrees. Track the longest rope found anywhere in the tree.
* **Tips & Interview Tricks**:
  * **Global Variable vs. Return Value**: The function returns *height* to the parent but updates *diameter* via a nonlocal/instance variable. This "compute one thing, return another" pattern is extremely common in tree problems (also seen in Maximum Path Sum).
  * **Off-by-One**: Diameter counts *edges*, not nodes. If your height function returns node count, the diameter at a node is `left_h + right_h` (no `+ 1`).
* **Complexity**:
  * Time: $O(n)$
  * Space: $O(h)$

---

## 4. Balanced Binary Tree (LeetCode 110) - Easy
* **Quick Links**: [LeetCode](https://leetcode.com/problems/balanced-binary-tree/) • [NeetCode Problem](https://neetcode.io/problems/balanced-binary-tree) • [NeetCode Solution](https://neetcode.io/solutions/balanced-binary-tree) • [YouTube Video](https://www.youtube.com/watch?v=QfJsau0ItOY)
* **Pattern**: Early-Failing Height DFS (-1 Sentinel)
* **Core Concept**:
  If any subtree has $|left\_h - right\_h| > 1$, immediately return $-1$ up the call stack to abort further recursive evaluation. A return value of $-1$ signals "unbalanced" and propagates upward without additional checks.
* **Mental Model**:
  A building inspector checking floor-by-floor. If any floor's left and right wings differ in height by more than 1 story, the building fails inspection immediately — no need to inspect higher floors.
* **Tips & Interview Tricks**:
  * **$O(n)$ vs. $O(n^2)$**: The naive approach calls `height()` at every node, giving $O(n^2)$ on skewed trees. The sentinel approach computes height and checks balance in a single pass — always use this in interviews.
  * **Sentinel Choice**: Using $-1$ as the sentinel works because valid heights are always $\ge 0$.
* **Complexity**:
  * Time: $O(n)$
  * Space: $O(h)$

---

## 5. Same Tree (LeetCode 100) - Easy
* **Quick Links**: [LeetCode](https://leetcode.com/problems/same-tree/) • [NeetCode Problem](https://neetcode.io/problems/same-binary-tree) • [NeetCode Solution](https://neetcode.io/solutions/same-tree) • [YouTube Video](https://www.youtube.com/watch?v=vRbbcKXCxOw)
* **Pattern**: Simultaneous Structural & Value Traversal
* **Core Concept**:
  Two trees are identical if and only if $p.val == q.val$ and both their left and right subtrees are recursively identical. Base cases: both `None` → `True`; exactly one `None` → `False`.
* **Mental Model**:
  Two people reading the same book aloud simultaneously. If at any point one person reads a different word, or one book ends before the other, the books aren't identical.
* **Tips & Interview Tricks**:
  * **Three Base Cases**: (1) both `None` → `True`, (2) one `None` → `False`, (3) `p.val != q.val` → `False`. Get these right and the recursion handles itself.
  * **Building Block**: This function is reused directly in Subtree of Another Tree (LC 572) as the equivalence checker.
* **Complexity**:
  * Time: $O(n)$
  * Space: $O(h)$

---

## 6. Subtree of Another Tree (LeetCode 572) - Easy
* **Quick Links**: [LeetCode](https://leetcode.com/problems/subtree-of-another-tree/) • [NeetCode Problem](https://neetcode.io/problems/subtree-of-a-binary-tree) • [NeetCode Solution](https://neetcode.io/solutions/subtree-of-another-tree) • [YouTube Video](https://www.youtube.com/watch?v=E36O5SWp-LE)
* **Pattern**: Traversal with Subtree Equivalence
* **Core Concept**:
  A tree $T$ contains subtree $S$ if $T$ is identical to $S$ (using `isSameTree`), or $S$ is a subtree of $T.left$, or $S$ is a subtree of $T.right$. This is a two-function recursive pattern: an outer traversal and an inner equivalence check.
* **Mental Model**:
  Searching for a specific jigsaw puzzle piece (subtree) within a larger completed puzzle (main tree). At each node, try to match the piece starting from that node. If it doesn't fit, try the left and right children.
* **Tips & Interview Tricks**:
  * **$O(n \cdot m)$ is Acceptable**: The brute-force approach calls `isSameTree` (an $O(m)$ operation) at each of the $n$ nodes. Interviewers generally accept this. For the $O(n + m)$ follow-up, mention tree serialization + string matching (e.g., KMP or hashing).
  * **Null Subtree**: If `subRoot` is `None`, every tree contains it. If `root` is `None` but `subRoot` is not, return `False`.
* **Complexity**:
  * Time: $O(n \cdot m)$ in worst case
  * Space: $O(h)$

---

## 7. Lowest Common Ancestor of a BST (LeetCode 235) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) • [NeetCode Problem](https://neetcode.io/problems/lowest-common-ancestor-in-binary-search-tree) • [NeetCode Solution](https://neetcode.io/solutions/lowest-common-ancestor-of-a-binary-search-tree) • [YouTube Video](https://www.youtube.com/watch?v=gs2LMfuOR9k)
* **Pattern**: BST Value-Split Navigation
* **Core Concept**:
  In a BST, if both $p$ and $q$ are greater than $root.val$, search right. If both are smaller, search left. The first node where $p$ and $q$ diverge to different subtrees (or one matches $root$) is the LCA.
* **Mental Model**:
  Two hikers starting from the same trailhead (root). They walk together as long as both want to go the same direction. The moment their paths split, the fork in the trail is the LCA.
* **Tips & Interview Tricks**:
  * **BST Property Exploit**: This is $O(h)$, not $O(n)$. In a general binary tree (LC 236), finding the LCA requires visiting every node. The BST ordering lets us eliminate half the tree at each step.
  * **Iterative is Cleaner**: The iterative version (`while True: if p.val > root.val and q.val > root.val: root = root.right ...`) uses $O(1)$ space and is more concise than recursion for this problem.
* **Complexity**:
  * Time: $O(h)$
  * Space: $O(1)$ iterative

---

## 8. Binary Tree Level Order Traversal (LeetCode 102) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/binary-tree-level-order-traversal/) • [NeetCode Problem](https://neetcode.io/problems/level-order-traversal-of-binary-tree) • [NeetCode Solution](https://neetcode.io/solutions/binary-tree-level-order-traversal) • [YouTube Video](https://www.youtube.com/watch?v=6ZnyEApgFYg)
* **Pattern**: BFS with Fixed-Level Queue Snapshots
* **Core Concept**:
  Use `level_len = len(queue)` at the start of each while loop iteration to process all nodes of the current level together. This creates a "snapshot" of the level before child nodes are enqueued.
* **Mental Model**:
  A photographer taking group photos floor by floor. Everyone on the current floor poses together. Their children line up for the next floor's photo. The photographer doesn't mix floors.
* **Tips & Interview Tricks**:
  * **The `len(queue)` Snapshot**: This is the core BFS-by-level technique. Without it, you'd process nodes across levels indiscriminately. This pattern is reused in Right Side View (LC 199), Zigzag Traversal (LC 103), and many others.
  * **Collections.deque**: Always use `collections.deque` in Python for BFS — `popleft()` is $O(1)$ vs. `list.pop(0)` which is $O(n)$.
* **Complexity**:
  * Time: $O(n)$
  * Space: $O(n)$ queue width

---

## 9. Binary Tree Right Side View (LeetCode 199) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/binary-tree-right-side-view/) • [NeetCode Problem](https://neetcode.io/problems/binary-tree-right-side-view) • [NeetCode Solution](https://neetcode.io/solutions/binary-tree-right-side-view) • [YouTube Video](https://www.youtube.com/watch?v=d4zLyf32e3I)
* **Pattern**: BFS Level-End Capture
* **Core Concept**:
  In level-order BFS, the last element processed in each level is the rightmost visible node. Alternatively, use DFS visiting right children first, adding the first node encountered at each new depth.
* **Mental Model**:
  Standing to the right of a building and looking left. You can only see the rightmost room on each floor. BFS processes each floor, and the last room processed on each floor is what you'd see.
* **Tips & Interview Tricks**:
  * **DFS Alternative**: A DFS approach (`right` child first, then `left`) with a depth tracker is equally valid: `if depth == len(result): result.append(node.val)`. This adds the first node seen at each depth, which is the rightmost.
  * **Left Side View Variant**: If asked for the left side view, simply take the *first* element of each BFS level, or visit `left` before `right` in the DFS approach.
* **Complexity**:
  * Time: $O(n)$
  * Space: $O(n)$

---

## 10. Count Good Nodes in Binary Tree (LeetCode 1448) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/count-good-nodes-in-binary-tree/) • [NeetCode Problem](https://neetcode.io/problems/count-good-nodes-in-binary-tree) • [NeetCode Solution](https://neetcode.io/solutions/count-good-nodes-in-binary-tree) • [YouTube Video](https://www.youtube.com/watch?v=7cp5imvDzl4)
* **Pattern**: DFS with Path Maximum Accumulator
* **Core Concept**:
  Pass down the maximum value encountered on the path from root to the current node. A node is "good" if $node.val \ge max\_so\_far$. Update `max_so_far = max(max_so_far, node.val)` before recursing into children.
* **Mental Model**:
  Hiking up a mountain range. At each peak, look back at your trail. A peak is "good" if it's the highest point you've reached so far (no taller peak behind you blocks the view).
* **Tips & Interview Tricks**:
  * **Root is Always Good**: The root has no ancestors, so it's always a good node. Initialize `max_so_far = root.val` (or `float('-inf')`) to handle this automatically.
  * **Top-Down Pattern**: This is a classic top-down pre-order problem — the parent passes information *down* to children. Contrast with bottom-up problems (Diameter, Max Path Sum) where children report *up* to parents.
* **Complexity**:
  * Time: $O(n)$
  * Space: $O(h)$

---

## 11. Validate Binary Search Tree (LeetCode 98) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/validate-binary-search-tree/) • [NeetCode Problem](https://neetcode.io/problems/valid-binary-search-tree) • [NeetCode Solution](https://neetcode.io/solutions/validate-binary-search-tree) • [YouTube Video](https://www.youtube.com/watch?v=s6ATEkipzow)
* **Pattern**: DFS with Open Interval Bounding
* **Core Concept**:
  Every node must satisfy $low < node.val < high$. When going left, update $high = node.val$. When going right, update $low = node.val$. Initialize with `low = -inf, high = inf`.
* **Mental Model**:
  A hallway that narrows as you walk deeper. Going left tightens the ceiling (upper bound). Going right raises the floor (lower bound). If any node touches the walls, the BST is invalid.
* **Tips & Interview Tricks**:
  * **Common Mistake**: Checking only `node.left.val < node.val < node.right.val` is WRONG. A left child's right subtree could violate the BST property against a distant ancestor. The interval approach catches this.
  * **In-Order Alternative**: A valid BST's in-order traversal is strictly increasing. Maintain a `prev` variable and verify `node.val > prev` at each step. This is equally valid.
* **Complexity**:
  * Time: $O(n)$
  * Space: $O(h)$

---

## 12. Kth Smallest Element in a BST (LeetCode 230) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) • [NeetCode Problem](https://neetcode.io/problems/kth-smallest-integer-in-bst) • [NeetCode Solution](https://neetcode.io/solutions/kth-smallest-element-in-a-bst) • [YouTube Video](https://www.youtube.com/watch?v=5LUXSvjmGCw)
* **Pattern**: In-Order Traversal (Iterative Stack)
* **Core Concept**:
  In-order traversal (Left, Root, Right) traverses a BST in strictly ascending order. Pop $k$ nodes from the stack to find the $k$-th smallest. The iterative approach allows early termination after exactly $k$ pops.
* **Mental Model**:
  Reading a sorted dictionary page by page. In-order traversal is the BST equivalent of turning pages in order. Stop at the $k$-th page.
* **Tips & Interview Tricks**:
  * **Iterative Over Recursive**: The iterative stack approach is preferred because you can return immediately after the $k$-th pop without traversing the rest of the tree: `k -= 1; if k == 0: return node.val`.
  * **Follow-Up (Frequent Queries)**: If the BST is modified frequently and `kthSmallest` is called often, augment each node with a subtree count. This enables $O(h)$ queries by navigating based on left subtree size.
* **Complexity**:
  * Time: $O(h + k)$
  * Space: $O(h)$

---

## 13. Construct Binary Tree from Preorder & Inorder Traversal (LeetCode 105) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) • [NeetCode Problem](https://neetcode.io/problems/binary-tree-from-preorder-and-inorder-traversal) • [NeetCode Solution](https://neetcode.io/solutions/construct-binary-tree-from-preorder-and-inorder-traversal) • [YouTube Video](https://www.youtube.com/watch?v=ihj4IQGZ2zc)
* **Pattern**: Subtree Partitioning via Inorder Hash Map
* **Core Concept**:
  Preorder's first element is always the root. Find this root's index $m$ in `inorder` to split elements into left subtree ($[:m]$) and right subtree ($(m+1:]$). Use a hash map for $O(1)$ inorder index lookup. The number of left-subtree elements determines the split point in `preorder` as well.
* **Mental Model**:
  A factory assembly line. Preorder tells you *"who is the boss?"* (root first). Inorder tells you *"who sits to the left vs. right of the boss?"* Together, they uniquely reconstruct the org chart.
* **Tips & Interview Tricks**:
  * **Hash Map Lookup**: Pre-build `inorder_map = {val: idx for idx, val in enumerate(inorder)}` to avoid $O(n)$ linear search per recursion level, reducing total time from $O(n^2)$ to $O(n)$.
  * **Index Tracking**: Use a global `pre_idx` counter (or pass indices) rather than slicing arrays, which creates unnecessary copies.
* **Complexity**:
  * Time: $O(n)$ with hash map lookup
  * Space: $O(n)$

---

## 14. Binary Tree Maximum Path Sum (LeetCode 124) - Hard
* **Quick Links**: [LeetCode](https://leetcode.com/problems/binary-tree-maximum-path-sum/) • [NeetCode Problem](https://neetcode.io/problems/binary-tree-maximum-path-sum) • [NeetCode Solution](https://neetcode.io/solutions/binary-tree-maximum-path-sum) • [YouTube Video](https://www.youtube.com/watch?v=Hr5cWUld4vU)
* **Pattern**: Post-Order Path Combination with Global Max
* **Core Concept**:
  At each node, compute the max gain from left and right children (floored at 0 to reject negative paths). A complete path "turns" at $node$: $node.val + left\_gain + right\_gain$. Return $node.val + \max(left\_gain, right\_gain)$ to the parent (you can only extend one branch upward).
* **Mental Model**:
  A river system. Water can flow from any tributary through a junction and out another tributary. At each junction (node), the maximum water flow is the sum of the best left tributary + the junction itself + the best right tributary. But water flowing *uphill* to a parent can only take one branch.
* **Tips & Interview Tricks**:
  * **Floor at Zero**: `left_gain = max(dfs(node.left), 0)`. Flooring at 0 means "don't extend into a subtree if it would decrease the sum." This elegantly handles negative-value subtrees.
  * **Two Different Quantities**: The function *updates* `max_sum` with the "turning path" (`node.val + left + right`) but *returns* the "extending path" (`node.val + max(left, right)`) to the parent. Confusing these is the #1 bug.
  * **Negative Values**: The answer can be negative (e.g., tree `[-3]`). Initialize `max_sum = float('-inf')`, not `0`.
* **Complexity**:
  * Time: $O(n)$
  * Space: $O(h)$

---

## 15. Serialize and Deserialize Binary Tree (LeetCode 297) - Hard
* **Quick Links**: [LeetCode](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) • [NeetCode Problem](https://neetcode.io/problems/serialize-and-deserialize-binary-tree) • [NeetCode Solution](https://neetcode.io/solutions/serialize-and-deserialize-binary-tree) • [YouTube Video](https://www.youtube.com/watch?v=u4JAi2JJhI8)
* **Pattern**: Pre-Order DFS with Sentinel Tokens
* **Core Concept**:
  Serialize using preorder traversal, emitting `node.val` for real nodes and a sentinel token (e.g., `'N'`) for null nodes, separated by commas. Deserialize recursively by consuming tokens from left to right: read a token, create a node (or return `None` for sentinel), then recursively build its left and right children.
* **Mental Model**:
  Writing directions to rebuild a Lego structure. *"Place a 3-block, attach a 2-block to its left, nothing on 2's left, nothing on 2's right, attach a 5-block to 3's right..."* The sentinel tokens (`'N'`) tell the builder "stop extending this branch."
* **Tips & Interview Tricks**:
  * **Why Preorder + Nulls Works**: Preorder alone (without nulls) is ambiguous — multiple trees can produce the same preorder sequence. The null sentinels make the encoding unique and self-delimiting.
  * **Iterator for Deserialization**: Use `iter(tokens)` and `next(it)` to consume tokens sequentially. This avoids index tracking and is cleaner than popping from a list.
  * **BFS Alternative**: Level-order serialization also works and may be more intuitive for some. Both are valid in interviews.
* **Complexity**:
  * Time: $O(n)$
  * Space: $O(n)$
