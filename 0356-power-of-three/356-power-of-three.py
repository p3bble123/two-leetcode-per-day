class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        else:
            return self.checkThree(n)

    def checkThree(self, n):
        if n == 1:
            return True
        if n % 2 == 0:
            return False
        else:
            if n % 3 == 0:
                return self.checkThree(n / 3)
            else:
                return False
