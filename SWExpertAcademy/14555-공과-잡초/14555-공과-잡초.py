import sys

def solution():
    numOfTests = int(input())
    fields = getInput(numOfTests)
    result = []
    for field in fields:
        result.append(countMinimumBalls(field))

    for i in range(len(result)):
        print(f"#{i+1} {result[i]}")


def getInput(numOfTests):
    fields = []
    for i in range(numOfTests):
        fields.append(input())

    return fields


def countMinimumBalls(field):
    minBalls = 0
    for i in range(len(field)):
        if field[i] == '(':
            minBalls += 1
        if field[i] == ')' and field[i-1] != '(':
            minBalls += 1

    return minBalls


solution()