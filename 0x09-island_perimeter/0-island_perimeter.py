#!/usr/bin/python3
"""
Module to calculate the perimeter of an island in a grid.
The grid is represented as a list of lists, where 0 represents water
and 1 represents land. The function counts the perimeter of the island.
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.

    Args:
        grid (list of list of int): A 2D grid where 0 represents water and
                                    1 represents land.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Start with a perimeter of 4 for each land cell
                perimeter += 4

                # Check the cell above (i-1, j)
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 1

                # Check the cell below (i+1, j)
                if i < rows - 1 and grid[i+1][j] == 1:
                    perimeter -= 1

                # Check the cell to the left (i, j-1)
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 1

                # Check the cell to the right (i, j+1)
                if j < cols - 1 and grid[i][j+1] == 1:
                    perimeter -= 1

    return perimeter
