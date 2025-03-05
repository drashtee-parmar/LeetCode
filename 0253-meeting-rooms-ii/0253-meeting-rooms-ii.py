class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0
        
        # Extract start and end times separately
        start_times = []
        end_times = []
        for interval in intervals:
            start_times.append(interval[0])
            end_times.append(interval[1])
        
        # Sort the start and end times separately
        start_times.sort()
        end_times.sort()
        
        # Initialize pointers for start and end times
        start_pointer = 0
        end_pointer = 0
        rooms = 0
        max_rooms = 0
        
        # Iterate through all start times
        while start_pointer < len(intervals):
            if start_times[start_pointer] < end_times[end_pointer]:
                # A new meeting starts before the previous one ends, need a new room
                rooms += 1
                start_pointer += 1
            else:
                # A meeting has ended, free up a room
                rooms -= 1
                end_pointer += 1
            
            # Update the maximum rooms needed
            max_rooms = max(max_rooms, rooms)
        
        return max_rooms