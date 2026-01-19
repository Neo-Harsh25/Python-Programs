class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = []
        a = 0
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if nums[i] > nums[j]:
                    a += 1
            count.append(a)
            a = 0
        return count