"""
NeetCode 150 - Module 4.3: Verification & Test Suite
Unit tests with comprehensive edge cases for all 6 Advanced Graph solutions.
"""

from solutions import (
    SolutionReconstructItinerary,
    SolutionMinCostConnectPoints,
    SolutionNetworkDelayTime,
    SolutionSwimInRisingWater,
    SolutionAlienDictionary,
    SolutionCheapestFlights,
)


def test_reconstruct_itinerary():
    sol = SolutionReconstructItinerary()
    tickets1 = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    assert sol.findItinerary(tickets1) == ["JFK", "MUC", "LHR", "SFO", "SJC"]

    tickets2 = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
    assert sol.findItinerary(tickets2) == ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]
    print("PASS: 1. Reconstruct Itinerary")


def test_min_cost_connect_points():
    sol = SolutionMinCostConnectPoints()
    points1 = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    assert sol.minCostConnectPoints(points1) == 20
    points2 = [[3, 12], [-2, 5], [-4, 1]]
    assert sol.minCostConnectPoints(points2) == 18
    assert sol.minCostConnectPoints([[0, 0]]) == 0
    print("PASS: 2. Min Cost to Connect All Points")


def test_network_delay_time():
    sol = SolutionNetworkDelayTime()
    assert sol.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2) == 2
    assert sol.networkDelayTime([[1, 2, 1]], 2, 1) == 1
    assert sol.networkDelayTime([[1, 2, 1]], 2, 2) == -1
    print("PASS: 3. Network Delay Time")


def test_swim_in_rising_water():
    sol = SolutionSwimInRisingWater()
    grid1 = [[0, 2], [1, 3]]
    assert sol.swimInWater(grid1) == 3
    grid2 = [
        [0, 1, 2, 3, 4],
        [24, 23, 22, 21, 5],
        [12, 13, 14, 15, 16],
        [11, 17, 18, 19, 20],
        [10, 9, 8, 7, 6]
    ]
    assert sol.swimInWater(grid2) == 16
    print("PASS: 4. Swim in Rising Water")


def test_alien_dictionary():
    sol = SolutionAlienDictionary()
    assert sol.alienOrder(["wrt", "wrf", "er", "ett", "rftt"]) == "wertf"
    assert sol.alienOrder(["z", "x"]) == "zx"
    assert sol.alienOrder(["z", "x", "z"]) == ""  # Cycle
    assert sol.alienOrder(["apple", "app"]) == ""  # Invalid prefix order
    print("PASS: 5. Alien Dictionary")


def test_cheapest_flights():
    sol = SolutionCheapestFlights()
    flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
    assert sol.findCheapestPrice(4, flights, 0, 3, 1) == 700
    assert sol.findCheapestPrice(4, flights, 0, 3, 2) == 400
    assert sol.findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0) == 500
    print("PASS: 6. Cheapest Flights Within K Stops")


if __name__ == "__main__":
    print("\n================ RUNNING ADVANCED GRAPHS VERIFICATION ================\n")
    test_reconstruct_itinerary()
    test_min_cost_connect_points()
    test_network_delay_time()
    test_swim_in_rising_water()
    test_alien_dictionary()
    test_cheapest_flights()
    print("\n================ ALL 6 TESTS PASSED! (100% VERIFIED) ================\n")
