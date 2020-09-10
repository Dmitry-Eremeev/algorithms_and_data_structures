from ctypes import py_object


class OneDimensionArray:
    def __init__(self, size=0):
        self.__size = size
        self.__array_type = py_object * self.__size
        self._array = self.__array_type()
        self._init_items()

    def _init_items(self):
        for index in range(len(self._array)):
            self._array[index] = None

    def __len__(self):
        return self.__size

    def __getitem__(self, index):
        self._is_index_out_of_range(index)
        return self._array[index]

    def __setitem__(self, index, value):
        self._is_index_out_of_range(index)
        self._array[index] = value

    def __iter__(self):
        return OneDimensionArrayIterator(self)

    def _is_index_out_of_range(self, index):
        assert 0 <= index < len(self._array), "Index out of range"


class OneDimensionArrayIterator:
    def __init__(self, array):
        self._size = len(array)
        self._array = array
        self._current_item_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._current_item_index == self._size:
            raise StopIteration
        current_item = self._array[self._current_item_index]
        self._current_item_index += 1
        return current_item
