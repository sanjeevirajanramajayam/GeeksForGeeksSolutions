import heapq
class Solution:
    def kthLargest(self, arr, k):
        # code here 
        minHeap = [] # size k
        ans = [] 
        for i in range(len(arr)):
            heapq.heappush(minHeap, arr[i])
            if len(minHeap) < k:
                ans.append(-1)
                continue
            if len(minHeap) > k :
                heapq.heappop(minHeap)
            # print(ans)
            ans.append(minHeap[0])
        return ans