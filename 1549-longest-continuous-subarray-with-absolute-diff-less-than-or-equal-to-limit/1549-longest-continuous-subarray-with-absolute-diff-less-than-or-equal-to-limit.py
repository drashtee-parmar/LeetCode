class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        max_deque = deque()  # Stores decreasing values (max at front)
        min_deque = deque()  # Stores increasing values (min at front)
        
        left = 0  # Left boundary of the sliding window
        max_length = 0  # Result
        
        for right in range(len(nums)):
            # Maintain decreasing order in max_deque
            while max_deque and nums[max_deque[-1]] < nums[right]:
                max_deque.pop()
            max_deque.append(right)
            
            # Maintain increasing order in min_deque
            while min_deque and nums[min_deque[-1]] > nums[right]:
                min_deque.pop()
            min_deque.append(right)
            
            # If the difference exceeds limit, shrink the window
            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                left += 1  # Move left pointer
                # Remove out-of-bound elements
                if max_deque[0] < left:
                    max_deque.popleft()
                if min_deque[0] < left:
                    min_deque.popleft()
            
            # Update the maximum length
            max_length = max(max_length, right - left + 1)
        
        return max_length