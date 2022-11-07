class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        x = 1
        while x < n:  x *= 3
        return x == n