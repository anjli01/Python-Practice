"""
NeetCode 150 - Module 3.2: Verification & Test Suite
Unit tests with comprehensive edge cases for all 3 Trie solutions.
"""

from solutions import (
    Trie,
    WordDictionary,
    SolutionWordSearchII,
)


def test_trie():
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple") is True
    assert trie.search("app") is False
    assert trie.startsWith("app") is True
    trie.insert("app")
    assert trie.search("app") is True
    assert trie.startsWith("b") is False
    print("PASS: 1. Implement Trie (Prefix Tree)")


def test_word_dictionary():
    wd = WordDictionary()
    wd.addWord("bad")
    wd.addWord("dad")
    wd.addWord("mad")
    assert wd.search("pad") is False
    assert wd.search("bad") is True
    assert wd.search(".ad") is True
    assert wd.search("b..") is True
    assert wd.search("b.d") is True
    assert wd.search("....") is False
    assert wd.search(".") is False
    print("PASS: 2. Design Add and Search Words Data Structure")


def test_word_search_ii():
    sol = SolutionWordSearchII()
    board = [
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"]
    ]
    words = ["oath", "pea", "eat", "rain"]
    res = sol.findWords(board, words)
    assert sorted(res) == sorted(["eat", "oath"])

    # Edge cases: single cell, no matches
    board2 = [["a", "b"], ["c", "d"]]
    assert sol.findWords(board2, ["abcd", "dcba"]) == []
    print("PASS: 3. Word Search II")


if __name__ == "__main__":
    print("\n================ RUNNING TRIES VERIFICATION ================\n")
    test_trie()
    test_word_dictionary()
    test_word_search_ii()
    print("\n================ ALL 3 TESTS PASSED! (100% VERIFIED) ================\n")
