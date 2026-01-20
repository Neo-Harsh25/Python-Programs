class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        a=[]
        for i in range(1,target[len(target)-1]):
            if i in target:
                a.append("Push")
            else:
                a.append("Push")
                a.append("Pop")
        a.append("Push")
        return a