class Solution(object):
    def findDisappearedNumbers(self, nums):
        setN=set(nums)
        ret=[]
        for i in range(1,len(nums)+1):
            if i not in setN:
                ret.append(i)    
        return ret