class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictionary = self.getDictionary(s)

        for char in t:
            if char not in dictionary:
                return False

            if dictionary[char] == 1:
                del dictionary[char]
                continue
            dictionary[char] -= 1

        if len(dictionary) > 0:
            return False
        return True


    def getDictionary(self, s):
        dictionary = {}

        for char in s:
            if char in dictionary:
                dictionary[char] += 1
                continue
            dictionary[char] = 1

        return dictionary