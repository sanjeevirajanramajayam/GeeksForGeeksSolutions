class Solution:
    def nextLargerElement(self, arr):
        # code here
        stack = []
        res = [-1] * len(arr)
        for i in range(len(arr) - 1, -1, -1):
            
            while stack and stack[-1] <= arr[i]:
                stack.pop()
            # print(i)
            if stack:
                res[i] = stack[-1]
            else:
                res[i] = -1
            
            stack.append(arr[i])
        
        return res
            