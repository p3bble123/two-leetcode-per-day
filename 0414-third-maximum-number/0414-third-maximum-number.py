class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        numSet = set()
        for num in nums:
            numSet.add(num)

        if len(numSet) < 3:
            return max(numSet)

        for i in range(2):
            numSet.remove(max(numSet))
        return max(numSet)
