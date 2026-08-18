from functools import cache
class Solution:
    def countWays(self, s):
        # code here
        @cache
        def fn(i, j, isTrue):
            if i > j:
                return 0
            if i == j:
                if isTrue:
                    if s[i] == 'T':
                        return 1
                    else:
                        return 0
                else:
                    if s[i] == 'F':
                        return 1
                    else:
                        return 0
            ways = 0
            for k in range(i + 1, j, 2):   
                lt = fn(i, k - 1, True)
                lf = fn(i, k - 1, False)
                rt = fn(k + 1, j, True)
                rf = fn(k + 1, j, False)
                if s[k] == '&':
                    if isTrue:
                        ways += (lt * rt)
                    else:
                        ways += (lt * rf) + (lf * rt) + (lf * rf)
                elif s[k] == '|':
                    if isTrue:
                        ways += (lt * rt) + (lt * rf) + (lf * rt)
                    else:
                        ways += (lf * rf)
                else:
                    if isTrue:
                        ways +=  (lt * rf) + (lf * rt)
                    else:
                        ways += (lf * rf) + (lt * rt)
                
            return ways
        return fn(0, len(s) - 1, True)