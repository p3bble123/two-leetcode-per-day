class Solution:
    def rob(self, nums: List[int]) -> int:
        mem = {}
        if len(nums) == 1:
            return nums[0]
        else:
            return max(self.robMax(1, nums, True, True, 0 + nums[0], mem),
                       self.robMax(1, nums, False, False, 0, mem))

    def robMax(self, cur, houses, firstRobbed, prevRobbed, money, mem):
        if (cur, firstRobbed, prevRobbed) in mem:
            return money + mem[(cur, firstRobbed, prevRobbed)]

        if cur == len(houses) - 1:
            if firstRobbed is False and prevRobbed is False:
                return money + houses[cur]
            else:
                return money

        if prevRobbed is True:
            result = self.robMax(cur + 1, houses, firstRobbed, False, money, mem)
            mem[(cur, firstRobbed, prevRobbed)] = result - money
            return result
        else:
            result = max(self.robMax(cur + 1, houses, firstRobbed, True, money + houses[cur], mem),
                         self.robMax(cur + 1, houses, firstRobbed, False, money, mem))
            mem[(cur, firstRobbed, prevRobbed)] = result - money
            return result
