class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        # return str(x) == str(x)[::-1] # Reverse and compare

        if x < 0 or (x % 10 == 0 and x != 0):  # Negative and trailing zero cases
            return False
        
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10  # Extract last digit
            x //= 10  # Remove last digit from x
        
        return x == reversed_half or x == reversed_half // 10  # Check for even/odd cases