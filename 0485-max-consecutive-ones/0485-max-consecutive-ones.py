class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxCount = 0
        currCount = 0

        for i in nums:
            if i == 1:
                currCount += 1
                maxCount = max(maxCount, currCount)
            else:
                currCount = 0
        return maxCount
