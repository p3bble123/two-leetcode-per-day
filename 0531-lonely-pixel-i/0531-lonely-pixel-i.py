class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        lonelyPixels = 0

        for row in range(len(picture)):
            for col in range(len(picture[0])):
                if picture[row][col] == "B":
                    if self.checkRow(row, col, picture) and self.checkCol(row, col, picture):
                        lonelyPixels += 1

        return lonelyPixels

    def checkRow(self, row, col, picture):
        for j in range(len(picture[0])):
            if j == col:
                continue
            if picture[row][j] == "B":
                return False
        return True

    def checkCol(self, row, col, picture):
        for i in range(len(picture)):
            if i == row:
                continue
            if picture[i][col] == "B":
                return False

        return True