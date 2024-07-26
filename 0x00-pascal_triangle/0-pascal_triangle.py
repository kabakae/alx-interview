#!/usr/bin/python3
def pascal_triangle(n):
    """
    Generate Pascal's Triangle of height n.

    Args:
        n (int): The number of rows in Pascal's Triangle.

    Returns:
        list of lists: Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        # Create a new row with `i + 1` elements initialized to 1
        row = [1] * (i + 1)

        # Compute the values for non-edge elements
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]

        # Append the row to the triangle
        triangle.append(row)

    return triangle
