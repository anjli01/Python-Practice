# Module 4.2: Graphs – Study Guide & Pattern Deep-Dive

Graph theory tests your understanding of **connectivity, traversal, cycle detection, and topological ordering**. The core formats include adjacency lists, 2D matrix grids, and functional graphs.

---

## 1. Number of Islands (LeetCode 200) - Medium
* **Pattern**: Grid DFS / Flood Fill
* **Core Concept**: Iterate through every cell. Upon discovering `'1'`, increment island count and trigger a DFS sinking all 4-directionally connected `'1'`s to `'0'`.
* **Complexity**: Time: $O(M \cdot N)$, Space: $O(M \cdot N)$ recursion stack.

---

## 2. Max Area of Island (LeetCode 695) - Medium
* **Pattern**: Component Size Accumulator DFS
* **Core Concept**: Return $1 + \sum \text{dfs}(\text{neighbors})$ from each land cell, zeroing visited land to prevent recount.
* **Complexity**: Time: $O(M \cdot N)$, Space: $O(M \cdot N)$.

---

## 3. Clone Graph (LeetCode 133) - Medium
* **Pattern**: DFS with Hash Map Mapping
* **Core Concept**: Map `old_node -> cloned_node`. Traverse neighbors; if a neighbor is already cloned, reuse the clone, otherwise create and recurse.
* **Complexity**: Time: $O(V + E)$, Space: $O(V)$.

---

## 4. Walls and Gates (LeetCode 286) - Medium
* **Pattern**: Multi-Source Simultaneous BFS
* **Core Concept**: Add all gates (`0`) to a queue. Expand outward level by level. When an empty room (`INF`) is reached, its distance is the current level counter.
* **Complexity**: Time: $O(M \cdot N)$, Space: $O(M \cdot N)$.

---

## 5. Rotting Oranges (LeetCode 994) - Medium
* **Pattern**: Multi-Source Level-Order BFS
* **Core Concept**: Enqueue all initially rotten oranges (`2`) and count fresh oranges (`1`). Each BFS level represents 1 minute rotting adjacent fresh oranges.
* **Complexity**: Time: $O(M \cdot N)$, Space: $O(M \cdot N)$.

---

## 6. Pacific Atlantic Water Flow (LeetCode 417) - Medium
* **Pattern**: Reverse Coastal Uphill Traversal
* **Core Concept**: Water flows downhill from cells to ocean. Equivalently, run DFS/BFS starting at the Pacific and Atlantic borders flowing **uphill** ($heights[next] \ge heights[curr]$). The intersection of both visited sets can reach both oceans.
* **Complexity**: Time: $O(M \cdot N)$, Space: $O(M \cdot N)$.

---

## 7. Surrounded Regions (LeetCode 130) - Medium
* **Pattern**: Border-Inversion Flood Fill
* **Core Concept**: Any `'O'` connected to the outer border cannot be surrounded. Run DFS from all border `'O'`s, marking them temporarily as `'T'`. Then flip remaining `'O'` $\to$ `'X'`, and revert `'T'` $\to$ `'O'`.
* **Complexity**: Time: $O(M \cdot N)$, Space: $O(M \cdot N)$.

---

## 8. Course Schedule (LeetCode 207) - Medium
* **Pattern**: Cycle Detection in Directed Graph (3-Color / Visiting Set DFS)
* **Core Concept**: Maintain `visiting` (current DFS path) and `visited` (fully explored and verified acyclic) sets. A cycle exists if a node is revisited while in `visiting`.
* **Complexity**: Time: $O(V + E)$, Space: $O(V + E)$.

---

## 9. Course Schedule II (LeetCode 210) - Medium
* **Pattern**: Kahn's Algorithm (In-Degree Topological Sort)
* **Core Concept**: Compute in-degrees for all nodes. Enqueue nodes with in-degree 0. As nodes are dequeued, decrement neighbor in-degrees; enqueue neighbors that reach in-degree 0. If order length equals $V$, a valid schedule exists.
* **Complexity**: Time: $O(V + E)$, Space: $O(V + E)$.

---

## 10. Graph Valid Tree (LeetCode 261) - Medium
* **Pattern**: Tree Equivalence Invariants
* **Core Concept**: An undirected graph of $n$ nodes is a valid tree if and only if:
  1. Exactly $n - 1$ edges exist.
  2. The graph is fully connected (DFS from node 0 visits all $n$ nodes with no cycles).
* **Complexity**: Time: $O(V + E)$, Space: $O(V + E)$.

---

## 11. Number of Connected Components (LeetCode 323) - Medium
* **Pattern**: Disjoint Set Union (Union-Find with Path Compression)
* **Core Concept**: Start with $n$ components. For each edge $(u, v)$, perform `union(u, v)`. If $u$ and $v$ were in different components, decrement component count by 1.
* **Complexity**: Time: $O(E \cdot \alpha(V)) \approx O(E)$, Space: $O(V)$.

---

## 12. Redundant Connection (LeetCode 684) - Medium
* **Pattern**: Union-Find Cycle Edge Identification
* **Core Concept**: Process edges sequentially. For edge $(u, v)$, if `find(u) == find(v)`, the edge connects two already-connected nodes and forms a cycle. Return $[u, v]$.
* **Complexity**: Time: $O(E \cdot \alpha(V))$, Space: $O(V)$.

---

## 13. Word Ladder (LeetCode 127) - Hard
* **Pattern**: BFS Shortest Path with Generic Wildcard Buckets
* **Core Concept**: Pre-process words into generic wildcard buckets (e.g., `"h*t" -> ["hot", "hit"]`). Run BFS from `beginWord`; the first time `endWord` is popped, the shortest transformation sequence is guaranteed.
* **Complexity**: Time: $O(M^2 \cdot N)$ where $M$ is word length and $N$ is word count, Space: $O(M^2 \cdot N)$.
