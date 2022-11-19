def solution():
    numOfTests = int(input())
    tests = getInput(numOfTests)
    print(tests)

def getInput(numOfTests):
    tests = []
    for i in range(numOfTests):
        tests.append(int(input()))
    return tests

solution()