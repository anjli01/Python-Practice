# Module 4.2: Graphs – Study Guide & Pattern Deep-Dive

Graph theory tests your understanding of **connectivity, traversal, cycle detection, and topological ordering**. The core formats include adjacency lists, 2D matrix grids, and functional graphs.

---

## 1. Number of Islands (LeetCode 200) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/number-of-islands/) • [NeetCode Problem](https://neetcode.io/problems/count-number-of-islands) • [NeetCode Solution](https://neetcode.io/solutions/number-of-islands) • [YouTube Video](https://www.youtube.com/watch?v=pV2kpPD66nE)
* **Pattern**: Grid DFS / Flood Fill
* **Core Concept**: Iterate through every cell. Upon discovering `'1'`, increment island count and trigger a DFS sinking all 4-directionally connected `'1'`s to `'0'`.
* **Complexity**: Time: $O(M \cdot N)$, Space: $O(M \cdot N)$ recursion stack.

---

## 2. Max Area of Island (LeetCode 695) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/max-area-of-island/) • [NeetCode Problem](https://neetcode.io/problems/max-area-of-island) • [NeetCode Solution](https://neetcode.io/solutions/max-area-of-island) • [YouTube Video](https://www.youtube.com/watch?v=iJGr1OtmH0c)
* **Pattern**: Component Size Accumulator DFS
* **Core Concept**: Return $1 + \sum \text{dfs}(\text{neighbors})$ from each land cell, zeroing visited land to prevent recount.
* **Complexity**: Time: $O(M \cdot N)$, Space: $O(M \cdot N)$.

---

## 3. Clone Graph (LeetCode 133) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/clone-graph/) • [NeetCode Problem](https://neetcode.io/problems/clone-graph) • [NeetCode Solution](https://neetcode.io/solutions/clone-graph) • [YouTube Video](https://www.youtube.com/watch?v=mQeF6bN8hMk)
* **Pattern**: DFS with Hash Map Mapping
* **Core Concept**: Map `old_node -> cloned_node`. Traverse neighbors; if a neighbor is already cloned, reuse the clone, otherwise create and recurse.
* **Complexity**: Time: $O(V + E)$, Space: $O(V)$.

---

## 4. Walls and Gates (LeetCode 286) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/walls-and-gates/) • [NeetCode Problem](https://neetcode.io/problems/islands-and-treasure) • [NeetCode Solution](https://neetcode.io/solutions/walls-and-gates) • [YouTube Video](https://www.youtube.com/watch?v=e69C6xhiSQE)
* **Pattern**: Multi-Source Simultaneous BFS
* **Core Concept**: Add all gates (`0`) to a queue. Expand outward level by level. When an empty room (`INF`) is reached, its distance is the current level counter.
* **Complexity**: Time: $O(M \cdot N)$, Space: $O(M \cdot N)$.

---

## 5. Rotting Oranges (LeetCode 994) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/rotting-oranges/) • [NeetCode Problem](https://neetcode.io/problems/rotting-fruit) • [NeetCode Solution](https://neetcode.io/solutions/rotting-oranges) • [YouTube Video](https://www.youtube.com/watch?v=y704fEOx0s0)
* **Pattern**: Multi-Source Level-Order BFS
* **Core Concept**: Enqueue all initially rotten oranges (`2`) and count fresh oranges (`1`). Each BFS level represents 1 minute rotting adjacent fresh oranges.
* **Complexity**: Time: $O(M \cdot N)$, Space: $O(M \cdot N)$.

---

## 6. Pacific Atlantic Water Flow (LeetCode 417) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/pacific-atlantic-water-flow/) • [NeetCode Problem](https://neetcode.io/problems/pacific-atlantic-water-flow) • [NeetCode Solution](https://neetcode.io/solutions/pacific-atlantic-water-flow) • [YouTube Video](https://www.youtube.com/watch?v=s-VkcjHqkGI)
* **Pattern**: Reverse Coastal Uphill Traversal
* **Core Concept**: Water flows downhill from cells to ocean. Equivalently, run DFS/BFS starting at the Pacific and Atlantic borders flowing **uphill** ($heights[next] \ge heights[curr]$). The intersection of both visited sets can reach both oceans.
* **Complexity**: Time: $O(M \cdot N)$, Space: $O(M \cdot N)$.

---

## 7. Surrounded Regions (LeetCode 130) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/surrounded-regions/) • [NeetCode Problem](https://neetcode.io/problems/surrounded-regions) • [NeetCode Solution](https://neetcode.io/solutions/surrounded-regions) • [YouTube Video](https://www.youtube.com/watch?v=9z2BunfoZ5Y)
* **Pattern**: Border-Inversion Flood Fill
* **Core Concept**: Any `'O'` connected to the outer border cannot be surrounded. Run DFS from all border `'O'`s, marking them temporarily as `'T'`. Then flip remaining `'O'` $\to$ `'X'`, and revert `'T'` $\to$ `'O'`.
* **Complexity**: Time: $O(M \cdot N)$, Space: $O(M \cdot N)$.

---

## 8. Course Schedule (LeetCode 207) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/course-schedule/) • [NeetCode Problem](https://neetcode.io/problems/course-schedule) • [NeetCode Solution](https://neetcode.io/solutions/course-schedule) • [YouTube Video](https://www.youtube.com/watch?v=EgI5nU9etnU)
* **Pattern**: Cycle Detection in Directed Graph (3-Color / Visiting Set DFS)
* **Core Concept**: Maintain `visiting` (current DFS path) and `visited` (fully explored and verified acyclic) sets. A cycle exists if a node is revisited while in `visiting`.
* **Complexity**: Time: $O(V + E)$, Space: $O(V + E)$.

---

## 9. Course Schedule II (LeetCode 210) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/course-schedule-ii/) • [NeetCode Problem](https://neetcode.io/problems/course-schedule-ii) • [NeetCode Solution](https://neetcode.io/solutions/course-schedule-ii) • [YouTube Video](https://www.youtube.com/watch?v=Akt3glAwyfY)
* **Pattern**: Kahn's Algorithm (In-Degree Topological Sort)
* **Core Concept**: Compute in-degrees for all nodes. Enqueue nodes with in-degree 0. As nodes are dequeued, decrement neighbor in-degrees; enqueue neighbors that reach in-degree 0. If order length equals $V$, a valid schedule exists.
* **Complexity**: Time: $O(V + E)$, Space: $O(V + E)$.

---

## 10. Graph Valid Tree (LeetCode 261) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/graph-valid-tree/) • [NeetCode Problem](https://neetcode.io/problems/valid-tree) • [NeetCode Solution](https://neetcode.io/solutions/graph-valid-tree) • [YouTube Video](https://www.youtube.com/watch?v=bXsUuownnoQ)
* **Pattern**: Tree Equivalence Invariants
* **Core Concept**: An undirected graph of $n$ nodes is a valid tree if and only if:
  1. Exactly $n - 1$ edges exist.
  2. The graph is fully connected (DFS from node 0 visits all $n$ nodes with no cycles).
* **Complexity**: Time: $O(V + E)$, Space: $O(V + E)$.

---

## 11. Number of Connected Components (LeetCode 323) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) • [NeetCode Problem](https://neetcode.io/problems/count-connected-components) • [NeetCode Solution](https://neetcode.io/solutions/number-of-connected-components-in-an-undirected-graph) • [YouTube Video](https://www.youtube.com/watch?v=8f1XPm4WOUc)
* **Pattern**: Disjoint Set Union (Union-Find with Path Compression)
* **Core Concept**: Start with $n$ components. For each edge $(u, v)$, perform `union(u, v)`. If $u$ and $v$ were in different components, decrement component count by 1.
* **Complexity**: Time: $O(E \cdot \alpha(V)) \approx O(E)$, Space: $O(V)$.

---

## 12. Redundant Connection (LeetCode 684) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/redundant-connection/) • [NeetCode Problem](https://neetcode.io/problems/redundant-connection) • [NeetCode Solution](https://neetcode.io/solutions/redundant-connection) • [YouTube Video](https://www.youtube.com/watch?v=1lNK80tOTfc)
* **Pattern**: Union-Find Cycle Edge Identification
* **Core Concept**: Process edges sequentially. For edge $(u, v)$, if `find(u) == find(v)`, the edge connects two already-connected nodes and forms a cycle. Return $[u, v]$.
* **Complexity**: Time: $O(E \cdot \alpha(V))$, Space: $O(V)$.

---

## 13. Word Ladder (LeetCode 127) - Hard
* **Quick Links**: [LeetCode](https://leetcode.com/problems/word-ladder/) • [NeetCode Problem](https://neetcode.io/problems/word-ladder) • [NeetCode Solution](https://neetcode.io/solutions/word-ladder) • [YouTube Video](https://www.youtube.com/watch?v=h9iTnkgv05E)
* **Pattern**: BFS Shortest Path with Generic Wildcard Buckets
* **Core Concept**: Pre-process words into generic wildcard buckets (e.g., `"h*t" -> ["hot", "hit"]`). Run BFS from `beginWord`; the first time `endWord` is popped, the shortest transformation sequence is guaranteed.
* **Complexity**: Time: $O(M^2 \cdot N)$ where $M$ is word length and $N$ is word count, Space: $O(M^2 \cdot N)$.
