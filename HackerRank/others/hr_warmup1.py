matrix_size = int(input())

# initialize a 2D matrix
matrix = [[0 for x in range(matrix_size)] for y in range(matrix_size)]

# taking input in 2D matrix
for i in range(matrix_size):
    matrix[i] = [int(x) for x in input().split()]

primary_diagonal = 0
secondary_diagonal = 0
for i in range(matrix_size):
    # summing the values
    primary_diagonal += matrix[i][i]
    secondary_diagonal += matrix[i][matrix_size-1-i]

# showing absolute difference in output
print(abs(primary_diagonal - secondary_diagonal))
