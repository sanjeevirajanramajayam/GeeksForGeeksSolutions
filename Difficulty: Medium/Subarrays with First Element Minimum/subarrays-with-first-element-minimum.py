class Solution:
    def countSubarrays(self, arr):
        # code here
        def nsee(arr):
            stack = []
            ans = 0
            for i in range(len(arr) - 1, -1, -1):
                while stack and arr[stack[-1]] >= arr[i]:
                    stack.pop()
                if not stack:
                    ans += len(arr) - i
                else:
                    ans += stack[-1] - i 
                stack.append(i)
                # print(stack, ans)
            return ans
        return nsee(arr)