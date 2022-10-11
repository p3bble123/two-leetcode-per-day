class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:

        dictLen = len(wordsDict)
        idx1, idx2, minDist = dictLen - 1, dictLen - 1, dictLen

        for i in range(dictLen):
            if wordsDict[i] == word1:
                idx1 = i
                dist = abs(idx2 - idx1)
                minDist = min(dist, minDist)

            if wordsDict[i] == word2:
                idx2 = i
                dist = abs(idx2 - idx1)
                minDist = min(dist, minDist)

        return minDist
