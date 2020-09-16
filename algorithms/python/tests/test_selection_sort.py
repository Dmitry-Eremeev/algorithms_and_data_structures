from random import shuffle

from ..selection_sort import selection_sort as sort

for sorting_order in ["ascending", "descending", "test"]:
    sequence = [item for item in range(10)]
    shuffle(sequence)
    print(sequence)
    print(f"sorting order: {sorting_order}")
    sort(sequence=sequence, sorting_order=sorting_order)
    print(sequence)
