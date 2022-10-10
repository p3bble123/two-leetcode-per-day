import copy

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        row = 1
        pascalRow = [1, 1]

        while row < rowIndex:
            temp = []
            temp.append(pascalRow[0])
            for i in range(row):
                temp.append(pascalRow[i] + pascalRow[i + 1])
            temp.append(pascalRow[-1])

            pascalRow = copy.deepcopy(temp)
            row += 1

        return pascalRow