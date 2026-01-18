class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        res = []
        for i in nums:
            if nums.count(i) > 1:
                res.append(i)
                break
        
        for i in range(1,len(nums)+1):
            if i not in nums:
                res.append(i)
                break
        
        return res