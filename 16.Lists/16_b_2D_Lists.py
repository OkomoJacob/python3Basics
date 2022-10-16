"""
Each and every item in the list are in another list.E.g 3 by 3 Matrix
Applicable in ML DS
"""

Matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [4, 7, 9]
]
for row in Matrix:
    for x in row:
        print(row)
