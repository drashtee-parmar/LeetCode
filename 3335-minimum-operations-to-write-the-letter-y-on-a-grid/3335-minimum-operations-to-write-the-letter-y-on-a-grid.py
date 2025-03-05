class Solution(object):
    def minimumOperationsToWriteY(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        center = n // 2  # Middle index
        
        # Count occurrences of 0, 1, 2 in Y-set and Non-Y-set
        y_count = [0, 0, 0]  # Counts for (0,1,2) in Y-set
        non_y_count = [0, 0, 0]  # Counts for (0,1,2) in Non-Y-set

        # Iterate over the grid
        for r in range(n):
            for c in range(n):
                val = grid[r][c]
                if (r == c and r <= center) or (r + c == n - 1 and r <= center) or (c == center and r >= center):
                    y_count[val] += 1
                else:
                    non_y_count[val] += 1

        # Total Y-cells and Non-Y-cells
        total_y_cells = sum(y_count)
        total_non_y_cells = sum(non_y_count)

        # Find the best Y value
        min_operations = float('inf')
        for y_val in range(3):  # Trying (0, 1, 2) for Y-set
            for non_y_val in range(3):  # Trying (0, 1, 2) for Non-Y-set
                if y_val == non_y_val:
                    continue  # Y-set and Non-Y-set must be different

                # Calculate changes needed
                changes_y = total_y_cells - y_count[y_val]
                changes_non_y = total_non_y_cells - non_y_count[non_y_val]

                min_operations = min(min_operations, changes_y + changes_non_y)

        return min_operations