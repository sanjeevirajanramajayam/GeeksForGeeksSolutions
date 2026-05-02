class Solution:
    def diagView(self, mat): 
        # code here 
        ROWS = len(mat)
        COLS = len(mat[0])
        ans=[]
        def goDownDiag(row, col):
            nonlocal ans
            while 0 <= row < ROWS and 0 <= col < COLS:
                ans.append(mat[row][col])
                row += 1
                col -= 1
        for i in range(COLS):
            goDownDiag(0, i)
        for i in range(1, ROWS):
            goDownDiag(i, COLS - 1)
        return (ans)