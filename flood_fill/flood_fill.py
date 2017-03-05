
class InvalidMatrix(Exception):
    pass


class FloodFill(object):
    def __init__(self, matrix, rows, cols):
        if not matrix:
            raise InvalidMatrix("Empty matrix provided as input.")
        if not isinstance(matrix, list) or not isinstance(matrix[0], list):
            raise InvalidMatrix("Inputted matrix is not 2D.")
        self.matrix = matrix
        self.rows = rows
        self.cols = cols

    def is_valid_point(self, row, col):
        return 1 <= row <= self.rows and 1 <= col <= self.cols

    def can_fill_point(self, row, col):
        return self.is_valid_point(row, col) and not self.matrix[row-1][col-1]

    def flood_fill(self, row, col):
        if self.can_fill_point(row, col):
            spots_to_fill = [(row, col)]
            while len(spots_to_fill) >= 1:
                fill_row, fill_col = spots_to_fill.pop()
                self.matrix[fill_row-1][fill_col-1] = 1
                for adj in [-1, 1]:
                    if self.can_fill_point(fill_row, fill_col + adj):
                        spots_to_fill.append((fill_row, fill_col + adj))
                    if self.can_fill_point(fill_row + adj, fill_col):
                        spots_to_fill.append((fill_row + adj, fill_col))