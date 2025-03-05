class Solution(object):
    def fullBloomFlowers(self, flowers, people):
        """
        :type flowers: List[List[int]]
        :type people: List[int]
        :rtype: List[int]
        """
        events = []  # Store (time, event_type)
        
        # Step 1: Convert flowers into start/end events
        for start, end in flowers:
            events.append((start, 1))  # Flower starts blooming
            events.append((end + 1, -1))  # Flower stops blooming after end

        # Step 2: Sort events by time
        events.sort()
        
        # Step 3: Process events and store bloom count at each time
        bloom_counts = []
        times = []
        active_flowers = 0

        for time, event in events:
            active_flowers += event
            times.append(time)
            bloom_counts.append(active_flowers)

        # Step 4: Answer queries using binary search
        result = []
        for person in people:
            idx = bisect.bisect_right(times, person) - 1
            result.append(bloom_counts[idx] if idx >= 0 else 0)

        return result