class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res = []  # Result list for justified lines
        line, line_len = [], 0  # Current line words & character length

        for word in words:
            if line and line_len + len(word) + len(line) > maxWidth:
                # Fully justify the current line before adding a new word
                for i in range(maxWidth - line_len):
                    line[i % (len(line) - 1 or 1)] += ' '  # Distribute spaces

                res.append(''.join(line))  # Add justified line to result
                line, line_len = [], 0  # Reset for next line

            # Add word to the current line
            line.append(word)
            line_len += len(word)

        # Left justify the last line
        res.append(' '.join(line).ljust(maxWidth))  # Left-justify & pad spaces

        return res