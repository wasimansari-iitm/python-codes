def determinant(matrix):
    # Base case: if the matrix is 1x1, the determinant is the only element
    if len(matrix) == 1:
        return matrix[0][0]

    # Base case: if the matrix is 2x2, apply the formula directly
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    # Recursive case: find the determinant of a larger matrix
    det = 0
    for col in range(len(matrix)):
        # Create a submatrix by excluding the current row (0) and column (col)
        submatrix = [row[:col] + row[col+1:] for row in matrix[1:]]

        # Recursive call to get the determinant of the submatrix
        cofactor = ((-1) ** col) * matrix[0][col] * determinant(submatrix)

        # Add the cofactor to the determinant
        det += cofactor

    return det

# Example usage:
matrix = [[4, 3, 7],[6, 3, 8],[7, 8, 5]]

print("Determinant:", determinant(matrix))
