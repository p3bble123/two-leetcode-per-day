class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cur, uniques = 0, 1
        size = len(nums)

        while cur < size - 1:
            if nums[cur] != nums[cur + 1]:
                nums[uniques] = nums[cur + 1]
                uniques += 1
            cur += 1
        return uniques