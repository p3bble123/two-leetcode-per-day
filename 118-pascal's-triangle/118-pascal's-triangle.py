class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = [[1], [1,1]]

        if numRows == 0:
            return []
        if numRows <= 2:
            return pascal[:numRows]

        row = 2

        while row < numRows:
            ithRow = []
            ithRow.append(pascal[row-1][0])

            for i in range(row-1):
                ithRow.append(pascal[row-1][i] + pascal[row-1][i+1])

            ithRow.append(pascal[row-1][-1])
            pascal.append(ithRow)
            row += 1

        return pascal[:numRows]