def transpose_matrix(matrix: list[list[int]]):
    transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    return transposed