matrix = [
    [1,2],
    [3,4],
    [5,6]
]

mat2 = []

for col in range(len(matrix[0])):
    temp = []
    for row in range(len(matrix)):
        temp.append(matrix[row][col])
    mat2.append(temp)

print(mat2)

# print(len(mat[2]))
