class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        arr1 = sorted(map(str, arr1))  # Convert to strings and sort
        arr2 = sorted(map(str, arr2))

        def common_prefix_length(s1, s2):
            """Returns the length of the common prefix between two strings."""
            length = 0
            for c1, c2 in zip(s1, s2):
                if c1 == c2:
                    length += 1
                else:
                    break
            return length

        i, j = 0, 0
        max_length = 0

        # Two-pointer technique to find max common prefix length
        while i < len(arr1) and j < len(arr2):
            max_length = max(max_length, common_prefix_length(arr1[i], arr2[j]))

            # Move the pointer of the smaller string to find a better match
            if arr1[i] < arr2[j]:
                i += 1
            else:
                j += 1

        return max_length