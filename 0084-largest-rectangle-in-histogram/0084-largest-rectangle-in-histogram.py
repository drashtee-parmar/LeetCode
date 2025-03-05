class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []  # Monotonic increasing stack (stores indices)
        max_area = 0
        n = len(heights)

        for i in range(n + 1):  # Iterate till `n` to pop all elements
            h = heights[i] if i < n else 0  # Add 0 at end to ensure last elements are popped
            
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]  # Pop the top element (height)
                width = i if not stack else i - stack[-1] - 1  # Calculate width
                max_area = max(max_area, height * width)

            stack.append(i)  # Push current index

        return max_area