def transpose(matrix: list[list[int]]) -> list[list[int]]:
    res = [[0] * len(matrix) for _ in range(len(matrix[0]))]

    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            res[c][r] = matrix[r][c]
    
    return res

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(transpose(matrix=matrix))