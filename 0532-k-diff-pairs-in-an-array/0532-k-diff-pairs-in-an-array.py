class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:  # k must be non-negative
            return 0
        
        num_count = Counter(nums)  # Frequency map
        count = 0

        if k == 0:
            # Count elements that appear at least twice
            count = sum(1 for num in num_count if num_count[num] > 1)
        else:
            # Check if num + k exists in the map
            count = sum(1 for num in num_count if num + k in num_count)
        
        return count 