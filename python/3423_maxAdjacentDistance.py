class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        diff = -math.inf
        for i in range(1, len(nums)):
            new = abs(nums[i-1] - nums[i])
            if new > diff:
                diff = new
        if abs(nums[0] - nums[-1]) > diff:
            diff = abs(nums[0] - nums[-1])
        return diff