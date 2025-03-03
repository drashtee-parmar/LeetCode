class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:  # Edge case: empty array
            return 0
        
        k = 0  # Pointer for the last unique element

        for i in range(1, len(nums)):  # Start from the second element
            if nums[i] != nums[k]:  # Found a new unique element
                k += 1
                nums[k] = nums[i]  # Move it to the correct position

        return k + 1  # Return count of unique elements
