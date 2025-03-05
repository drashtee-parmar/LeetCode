class Solution(object):
    def getBiggestThree(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """

        m, n = len(grid), len(grid[0])
        unique_sums = SortedSet()

        # Step 1: Add all single-cell rhombus sums (size 0)
        for i in range(m):
            for j in range(n):
                unique_sums.add(grid[i][j])
                if len(unique_sums) > 3:
                    unique_sums.discard(unique_sums[0])  # Keep only top 3

        # Step 2: Check larger rhombuses (size >= 1)
        max_size = min(m, n) // 2  # Maximum possible rhombus size
        for size in range(1, max_size + 1):
            for i in range(size, m - size):  # Center row range
                for j in range(size, n - size):  # Center column range
                    # Ensure rhombus is within bounds
                    if i - size < 0 or i + size >= m or j - size < 0 or j + size >= n:
                        continue

                    # Compute rhombus sum using its borders
                    rhombus_sum = grid[i - size][j] + grid[i + size][j] + grid[i][j - size] + grid[i][j + size]
                    for k in range(1, size):
                        rhombus_sum += grid[i - size + k][j - k]  # Top-left to bottom-right
                        rhombus_sum += grid[i - size + k][j + k]  # Top-right to bottom-left
                        rhombus_sum += grid[i + size - k][j - k]  # Bottom-left to top-right
                        rhombus_sum += grid[i + size - k][j + k]  # Bottom-right to top-left

                    unique_sums.add(rhombus_sum)
                    if len(unique_sums) > 3:
                        unique_sums.discard(unique_sums[0])  # Keep only top 3

        return sorted(unique_sums, reverse=True)