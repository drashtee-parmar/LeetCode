class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1 # going left to right i.e. 0 to n-1
        while left < right:
            s[left], s[right] = s[right], s[left] #swap character
            left += 1
            right -= 1
        return s