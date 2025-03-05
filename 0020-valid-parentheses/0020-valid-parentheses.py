class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:  # If empty, it's valid
            return True
        for pair in ["()", "{}", "[]"]:
            if pair in s:
                return self.isValid(s.replace(pair, ""))  # Remove pair and recurse
        return False  # If no valid pair is found