class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        size = len(s)
        for i in range(len(s) // 2):
            temp = s[i]
            s[i] = s[size - i - 1]
            s[size - i - 1] = temp

        return s
