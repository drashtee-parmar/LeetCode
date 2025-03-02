class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = [0] * n  # Initialize result array
        left, right = 0, n - 1  # Two pointers at both ends
        index = n - 1  # Fill result array from the end

        while left <= right:
            left_square = nums[left] ** 2
            right_square = nums[right] ** 2

            if left_square > right_square:
                result[index] = left_square
                left += 1
            else:
                result[index] = right_square
                right -= 1

            index -= 1  # Move to the next position

        return result        
        