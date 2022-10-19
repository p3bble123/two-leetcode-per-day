class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [str(nums[0])]

        start, numsLen = nums[0], len(nums)

        ranges = []

        for i in range(1, numsLen):
            if i == numsLen - 1:
                if nums[i] - nums[i - 1] > 1:
                    ranges.append(self.getRange(start, nums[i - 1]))
                    ranges.append(str(nums[i]))
                else:
                    ranges.append(self.getRange(start, nums[i]))
                break

            if nums[i] - nums[i - 1] > 1:
                ranges.append(self.getRange(start, nums[i - 1]))
                start = nums[i]

        return ranges

    def getRange(self, start, end):
        start, end, arrow = str(start), str(end), '->'
        return str(start) if (start == end) else (start + arrow + end)
