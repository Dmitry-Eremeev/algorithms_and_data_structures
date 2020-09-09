from ..one_dimension_array import OneDimensionArray
from random import random


value_array = OneDimensionArray(2)

for index in range(len(value_array)):
    value_array[index] = random()
    print(value_array[index])

for value in value_array:
    print(value)
