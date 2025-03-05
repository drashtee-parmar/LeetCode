class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
                
        # Step 1: Sort intervals by ending time
        intervals.sort(key=lambda x: x[1])
        
        count = 0  # Count of removed intervals
        prev_end = float('-inf')  # Keep track of last non-overlapping interval's end

        # Step 2: Iterate through intervals and apply the greedy choice
        for start, end in intervals:
            if start < prev_end:  # Overlapping interval found
                count += 1  # Remove this interval
            else:
                prev_end = end  # Update the end of last non-overlapping interval

        return count