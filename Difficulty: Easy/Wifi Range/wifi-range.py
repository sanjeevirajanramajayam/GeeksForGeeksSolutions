class Solution:
    def wifiRange(self, s, x):
        # code here
        protected = set()
        stack = []
        cnt = 0
        for i in range(len(s)):
            if s[i] == "1":
                z = 0
                while stack and z < x:
                    # print(stack)
                    if stack[-1] >= i - x:
                        protected.add(stack.pop())
                    z += 1
            else:
                cnt += 1
                stack.append(i)
        stack = []
        cnt = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "1":
                z = 0
                while stack and z < x:
                    if stack[-1] <= i + x:
                        protected.add(stack.pop())
                    z += 1
            else:
                stack.append(i)
                cnt += 1
        # print(protected, cnt)
        return len(protected) == cnt