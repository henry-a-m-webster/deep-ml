def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    output = []
    for i in range(len(a[0])):
        row = []
        for k in range(len(a)):
            row.append(a[k][i])
        output.append(row)
    return output