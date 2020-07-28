class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

#---------------------Solution1----------------------#

        x = set(nums)
        for i in x:
            if nums.count(i) > 1:
                return i

#---------------------Solution2----------------------#

        for _ in range(len(nums)):
            x = nums.pop(0)
            if x in nums:
                return x
