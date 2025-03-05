class Solution(object):
    def isValid(self, s):
        # """
        # :type s: str
        # :rtype: bool
        # """
        # if not s:  # If empty, it's valid
        #     return True
        # for pair in ["()", "{}", "[]"]:
        #     if pair in s:
        #         return self.isValid(s.replace(pair, ""))  # Remove pair and recurse
        # return False  # If no valid pair is found

        stack = []
        mapping = {')': '(', '}': '{', ']': '['}  # Closing to opening bracket map

        for char in s:
            if char in mapping:  # If it's a closing bracket
                top_element = stack.pop() if stack else '#'  # Get last element or dummy value
                if mapping[char] != top_element:  # Check if it matches the expected opening bracket
                    return False
            else:
                stack.append(char)  # If it's an opening bracket, push onto stack
        
        return not stack  # Stack must be empty for a valid string