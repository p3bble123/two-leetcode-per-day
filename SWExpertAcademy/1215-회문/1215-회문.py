def solution():
    numOfTests = 10
    tests = getInput(numOfTests)
    result = [findPalindromes(test) for test in tests]

    for i in range(len(result)):
        print(f'#{i+1} {result[i]}')


def getInput(numOfTests):
    tests, sizeOfGrid = [], 8
    for i in range(numOfTests):
        grid = []
        palindromeSize = int(input())
        for j in range(sizeOfGrid):
            grid.append(input())

        tests.append([grid, palindromeSize])

    return tests


def findPalindromes(test):
    grid, palindromeSize = test[0], test[1]
    validPalindromes, sizeOfGrid = 0, 8

    for row in range(sizeOfGrid):
        for col in range(0, sizeOfGrid - palindromeSize + 1):
            candidate = grid[row][col:col+palindromeSize]
            if isValidPalindrome(candidate):
                validPalindromes += 1


    for col in range(sizeOfGrid):
        colStr = getColumn(grid, col)
        for i in range(0, sizeOfGrid - palindromeSize + 1):
            candidate = colStr[i:i+palindromeSize]
            if isValidPalindrome(candidate):
                validPalindromes += 1

    return validPalindromes


def isValidPalindrome(candidate):
    mid, idx = len(candidate)//2, 0
    while idx < mid:
        if candidate[idx] != candidate[-idx-1]:
            return False
        idx += 1
    return True

def getColumn(grid, col):
    colStr = ''
    for i in range(len(grid)):
        colStr += grid[i][col]

    return colStr


solution()
