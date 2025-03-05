class FileSystem(object):

    def __init__(self):
        self.trie = {"": {}}  # Root Trie with an empty path


    def createPath(self, path, value):
        """
        :type path: str
        :type value: int
        :rtype: bool
        """

        parts = path.split("/")[1:]  # Split into directory components
        node = self.trie

        # Traverse to the parent path
        for i in range(len(parts) - 1):
            if parts[i] not in node:
                return False  # Parent path doesn't exist
            node = node[parts[i]]

        # Create the new path if it doesn't exist
        if parts[-1] in node:
            return False  # Path already exists

        node[parts[-1]] = {"value": value}  # Store value at leaf
        return True

    def get(self, path):
        """
        :type path: str
        :rtype: int
        """
        parts = path.split("/")[1:]
        node = self.trie

        # Traverse the Trie to find the path
        for part in parts:
            if part not in node:
                return -1  # Path doesn't exist
            node = node[part]

        return node.get("value", -1)