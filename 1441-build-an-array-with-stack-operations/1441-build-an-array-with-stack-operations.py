class Solution(object):
   
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        # stack = []
        # for i in range(1,n+1):
        #     if i in target:
        #         stack.append("Push")
        #     else:
        #         stack.append("Push")
        #         stack.append("Pop")
        # return stack     
        index = 0
        stack = []
        for stream in range(1, n+1):
            if index >= len(target):
                break

            if stream == target[index]:
                stack.append("Push")
                index +=1

            else:
                stack.append("Push")
                stack.append("Pop")  

        return stack              