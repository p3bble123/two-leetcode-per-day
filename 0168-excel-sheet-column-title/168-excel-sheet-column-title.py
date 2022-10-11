class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        n = columnNumber
        columnTitle = ''
        capitals = [chr(x) for x in range(ord('A'), ord('Z') + 1)]

        while n > 0:
            columnTitle = capitals[(n - 1) % 26] + columnTitle
            n = (n - 1) // 26

        return columnTitle