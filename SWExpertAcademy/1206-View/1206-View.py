# import sys

def solution():
    numOfTests = 10
    tests = getInput(numOfTests)
    result = []

    for test in tests:
        result.append(checkView(test))

    for i in range(len(result)):
        print(f"#{i+1} {result[i]}")

    return

def getInput(numOfTests):
    tests = []
    for i in range(numOfTests):
        testLength = input()
        testInput = input().split(' ')
        test = list(map(int, testInput))
        tests.append(test)

    return tests


def checkView(test):
    validViews = 0
    for i in range(2, len(test)-2):
        if test[i-1] < test[i] and test[i-2] < test[i]:
            if test[i+1] < test[i] and test[i+2] < test[i]:
                validViews += test[i] - max(test[i+1], test[i+2], test[i-1], test[i-2])

    return validViews


solution()