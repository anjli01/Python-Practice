"""
NeetCode 150 - Module 4.2: Graphs
Detailed, fully-commented Python 3 solutions for all 13 problems.
"""

from typing import List, Optional, Dict
from collections import deque, defaultdict


class Node:
    """Graph Node definition."""
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# ============================================================================
# Problem 1: Number of Islands (LeetCode 200) - Medium
# Pattern: Grid DFS Flood Fill
# ============================================================================
class SolutionNumberIslands:
    def numIslands(self, grid: List[List[str]]) -> int:
        """Counts the number of connected components of '1's."""
        if not grid:
            return 0
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def dfs(r: int, c: int):
            if not (0 <= r < ROWS and 0 <= c < COLS) or grid[r][c] != '1':
                return
            grid[r][c] = '0'  # Sink island in-place
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    islands += 1
                    dfs(r, c)
        return islands


# ============================================================================
# Problem 2: Max Area of Island (LeetCode 695) - Medium
# Pattern: Component Accumulator DFS
# ============================================================================
class SolutionMaxAreaOfIsland:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """Finds the maximum area (number of cells) of an island in grid."""
        ROWS, COLS = len(grid), len(grid[0])
        max_area = 0

        def dfs(r: int, c: int) -> int:
            if not (0 <= r < ROWS and 0 <= c < COLS) or grid[r][c] != 1:
                return 0
            grid[r][c] = 0
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))
        return max_area


# ============================================================================
# Problem 3: Clone Graph (LeetCode 133) - Medium
# Pattern: DFS with Visited Node Hash Map
# ============================================================================
class SolutionCloneGraph:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """Deep copies an undirected connected graph."""
        if not node:
            return None
        old_to_new: Dict[Node, Node] = {}

        def dfs(curr: Node) -> Node:
            if curr in old_to_new:
                return old_to_new[curr]
            copy = Node(curr.val)
            old_to_new[curr] = copy
            for neighbor in curr.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy

        return dfs(node)


# ============================================================================
# Problem 4: Walls and Gates (LeetCode 286) - Medium
# Pattern: Multi-Source Simultaneous BFS
# ============================================================================
class SolutionWallsAndGates:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """Fills empty rooms (2147483647) with distance to nearest gate (0) in-place."""
        ROWS, COLS = len(rooms), len(rooms[0])
        queue = deque()

        # Seed queue with all gates simultaneously
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    queue.append((r, c))

        dist = 0
        while queue:
            dist += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and rooms[nr][nc] == 2147483647:
                        rooms[nr][nc] = dist
                        queue.append((nr, nc))


# ============================================================================
# Problem 5: Rotting Oranges (LeetCode 994) - Medium
# Pattern: Multi-Source Level-by-Level BFS
# ============================================================================
class SolutionRottingOranges:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """Calculates minimum minutes until no fresh orange remains."""
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        minutes = 0
        while queue and fresh > 0:
            minutes += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))

        return minutes if fresh == 0 else -1


# ============================================================================
# Problem 6: Pacific Atlantic Water Flow (LeetCode 417) - Medium
# Pattern: Reverse Coastal Reachability BFS/DFS
# ============================================================================
class SolutionPacificAtlantic:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """Finds grid coordinates that can flow water to both Pacific and Atlantic."""
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r: int, c: int, visited: set):
            visited.add((r, c))
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visited:
                    if heights[nr][nc] >= heights[r][c]:  # Reverse flow uphill
                        dfs(nr, nc, visited)

        for c in range(COLS):
            dfs(0, c, pac)               # Top Pacific
            dfs(ROWS - 1, c, atl)        # Bottom Atlantic
        for r in range(ROWS):
            dfs(r, 0, pac)               # Left Pacific
            dfs(r, COLS - 1, atl)        # Right Atlantic

        return [[r, c] for r, c in (pac & atl)]


# ============================================================================
# Problem 7: Surrounded Regions (LeetCode 130) - Medium
# Pattern: Boundary-Inversion Flood Fill
# ============================================================================
class SolutionSurroundedRegions:
    def solve(self, board: List[List[str]]) -> None:
        """Captures all regions of 'O's completely surrounded by 'X' in-place."""
        if not board:
            return
        ROWS, COLS = len(board), len(board[0])

        def dfs(r: int, c: int):
            if not (0 <= r < ROWS and 0 <= c < COLS) or board[r][c] != 'O':
                return
            board[r][c] = 'T'  # Temporarily mark border-connected
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS - 1)
        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS - 1, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'


# ============================================================================
# Problem 8: Course Schedule (LeetCode 207) - Medium
# Pattern: Cycle Detection in Directed Graph (DFS Visiting Set)
# ============================================================================
class SolutionCourseSchedule:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """Determines if all courses can be finished without circular dependencies."""
        adj = defaultdict(list)
        for crs, pre in prerequisites:
            adj[crs].append(pre)

        visiting = set()
        visited = set()

        def has_cycle(crs: int) -> bool:
            if crs in visiting:
                return True
            if crs in visited:
                return False

            visiting.add(crs)
            for pre in adj[crs]:
                if has_cycle(pre):
                    return True
            visiting.remove(crs)
            visited.add(crs)
            return False

        for crs in range(numCourses):
            if has_cycle(crs):
                return False
        return True


# ============================================================================
# Problem 9: Course Schedule II (LeetCode 210) - Medium
# Pattern: Topological Sort (Kahn's In-Degree Algorithm)
# ============================================================================
class SolutionCourseScheduleII:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """Returns topological ordering of courses to take."""
        adj = defaultdict(list)
        in_degree = [0] * numCourses

        for crs, pre in prerequisites:
            adj[pre].append(crs)
            in_degree[crs] += 1

        queue = deque([crs for crs in range(numCourses) if in_degree[crs] == 0])
        order = []

        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in adj[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return order if len(order) == numCourses else []


# ============================================================================
# Problem 10: Graph Valid Tree (LeetCode 261) - Medium
# Pattern: Tree Invariants (Edges == n-1 and Fully Connected)
# ============================================================================
class SolutionGraphValidTree:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """Determines whether an undirected graph forms a valid tree."""
        # A valid tree with n nodes must have exactly n - 1 edges
        if len(edges) != n - 1:
            return False

        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()

        def dfs(node: int, parent: int) -> bool:
            if node in visited:
                return False
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor, node):
                    return False
            return True

        if not dfs(0, -1):
            return False
        return len(visited) == n


# ============================================================================
# Problem 11: Number of Connected Components in an Undirected Graph (LeetCode 323) - Medium
# Pattern: Disjoint Set Union (Union-Find)
# ============================================================================
class SolutionConnectedComponents:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """Counts the number of connected components using Union-Find."""
        parent = list(range(n))
        rank = [1] * n

        def find(x: int) -> int:
            while x != parent[x]:
                parent[x] = parent[parent[x]]  # Path compression
                x = parent[x]
            return x

        def union(x: int, y: int) -> int:
            p1, p2 = find(x), find(y)
            if p1 == p2:
                return 0
            if rank[p1] >= rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return 1

        components = n
        for u, v in edges:
            components -= union(u, v)
        return components


# ============================================================================
# Problem 12: Redundant Connection (LeetCode 684) - Medium
# Pattern: Union-Find Cycle Edge Detection
# ============================================================================
class SolutionRedundantConnection:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """Finds an edge that creates a cycle in an undirected graph."""
        n = len(edges)
        parent = list(range(n + 1))
        rank = [1] * (n + 1)

        def find(x: int) -> int:
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for u, v in edges:
            p1, p2 = find(u), find(v)
            if p1 == p2:
                # Cycle formed!
                return [u, v]
            if rank[p1] >= rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]

        return []


# ============================================================================
# Problem 13: Word Ladder (LeetCode 127) - Hard
# Pattern: BFS Shortest Path with Generic Wildcard Patterns
# ============================================================================
class SolutionWordLadder:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """Finds shortest transformation sequence length from beginWord to endWord."""
        if endWord not in wordList:
            return 0

        # Pattern dictionary: e.g. "*ot" -> ["hot", "dot", "lot"]
        neighbors = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                neighbors[pattern].append(word)

        visited = {beginWord}
        queue = deque([beginWord])
        length = 1

        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return length
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for nei in neighbors[pattern]:
                        if nei not in visited:
                            visited.add(nei)
                            queue.append(nei)
            length += 1

        return 0
