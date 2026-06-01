class Solution:
    def replaceElements(self, arr):
        # code here
        n = len(arr)
        prev = arr[0]
        arr[0] = prev ^ arr[1]
        for i in range(1, len(arr) - 1):
            val = prev ^ arr[i + 1]
            prev = arr[i]
            arr[i] = val
        arr[n - 1] = arr[n - 1] ^ prev 
        return arr