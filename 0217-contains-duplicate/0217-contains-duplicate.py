class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        appearance = {}

        for num in nums:
            if num in appearance:
                return True
            appearance[num] = 1

        return False