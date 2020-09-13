from .two_dimension_array import TwoDimensionArray


class Matrix(TwoDimensionArray):
    def __init__(self, rows, columns, data=None):
        super().__init__(rows_number=rows, columns_number=columns, init_value=0, data=data)

    def scale_by(self, scalar):
        for row in range(self.row_number):
            for column in range(self.column_number):
                self[row, column] *= scalar

    def transpose(self):
        transposed_matrix = Matrix(rows=self.column_number, columns=self.row_number)
        for row in range(self.row_number):
            for column in range(self.column_number):
                transposed_matrix[column, row] = self[row, column]
        return transposed_matrix

    def __add__(self, other_matrix):
        return self._add_or_subtract(other_matrix=other_matrix, add_or_subtract_method="__add__")

    def __sub__(self, other_matrix):
        return self._add_or_subtract(other_matrix=other_matrix, add_or_subtract_method="__sub__")

    def _add_or_subtract(self, other_matrix, add_or_subtract_method):
        assert add_or_subtract_method in ["__add__", "__sub__"], "Method must be '__add__' or '__sub__'"
        assert self.row_number == other_matrix.row_number and self.column_number == other_matrix.column_number, \
            "Matrices must be equal."
        result_matrix = Matrix(rows=self.row_number, columns=self.column_number)
        for row in range(self.row_number):
            for column in range(self.column_number):
                required_method = getattr(self[row, column], add_or_subtract_method)
                result_matrix[row, column] = required_method(other_matrix[row, column])
        return result_matrix

    def __mul__(self, other_matrix):
        assert self.column_number == other_matrix.row_number, "The number of columns in the matrix on the left hand \
        side must be equal to the number of rows in the matrix on the right hand side."
        result_matrix = Matrix(rows=self.row_number, columns=other_matrix.column_number)
        for result_row in range(result_matrix.row_number):
            for result_column in range(result_matrix.column_number):
                multiplication = 0
                for shift in range(self.column_number):
                    multiplication += self[result_row, shift] * other_matrix[shift, result_column]
                result_matrix[result_row, result_column] = multiplication
        return result_matrix

    def __str__(self):
        matrix_string = str()
        max_item_size = int()
        for row in range(self.row_number):
            for column in range(self.column_number):
                max_item_size = max(max_item_size, len(str(self[row, column])))
        max_item_size += 1
        for row in range(self.row_number):
            for column in range(self.column_number):
                matrix_string += f"{self[row, column]:<{max_item_size}}"
            matrix_string += "\n"
        return matrix_string




