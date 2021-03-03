matrix_one = np.asarray([
    [30, -1, -500],
    [50, -1, -100]
], dtype=np.float32)
# Swap the second row (at index value 1) with the first row (at index value 0).
matrix = matrix[[1,0]]
# Multipy the second row by 2.
matrix[1] = 2*matrix[1]
# Add the second row to the first row.
matrix[1] = matrix[1] + matrix[0]
#divide the first row by 30
matrix_one[0] /= 30



import matplotlib.pyplot as plt
import numpy as np

plt.axhline(0, c='black', lw=0.5)
plt.axvline(0, c='black', lw=0.5)
plt.xlim(-3,3)
plt.ylim(-4,4)

# This code draws the x and y axis as lines.
plt.quiver(0,0,2,3, angles='xy', scale_units='xy', scale=1, color='blue')
plt.quiver(0,0,-2,-3, angles='xy', scale_units='xy', scale=1, color='blue')
plt.quiver(0,0,1,1, angles='xy', scale_units='xy', scale=1, color='gold')
plt.quiver(0,0,2,2, angles='xy', scale_units='xy', scale=1, color='gold')
plt.show()


import numpy as np

vector_one = np.asarray([
    [1],
    [2],
    [1]
], dtype=np.float32)

vector_two = np.asarray([
    [3],
    [0],
    [1]
],dtype=np.float32)

vector_linear_combination = vector_one*2 + vector_two*5

dot_product = np.dot(vector_one[:,0], vector_two) #first vector has to be represented in terms of rows and the second vector has to be represented in terms of columns
print(dot_product)





matrix_a = np.asarray([
    [0.7, 3, 9],
    [1.7, 2, 9],
    [0.7, 9, 2]
], dtype=np.float32)

vector_b = np.asarray([
    [1],
    [2],
    [1]
], dtype=np.float32)

ab_product = np.dot(matrix_a, vector_b)




i_2 = np.identity(2)
i_3 = np.identity(3)

matrix_33 = np.asarray([
    [2,3,4],
    [5,6,7],
    [1,5,9]
], dtype = np.float32)

matrix_23 = np.asarray([
    [1,2,6],
    [3,4,5]
], dtype=np.float32)

identity_33 = np.dot(matrix_33, i_3)
identity_23 = np.dot(i_2, matrix_23)




matrix_a = np.asarray([
    [1.5, 3],
    [1, 4]
])
def matrix_inverse_two(mat):
    det = (mat[0,0]*mat[1,1] - mat[0,1]*mat[1,0])
    if det == 0:
        raise ValueError("The matrix isn't invertible")
    right_mat = np.asarray([
        [mat[1,1], -mat[0,1]],
        [-mat[1,0], mat[0,0]]
    ])
    inv_mat = np.dot(1/det, right_mat)
    return inv_mat
inverse_a = matrix_inverse_two(matrix_a)
i_2 = np.dot(inverse_a, matrix_a)
print(i_2)




matrix_a = ([
    [30, -1],
    [50, -1]
])

vector_b = np.asarray([
    [-1000],
    [-100]
])

matrix_a_inverse = np.linalg.inv(matrix_a)
solution_x = np.dot(matrix_a_inverse, vector_b)
print(solution_x)



matrix_22 = np.asarray([
    [8, 4],
    [4, 2]
])

matrix_33 = np.asarray([
    [1, 1, 1],
    [1, 1, 6],
    [7, 8, 9]
])

det_22 = np.linalg.det(matrix_22)
det_33 = np.linalg.det(matrix_33)
