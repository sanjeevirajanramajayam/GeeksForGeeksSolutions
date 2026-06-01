class Solution:
    def makeBeautiful(self, arr: list[int]) -> list[int]:
        # code here
        def diff(x, y):
            if (x >= 0 and y < 0) or (x < 0 and y >= 0):
                return True
            return False
        stack = []
        for i in range(len(arr)):
            # print(stack)
            cont=False
            while stack and diff(arr[i], stack[-1]):
                stack.pop()
                cont = True
                break
            if cont:
                continue
            stack.append(arr[i])
        return stack