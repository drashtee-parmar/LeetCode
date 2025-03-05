class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # def dfs(row, col):
        # # Stop if we're out of bounds or if we hit water ('0')
        #     if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == '0':
        #         return

        #     # Mark the current land ('1') as visited by setting it to water ('0')
        #     grid[row][col] = '0'

        #     # Explore the neighboring cells (up, down, left, right)
        #     dfs(row - 1, col)  # up
        #     dfs(row + 1, col)  # down
        #     dfs(row, col - 1)  # left
        #     dfs(row, col + 1)  # right

        # # Variable to count islands
        # count = 0

        # # Loop through each cell in the grid
        # for row in range(len(grid)):
        #     for col in range(len(grid[0])):
        #         # If we find land ('1'), it's a new island
        #         if grid[row][col] == '1':
        #             # Start DFS to mark the whole island
        #             dfs(row, col)
        #             # Increment the island count
        #             count += 1

        # # Return the total number of islands
        # return count
        

        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        island_count = 0

        def dfs(i, j):
            # Boundary check & stop recursion if water ('0')
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0':
                return
            
            grid[i][j] = '0'  # Mark as visited
            # Visit all 4 directions
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        # Scan the entire grid
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':  # New island found
                    island_count += 1
                    dfs(i, j)  # Mark the entire island

        return island_count