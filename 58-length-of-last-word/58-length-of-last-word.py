class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        splitS = s.split()
        
        return len(splitS[len(splitS)-1])