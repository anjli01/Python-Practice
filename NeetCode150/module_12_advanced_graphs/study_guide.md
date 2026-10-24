# Module 4.3: Advanced Graphs – Study Guide & Pattern Deep-Dive

Advanced Graph problems elevate foundational graph concepts to **weighted edges, minimum spanning trees, Eulerian paths, and shortest paths with state constraints**.

---

## 1. Reconstruct Itinerary (LeetCode 332) - Hard
* **Pattern**: Hierholzer's Algorithm (Eulerian Path)
* **Core Concept**:
  An Eulerian path visits every edge exactly once. Sort destination edges reverse-lexicographically. Greedily advance; when a vertex has no remaining outgoing edges, append it to the itinerary. The final itinerary is the reverse of this post-order sequence.
* **Complexity**: Time: $O(E \log E)$, Space: $O(V + E)$.

---

## 2. Min Cost to Connect All Points (LeetCode 1584) - Medium
* **Pattern**: Prim's Algorithm (Minimum Spanning Tree)
* **Core Concept**:
  Grow a tree by greedily adding the cheapest edge that connects an unvisited node to the visited component using a Min-Heap.
* **Complexity**: Time: $O(N^2 \log N)$, Space: $O(N^2)$.

---

## 3. Network Delay Time (LeetCode 743) - Medium
* **Pattern**: Dijkstra's Algorithm (Single-Source Shortest Path)
* **Core Concept**:
  Maintain a min-heap of `(accumulated_time, node)`. Greedily pop the minimum time node, record its shortest path, and relax outgoing edges.
* **Complexity**: Time: $O(E \log V)$, Space: $O(V + E)$.

---

## 4. Swim in Rising Water (LeetCode 778) - Hard
* **Pattern**: Modified Dijkstra / Min-Max Path
* **Core Concept**:
  Find a path from $(0, 0)$ to $(N-1, N-1)$ minimizing the maximum cell elevation encountered. Use a Min-Heap of `(max_elevation, r, c)`.
* **Complexity**: Time: $O(N^2 \log N)$, Space: $O(N^2)$.

---

## 5. Alien Dictionary (LeetCode 269) - Hard
* **Pattern**: Lexicographical Graph + Topological Sort
* **Core Concept**:
  Compare adjacent words. The first differing character between `words[i]` and `words[i+1]` defines a directed dependency $c_1 \to c_2$. Run topological sort to find the character order. Return `""` if a cycle is detected or if an invalid prefix ordering occurs (e.g., `"apple"` before `"app"`).
* **Complexity**: Time: $O(C)$ total characters, Space: $O(1)$ (26 letters).

---

## 6. Cheapest Flights Within K Stops (LeetCode 787) - Medium
* **Pattern**: Bellman-Ford with Step Limit
* **Core Concept**:
  Run $k + 1$ iterations of edge relaxation using a cloned price array from the previous step. The snapshot array ensures each iteration uses strictly $\le$ one additional flight hop.
* **Complexity**: Time: $O(K \cdot E)$, Space: $O(V)$.
