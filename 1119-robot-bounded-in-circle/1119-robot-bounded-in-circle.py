class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        """
        Determines if robot stays within a bounded circle after repeating instructions infinitely.
        
        :param instructions: str - sequence of 'G', 'L', 'R' commands
        :return: bool - True if robot is bounded, False otherwise
        """
        # Directions: N(0,1), E(1,0), S(0,-1), W(-1,0)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y = 0, 0  # Starting position
        dir_index = 0  # Start facing North

        for instruction in instructions:
            if instruction == 'G':
                dx, dy = directions[dir_index]
                x += dx
                y += dy
            elif instruction == 'L':
                dir_index = (dir_index - 1) % 4  # Turn left
            elif instruction == 'R':
                dir_index = (dir_index + 1) % 4  # Turn right

        # Bounded if at origin or not facing North after one cycle
        return (x, y) == (0, 0) or dir_index != 0