def bubble_sort(sequence, sorting_order):
    if sorting_order == "ascending":
        sorting_method = "__gt__"
    elif sorting_order == "descending":
        sorting_method = "__lt__"
    else:
        print("Sorting order can be ascending or descending")
        return
    last_index = len(sequence) - 1
    print(f"last index: {last_index}")
    for sorted_items in range(last_index):
        print(f"sorted items: {sorted_items}")
        already_sorted = True
        for index in range(last_index - sorted_items):
            next_index = index + 1
            if sequence[index].__getattribute__(sorting_method)(sequence[next_index]):
                already_sorted = False
                temp = sequence[index]
                sequence[index] = sequence[next_index]
                sequence[next_index] = temp
        print(f"sequence: {sequence}")
        if already_sorted:
            print("already sorted")
            break
