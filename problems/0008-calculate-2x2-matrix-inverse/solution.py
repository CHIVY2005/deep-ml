def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    """
    Calculate the inverse of a 2x2 matrix.
    
    Args:
        matrix: A 2x2 matrix represented as [[a, b], [c, d]]
    
    Returns:
        The inverse matrix as a 2x2 list, or None if the matrix is singular
        (i.e., determinant equals zero)
    """
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    d = matrix[1][1]
    # Your code here
    det = a * d - b * c
    final = []
    if det == 0:
        return None
    inverse_matrix = [
        [d, -b],
        [-c, a]
    ]
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[i])):
            cal = inverse_matrix[i][j] / det
            row.append(cal)
        final.append(row)
    return final
