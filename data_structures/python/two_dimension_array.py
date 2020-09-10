from .one_dimension_array import OneDimensionArray


class TwoDimensionArray:
    def __init__(self, rows_number, column_number):
        self.__rows_number = rows_number
        self.__column_number = column_number
        self.__array = OneDimensionArray(size=self.__rows_number)
        for index in range(len(self.__array)):
            self.__array[index] = OneDimensionArray(size=self.__column_number)

    def __getitem__(self, row_and_column):
        assert len(row_and_column) == 2, "Invalid number of array subscripts"
        row = row_and_column[0]
        assert 0 <= row < self.__rows_number, "Row index out of range"
        column = row_and_column[1]
        assert 0 <= column < self.__column_number, "Column index out of range"
        return self.__array[row][column]

    def __setitem__(self, row_and_column, value):
        row = row_and_column[0]
        assert 0 <= row < self.__rows_number, "Row index out of range"
        column = row_and_column[1]
        assert 0 <= column < self.__column_number, "Column index out of range"
        self.__array[row][column] = value
