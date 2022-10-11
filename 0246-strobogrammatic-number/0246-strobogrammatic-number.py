class Solution:
    def isStrobogrammatic(self, num: str) -> bool:

        invalidNums = ['2', '4', '3', '5', '7']
        flippable = {'1': '1', '6': '9', '8': '8', '9': '6', '0': '0'}

        n = len(num)
        flipped = ''

        for i in range(n):
            if num[n - 1 - i] in invalidNums:
                return False
            else:
                flipped += flippable[num[n - 1 - i]]

        if flipped == num:
            return True
        else:
            return False
