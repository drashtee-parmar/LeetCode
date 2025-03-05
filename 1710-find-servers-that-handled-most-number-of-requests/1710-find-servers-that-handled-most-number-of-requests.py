class Solution(object):
    def busiestServers(self, k, arrival, load):
        """
        :type k: int
        :type arrival: List[int]
        :type load: List[int]
        :rtype: List[int]
        """
        busy_servers = []  # Min-heap of (release_time, server_id)
        available_servers = SortedSet(range(k))  # Ordered set of available server IDs
        requests_count = [0] * k  # Count of requests handled by each server

        # Iterate over all requests
        for i, (arr, ld) in enumerate(zip(arrival, load)):
            # Free up servers whose work has completed
            while busy_servers and busy_servers[0][0] <= arr:
                _, server_id = heapq.heappop(busy_servers)
                available_servers.add(server_id)

            # Find the next available server
            if len(available_servers) == 0:
                continue  # Drop request if no servers are free

            idx = available_servers.bisect_left(i % k)  # Find first available server ≥ (i % k)
            if idx == len(available_servers):  # Wrap around if needed
                idx = 0

            server_id = available_servers.pop(idx)  # Assign request to this server
            heapq.heappush(busy_servers, (arr + ld, server_id))  # Mark server as busy
            requests_count[server_id] += 1  # Track request count

        # Find the maximum number of requests handled
        max_requests = max(requests_count)
        return [i for i in range(k) if requests_count[i] == max_requests]