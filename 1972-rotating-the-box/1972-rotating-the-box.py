class Solution(object):
    def rotateTheBox(self, boxGrid):
        """
        :type boxGrid: List[List[str]]
        :rtype: List[List[str]]
        """
        m, n = len(boxGrid), len(boxGrid[0])
        
        # Step 1: Rotate the matrix 90 degrees clockwise
        rotated = [['.'] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                rotated[j][m - 1 - i] = boxGrid[i][j]

        # Step 2: Simulate gravity in the rotated box
        for col in range(m):  # Iterate over columns in rotated grid
            empty_row = n - 1  # Start from the bottom row
            for row in range(n - 1, -1, -1):  # Process from bottom to top
                if rotated[row][col] == '#':
                    # Move stone to lowest available row
                    rotated[row][col], rotated[empty_row][col] = '.', '#'
                    empty_row -= 1
                elif rotated[row][col] == '*':
                    # Obstacle found, update empty row
                    empty_row = row - 1

        return rotated