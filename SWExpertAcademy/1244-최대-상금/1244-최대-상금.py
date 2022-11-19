def solution():
    numOfTests = int(input())
    tests = getInput(numOfTests)
    result = [getMaxPrizeMoney(test) for test in tests]

    for i in range(len(result)):
        nums = [str(x) for x in result[i]]
        nums = ''.join(nums)
        print(f'#{i+1} {nums}')


def getMaxPrizeMoney(test):
    originalNums, swaps = test[0], test[1]
    sortedNums = sorted(originalNums, reverse=True)
    idxDict = {}

    # print(originalNums, sortedNums)

    for i in range(len(originalNums)):
        if originalNums[i] not in idxDict:
            idxDict[originalNums[i]] = []
        idxDict[originalNums[i]].append(i)

    idx = 0

    while swaps > 0:
        if idx >= len(originalNums):
            if swaps%2:
                originalNums[-1], originalNums[-2] = originalNums[-2], originalNums[-1]
            return originalNums

        if originalNums[idx] != sortedNums[idx]:
            curNum = originalNums[idx]  # 2
            swapNum = sortedNums[idx]   # 7

            swapIdx = max(idxDict[swapNum])

            # print(idx, swapIdx, curNum, idxDict)

            idxDict[curNum].remove(idx)
            idxDict[curNum].append(swapIdx)

            idxDict[swapNum].remove(swapIdx)
            idxDict[swapNum].append(idx)

            originalNums[idx], originalNums[swapIdx] = originalNums[swapIdx], originalNums[idx]

            swaps -= 1

        idx += 1

    return originalNums


def getInput(numOfTests):
    tests = []
    for i in range(numOfTests):
        test = input().split()
        numbers = list(map(int, test[0]))
        swaps = int(test[1])
        tests.append([numbers, swaps])

    return tests


solution()