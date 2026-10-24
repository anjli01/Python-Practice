"""
NeetCode 150 - Module 4.3: Advanced Graphs
Detailed, fully-commented Python 3 solutions for all 6 problems.
"""

from typing import List
from collections import defaultdict, deque
import heapq


# ============================================================================
# Problem 1: Reconstruct Itinerary (LeetCode 332) - Hard
# Pattern: Hierholzer's Algorithm (Eulerian Path)
# ============================================================================
class SolutionReconstructItinerary:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """Reconstructs the itinerary in lexicographical order starting from JFK."""
        adj = defaultdict(list)
        # Sort tickets reverse-lexicographically so we can pop from the back in O(1)
        for src, dst in sorted(tickets, reverse=True):
            adj[src].append(dst)

        itinerary = []

        def dfs(src: str):
            while adj[src]:
                next_dst = adj[src].pop()
                dfs(next_dst)
            itinerary.append(src)

        dfs("JFK")
        return itinerary[::-1]


# ============================================================================
# Problem 2: Min Cost to Connect All Points (LeetCode 1584) - Medium
# Pattern: Prim's Algorithm (Minimum Spanning Tree)
# ============================================================================
class SolutionMinCostConnectPoints:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """Finds the minimum cost to make all points connected using Manhattan distance."""
        n = len(points)
        visited = set()
        min_heap = [(0, 0)]  # (cost, point_index)
        total_cost = 0

        while len(visited) < n:
            cost, curr = heapq.heappop(min_heap)
            if curr in visited:
                continue
            visited.add(curr)
            total_cost += cost

            x1, y1 = points[curr]
            for next_pt in range(n):
                if next_pt not in visited:
                    x2, y2 = points[next_pt]
                    manhattan_dist = abs(x1 - x2) + abs(y1 - y2)
                    heapq.heappush(min_heap, (manhattan_dist, next_pt))

        return total_cost


# ============================================================================
# Problem 3: Network Delay Time (LeetCode 743) - Medium
# Pattern: Dijkstra's Algorithm (Single-Source Shortest Path)
# ============================================================================
class SolutionNetworkDelayTime:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """Calculates minimum time for all n nodes to receive signal from k."""
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))

        min_heap = [(0, k)]  # (time, node)
        visited = {}

        while min_heap:
            time, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            visited[node] = time

            for neighbor, weight in adj[node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (time + weight, neighbor))

        return max(visited.values()) if len(visited) == n else -1


# ============================================================================
# Problem 4: Swim in Rising Water (LeetCode 778) - Hard
# Pattern: Modified Dijkstra / Min-Max Path on Grid
# ============================================================================
class SolutionSwimInRisingWater:
    def swimInWater(self, grid: List[List[int]]) -> int:
        """Finds the least time until you can reach bottom-right from top-left."""
        n = len(grid)
        visited = {(0, 0)}
        min_heap = [(grid[0][0], 0, 0)]  # (max_elevation_on_path, r, c)

        while min_heap:
            elevation, r, c = heapq.heappop(min_heap)
            if r == n - 1 and c == n - 1:
                return elevation

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    heapq.heappush(min_heap, (max(elevation, grid[nr][nc]), nr, nc))

        return 0


# ============================================================================
# Problem 5: Alien Dictionary (LeetCode 269) - Hard
# Pattern: Character Dependency Graph + Topological Sort
# ============================================================================
class SolutionAlienDictionary:
    def alienOrder(self, words: List[str]) -> str:
        """Derives the alphabetical order of characters in an alien language."""
        adj = {char: set() for word in words for char in word}

        # Build directed edges from adjacent word pairs
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            # Invalid prefix condition: "apple" comes before "app"
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        visited = {}  # False = visiting (in call stack), True = visited
        order = []

        def dfs(c: str) -> bool:
            if c in visited:
                return visited[c]
            visited[c] = False  # Mark visiting

            for neighbor in adj[c]:
                if not dfs(neighbor):
                    return False

            visited[c] = True
            order.append(c)
            return True

        for c in adj:
            if not dfs(c):
                return ""

        return "".join(order[::-1])


# ============================================================================
# Problem 6: Cheapest Flights Within K Stops (LeetCode 787) - Medium
# Pattern: Bellman-Ford Shortest Path with Hop Limits
# ============================================================================
class SolutionCheapestFlights:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """Finds cheapest price from src to dst with at most k intermediate stops."""
        prices = [float('inf')] * n
        prices[src] = 0

        # Run Bellman-Ford relaxation for k + 1 flights
        for _ in range(k + 1):
            temp_prices = prices.copy()
            for u, v, p in flights:
                if prices[u] == float('inf'):
                    continue
                if prices[u] + p < temp_prices[v]:
                    temp_prices[v] = prices[u] + p
            prices = temp_prices

        return int(prices[dst]) if prices[dst] != float('inf') else -1
