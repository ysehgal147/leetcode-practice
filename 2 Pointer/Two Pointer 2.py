class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        #Two Pointer Approach

        start = 0
        end = len(numbers)-1
        
        while end>start:
            if numbers[start]+numbers[end]==target:
                return [start+1,end+1]
            elif numbers[start]+numbers[end]>target:
                end-=1
            else:
                start+=1
        
        #Stack Approach

        dict={}
        for i in numbers:
            difference = target - i
            if difference in dict:
                if dict[difference]==numbers.index(i):
                    return [dict[difference]+1,dict[difference]+2]
                return [dict[difference]+1,numbers.index(i)+1]
            else:
                dict[i]=numbers.index(i)
