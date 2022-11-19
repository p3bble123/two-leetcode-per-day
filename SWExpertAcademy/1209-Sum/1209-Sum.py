def solution():
    numOfTests = 10
    tests = getInput(numOfTests)
    results = [getMaxSum(test) for test in tests]

    for i in range(len(results)):
        print(f'#{i+1} {results[i]}')


def getInput(numOfTests):
    tests = []
    for i in range(numOfTests):
        testNumber, test = input(), []
        for i in range(100):
            row = list(map(int, input().split()))
            test.append(row)
        tests.append(test)

    return tests


def getDiagonalSumTopToBottom(test):
    diagonalSum = 0
    for i in range(len(test)):
        diagonalSum += test[i][i]

    return diagonalSum


def getDiagonalSumBottomToTop(test):
    diagonalSum = 0
    for i in range(len(test)):
        diagonalSum += test[-i-1][-i-1]

    return diagonalSum

def getMaxColumnSum(test):
    maxColumnSum = 0
    for col in range(len(test[0])):
        columnSum = 0
        for row in range(len(test)):
            columnSum += test[row][col]

        maxColumnSum = max(maxColumnSum, columnSum)

    return maxColumnSum

def getMaxSum(test):
    maxSum = 0

    for row in range(len(test)):
        maxSum = max(maxSum, sum(test[row]))

    maxSum = max(maxSum, getMaxColumnSum(test))
    maxSum = max(maxSum, getDiagonalSumBottomToTop(test))
    maxSum = max(maxSum, getDiagonalSumTopToBottom(test))

    return maxSum



solution()