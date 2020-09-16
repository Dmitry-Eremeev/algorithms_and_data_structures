from random import shuffle

from ..bubble_sort import bubble_sort

for sorting_order in ["ascending", "descending", "test"]:
    sequence = [item for item in range(10)]
    shuffle(sequence)
    print(sequence)
    print(f"sorting order: {sorting_order}")
    bubble_sort(sequence=sequence, sorting_order=sorting_order)
    print(sequence)


