class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

#---------------------Solution1----------------------# Dutch Flag Problem

        zero, one, two = 0, 0, len(nums)-1

        while one <= two:
            if nums[one] == 0:
                nums[one], nums[zero] = nums[zero], nums[one]
                zero += 1
                one += 1
            elif nums[one] == 1:
                one += 1
            else:
                nums[one], nums[two] = nums[two], nums[one]
                two -= 1


#---------------------Solution2----------------------# Brute Force, Fast

        zeros=nums.count(0)
        for _ in range(zeros):
            nums.remove(0)
            nums.append(0)
        ones=nums.count(1)
        for _ in range(ones):
            nums.remove(1)
            nums.append(1)
        twos=nums.count(2)
        for _ in range(twos):
            nums.remove(2)
            nums.append(2)

