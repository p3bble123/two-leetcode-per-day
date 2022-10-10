class Solution:
    def isPalindrome(self, x: int) -> bool:
        number = str(x)
        
        for i in range(len(number)//2):
            left = i
            right = len(number)-1-i

            if right == left or right < left:
                break

            if number[right] != number[left]:
                return False

        return True
