# Module 4.2: Graphs – Study Guide & Pattern Deep-Dive

Graph theory tests your understanding of **connectivity, traversal, cycle detection, and topological ordering**. The core formats include adjacency lists, 2D matrix grids, and functional graphs.

---

## 1. Number of Islands (LeetCode 200) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/number-of-islands/) • [NeetCode Problem](https://neetcode.io/problems/count-number-of-islands) • [NeetCode Solution](https://neetcode.io/solutions/number-of-islands) • [YouTube Video](https://www.youtube.com/watch?v=pV2kpPD66nE)
* **Pattern**: Grid DFS / Flood Fill
* **Core Concept**:
  Iterate through every cell. Upon discovering `'1'`, increment island count and trigger a DFS/BFS sinking all 4-directionally connected `'1'`s to `'0'`. This ensures each island is counted exactly once.
* **Mental Model**:
  Painting over islands on a map. When you find a land cell, pour paint over it and watch it flood-fill the entire island. Count how many times you had to start a new paint pour.
* **Tips & Interview Tricks**:
  * **In-Place Modification**: Sinking `'1'` → `'0'` eliminates the need for a separate `visited` set, saving $O(M \cdot N)$ space. Mention this trade-off: it modifies the input, which may not be acceptable in some interviews.
  * **BFS vs. DFS**: DFS can hit Python's recursion limit on very large grids. BFS with a deque avoids this. Mention both options.
* **Complexity**:
  * Time: $O(M \cdot N)$
  * Space: $O(M \cdot N)$ recursion stack (DFS) or queue (BFS)

---

## 2. Max Area of Island (LeetCode 695) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/max-area-of-island/) • [NeetCode Problem](https://neetcode.io/problems/max-area-of-island) • [NeetCode Solution](https://neetcode.io/solutions/max-area-of-island) • [YouTube Video](https://www.youtube.com/watch?v=iJGr1OtmH0c)
* **Pattern**: Component Size Accumulator DFS
* **Core Concept**:
  Return $1 + \sum \text{dfs}(\text{neighbors})$ from each land cell, zeroing visited land to prevent recount. Track the maximum area across all DFS calls.
* **Mental Model**:
  Counting tiles in each room of a building by walking through connected tiles. Each DFS call returns the room size. The largest room wins.
* **Tips & Interview Tricks**:
  * **Return Value Accumulation**: The DFS function should return the area count, not use a global counter. `return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)` is cleaner and less error-prone than mutating a shared variable.
  * **Identical to Number of Islands**: The only difference is tracking area instead of count. If you can solve one, you can solve the other.
* **Complexity**:
  * Time: $O(M \cdot N)$
  * Space: $O(M \cdot N)$

---

## 3. Clone Graph (LeetCode 133) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/clone-graph/) • [NeetCode Problem](https://neetcode.io/problems/clone-graph) • [NeetCode Solution](https://neetcode.io/solutions/clone-graph) • [YouTube Video](https://www.youtube.com/watch?v=mQeF6bN8hMk)
* **Pattern**: DFS with Hash Map Mapping
* **Core Concept**:
  Map `old_node -> cloned_node` in a hash map. Traverse neighbors; if a neighbor is already cloned, reuse the clone, otherwise create a new clone and recurse. The hash map serves double duty as both a clone registry and a visited set.
* **Mental Model**:
  Photocopying an organizational chart. Whenever you encounter a person, check if you've already made their copy. If yes, use it. If not, make a new copy and then copy all their connections.
* **Tips & Interview Tricks**:
  * **Hash Map = Visited Set**: The `old_to_new` map eliminates the need for a separate `visited` set. If `node in old_to_new`, it's already been cloned and visited.
  * **BFS Alternative**: A BFS approach works identically — clone nodes as they enter the queue. Both DFS and BFS are $O(V + E)$.
* **Complexity**:
  * Time: $O(V + E)$
  * Space: $O(V)$

---

## 4. Walls and Gates (LeetCode 286) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/walls-and-gates/) • [NeetCode Problem](https://neetcode.io/problems/islands-and-treasure) • [NeetCode Solution](https://neetcode.io/solutions/walls-and-gates) • [YouTube Video](https://www.youtube.com/watch?v=e69C6xhiSQE)
* **Pattern**: Multi-Source Simultaneous BFS
* **Core Concept**:
  Add all gates (`0`) to a queue simultaneously. Expand outward level by level. When an empty room (`INF`) is reached, its distance is the current level counter. Because BFS is run from all gates at once, each room is guaranteed to receive the shortest distance to any gate.
* **Mental Model**:
  Dropping pebbles into a pond from multiple points simultaneously. The ripples from each pebble expand outward in rings. Each empty room is reached by the closest ripple first.
* **Tips & Interview Tricks**:
  * **Multi-Source BFS**: The key insight is initializing the queue with ALL gates, not running BFS from each gate separately. Separate BFS per gate is $O(k \cdot M \cdot N)$; simultaneous BFS is $O(M \cdot N)$.
  * **Only Visit `INF` Cells**: When a cell already has a value < `INF`, it was already reached by a closer gate. Skip it.
* **Complexity**:
  * Time: $O(M \cdot N)$
  * Space: $O(M \cdot N)$

---

## 5. Rotting Oranges (LeetCode 994) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/rotting-oranges/) • [NeetCode Problem](https://neetcode.io/problems/rotting-fruit) • [NeetCode Solution](https://neetcode.io/solutions/rotting-oranges) • [YouTube Video](https://www.youtube.com/watch?v=y704fEOx0s0)
* **Pattern**: Multi-Source Level-Order BFS
* **Core Concept**:
  Enqueue all initially rotten oranges (`2`) and count fresh oranges (`1`). Each BFS level represents 1 minute, rotting all adjacent fresh oranges simultaneously. When the queue empties, if fresh oranges remain, return $-1$. Otherwise, return the number of minutes elapsed.
* **Mental Model**:
  A zombie outbreak. All initially infected (rotten) oranges spread the infection to adjacent healthy oranges each minute. Track how many minutes until all oranges are infected — or determine it's impossible if some are unreachable.
* **Tips & Interview Tricks**:
  * **Track Fresh Count**: Maintain a `fresh` counter decremented whenever an orange rots. At the end, if `fresh > 0`, isolated oranges exist and the answer is $-1$.
  * **Time = BFS Levels - 1**: The initial rotten oranges are at time 0. The first round of rotting is time 1. Be careful with off-by-one: return `max(0, time)` to handle the edge case of no fresh oranges.
* **Complexity**:
  * Time: $O(M \cdot N)$
  * Space: $O(M \cdot N)$

---

## 6. Pacific Atlantic Water Flow (LeetCode 417) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/pacific-atlantic-water-flow/) • [NeetCode Problem](https://neetcode.io/problems/pacific-atlantic-water-flow) • [NeetCode Solution](https://neetcode.io/solutions/pacific-atlantic-water-flow) • [YouTube Video](https://www.youtube.com/watch?v=s-VkcjHqkGI)
* **Pattern**: Reverse Coastal Uphill Traversal
* **Core Concept**:
  Water flows downhill from cells to ocean. Equivalently, run DFS/BFS starting at the Pacific and Atlantic borders flowing **uphill** ($heights[next] \ge heights[curr]$). The intersection of both visited sets can reach both oceans.
* **Mental Model**:
  Instead of asking *"Where does rain flow?"*, ask *"How far inland can each ocean reach?"* Start at the coastline and push upstream. Cells reachable from both coasts are the answer.
* **Tips & Interview Tricks**:
  * **Reverse Thinking**: The naive approach (DFS from every cell to see if it reaches both oceans) is $O((MN)^2)$. The reverse approach (two DFS passes from ocean borders) is $O(MN)$. Always explain why the reverse is better.
  * **Two Separate Sets**: Maintain `pacific_reachable` and `atlantic_reachable` as sets. The answer is their intersection: `pacific_reachable & atlantic_reachable`.
* **Complexity**:
  * Time: $O(M \cdot N)$
  * Space: $O(M \cdot N)$

---

## 7. Surrounded Regions (LeetCode 130) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/surrounded-regions/) • [NeetCode Problem](https://neetcode.io/problems/surrounded-regions) • [NeetCode Solution](https://neetcode.io/solutions/surrounded-regions) • [YouTube Video](https://www.youtube.com/watch?v=9z2BunfoZ5Y)
* **Pattern**: Border-Inversion Flood Fill
* **Core Concept**:
  Any `'O'` connected to the outer border cannot be surrounded. Run DFS from all border `'O'`s, marking them temporarily as `'T'`. Then flip remaining `'O'` → `'X'` (these are truly surrounded), and revert `'T'` → `'O'` (these touch the border).
* **Mental Model**:
  A castle under siege. The enemy (X) captures all regions except those connected to the castle walls (border). First, mark all border-connected safe zones, then capture everything else.
* **Tips & Interview Tricks**:
  * **Three-Phase Process**: (1) Mark border-connected `'O'`s as `'T'`, (2) flip all remaining `'O'` → `'X'`, (3) revert `'T'` → `'O'`. This is cleaner than trying to determine "surrounded" directly.
  * **Same Pattern as Pacific Atlantic**: Both problems use "start from the boundary and work inward." Recognizing this pattern transfers between problems.
* **Complexity**:
  * Time: $O(M \cdot N)$
  * Space: $O(M \cdot N)$

---

## 8. Course Schedule (LeetCode 207) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/course-schedule/) • [NeetCode Problem](https://neetcode.io/problems/course-schedule) • [NeetCode Solution](https://neetcode.io/solutions/course-schedule) • [YouTube Video](https://www.youtube.com/watch?v=EgI5nU9etnU)
* **Pattern**: Cycle Detection in Directed Graph (3-Color / Visiting Set DFS)
* **Core Concept**:
  Maintain `visiting` (current DFS path) and `visited` (fully explored and verified acyclic) sets. A cycle exists if a node is revisited while in `visiting`. If a node is in `visited`, it's already verified safe — skip it.
* **Mental Model**:
  Following a chain of prerequisites. If you ever loop back to a course you're currently trying to verify, you've found a circular dependency — impossible to complete.
* **Tips & Interview Tricks**:
  * **Optimization**: When DFS completes for a node without finding a cycle, move it from `visiting` to `visited` and clear its adjacency list (`graph[node] = []`). This prevents redundant exploration from other entry points.
  * **Adjacency List Construction**: Use `defaultdict(list)` and add edges: `for a, b in prerequisites: graph[a].append(b)`.
* **Complexity**:
  * Time: $O(V + E)$
  * Space: $O(V + E)$

---

## 9. Course Schedule II (LeetCode 210) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/course-schedule-ii/) • [NeetCode Problem](https://neetcode.io/problems/course-schedule-ii) • [NeetCode Solution](https://neetcode.io/solutions/course-schedule-ii) • [YouTube Video](https://www.youtube.com/watch?v=Akt3glAwyfY)
* **Pattern**: Kahn's Algorithm (In-Degree Topological Sort)
* **Core Concept**:
  Compute in-degrees for all nodes. Enqueue nodes with in-degree 0. As nodes are dequeued, decrement neighbor in-degrees; enqueue neighbors that reach in-degree 0. If the order length equals $V$, a valid schedule exists; otherwise, a cycle prevents completion.
* **Mental Model**:
  Peeling an onion layer by layer. Courses with no remaining prerequisites (in-degree 0) are "exposed" and can be taken. Completing them exposes new courses whose prerequisites are now satisfied.
* **Tips & Interview Tricks**:
  * **Kahn's vs. DFS Topological Sort**: Kahn's (BFS-based) naturally detects cycles (output length < $V$) and produces the ordering iteratively. DFS-based topological sort appends to a stack in post-order. Know both.
  * **Cycle Detection**: If `len(order) != numCourses`, a cycle exists. Return `[]`.
* **Complexity**:
  * Time: $O(V + E)$
  * Space: $O(V + E)$

---

## 10. Graph Valid Tree (LeetCode 261) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/graph-valid-tree/) • [NeetCode Problem](https://neetcode.io/problems/valid-tree) • [NeetCode Solution](https://neetcode.io/solutions/graph-valid-tree) • [YouTube Video](https://www.youtube.com/watch?v=bXsUuownnoQ)
* **Pattern**: Tree Equivalence Invariants
* **Core Concept**:
  An undirected graph of $n$ nodes is a valid tree if and only if:
  1. Exactly $n - 1$ edges exist (necessary for acyclicity with connectivity).
  2. The graph is fully connected (DFS/BFS from node 0 visits all $n$ nodes).
* **Mental Model**:
  A valid tree is a *connected graph with no wasted roads*. If you have $n$ cities, you need exactly $n - 1$ roads to connect them all without any loops. Fewer roads = disconnected. More roads = cycles.
* **Tips & Interview Tricks**:
  * **Quick Edge Count Check**: If `len(edges) != n - 1`, return `False` immediately. This $O(1)$ check eliminates many cases before traversal.
  * **Union-Find Alternative**: Instead of DFS, Union-Find can detect both connectivity and cycles in a single pass through the edges. If `union(u, v)` finds $u$ and $v$ already connected, a cycle exists.
* **Complexity**:
  * Time: $O(V + E)$
  * Space: $O(V + E)$

---

## 11. Number of Connected Components (LeetCode 323) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) • [NeetCode Problem](https://neetcode.io/problems/count-connected-components) • [NeetCode Solution](https://neetcode.io/solutions/number-of-connected-components-in-an-undirected-graph) • [YouTube Video](https://www.youtube.com/watch?v=8f1XPm4WOUc)
* **Pattern**: Disjoint Set Union (Union-Find with Path Compression)
* **Core Concept**:
  Start with $n$ components. For each edge $(u, v)$, perform `union(u, v)`. If $u$ and $v$ were in different components, decrement component count by 1. Path compression and union by rank ensure near-constant time per operation.
* **Mental Model**:
  Islands connected by bridges. Initially, each island is its own country. Each bridge merges two countries into one. Count the remaining distinct countries at the end.
* **Tips & Interview Tricks**:
  * **Union-Find Template**: Memorize the 3 components: `parent[]` array, `find(x)` with path compression (`parent[x] = find(parent[x])`), and `union(x, y)` with rank-based merging. This template applies to dozens of graph problems.
  * **DFS Alternative**: Simple DFS counting connected components also works in $O(V + E)$ and is easier to code. Use Union-Find when the problem involves dynamic edge additions or requires merging operations.
* **Complexity**:
  * Time: $O(E \cdot \alpha(V)) \approx O(E)$
  * Space: $O(V)$

---

## 12. Redundant Connection (LeetCode 684) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/redundant-connection/) • [NeetCode Problem](https://neetcode.io/problems/redundant-connection) • [NeetCode Solution](https://neetcode.io/solutions/redundant-connection) • [YouTube Video](https://www.youtube.com/watch?v=1lNK80tOTfc)
* **Pattern**: Union-Find Cycle Edge Identification
* **Core Concept**:
  Process edges sequentially. For edge $(u, v)$, if `find(u) == find(v)`, the edge connects two already-connected nodes and forms a cycle. Return $[u, v]$ as the redundant edge. Since edges are processed in order, the last cycle-forming edge is the answer.
* **Mental Model**:
  Building a road network. Each new road connects two towns. The moment you build a road between two towns that are already reachable from each other, that road is redundant — it creates a loop.
* **Tips & Interview Tricks**:
  * **Why Union-Find Over DFS?**: Union-Find naturally processes edges incrementally. DFS would require rebuilding the graph for each edge candidate, making it less elegant for this problem.
  * **"Last" Redundant Edge**: The problem guarantees exactly one extra edge. The last edge that forms a cycle (in the given order) is the answer.
* **Complexity**:
  * Time: $O(E \cdot \alpha(V))$
  * Space: $O(V)$

---

## 13. Word Ladder (LeetCode 127) - Hard
* **Quick Links**: [LeetCode](https://leetcode.com/problems/word-ladder/) • [NeetCode Problem](https://neetcode.io/problems/word-ladder) • [NeetCode Solution](https://neetcode.io/solutions/word-ladder) • [YouTube Video](https://www.youtube.com/watch?v=h9iTnkgv05E)
* **Pattern**: BFS Shortest Path with Generic Wildcard Buckets
* **Core Concept**:
  Pre-process words into generic wildcard buckets (e.g., `"h*t" -> ["hot", "hit"]`). Run BFS from `beginWord`; the first time `endWord` is reached, the current BFS level is the shortest transformation sequence length. BFS guarantees shortest path in an unweighted graph.
* **Mental Model**:
  A word mutation game. Each word can mutate into any word that differs by exactly one letter. BFS explores all single-mutation neighbors level by level, finding the shortest mutation chain.
* **Tips & Interview Tricks**:
  * **Wildcard Buckets vs. Pairwise Comparison**: Comparing every word pair is $O(N^2 \cdot M)$. Wildcard buckets reduce neighbor lookup to $O(M \cdot 26)$ per word by generating all possible single-character mutations.
  * **Bidirectional BFS**: For the ultimate optimization, run BFS from both `beginWord` and `endWord` simultaneously, alternating between the two frontiers. When they meet, the path is found. This reduces time from $O(26^{M/2})$ to $O(2 \cdot 26^{M/4})$.
  * **Return Sequence Length, Not Steps**: The answer is the number of words in the transformation sequence (including start and end), not the number of transformations. Off-by-one here is common.
* **Complexity**:
  * Time: $O(M^2 \cdot N)$ where $M$ is word length and $N$ is word count
  * Space: $O(M^2 \cdot N)$
