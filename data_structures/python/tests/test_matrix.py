from ..matrix import Matrix

matrix_1 = Matrix(rows=3, columns=2, data=(0, 1, 2, 3, 4, 5,))
print(matrix_1)

data_2 = (6, 7, 8, 9, 1, 0,)
matrix_2 = Matrix(rows=3, columns=2, data=data_2)
print(matrix_2)

print(matrix_1 + matrix_2)

print(matrix_1 - matrix_2)

matrix_2.scale_by(scalar=3)
print(matrix_2)

matrix_3 = Matrix(rows=2, columns=3, data=data_2)
print(matrix_3)
print(matrix_1 * matrix_3)

print(matrix_1.transpose())



