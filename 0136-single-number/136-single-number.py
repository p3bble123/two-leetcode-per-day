class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mem = {}

        for num in nums:
            if num not in mem:
                mem[num] = 1
            else:
                del mem[num]

        return list(mem.keys())[0]