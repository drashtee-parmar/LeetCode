class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        i = len(num1) - 1
        j = len(num2) - 1
        result = [] # store the sum digit
        carry = 0 # for addition

        while i >= 0 or j >= 0 or carry:
            digit1 = int(num1[i]) if i >= 0 else 0 # get digit or if out of range
            digit2 = int(num2[j]) if j >= 0 else 0 # get digit or if out of range

            sum_val = digit1 + digit2 + carry # sum
            carry = sum_val //10 # compute the new carry
            result.append(str(sum_val % 10)) # storing last digit of sum

            i -= 1 # move to next left digit
            j -= 1
        return ''.join(result[::-1]) # reverse the result and return the string

