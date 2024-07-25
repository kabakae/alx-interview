# 0-pascal_triangle.py
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
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)

    return triangle
