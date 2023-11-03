# Write your solution here

def transpose(matrix: list):
    new_matrix = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[i])):
            row.append(matrix[i][j])
        new_matrix.append(row)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrix[i][j] = new_matrix[j][i]
