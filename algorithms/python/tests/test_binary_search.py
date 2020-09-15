from random import randint

from ..binary_search import binary_search

sorted_sequence = list()
max_number = 100
min_number = 0
max_step = 10

for item in range(min_number, max_number, randint(1, max_step)):
    print(item)
    sorted_sequence.append(item)

target = randint(min_number, max_number)
print(f"target: {target}")

if binary_search(sequence=sorted_sequence, target=target):
    print("found")

