class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True

        isFirstCapital = word[0].isupper()
        isSecondCapital = word[1].isupper()

        if isSecondCapital:
            for char in word:
                if char.islower():
                    return False
            return True

        for i in range(2, len(word)):
            if word[i].isupper():
                return False

        return True