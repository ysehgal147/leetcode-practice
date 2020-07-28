class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

#---------------------Solution1----------------------#

        max_so_far = min(nums)
        maximum = 0
        for i in nums:
            maximum += i
            if maximum < i:
                maximum = i
            if max_so_far < maximum:
                max_so_far = maximum
        return max_so_far

#---------------------Solution2----------------------# Concise

        curSum = maxSum = nums[0]
        for num in nums[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)

        return maxSum
