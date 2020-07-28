class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        #---------------------Solution1----------------------# Brute Force, Won't Work With All Cases
        a = min(nums)
        b = max(nums)
        for i in range(a,b+1):
            if i not in nums:
                return i
        
        #---------------------Solution2----------------------# More Speed, More Memory 
        data = set(i for i in range(len(nums)+1))
        x = data - set(nums)
        return list(x)[0]

        #---------------------Solution3----------------------# Mathematical
        n = len(nums)
        return int(n * (n+1) / 2 - sum(nums))
