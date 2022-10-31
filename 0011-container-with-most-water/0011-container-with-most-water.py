class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxWater = self.getWater(height, left, right)

        while True:
            if left + 1 == right or right - 1 == left:
                break

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

            maxWater = max(maxWater, self.getWater(height, left, right))

        return maxWater

    def getWater(self, height, left, right):
        leftVal, rightVal = height[left], height[right]
        water = min(leftVal, rightVal) * (right - left)

        return water