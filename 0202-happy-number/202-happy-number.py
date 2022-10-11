class Solution:
    def isHappy(self, n: int) -> bool:
        return self.checkHappy(n, {})

    def checkHappy(self, n, visited):
        n = str(n)
        squareDigits = 0

        for digit in n:
            squareDigits += int(digit) ** 2

        if squareDigits == 1:
            return True
        if squareDigits in visited:
            return False

        visited[squareDigits] = 1
        return self.checkHappy(squareDigits, visited)