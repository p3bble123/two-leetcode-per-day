def solution():
    numOfTests = int(input())
    tests = getInput(numOfTests)
    results = [getTimesModified(test) for test in tests]

    for i in range(len(results)):
        print(f"#{i+1} {results[i]}")


def getInput(numOfTests):
    return [input() for i in range(numOfTests)]

def getTimesModified(test):
    timesModified, shouldBeEqual = 0, True

    for i in range(len(test)):
        if (test[i] == '0') != shouldBeEqual:
            timesModified += 1
            shouldBeEqual = not shouldBeEqual

    return timesModified


solution()