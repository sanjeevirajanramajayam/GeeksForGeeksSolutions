class Solution:
    def isToeplitz(self, mat):
        # code here
        ROWS = len(mat)
        COLS = len(mat[0])
        ans=[]
        def goDownDiag(row, col):
            prev = float('inf')
            while 0 <= row < ROWS and 0 <= col < COLS:
                if prev == float('inf'):
                    prev = mat[row][col]
                elif prev != mat[row][col]:
                    return False
                row += 1
                col += 1
        for i in range(ROWS - 1, -1, -1):
            if goDownDiag(i, 0) == False:
                return False
        for i in range(1, COLS):
            if goDownDiag(0, i) == False:
                return False
        return (True)