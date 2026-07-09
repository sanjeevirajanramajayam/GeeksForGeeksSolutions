class Solution:
    def fractionalKnapsack(self, val, wt, capacity):
        #code here
        valq = [[val[i] / wt[i], val[i], wt[i]] for i in range(len(val))]
        valq.sort(key=lambda x: x[0], reverse=True)
        ans = 0
        for ratio, val, wt in valq:
            if (wt > capacity):
                ans += (capacity / wt) * val
                break
            else:
                ans += val
                capacity -= wt
        return ans