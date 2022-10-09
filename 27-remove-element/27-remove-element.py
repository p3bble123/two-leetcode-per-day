class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        nums[:] = (value for value in nums if value != val)

        return len(nums)