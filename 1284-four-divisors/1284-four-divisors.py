class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def getDivisors(n):
            divisors = set()
            for d in range(1, int(n ** 0.5) + 1):
                if n % d == 0:
                    divisors.add(d)
                    divisors.add(n // d)
                if len(divisors) > 4:  # Stop early if more than 4 divisors
                    return 0
            return sum(divisors) if len(divisors) == 4 else 0
        
        return sum(getDivisors(num) for num in nums)