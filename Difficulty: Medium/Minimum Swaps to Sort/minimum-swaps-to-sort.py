class Solution:
    
    #Function to find the minimum number of swaps required to sort the array.
	def minSwaps(self, arr):
		#Code here
		indexMap = {}
		sortedArr = sorted(arr)
		
		for i in range(len(arr)):
		    indexMap[arr[i]] = i
		swaps = 0
		for i in range(len(arr)):
		    if sortedArr[i] != arr[i]:
                o_i = i
                o_si = indexMap[sortedArr[i]]
                
                indexMap[arr[o_i]] = o_si
                indexMap[arr[o_si]] = o_i
                
                arr[o_i], arr[o_si] = arr[o_si], arr[o_i]
                

                swaps += 1
        # print(arr)
        return swaps