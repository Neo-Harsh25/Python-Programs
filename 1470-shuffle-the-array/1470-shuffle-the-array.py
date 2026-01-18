import random
class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        
        newNums = []
        first_half = nums[:n]
        second_half = nums[n:]
        for i in range(n):
            newNums.append(first_half[i])
            newNums.append(second_half[i])

        return newNums