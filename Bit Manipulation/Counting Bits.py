class Solution:
    def countBits(self, num: int) -> List[int]:
        res = []
        for i in range(num+1):
            temp = str(bin(i))
            res.append(temp.count("1"))
        return res
 
 #---------------------Solution2----------------# using Bit Manipulation

        res=[]
        for i in range(num+1):
            count=0
            while i != 0:
                i = i&(i-1)
                count+=1
            res.append(count)
        return res
