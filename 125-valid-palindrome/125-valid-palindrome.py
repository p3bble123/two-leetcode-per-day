class Solution:
    def isPalindrome(self, s: str) -> bool:
        toLower = s.lower()
        alphabets = ''
        for char in toLower:
            order = ord(char)
            if (order >= 48 and order <= 57) or (order >= 97 and order <=122):
                alphabets += char

        for i in range(len(alphabets)//2):
            if alphabets[i] != alphabets[len(alphabets)-1-i]:
                return False

        return True