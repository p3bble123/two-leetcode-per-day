class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        appeared = {}

        if len(nums) % 2 == 0:
            n = len(nums) // 2
        else:
            n = len(nums) // 2 + 1

        for num in nums:
            if num in appeared:
                appeared[num] += 1
                if appeared[num] >= n:
                    return num
                continue
            else:
                appeared[num] = 1
