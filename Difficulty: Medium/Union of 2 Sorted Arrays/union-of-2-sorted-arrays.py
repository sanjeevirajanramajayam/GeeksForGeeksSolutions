class Solution:
    def findUnion(self, a, b):
        # code here 
        l = 0
        r = 0
        ln = len(a)
        rn = len(b)
        ans = []
        while l < len(a) and r < len(b):
            if a[l] <= b[r]:
                if not ans or ans[-1] != a[l]:
                    ans.append(a[l])
                l += 1
            else:
                if not ans or ans[-1] != b[r]:
                    ans.append(b[r])
                r += 1
        
        while l < len(a):
            if ans[-1] != a[l]:
                ans.append(a[l])
            l += 1

        while r < len(b):
            if ans[-1] != b[r]:
                ans.append(b[r])
            r += 1
        
        return ans