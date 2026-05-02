class Solution:
    def smallestSubstring(self, s):
        # code here
        ans = float('inf')
        lastz = -1
        lasto = -1
        lastt = -1
        for i in range(len(s)):
            if s[i] == '0':
                lastz = i
            if s[i] == '1':
                lasto = i
            if s[i] == '2':
                lastt = i
            
            if lastz != -1 and lasto != -1 and lastt != -1:
                ans = min(ans, max(lastz, lasto, lastt) - min(lastz, lasto, lastt) + 1)
            
        if ans == float('inf'):
            return -1
        
        return ans