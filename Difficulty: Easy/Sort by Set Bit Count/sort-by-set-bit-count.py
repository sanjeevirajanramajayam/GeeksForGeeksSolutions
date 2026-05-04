class Solution:
    def sortBySetBitCount(self, arr):
        # code here
        def bit_count(num):
            cnt = 0
            while num > 0:
                bit = num & 1
                num >>= 1
                # print(num, bit)
                if bit == 1:
                    cnt += 1
            return cnt
        
        arr.sort(key = lambda x: bit_count(x), reverse = True)
        return arr