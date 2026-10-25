# Module 4.3: Advanced Graphs – Study Guide & Pattern Deep-Dive

Advanced Graph problems elevate foundational graph concepts to **weighted edges, minimum spanning trees, Eulerian paths, and shortest paths with state constraints**.

---

## 1. Reconstruct Itinerary (LeetCode 332) - Hard
* **Quick Links**: [LeetCode](https://leetcode.com/problems/reconstruct-itinerary/) • [NeetCode Problem](https://neetcode.io/problems/reconstruct-flight-path) • [NeetCode Solution](https://neetcode.io/solutions/reconstruct-itinerary) • [YouTube Video](https://www.youtube.com/watch?v=ZyB_gQ8vqGA)
* **Pattern**: Hierholzer's Algorithm (Eulerian Path)
* **Core Concept**:
  An Eulerian path visits every edge exactly once. Sort destination edges in reverse-lexicographic order (so the smallest destination is popped last). Greedily advance by popping destinations; when a vertex has no remaining outgoing edges, append it to the itinerary. The final itinerary is the reverse of this post-order sequence.
* **Mental Model**:
  A traveler with a stack of boarding passes sorted alphabetically. At each airport, use the alphabetically smallest available ticket. When you're stuck (no more tickets from this airport), write down the airport name. The final journal, read backwards, is the optimal itinerary.
* **Tips & Interview Tricks**:
  * **Why Reverse-Sorted + Pop?**: Use `adj[src].sort(reverse=True)` so that `adj[src].pop()` yields the lexicographically smallest destination in $O(1)$. Alternatively, use `collections.deque` or a `SortedList`.
  * **Post-Order Reversal**: The key insight is that dead-end airports get recorded first. Reversing at the end correctly reconstructs the path. This is non-intuitive — practice it.
* **Complexity**:
  * Time: $O(E \log E)$
  * Space: $O(V + E)$

---

## 2. Min Cost to Connect All Points (LeetCode 1584) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/min-cost-to-connect-all-points/) • [NeetCode Problem](https://neetcode.io/problems/min-cost-to-connect-points) • [NeetCode Solution](https://neetcode.io/solutions/min-cost-to-connect-all-points) • [YouTube Video](https://www.youtube.com/watch?v=f7JOBJIC-NA)
* **Pattern**: Prim's Algorithm (Minimum Spanning Tree)
* **Core Concept**:
  Grow a tree by greedily adding the cheapest edge that connects an unvisited node to the visited component. Use a Min-Heap of `(cost, node)`. Start from any node, and repeatedly pop the cheapest edge to an unvisited node until all nodes are connected.
* **Mental Model**:
  Building a power grid. Start from one house. Always extend the grid to the nearest unconnected house. Repeat until every house has power. The result is the cheapest possible network.
* **Tips & Interview Tricks**:
  * **Prim's vs. Kruskal's**: For dense graphs (like this one where every pair of points is connected), Prim's with a heap is $O(N^2 \log N)$. Kruskal's requires sorting all $O(N^2)$ edges, giving $O(N^2 \log N)$ as well, but with higher constant factors.
  * **Manhattan Distance**: The cost between points is $|x_1 - x_2| + |y_1 - y_2|$. Don't use Euclidean distance.
  * **Visited Check**: After popping from the heap, check `if node in visited: continue`. This avoids processing stale heap entries.
* **Complexity**:
  * Time: $O(N^2 \log N)$
  * Space: $O(N^2)$

---

## 3. Network Delay Time (LeetCode 743) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/network-delay-time/) • [NeetCode Problem](https://neetcode.io/problems/network-delay-time) • [NeetCode Solution](https://neetcode.io/solutions/network-delay-time) • [YouTube Video](https://www.youtube.com/watch?v=EaphyqKU4PQ)
* **Pattern**: Dijkstra's Algorithm (Single-Source Shortest Path)
* **Core Concept**:
  Maintain a min-heap of `(accumulated_time, node)`. Greedily pop the minimum-time node, record its shortest path time, and relax outgoing edges by pushing `(time + edge_weight, neighbor)` onto the heap. When all reachable nodes are visited, the maximum recorded time is the network delay.
* **Mental Model**:
  Sending a signal through a network of wires with varying transmission delays. The signal radiates outward, always reaching the closest un-signaled node next. The last node to receive the signal determines the total delay.
* **Tips & Interview Tricks**:
  * **Dijkstra's Template**: `while heap: time, node = heappop(heap); if node in visited: continue; visited.add(node); for neighbor, weight in graph[node]: heappush(heap, (time + weight, neighbor))`. Memorize this — it's used in many problems.
  * **Return -1 if Disconnected**: If `len(visited) < n` after the heap is empty, some nodes are unreachable. Return $-1$.
  * **No Negative Weights**: Dijkstra's only works with non-negative edge weights. If negative weights exist, use Bellman-Ford.
* **Complexity**:
  * Time: $O(E \log V)$
  * Space: $O(V + E)$

---

## 4. Swim in Rising Water (LeetCode 778) - Hard
* **Quick Links**: [LeetCode](https://leetcode.com/problems/swim-in-rising-water/) • [NeetCode Problem](https://neetcode.io/problems/swim-in-rising-water) • [NeetCode Solution](https://neetcode.io/solutions/swim-in-rising-water) • [YouTube Video](https://www.youtube.com/watch?v=amvrKlMLuGY)
* **Pattern**: Modified Dijkstra / Min-Max Path
* **Core Concept**:
  Find a path from $(0, 0)$ to $(N-1, N-1)$ minimizing the maximum cell elevation encountered. Use a Min-Heap of `(max_elevation_on_path, r, c)`. At each step, pop the cell with the smallest maximum elevation and expand to neighbors, pushing `(max(curr_max, grid[nr][nc]), nr, nc)`.
* **Mental Model**:
  Rising floodwaters. You want to swim from the top-left to the bottom-right corner. Water rises to a uniform level $t$. You can swim through any cell where $grid[r][c] \le t$. Find the minimum $t$ that creates a connected path — this is the maximum elevation along the optimal path.
* **Tips & Interview Tricks**:
  * **Modified Dijkstra**: Standard Dijkstra minimizes sum of weights. Here, you minimize the *maximum* weight along the path. The heap priority changes from `cost + weight` to `max(cost, weight)`.
  * **Binary Search Alternative**: Binary search on the answer $t \in [0, N^2-1]$, and for each candidate $t$, BFS/DFS to check if a path exists using only cells $\le t$. This is $O(N^2 \log N)$ and equally valid.
* **Complexity**:
  * Time: $O(N^2 \log N)$
  * Space: $O(N^2)$

---

## 5. Alien Dictionary (LeetCode 269) - Hard
* **Quick Links**: [LeetCode](https://leetcode.com/problems/alien-dictionary/) • [NeetCode Problem](https://neetcode.io/problems/foreign-dictionary) • [NeetCode Solution](https://neetcode.io/solutions/alien-dictionary) • [YouTube Video](https://www.youtube.com/watch?v=6kTZYvNNyps)
* **Pattern**: Lexicographical Graph + Topological Sort
* **Core Concept**:
  Compare adjacent words. The first differing character between `words[i]` and `words[i+1]` defines a directed dependency $c_1 \to c_2$. Run topological sort to find the character order. Return `""` if a cycle is detected or if an invalid prefix ordering occurs (e.g., `"apple"` before `"app"`).
* **Mental Model**:
  Deciphering an alien alphabet by comparing pairs of words in the alien dictionary. Each adjacent word pair reveals one letter-ordering rule. Combining all rules via topological sort reconstructs the full alphabet.
* **Tips & Interview Tricks**:
  * **Invalid Prefix Check**: If `words[i]` is longer than `words[i+1]` and `words[i+1]` is a prefix of `words[i]`, the ordering is invalid — return `""`. This edge case is frequently missed.
  * **Only First Difference Matters**: When comparing two adjacent words character by character, only the FIRST difference produces a valid ordering constraint. Subsequent differences are meaningless because they depend on the unknown relative ordering.
  * **Include All Characters**: Characters that appear in the words but don't participate in any ordering constraint should still appear in the result. Initialize the graph with all unique characters.
* **Complexity**:
  * Time: $O(C)$ total characters
  * Space: $O(1)$ (at most 26 letters)

---

## 6. Cheapest Flights Within K Stops (LeetCode 787) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/cheapest-flights-within-k-stops/) • [NeetCode Problem](https://neetcode.io/problems/cheapest-flight-path) • [NeetCode Solution](https://neetcode.io/solutions/cheapest-flights-within-k-stops) • [YouTube Video](https://www.youtube.com/watch?v=5eIK3zUdYmE)
* **Pattern**: Bellman-Ford with Step Limit
* **Core Concept**:
  Run $k + 1$ iterations of edge relaxation using a cloned price array from the previous step. The snapshot array ensures each iteration uses strictly $\le$ one additional flight hop. After $k + 1$ rounds, `prices[dst]` holds the cheapest cost with at most $k$ stops.
* **Mental Model**:
  Planning a road trip with a limited number of gas stations. Each round, you extend your reach by one more stop. The snapshot array ensures you don't "teleport" by using results from the current round — only routes discovered in previous rounds are valid starting points.
* **Tips & Interview Tricks**:
  * **Why Not Dijkstra?**: Standard Dijkstra doesn't respect the hop limit $k$. A modified Dijkstra with state `(cost, node, stops)` works but is more complex. Bellman-Ford with $k + 1$ iterations is simpler and more intuitive for this constraint.
  * **Snapshot Array**: `temp = prices[:]` at the start of each iteration prevents using edges relaxed in the current round. Without this, you'd count paths with more than $k$ stops.
  * **Initialization**: Set `prices[src] = 0` and all others to `float('inf')`. If `prices[dst]` remains `inf` after all iterations, return $-1$.
* **Complexity**:
  * Time: $O(K \cdot E)$
  * Space: $O(V)$
