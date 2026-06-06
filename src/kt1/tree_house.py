from typing import TypedDict

type Matrix = list[list[int]]


class Coordinate(TypedDict):
    row: int
    column: int


def get_good_coordinates(matrix: Matrix) -> list[Coordinate]:
    if not matrix:
        return []

    first_len = len(matrix[0])
    for row in matrix:
        if len(row) != first_len:
            raise ValueError("irregular matrix")

    if first_len == 0:
        return []

    rows = len(matrix)
    cols = first_len
    res = []

    for r in range(rows):
        for c in range(cols):
            val = matrix[r][c]

            is_max = True
            for x in matrix[r]:
                if x > val:
                    is_max = False
                    break

            is_min = True
            for i in range(rows):
                if matrix[i][c] < val:
                    is_min = False
                    break

            if is_max and is_min:
                res.append({"row": r + 1, "column": c + 1})

    return res
