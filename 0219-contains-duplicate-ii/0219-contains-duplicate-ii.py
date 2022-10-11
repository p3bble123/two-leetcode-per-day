class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # value = [indices]
        appearance = {}

        for i in range(len(nums)):
            if nums[i] in appearance:
                for idx in appearance[nums[i]]:
                    if abs(i - idx) <= k:
                        return True
                appearance[nums[i]].append(i)

            appearance[nums[i]] = [i]

        return False