class Solution(object):
    def countOperations(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        operations = 0
        
        while num1 > 0 and num2 > 0:
            if num1 >= num2:
                operations += num1 // num2  # Count how many times num2 fits in num1
                num1 %= num2  # Get the remainder
            else:
                operations += num2 // num1  # Count how many times num1 fits in num2
                num2 %= num1  # Get the remainder
        
        return operations