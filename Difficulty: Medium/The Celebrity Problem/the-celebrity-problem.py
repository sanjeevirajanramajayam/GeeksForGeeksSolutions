class Solution:
    def celebrity(self, mat):
        # code here
        left = 0
        right = len(mat) - 1
        
        while left < right:
            if mat[left][right] == 1:
                left += 1
            else:
                right -= 1
        
        for i in range(len(mat)):
            if i == left:
                continue
            
            if not (mat[i][left] == 1 and mat[left][i] == 0):
                return -1
        return left