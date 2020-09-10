from ..py_list import PyList

py_list = PyList((4, 12, 2, 34, 17,))
print(py_list)

py_list.append(50)
print(py_list)

py_list.append(18)
print(py_list)
py_list.append(64)
print(py_list)
py_list.append(6)
print(py_list)

py_list_2 = PyList((4, 6, 31, 9,))
print(py_list_2)
py_list.extend(py_list_2)
print(py_list)

py_list.insert(3, 79)
print(py_list)

print(py_list.pop(0))
print(py_list)
print(py_list.pop())
print(py_list)

py_list_2 = py_list.slice(1, len(py_list) - 1, 2)
print(py_list_2)

