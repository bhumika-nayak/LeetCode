class Solution(object):
    def setZeroes(self, matrix):
        n=len(matrix)
        m=len(matrix[0])
        row=[0]*n
        column=[0]*m
        for i in range(n):
            for j in range (m):
                if matrix[i][j]==0:
                    row[i]=1
                    column[j]=1
        for i in range (n):
            for j in range (m):
                if row[i] or column[j]:
                    matrix[i][j]=0
        return matrix

        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
    