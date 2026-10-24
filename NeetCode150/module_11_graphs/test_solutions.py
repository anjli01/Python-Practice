"""
NeetCode 150 - Module 4.2: Verification & Test Suite
Unit tests with comprehensive edge cases for all 13 Graph solutions.
"""

from solutions import (
    Node,
    SolutionNumberIslands,
    SolutionMaxAreaOfIsland,
    SolutionCloneGraph,
    SolutionWallsAndGates,
    SolutionRottingOranges,
    SolutionPacificAtlantic,
    SolutionSurroundedRegions,
    SolutionCourseSchedule,
    SolutionCourseScheduleII,
    SolutionGraphValidTree,
    SolutionConnectedComponents,
    SolutionRedundantConnection,
    SolutionWordLadder,
)


def test_number_of_islands():
    sol = SolutionNumberIslands()
    grid1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    assert sol.numIslands(grid1) == 1
    grid2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    assert sol.numIslands(grid2) == 3
    assert sol.numIslands([]) == 0
    print("PASS: 1. Number of Islands")


def test_max_area_of_island():
    sol = SolutionMaxAreaOfIsland()
    grid = [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
    ]
    assert sol.maxAreaOfIsland(grid) == 6
    assert sol.maxAreaOfIsland([[0, 0, 0, 0]]) == 0
    print("PASS: 2. Max Area of Island")


def test_clone_graph():
    sol = SolutionCloneGraph()
    n1 = Node(1)
    n2 = Node(2)
    n1.neighbors = [n2]
    n2.neighbors = [n1]
    clone = sol.cloneGraph(n1)
    assert clone is not n1
    assert clone.val == 1
    assert clone.neighbors[0].val == 2
    assert clone.neighbors[0].neighbors[0] is clone
    assert sol.cloneGraph(None) is None
    print("PASS: 3. Clone Graph")


def test_walls_and_gates():
    sol = SolutionWallsAndGates()
    INF = 2147483647
    rooms = [
        [INF, -1, 0, INF],
        [INF, INF, INF, -1],
        [INF, -1, INF, -1],
        [0, -1, INF, INF]
    ]
    sol.wallsAndGates(rooms)
    expected = [
        [3, -1, 0, 1],
        [2, 2, 1, -1],
        [1, -1, 2, -1],
        [0, -1, 3, 4]
    ]
    assert rooms == expected
    print("PASS: 4. Walls and Gates")


def test_rotting_oranges():
    sol = SolutionRottingOranges()
    assert sol.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4
    assert sol.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]) == -1
    assert sol.orangesRotting([[0, 2]]) == 0
    print("PASS: 5. Rotting Oranges")


def test_pacific_atlantic():
    sol = SolutionPacificAtlantic()
    heights = [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4]
    ]
    res = sol.pacificAtlantic(heights)
    expected = [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
    assert sorted(res) == sorted(expected)
    print("PASS: 6. Pacific Atlantic Water Flow")


def test_surrounded_regions():
    sol = SolutionSurroundedRegions()
    board = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"]
    ]
    sol.solve(board)
    expected = [
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "O", "X", "X"]
    ]
    assert board == expected
    print("PASS: 7. Surrounded Regions")


def test_course_schedule():
    sol = SolutionCourseSchedule()
    assert sol.canFinish(2, [[1, 0]]) is True
    assert sol.canFinish(2, [[1, 0], [0, 1]]) is False
    print("PASS: 8. Course Schedule")


def test_course_schedule_ii():
    sol = SolutionCourseScheduleII()
    order1 = sol.findOrder(2, [[1, 0]])
    assert order1 == [0, 1]
    order2 = sol.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
    assert order2 in ([0, 1, 2, 3], [0, 2, 1, 3])
    assert sol.findOrder(2, [[0, 1], [1, 0]]) == []
    print("PASS: 9. Course Schedule II")


def test_graph_valid_tree():
    sol = SolutionGraphValidTree()
    assert sol.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]) is True
    assert sol.validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]) is False
    assert sol.validTree(4, [[0, 1], [2, 3]]) is False  # Disconnected
    print("PASS: 10. Graph Valid Tree")


def test_connected_components():
    sol = SolutionConnectedComponents()
    assert sol.countComponents(5, [[0, 1], [1, 2], [3, 4]]) == 2
    assert sol.countComponents(5, [[0, 1], [1, 2], [2, 3], [3, 4]]) == 1
    print("PASS: 11. Number of Connected Components")


def test_redundant_connection():
    sol = SolutionRedundantConnection()
    assert sol.findRedundantConnection([[1, 2], [1, 3], [2, 3]]) == [2, 3]
    assert sol.findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]) == [1, 4]
    print("PASS: 12. Redundant Connection")


def test_word_ladder():
    sol = SolutionWordLadder()
    assert sol.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == 5
    assert sol.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == 0
    print("PASS: 13. Word Ladder")


if __name__ == "__main__":
    print("\n================ RUNNING GRAPH VERIFICATION ================\n")
    test_number_of_islands()
    test_max_area_of_island()
    test_clone_graph()
    test_walls_and_gates()
    test_rotting_oranges()
    test_pacific_atlantic()
    test_surrounded_regions()
    test_course_schedule()
    test_course_schedule_ii()
    test_graph_valid_tree()
    test_connected_components()
    test_redundant_connection()
    test_word_ladder()
    print("\n================ ALL 13 TESTS PASSED! (100% VERIFIED) ================\n")
