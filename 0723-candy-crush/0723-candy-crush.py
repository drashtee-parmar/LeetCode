class Solution(object):
    def candyCrush(self, board):
        """
        :type board: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(board), len(board[0])
        
        while True:
            to_crush = set()

            # Step 1: Identify candies to crush
            for i in range(m):
                for j in range(n - 2):  # Check horizontal
                    if abs(board[i][j]) > 0 and board[i][j] == board[i][j+1] == board[i][j+2]:
                        to_crush.update([(i, j), (i, j+1), (i, j+2)])

            for j in range(n):
                for i in range(m - 2):  # Check vertical
                    if abs(board[i][j]) > 0 and board[i][j] == board[i+1][j] == board[i+2][j]:
                        to_crush.update([(i, j), (i+1, j), (i+2, j)])

            # If no candies to crush, return stable board
            if not to_crush:
                return board

            # Step 2: Crush candies (set to 0)
            for i, j in to_crush:
                board[i][j] = 0

            # Step 3: Drop candies
            for j in range(n):  # Process column by column
                # Extract non-zero values (candies that fall)
                non_zero_values = [board[i][j] for i in range(m) if board[i][j] > 0]
                
                # Fill the column with zeros
                for i in range(m):
                    board[i][j] = 0
                
                # Place non-zero values at the bottom
                for i in range(m - len(non_zero_values), m):
                    board[i][j] = non_zero_values[i - (m - len(non_zero_values))]