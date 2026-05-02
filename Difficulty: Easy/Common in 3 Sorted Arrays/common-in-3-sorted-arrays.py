class Solution:
    def commonElements(self, a, b, c):
        # code here
        a = set(a)
        b = set(b)
        c = set(c)
        u = a.intersection(b)
        u = u.intersection(c)
        u = list(u)
        u.sort()
        return u