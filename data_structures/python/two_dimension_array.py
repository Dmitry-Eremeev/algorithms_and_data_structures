from .one_dimension_array import OneDimensionArray


class TwoDimensionArray:
    def __init__(self, rows_number, columns_number, init_value=None, data=None):
        self.__rows_number = rows_number
        self.__columns_number = columns_number
        self._array = OneDimensionArray(size=self.__rows_number, init_value=init_value)
        for index in range(len(self._array)):
            self._array[index] = OneDimensionArray(size=self.__columns_number, init_value=init_value)
        if data:
            assert len(data) == rows_number * columns_number, "Data items number must be equal matrix size."
            data_index = 0
            for row in range(self.__rows_number):
                for column in range(self.__columns_number):
                    self._array[row][column] = data[data_index]
                    data_index += 1

    @property
    def row_number(self):
        return self.__rows_number

    @property
    def column_number(self):
        return self.__columns_number

    def __getitem__(self, row_and_column):
        assert len(row_and_column) == 2, "Invalid number of array subscripts"
        row = row_and_column[0]
        assert 0 <= row < self.__rows_number, "Row index out of range"
        column = row_and_column[1]
        assert 0 <= column < self.__columns_number, "Column index out of range"
        return self._array[row][column]

    def __setitem__(self, row_and_column, value):
        row = row_and_column[0]
        assert 0 <= row < self.__rows_number, "Row index out of range"
        column = row_and_column[1]
        assert 0 <= column < self.__columns_number, "Column index out of range"
        self._array[row][column] = value
