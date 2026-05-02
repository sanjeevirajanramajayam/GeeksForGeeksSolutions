class Solution:
    def subarrayXor(self, arr, k):
        xhash = {0: 1}
        cXOR = 0
        cnt = 0
        for i in range(len(arr)):
            cXOR ^= arr[i]
            if cXOR ^ k in xhash:
                cnt += xhash[cXOR ^ k]
            xhash[cXOR] = xhash.get(cXOR, 0) + 1
        return cnt