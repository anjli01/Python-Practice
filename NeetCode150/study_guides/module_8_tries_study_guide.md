# Module 3.2: Tries – Study Guide & Pattern Deep-Dive

A **Trie (Prefix Tree)** is a tree data structure used to store an associative array of keys (typically strings). It provides $O(L)$ search and insert where $L$ is the key length, independent of the number of words stored in the dataset.

---

## 1. Implement Trie (Prefix Tree) (LeetCode 208) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/implement-trie-prefix-tree/) • [NeetCode Problem](https://neetcode.io/problems/implement-prefix-tree) • [NeetCode Solution](https://neetcode.io/solutions/implement-trie-prefix-tree) • [YouTube Video](https://www.youtube.com/watch?v=oobqoCJlHA0)
* **Pattern**: N-ary Character Tree with `is_end` Flag
* **Core Concept**:
  Each node represents a character transition via a `children` dictionary mapping characters to child nodes. A boolean `is_end` marks whether the path from the root to this node constitutes a complete word. `search` requires `is_end == True` at the terminal node; `startsWith` does not.
* **Mental Model**:
  An autocomplete dropdown. Each keypress navigates one level deeper into the tree. If you reach a dead end (character not in `children`), the word doesn't exist. If you arrive at a node marked as a word boundary (`is_end`), the word is valid.
* **Tips & Interview Tricks**:
  * **Node Design**: Use `self.children = {}` (dictionary) rather than a fixed-size array of 26 for flexibility. In interviews, mention both options and trade-offs: the dictionary is cleaner in Python; a 26-element array is faster in C++/Java.
  * **`search` vs. `startsWith`**: These are nearly identical traversals. Factor out a `_find(word)` helper that returns the terminal node (or `None`), then `search` checks `node.is_end` while `startsWith` simply checks `node is not None`.
* **Complexity**:
  * Time: $O(L)$ for `insert`, `search`, `startsWith`
  * Space: $O(N \cdot L)$ total characters stored

---

## 2. Design Add and Search Words Data Structure (LeetCode 211) - Medium
* **Quick Links**: [LeetCode](https://leetcode.com/problems/design-add-and-search-words-data-structure/) • [NeetCode Problem](https://neetcode.io/problems/design-word-search-data-structure) • [NeetCode Solution](https://neetcode.io/solutions/design-add-and-search-words-data-structure) • [YouTube Video](https://www.youtube.com/watch?v=BTf05gs_8iU)
* **Pattern**: Trie with Wildcard DFS Backtracking
* **Core Concept**:
  For literal characters, branch down the specific child. For the wildcard `'.'`: iterate and recursively explore **all** active branches (`for child in node.children.values()`). If any branch leads to a successful match, return `True`.
* **Mental Model**:
  A multi-lane highway toll booth. Literal characters take a specific lane. The wildcard `'.'` is a VIP pass that lets you try every open lane simultaneously — if any lane leads to the destination, you're through.
* **Tips & Interview Tricks**:
  * **Worst-Case Wildcard**: A query like `"..."` (all dots) triggers exponential branching — $O(26^L)$ in the worst case. Mention this to the interviewer to demonstrate awareness of the complexity trade-off.
  * **Recursive Helper**: Write `def _search(node, word, idx)` that takes the current Trie node and the current character index. This avoids slicing the string repeatedly.
* **Complexity**:
  * Time: $O(L)$ for literal words, $O(26^L)$ in worst-case wildcard queries
  * Space: $O(N \cdot L)$

---

## 3. Word Search II (LeetCode 212) - Hard
* **Quick Links**: [LeetCode](https://leetcode.com/problems/word-search-ii/) • [NeetCode Problem](https://neetcode.io/problems/search-for-word-ii) • [NeetCode Solution](https://neetcode.io/solutions/word-search-ii) • [YouTube Video](https://www.youtube.com/watch?v=asbcE9mZz_U)
* **Pattern**: 2D Grid Backtracking Guided by Trie
* **Core Concept**:
  Searching each word independently across the board takes $O(W \cdot M \cdot N \cdot 4^L)$.
  Instead, build a Trie containing all $W$ words, and run a single DFS from each grid cell, navigating the board and Trie simultaneously. The Trie acts as a shared prefix filter, pruning paths the moment a prefix doesn't match any remaining word.
* **Mental Model**:
  Exploring a maze with a dictionary in hand. Instead of searching for each word separately, you walk the maze once while flipping through the dictionary. If your current path doesn't match any dictionary prefix, turn around immediately.
* **Tips & Interview Tricks**:
  * **In-Place Visited Marker**: Mark cells as `'#'` during traversal and restore the original character on backtracking to avoid allocating a separate `visited` set.
  * **Duplicate Prevention**: Once a word is discovered, set `curr_node.word = ""` so subsequent visits along alternative paths do not re-add the word.
  * **Trie Pruning Optimization**: After finding a word, prune empty leaf nodes from the Trie to prevent unnecessary future exploration down dead-end branches.
* **Complexity**:
  * Time: $O(M \cdot N \cdot 4^L)$
  * Space: $O(W \cdot L)$ for the Trie
