#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return []
    triangle = []
    for i in range(1, n + 1):
        row = []
        for j in range(1, i + 1):
            if (j == 1 or j == i or i <= 2):
                element = 1
            else:
                element = triangle[i - 2][j - 1] + triangle[i - 2][j - 2]
            row.append(element)
        triangle.append(row)
    return triangle
