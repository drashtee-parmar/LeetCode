class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # Store word at end node

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
         # Build Trie
        if not board or not board[0] or not words:
            return []  # Handle empty input case

        # Build Trie
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word  # Store the complete word at the end node

        rows, cols = len(board), len(board[0])
        result = set()  # Use a set to avoid duplicate words

        # Backtracking DFS
        def backtrack(i, j, node):
            char = board[i][j]
            if char not in node.children:
                return  # Prune if character doesn't exist in Trie

            next_node = node.children[char]
            if next_node.word:  # Found a valid word
                result.add(next_node.word)
                next_node.word = None  # Prevent duplicate results

            # Mark as visited
            board[i][j] = "#"

            # Explore all 4 directions
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + dx, j + dy
                if 0 <= ni < rows and 0 <= nj < cols and board[ni][nj] != "#":
                    backtrack(ni, nj, next_node)

            # Restore board state
            board[i][j] = char

            # Optimization: Remove Trie branch if empty
            if not next_node.children:
                del node.children[char]  # Safe deletion

        # Start DFS from every cell
        for i in range(rows):
            for j in range(cols):
                backtrack(i, j, root)

        return list(result)