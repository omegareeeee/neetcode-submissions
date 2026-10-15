class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_length = len(matrix) 
        col_length = len(matrix[0])
        length = row_length * col_length - 1

        l, r = 0, length

        while(l <= r):
            m = l + ((r - l) // 2) #why does the other anaswer overflow?? 1 + 0 = 1
            row = m // col_length
            col = m %  col_length

            val = matrix[row][col]

            if (val > target):
                r = m - 1
            elif(val < target):
                l = m + 1
            else:
                return True

        return False

            