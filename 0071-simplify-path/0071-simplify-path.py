class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        parts = path.split('/')  # Split by '/' to get components

        for part in parts:
            if part == "..":
                if stack:  # Go up one level if possible
                    stack.pop()
            elif part and part != ".":  # Ignore empty strings and "."
                stack.append(part)

        return "/" + "/".join(stack)  # Construct simplified path