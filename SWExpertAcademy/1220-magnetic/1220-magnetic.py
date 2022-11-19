def solution():
    numOfTests = 10
    tests = getInput(numOfTests)
    results = [findDeadlocks(test) for test in tests]

    for i in range(len(results)):
        print(f"#{i+1} {results[i]}")


def getInput(numOfTests):
    tests = []
    for i in range(numOfTests):
        grid = []
        numOfRows = int(input())
        for row in range(numOfRows):
            grid.append(list(map(int, input().split())))

        tests.append(grid)

    return tests


def findDeadlocks(test):
    deadlocks = 0

    for col in range(len(test[0])):
        northFirst, southSecond = False, False

        for row in range(len(test)):
            if test[row][col] == 1:
                northFirst = True
            if northFirst and test[row][col] == 2:
                deadlocks += 1
                northFirst, southSecond = False, False

    return deadlocks


solution()