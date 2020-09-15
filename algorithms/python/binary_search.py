def binary_search(sequence, target):
    low = 0
    high = len(sequence) - 1
    while low <= high:
        middle = (high + low) // 2
        print(f"low = {low}, high = {high}, middle = {middle}")
        if sequence[middle] == target:
            return True
        elif sequence[middle] > target:
            high = middle - 1
        else:
            low = middle + 1
    return False
