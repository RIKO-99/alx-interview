#!/usr/bin/python3
"""The Island Perimeter challange."""


def island_perimeter(grid):
    """Returns the perimeter of the island described in grid.

    Args:
        grid (list): A list of lists of integers.

    Returns:
        int: The perimeter of the island described in grid.
    """
    assumed_perimeter = 0
    connections = 0
    top_conn = 0
    left_conn = 0

    for row_idx, row in enumerate(grid):
        for col_idx, col in enumerate(row):
            if col == 1:
                assumed_perimeter += 4
                if row_idx > 0:
                    if grid[row_idx - 1][col_idx] == 1:
                        top_conn += 1
                if col_idx > 0:
                    if row[col_idx - 1] == 1:
                        left_conn += 1
    connections += top_conn + left_conn
    total_connections = connections * 2
    total_perimeter = assumed_perimeter - total_connections
    return total_perimeter
