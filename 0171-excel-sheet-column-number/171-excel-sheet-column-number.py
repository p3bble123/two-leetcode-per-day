class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        capitals = {}
        columnNumber = 0
        n = len(columnTitle)-1

        for i in range(ord('A'), ord('Z')+1):
            capitals[chr(i)] = i-64

        for i in range(len(columnTitle)):
            columnNumber += capitals[columnTitle[n-i]] * (26**i)

        return columnNumber