class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # left, right = 0, len(nums) -1
        # result = []

        
        # while left <= right:
        #     if abs(nums[left]) > abs(nums[right]):
        #         result.append(nums[left] ** 2)
        #         left += 1
        #     else:
        #         result.append(nums[right] ** 2)
        #         right -= 1

        # return result[::-1]  # Reverse the result since we filled it from largest to smallest



        for i in range(len(nums)):
            nums[i] = nums[i]**2
        nums.sort()
        return nums