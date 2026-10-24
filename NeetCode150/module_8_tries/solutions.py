"""
NeetCode 150 - Module 3.2: Tries
Detailed, fully-commented Python 3 solutions for all 3 problems.
"""

from typing import List, Dict


class TrieNode:
    """Trie (Prefix Tree) node."""
    def __init__(self):
        self.children: Dict[str, TrieNode] = {}
        self.is_end: bool = False
        self.word: str = ""  # Useful for Word Search II


# ============================================================================
# Problem 1: Implement Trie (Prefix Tree) (LeetCode 208) - Medium
# Pattern: N-ary Character Tree with End-of-Word Flag
# ============================================================================
class Trie:
    """Standard Prefix Tree for fast word and prefix lookups."""
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Inserts a word into the trie in O(L) time."""
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end = True

    def search(self, word: str) -> bool:
        """Returns True if the exact word exists in the trie."""
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.is_end

    def startsWith(self, prefix: str) -> bool:
        """Returns True if any word in the trie starts with the given prefix."""
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True


# ============================================================================
# Problem 2: Design Add and Search Words Data Structure (LeetCode 211) - Medium
# Pattern: Trie with Wildcard DFS Backtracking
# ============================================================================
class WordDictionary:
    """Dictionary supporting exact matches and wildcard '.' searches."""
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end = True

    def search(self, word: str) -> bool:
        def dfs(node: TrieNode, idx: int) -> bool:
            if idx == len(word):
                return node.is_end
                
            char = word[idx]
            if char == '.':
                # Wildcard: Explore all child branches
                for child in node.children.values():
                    if dfs(child, idx + 1):
                        return True
                return False
            else:
                if char not in node.children:
                    return False
                return dfs(node.children[char], idx + 1)

        return dfs(self.root, 0)


# ============================================================================
# Problem 3: Word Search II (LeetCode 212) - Hard
# Pattern: Grid DFS Backtracking Guided by Trie with In-Place Pruning
# ============================================================================
class SolutionWordSearchII:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        Finds all words from the dictionary that can be formed in the board grid.
        
        Concept / Pattern:
        - Insert all words into a Trie.
        - Backtrack through the 2D grid: Only traverse adjacent cells if the character
          exists in the current Trie node's children!
        - Optimization & Pruning: Once a word is found, set `node.word = ""` to avoid
          duplicates.
        
        Complexity:
        - Time: O(M * N * 4^L) where L is the maximum word length.
        - Space: O(total characters in words) for the Trie.
        """
        root = TrieNode()
        for w in words:
            curr = root
            for c in w:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.is_end = True
            curr.word = w

        ROWS, COLS = len(board), len(board[0])
        result = []

        def dfs(r: int, c: int, parent_node: TrieNode):
            char = board[r][c]
            if char not in parent_node.children:
                return
                
            curr_node = parent_node.children[char]
            
            # Found a word
            if curr_node.is_end and curr_node.word:
                result.append(curr_node.word)
                curr_node.word = ""  # Prevent duplicate addition
                
            # Mark cell as visited in-place
            board[r][c] = '#'
            
            # Explore all 4 orthogonal directions
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] != '#':
                    dfs(nr, nc, curr_node)
                    
            # Backtrack
            board[r][c] = char

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root)
                
        return result
