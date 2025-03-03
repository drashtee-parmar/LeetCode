class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # using dictionary of roman number using key value pair
        roman_value = {
            'I' : 1,
            'V' : 5,
            'X' : 10, 
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        total = 0
        prev_value = 0

        for char in reversed(s):
            current_value = roman_value[char]

            if current_value < prev_value:
                total -= current_value #subtraction
            else:
                total += current_value #Addition

            prev_value = current_value # updating previous value for next iteration
        return total
