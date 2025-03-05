class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not board[0]:
            return False
        
        m, n = len(board), len(board[0])

        def dfs(i, j, k):
            # Base Case: If word is fully matched
            if k == len(word):
                return True

            # Boundary and character check
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[k]:
                return False

            # Mark cell as visited
            temp = board[i][j]
            board[i][j] = "#"

            # Explore in all 4 directions
            found = (dfs(i+1, j, k+1) or  # Down
                     dfs(i-1, j, k+1) or  # Up
                     dfs(i, j+1, k+1) or  # Right
                     dfs(i, j-1, k+1))    # Left

            # Restore original value (Backtrack)
            board[i][j] = temp

            return found

        # Try starting from each cell
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):  # Start DFS if first letter matches
                    return True

        return False