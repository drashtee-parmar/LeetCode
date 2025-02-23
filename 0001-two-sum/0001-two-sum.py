class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
# -------------------------
# Brute force Approach
#Time Complexity: O(n^2), where n is the number of elements in the array. We check each pair of elements, resulting in quadratic time complexity.
#Space Complexity: O(1), as no additional space proportional to the input size is required (only a few variables).
        # n = len(nums)        
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
# -------------------------

# Using two-pointer Approach

# Time Complexity: O(n \log n) due to sorting the array.
# Space Complexity: O(n) because of the space required to store the sorted list with the original indices.

        indices = []
        n = len(nums)
        # Create a list of tuples (number, index) using a simple for loop
        for i in range(n):
            indices.append((nums[i], i))
        # Sort the list of tuples based on the numbers
        indices.sort()
        # Initialize two pointers
        left = 0
        right = len(nums) - 1
        
        # Iterate while the left pointer is less than the right pointer
        while left < right:
            # Get the value and original index from each pointer
            left_num, left_index = indices[left]
            right_num, right_index = indices[right]
            
            # Calculate the sum of the two numbers
            current_sum = left_num + right_num
            
            # If the sum matches the target, return the original indices
            if current_sum == target:
                return [left_index, right_index]
            # If the sum is less than the target, move the left pointer to the right
            elif current_sum < target:
                left += 1
            # If the sum is greater than the target, move the right pointer to the left
            else:
                right -= 1





        