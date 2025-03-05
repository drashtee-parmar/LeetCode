class Solution(object):
    def countAlternatingSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        length = 1  # Every element is an alternating subarray itself
        
        for i in range(len(nums)):
            if i > 0 and nums[i] != nums[i - 1]:  # If alternating
                length += 1
            else:
                length = 1  # Reset if not alternating
            
            count += length  # Add all subarrays ending at index i
        
        return count