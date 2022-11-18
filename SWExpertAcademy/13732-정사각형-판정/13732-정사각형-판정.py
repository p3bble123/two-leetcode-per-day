import sys

def solution():
    numOfTests = int(input())
    grids = getInput(numOfTests)
    result = []

    for grid in grids:
        result.append(validateGrid(grid))

    for i in range(len(result)):
        print(f"#{i+1} {result[i]}")


def getInput(numOfTests):
    grids = []
    for i in range(numOfTests):
        numOfRows, grid = int(input()), []
        for j in range(numOfRows):
            grid.append(input())
        grids.append(grid)

    return grids


def validateGrid(grid):
    visited = set([])
    numOfSingleBlocks = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '#' and (row, col) not in visited:
                visited.add((row, col))

                edgeLength = getEdgeLength(grid[row], col)
                if edgeLength == 1:
                    numOfSingleBlocks += 1
                    continue

                isValidSquare = validateSquare(grid, edgeLength, row, col, visited)
                if not isValidSquare:
                    return 'no'

    if numOfSingleBlocks > 1:
        return 'no'
    return 'yes'


def getEdgeLength(gridRow, col):
    edge = 1
    curCol = col+1
    while curCol < len(gridRow) and gridRow[curCol] == '#':
        edge += 1
        curCol += 1

    return edge


def validateSquare(grid, edgeLength, row, col, visited):
    for r in range(row, row+edgeLength):
        for c in range(col, col+edgeLength):
            if r >= len(grid) or c >= len(grid[0]):
                return False

            visited.add((r, c))
            if grid[r][c] != '#':
                return False

    return True


solution()