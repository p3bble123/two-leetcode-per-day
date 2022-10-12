class Solution:
    def longestPalindrome(self, s: str) -> int:
        charDict = {}
        palindromeLen, oddNums = 0, []

        for char in s:
            if char in charDict:
                charDict[char] += 1
            else:
                charDict[char] = 1

        for char in charDict:
            if charDict[char] % 2 == 0:
                palindromeLen += charDict[char]
            else:
                oddNums.append(charDict[char])

        if len(oddNums) > 0:
            palindromeLen += sum(oddNums) - len(oddNums) + 1

        return palindromeLen
