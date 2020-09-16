def insertion_sort(sequence, sorting_order):
    if sorting_order == "ascending":
        sorting_method = "__lt__"
    elif sorting_order == "descending":
        sorting_method = "__gt__"
    else:
        print("Sorting order can be ascending or descending")
        return
    for division in range(1, len(sequence)):
        value = sequence[division]
        position = division
        while position > 0 and value.__getattribute__(sorting_method)(sequence[position - 1]):
            sequence[position] = sequence[position - 1]
            position -= 1
        sequence[position] = value
