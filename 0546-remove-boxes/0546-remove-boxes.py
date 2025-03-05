class Solution(object):
    def removeBoxes(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
    
        cache = {}  # Memoization dictionary

        def dfs(i, j, k):
            if i > j:
                return 0  # No boxes left

            if (i, j, k) in cache:
                return cache[(i, j, k)]  # Return cached value
            
            # Step 1: Count consecutive boxes of the same color
            cnt = 0
            while (i + cnt) <= j and boxes[i] == boxes[i + cnt]:
                cnt += 1  # Count same-colored boxes at start
            i2 = i + cnt  # Move to the next different box
            
            # Step 2: Remove current contiguous block and solve the rest
            res = dfs(i2, j, 0) + (k + cnt) ** 2  # Remove first block

            # Step 3: Try merging non-adjacent occurrences of `boxes[i]`
            for m in range(i2, j + 1):
                if boxes[m] == boxes[i]:
                    res = max(res, dfs(i2, m - 1, 0) + dfs(m, j, k + cnt))

            cache[(i, j, k)] = res  # Store result in cache
            return res

        return dfs(0, len(boxes) - 1, 0)