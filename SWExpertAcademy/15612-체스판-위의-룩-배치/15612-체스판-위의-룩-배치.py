import sys
# sys.stdin = open("15612-체스판-위의-룩-배치/input.txt", "r")

def solution():
    numOfTests = int(input())
    if numOfTests < 1: return
    grids = getGrids(numOfTests)

    results = [validateRooks(grid) for grid in grids]

    for num in range(len(results)):
        print(f'#{num+1} {results[num]}')


def getGrids(numOfTests):
    grids, grid, lineCount = [], [], 0

    for i in range(8 * numOfTests):
        lineCount += 1
        grid.append(input())
        if lineCount == 8:
            grids.append(grid)
            grid, lineCount = [], 0
    return grids


def validateRooks(grid):
    visitedRows, visitedCols, numOfRooks = set([]), set([]), 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 'O':
                if col in visitedCols or row in visitedRows:
                    return 'no'

                visitedRows.add(row)
                visitedCols.add(col)
                numOfRooks += 1

    if numOfRooks == 8: return 'yes'
    return 'no'


solution()