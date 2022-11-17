import sys
# sys.stdin = open("15230-알파벳-공부/input.txt", "r")

def solution():
    numOfTests = int(input())
    if numOfTests < 1: return

    lines = getInput(numOfTests)

    result = [validateLine(line) for line in lines]

    for i in range(len(result)):
        print(f"#{i+1} {result[i]}")


def getInput(numOfTests):
    lines = []
    for i in range(numOfTests):
        lines.append(input())

    return lines


def validateLine(line):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    validChars = 0
    for i in range(len(line)):
        if line[i] == alphabets[i]:
            validChars += 1
        else:
            return validChars

    return validChars

solution()