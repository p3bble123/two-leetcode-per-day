class Solution:
    def reverse(self, x: int) -> int:

        isNegative = True if x < 0 else False
        digits = self.numToString(x)
        reversed = 0

        for i in range(len(digits)):
            reversed += int(digits[i]) * (10 ** i)

        if reversed > (2 ** 31) - 1 or reversed < -(2 ** 31):
            return 0
        return -reversed if isNegative else reversed

    def numToString(self, n):
        if n < 0:
            return str(n)[1:]
        else:
            return str(n)