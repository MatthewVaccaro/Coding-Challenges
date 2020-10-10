# https: // www.codewars.com/kata/526233aefd4764272800036f/train/python
# Write a function that accepts two square matrices(N x N two dimensional arrays), and return the sum of the two. Both matrices being passed into the
# function will be of size N x N(square), containing only integers.
# How to sum two matrices:
# Take each cell[n][m] from the first matrix, and add it with the same[n][m] cell from the second matrix. This will be cell[n][m] of the solution matrix.

def matrix_addition(a, b):
    matrix = []
    innerList = []

    for row in range(len(a)):
        for col in range(len(b)):
            innerList.append(a[row][col] + b[row][col])
        matrix.append(innerList)
        innerList = []
    return matrix
        
           
print(matrix_addition([[1, 2],
                       [1, 2] ],
                      [[2, 3],
                       [2, 3]]))
