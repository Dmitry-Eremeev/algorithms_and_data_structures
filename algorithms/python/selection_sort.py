def selection_sort(sequence, sorting_order):
    if sorting_order == "ascending":
        sorting_method = "__lt__"
    elif sorting_order == "descending":
        sorting_method = "__gt__"
    else:
        print("Sorting order can be ascending or descending")
        return
    length = len(sequence)
    for target_index in range(length - 1):
        real_target = target_index
        for checking_index in range(target_index + 1, length):
            if sequence[checking_index].__getattribute__(sorting_method)(sequence[real_target]):
                real_target = checking_index
        if real_target != target_index:
            temp = sequence[real_target]
            sequence[real_target] = sequence[target_index]
            sequence[target_index] = temp
