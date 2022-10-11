class Solution:
    def addDigits(self, num: int) -> int:
        digitSum = num

        while digitSum > 9:
            n = str(digitSum)
            digitSum = 0

            for digit in n:
                digitSum += int(digit)

        return digitSum