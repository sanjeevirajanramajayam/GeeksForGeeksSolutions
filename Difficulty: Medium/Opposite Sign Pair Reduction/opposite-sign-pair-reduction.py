class Solution:
    def reducePairs(self, arr):
        # code here
        def diff(a, b):
            return a / abs(a) == b / abs(b)
        
        stack = []
        for i in range(len(arr)):
            # print(stack, arr[i])
            while stack and not diff(arr[i], stack[-1]) and abs(arr[i]) > abs(stack[-1]):
                stack.pop()
            
            if stack and not diff(arr[i], stack[-1]) and abs(arr[i]) == abs(stack[-1]):
                stack.pop()
                continue
            
            if stack and not diff(arr[i], stack[-1]) and abs(arr[i]) < abs(stack[-1]):
                continue
            
            stack.append(arr[i])
        
        return stack
            