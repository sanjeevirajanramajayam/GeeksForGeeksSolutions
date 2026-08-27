class Solution:
    def inversionCount(self, arr):
        # code here
        ans = 0
        def merge(l1, r1, l2, r2):
            nonlocal ans
            newArr = []
            i = l1
            j = l2
            while i <= r1 and j <= r2:
                if arr[i] > arr[j]:
                    newArr.append(arr[j])
                    j += 1
                    ans += (r1 - i + 1)
                else:
                    newArr.append(arr[i])
                    i += 1

            while i <= r1:
                newArr.append(arr[i])
                i += 1

            while j <= r2:
                newArr.append(arr[j])
                j += 1
            # print(arr[l1:r2+1], newArr)
            for i in range(l1, r2 + 1):
                arr[i] = newArr[i - l1]
            # print(arr[l1:r2+1], newArr)

        def mergeSort(low, high):
            # print(low, high)
            if low >= high:
                return
            mid = (low + high) // 2
            left = mergeSort(low, mid)
            right = mergeSort(mid + 1, high)
            return merge(low, mid, mid + 1, high)
        mergeSort(0, len(arr) - 1)
        return ans