from .one_dimension_array import OneDimensionArray


class PyList:
    __CAPACITY_CHANGE_COEFFICIENT = 2

    def __init__(self, sequence=None):
        self.__size = len(sequence) if sequence else 0
        self.__capacity = self.__size * self.__CAPACITY_CHANGE_COEFFICIENT
        print(f"capacity: {self.__capacity}")
        self.__array = OneDimensionArray(size=self.__capacity)
        if sequence:
            for index, value in enumerate(sequence):
                self.__array[index] = value

    def append(self, value):
        self.__adjust_capacity(increase=1)
        self.__array[self.__size] = value
        self.__size += 1

    def extend(self, sequence):
        sequence_size = len(sequence)
        self.__adjust_capacity(increase=sequence_size)
        for index, value in enumerate(sequence):
            self.__array[self.__size + index] = value
        self.__size += sequence_size

    def insert(self, index, value):
        assert 0 <= index <= self.__size, "index out of range"
        self.__adjust_capacity(increase=1)
        for array_index in range(self.__size, index - 1, -1):
            self.__array[array_index] = self.__array[array_index - 1]
        self.__array[index] = value
        self.__size += 1

    def pop(self, index=None):
        if index is None:
            index = self.__size - 1
        assert 0 <= index < self.__size, "index out of range"
        self.__adjust_capacity(decrease=1)
        removed_value = self.__array[index]
        for array_index in range(index, self.__size - 1):
            self.__array[array_index] = self.__array[array_index + 1]
        self.__size -= 1
        return removed_value

    def slice(self, start=0, stop=None, step=1):
        if not stop:
            stop = self.__size
        assert 0 <= start < self.__size, "start index out of range"
        assert 0 <= stop <= self.__size, "stop index out of range"
        assert start <= stop, "start index must be less or equal stop index"
        slice_list = PyList()
        index = start
        while index < stop:
            slice_list.append(self.__array[index])
            index += step
        return slice_list

    def __len__(self):
        return self.__size

    def __adjust_capacity(self, increase=None, decrease=None):
        assert not(increase and decrease) or not(not increase and not decrease), "List must increased or decreased."
        new_array = None
        if increase:
            new_size = self.__size + increase
            if self.__capacity < new_size:
                self.__capacity = new_size * self.__CAPACITY_CHANGE_COEFFICIENT
                new_array = OneDimensionArray(size=self.__capacity)
        if decrease:
            new_size = self.__size - decrease
            if self.__capacity > new_size * self.__CAPACITY_CHANGE_COEFFICIENT:
                self.__capacity //= self.__CAPACITY_CHANGE_COEFFICIENT
                new_array = OneDimensionArray(size=self.__capacity)
        if new_array:
            for index in range(self.__size):
                new_array[index] = self.__array[index]
            self.__array = new_array
        print(f"capacity: {self.__capacity}")

    def __iter__(self):
        return self.__array.__iter__()

    def __str__(self):
        str_list = str()
        for index in range(self.__size):
            str_list += f"index: {index}, value: {self.__array[index]}\n"
        return str_list




