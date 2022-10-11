class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        patternInts = self.listToInt([*pattern])
        sInts = self.listToInt(s.split())

        return True if patternInts == sInts else False


    def listToInt(self, elements):
        count, intList, dictionary = 1, [], {}

        for element in elements:
            if element in dictionary:
                intList.append(dictionary[element])
                continue
            dictionary[element] = count
            intList.append(dictionary[element])
            count += 1

        return intList
