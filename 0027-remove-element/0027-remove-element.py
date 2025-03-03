class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        
        for i in range(len(nums)):  # Iterate through nums
            if nums[i] != val:  # If the element is not equal to val
                nums[k] = nums[i]  # Move it to the front
                k += 1  # Increment count of valid elements

        return k  # Return the count of elements that are not val

        
        # for i in nums:
        #     if i != val:
        #         nums[k] = i
        #         k += 1
        # return k
        