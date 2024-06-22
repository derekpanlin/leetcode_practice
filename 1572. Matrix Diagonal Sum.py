# https://leetcode.com/problems/matrix-diagonal-sum/description/

# Given a square matrix mat, return the sum of the matrix diagonals.

# Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

 

# Example 1:


# Input: mat = [[1,2,3],
#               [4,5,6],
#               [7,8,9]]
# Output: 25
# Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
# Notice that element mat[1][1] = 5 is counted only once.
# Example 2:

# Input: mat = [[1,1,1,1],
#               [1,1,1,1],
#               [1,1,1,1],
#               [1,1,1,1]]
# Output: 8
# Example 3:

# Input: mat = [[5]]
# Output: 5
 

# Constraints:

# n == mat.length == mat[i].length
# 1 <= n <= 100
# 1 <= mat[i][j] <= 100

# POLYAS
# Check if mat is odd or even
# Create var to store sum
# If mat is odd and im at the mid row
    # a. I will add the 1 num
# Otherwise
    # b. Add 2 nums 

def diagonalSum(self, mat: List[List[int]]) -> int:
    length = len(mat[0])   
    is_odd = length % 2
    diag_sum = 0
    
    for row in range(length):
        if is_odd and row == length // 2:
            diag_sum += mat[row][row]
        else:
            diag_sum += mat[row][row]
            diag_sum += mat[row][length - 1 - row]
        
    return diag_sum
