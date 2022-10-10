class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        high, low = len(nums), 0

        while high > low:
            mid = (high + low) // 2

            if nums[mid] == target:
                return mid

            # use binary search (O(logn))
            if nums[mid] > target:
                high = mid
            else:
                low = mid + 1

        return low