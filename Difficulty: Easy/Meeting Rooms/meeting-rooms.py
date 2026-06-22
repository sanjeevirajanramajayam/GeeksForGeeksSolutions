class Solution:
    def canAttend(self, arr):
        # Code Here
        arr = sorted(arr, key=lambda x: (x[0], x[1]))
        ans = []
        # print(arr)
        for x in arr:
            if not ans:
                ans.append(x)
            elif ans[-1][1] > x[0]:
                return False
            else:
                ans.append(x)
        return True